#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Copyright 2011 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Classes and methods to get current user's status."""



import httplib
import itertools
import json
import sys
import time

from lib import error
from lib import http_interface


class ProblemInputStatus(object):
  def __init__(self, input_type, solved_time, wrong_tries, current_attempt,
               submitted):
    """Constructor.

    Args:
      input_type: String with this status's input type (e.g., small or large).
      solved_time: Number of seconds elapsed since the beginning of the contest
          at which this problem input was solved, or -1 if it has not been
          solved yet.
      wrong_tries: How many wrong tries have been done for this problem input,
          does not include the current one.
      current_attempt: Number of seconds left to submit the output for the
          current attempt for this problem input, or -1 if there is no timer
          active for this problem input.
      submitted: Boolean indicating if there is an output submitted for this
          problem input.
    """
    self.input_type = input_type
    self.solved_time = solved_time
    self.wrong_tries = wrong_tries
    self.current_attempt = current_attempt
    self.submitted = submitted


class UserStatus(object):
  def __init__(self, rank, points, problem_inputs):
    """Constructor.

    Args:
      rank: Position of the user in the scoreboard.
      points: Number of points of the user.
      problem_inputs: The position [p][i] contains the status for the input i of
          problem p.
    """
    self.rank = rank
    self.points = points
    self.problem_inputs = problem_inputs

  @staticmethod
  def _ConstructProblemInputStatus(problems, io_set_status):
    """Create ProblemInputStatus objects for all problems' I/O sets.

    Args:
      problems: List with all problems in the contest.
      io_set_status: A list of (solved, wrong_tries, current_passed, submitted)
          tuples with all I/O sets' statuses, where:

        solved is the time when the I/O set was solved, or -1 to indicate that
            the I/O set has not been solved yet.
        wrong_tries is the number of bad attempts for that I/O set.
        current_passed is the time elapsed for the currently downloaded input,
            or -1 if no input is active.
        submitted is a boolean indicating if the a solution has been submitted
            for this I/O set or not.

    Returns:
      A list of lists of ProblemInputStatus objects for each I/O set in all
          problems. The position [p][i] contains the status for the I/O set i of
          problem p.
    """
    problem_inputs = []
    for problem in problems:
      inputs = []
      for io_set in problem['io_sets']:
        # Get information for the current I/O set.
        status = io_set_status[io_set['global_index']]
        solved, wrong_tries, current_passed, submitted = status

        # Calculate the remaining time for the current attempt using the time
        # limit in the io_set.
        time_limit = io_set['time_limit']
        time_left = -1 if current_passed == -1 else time_limit - current_passed

        # Save the I/O set status for this problem input.
        inputs.append(ProblemInputStatus(io_set['name'], solved, wrong_tries,
                                         time_left, submitted))
      problem_inputs.append(inputs)
    return problem_inputs

  @staticmethod
  def FromJsonResponse(json_response, problems):
    """Construct an UserStatus object using a server json_response.

    Args:
      json_response: JSON response returned by the server when asked for the
          current user status.
      problems: List with all problems in the contest.

    Returns:
      An UserStatus object with the information contained in the json_response,
      or None if the user is not participating/did not participate in this
      contest.

    Raises:
      error.ServerError: If there is a key missing from the server response.
    """
    try:
      # Extract the rank and check if the user is participating or participated
      # in this contest.
      rank = json_response['rank']
      if rank == -1:
        return None

      # Extract problem information from the response and create problem input
      # status objects for each problem.
      json_attempts = json_response['a']
      json_solved_time = json_response['s']
      json_current = json_response['p']
      json_submitted = json_response['submitted']
      json_points = json_response['pts']

    except KeyError as e:
      raise error.ServerError('Cannot find needed key in server status '
                              'response: {0}.\n'.format(e))

    # Get a list of with all I/O sets' status, see _ConstructProblemInputStatus
    # for more details.
    io_set_status = []
    for index, (attempts, solved, current_passed, submitted) in enumerate(
        itertools.izip(json_attempts, json_solved_time, json_current,
                       json_submitted)):
      # Remove the correct submission and the current attempt from the wrong
      # tries, if any.
      wrong_tries = attempts
      if solved != -1: wrong_tries -= 1
      if current_passed != -1: wrong_tries -= 1

      # Store a tuple for this I/O set, which is used when constructing the
      # final UserStatus.
      io_set_status.append((solved, wrong_tries, current_passed,
                            bool(submitted)))

    # Return an user status object with the extracted information.
    problem_inputs = UserStatus._ConstructProblemInputStatus(problems,
                                                             io_set_status)
    return UserStatus(rank, json_points, problem_inputs)


def GetUserStatus(host, cookie, middleware_token, contest_id, problems):
  """Get the current user's status from the server.

  Args:
    host: Domain name of the server where the contest is running.
    cookie: Cookie for the current user.
    middleware_token: Middleware authentication token for the current user.
    contest_id: Id of the contest where the user is participating.
    problems: List with all problems in the contest.

  Returns:
    An UserStatus object with the current user's status.

  Raises:
    error.NetworkError: If a network error occurs while communicating with the
      server.
    error.ServerError: If the server answers code distinct than 200 or the
      response is a malformed JSON.
  """
  # Send an HTTP request to get the user status.
  sys.stdout.write('Getting user status at contest {0} from "{1}"...\n'.format(
      contest_id, host))
  request_referer = 'http://{0}/codejam/contest/dashboard?c={1}'.format(
      host, contest_id)
  request_arguments = {
      'cmd': 'GetUserStatus',
      'contest': contest_id,
      'zx': str(int(time.time())),
      'csrfmiddlewaretoken': str(middleware_token),
      }
  request_headers = {
      'Referer': request_referer,
      'Cookie': cookie,
      }
  try:
    status, reason, response = http_interface.Get(
        host, '/codejam/contest/dashboard/do', request_arguments,
        request_headers)
  except httplib.HTTPException as e:
    raise error.NetworkError('HTTP exception while user status from the Google '
                             'Code Jam server: {0}.\n'.format(e))

  # Check if the status is not good.
  if status != 200 or reason != 'OK':
    raise error.ServerError('Error while communicating with the server, cannot '
                            'get user status. Check that the host, username '
                            'and contest id are valid.\n')

  # Parse the JSON response and return an object with the user status.
  try:
    json_response = json.loads(response)
    return UserStatus.FromJsonResponse(json_response, problems)
  except ValueError as e:
    raise error.ServerError('Invalid response received from the server, cannot '
                            'get user status. Check that the contest id is '
                            'valid: {0}.\n'.format(e))


def _GetInputStatusForSubmission(status, submission):
  """Return the problem input status for a submission.

  Args:
    status: user_status.UserStatus object with the current user status.
    submission: user_submission.UserSubmission object whose problem input status
      must be retrieved.

  Returns:
    An user_status.ProblemInputStatus object with the problem input status
    corresponding to the submission.
  """
  return status.problem_inputs[submission.problem][submission.input_id]


def FixStatusWithSubmissions(status, submissions):
  """Calculate problem input statuses from user submissions.

  Args:
    status: user_status.UserStatus to modify.
    submissions: Sequence of user_submissions.UserSubmission objects with the
      user submissions. If None, an empty list will be used.
  """
  # The submissions array might be None, in this case substitute it with an
  # empty list.
  if submissions is None:
    submissions = []

  # Reset all information in problem input statuses (except for current
  # attempts), everything will be calculated from scratch using the submissions.
  for problem_status in status.problem_inputs:
    for input_status in problem_status:
      input_status.solved_time = -1
      input_status.wrong_tries = 0
      input_status.submitted = False

  # Make a first pass over all submissions to mark correctly solved problem
  # inputs and get the right timestamp.
  for submission in submissions:
    # Get the corresponding input status and update submission flag. Then update
    # solved time if this submission is correct.
    input_status = _GetInputStatusForSubmission(status, submission)
    input_status.submitted = True
    if submission.correct:
      if (input_status.solved_time == -1 or
          submission.timestamp < input_status.solved_time):
        input_status.solved_time = submission.timestamp

  # Make a second pass over all submissions to count all wrong attempts, taking
  # of ignoring attempts after the first correct submission.
  for submission in submissions:
    # Get the corresponding input status and count it as wrong if it is wrong
    # and was submitted before the problem input was submitted correctly.
    input_status = _GetInputStatusForSubmission(status, submission)
    if submission.wrong:
      if (input_status.solved_time == -1 or
          submission.timestamp <= input_status.solved_time):
        input_status.wrong_tries += 1
