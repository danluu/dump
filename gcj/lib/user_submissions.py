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

"""Classes and methods to get current user's submissions."""



import httplib
import json
import sys
import time

from lib import error
from lib import http_interface
from lib import utils


class UserSubmission(object):
  """A submission for a problem input, including result and timestamp."""
  # There is are two statuses that are treated in a special way:
  #
  # - Submitted: This status is assigned to submissions for inputs for which the
  #   judgement is not yet available. We optimistically consider Submitted
  #   inputs to be correct.
  #
  # - Correct (+4 minutes): This status marks a solution as correct but also
  #   adds a 4 minute penalty. To count these submissions correctly, we mark
  #   them as correct and wrong at the same time, which gives points to the user
  #   but also adds one wrong try in that input.
  _CORRECT_STATUSES = frozenset(['Correct', 'Submitted',
                                 'Correct (+4 minutes)'])
  _WRONG_STATUSES = frozenset(['Incorrect', 'Time Expired',
                               'Correct (+4 minutes)'])
  _TIME_UNITS_TO_SECONDS = {'h': 3600, 'm': 60, 's': 1}

  def __init__(self, key, problem, input_id, status, timestamp):
    """Constructor.

    Args:
      key: String with the submission key.
      problem: 0-based index of the submission's problem.
      input_id: Integer with the input id of the submission.
      status: String with the submission's status (Correct, Incorrect, etc.).
      timestamp: Number of seconds that have passed since the contest started
          when the submission was made.
    """
    self.key = key
    self.problem = problem
    self.input_id = input_id
    self.status = status
    self.correct = UserSubmission._GetCorrectnessFromStatus(self.status)
    self.wrong = UserSubmission._GetWrongnessFromStatus(self.status)
    self.timestamp = timestamp

  @staticmethod
  def _GetCorrectnessFromStatus(status):
    """Check whether the submission is correct given its status.

    Args:
      status: String with a submission's status.

    Returns:
      True if the submission's output is correct.
    """
    # Correct types are specified in the _CORRECT_STATUSES set.
    return status in UserSubmission._CORRECT_STATUSES

  @staticmethod
  def _GetWrongnessFromStatus(status):
    """Check whether the submission is wrong given its status.

    Args:
      status: String with a submission's status.

    Returns:
      True if the submission's output is wrong.
    """
    # Wrong types are specified in the _WRONG_STATUSES set.
    return status in UserSubmission._WRONG_STATUSES

  @staticmethod
  def _ConvertTimestampToSeconds(timestamp):
    """Convert a timestamp from a readable format into a number of seconds.

    The specified timestamp must be formatted as "[[%dh] %dm] %ds", where "%d"
    are integers.

    Args:
      timestamp: String with the human-readable timestamp.

    Returns:
      The number of seconds since the beginning of the contest represented by
      timestamp.
    """
    seconds = 0
    for token in timestamp.split():
      time, unit = int(token[:-1]), token[-1]
      seconds += time * UserSubmission._TIME_UNITS_TO_SECONDS[unit]
    return seconds

  @staticmethod
  def FromJsonResponse(json_response, problems):
    """Convert a JSON response with a submission into a more usable format.

    Args:
      json_response: JSON response recevied from the server that must be parsed.
      problems: Iterable with all problems in the current contest.

    Returns:
      An UserSubmission object with the parsed json_response.

    Raises:
      error.ServerError: An error
    """
    # Extract information needed from the JSON response.
    try:
      submission_key = json_response['k']
      problem_key = json_response['p']
      input_id = json_response['d']
      status = json_response['s']
      timestamp = json_response['t']
    except KeyError as e:
      raise error.ServerError('Cannot find field {0} in user '
                              'submission.\n'.format(e))

    # Parse information into a more usable format and return an user submission.
    problem_index = utils.GetProblemIndexFromKey(problems, problem_key)
    parsed_timestamp = UserSubmission._ConvertTimestampToSeconds(timestamp)
    return UserSubmission(submission_key, problem_index, input_id, status,
                          parsed_timestamp)


def GetUserSubmissions(host, cookie, contest_id, problems):
  """Get the current user's submissions for the current contest.

  Args:
    host: Domain name of the server where the contest is running.
    cookie: Cookie for the current user.
    contest_id: Id of the contest where the user is participating.
    problems: Iterable with all problems in the current contest.

  Returns:
    A list of UserSubmission objects with the user submissions for the current
    contest.

  Raises:
    error.NetworkError: If a network error occurs while communicating with the
      server.
    error.ServerError: If the server answers code distinct than 200 or the
      response is a malformed JSON.
  """
  # Send an HTTP request to get the contest events.
  sys.stdout.write('Getting events of contest {0} from "{1}"...\n'.format(
      contest_id, host))
  request_referer = 'http://{0}/codejam/contest/dashboard?c={1}'.format(
      host, contest_id)
  request_arguments = {
      'cmd': 'GetEvents',
      'contest': contest_id,
      'zx': str(int(time.time())),
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
    raise error.NetworkError(
        'HTTP exception while retrieving user submissions from the Google Code '
        'Jam server: {0}.\n'.format(e))

  # Check if the status is not good.
  if status != 200 or reason != 'OK':
    raise error.ServerError('Error while communicating with the server, cannot '
                            'get contest events. Check that the host, username '
                            'and contest id are valid.\n')

  # Parse the JSON response and extract the user submissions (or attempts).
  try:
    json_response = json.loads(response)
    submissions = json_response.get('a')
    if submissions is None:
      return None
  except ValueError as e:
    raise error.ServerError('Cannot parse JSON from server response: '
                            '{0}.\n'.format(e))

  # Process each user submission and return them in a list.
  return [UserSubmission.FromJsonResponse(submission, problems)
          for submission in submissions]
