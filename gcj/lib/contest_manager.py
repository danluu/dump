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

"""This file provides a method to initialize the tool with a specific contest
given its id."""



import collections
import httplib
import json
import os
import shutil
import sys
import time

from lib import code_jam_login
from lib import constants
from lib import data_manager
from lib import error
from lib import http_interface

PLANNED, ACTIVE, QUIET, FINISHED, PRACTICE = range(0, 5)

_IO_DIFFICULTY_SPEC = {
    0: {'difficulty_name': 'small',
        'difficulty': 0,
        'time_limit': 4 * 60,
        'public': True},
    1: {'difficulty_name': 'large',
        'difficulty': 1,
        'time_limit': 8 * 60,
        'public': False},
    }


def _GetProblemIoSets(io_sets, io_difficulty_specs, base_index):
  """Get all problem I/O sets with necessary names and ids.

  Args:
    io_sets: Sequence of dictionaries with different I/O sets for a problem.
      Each dictionary has the name, id, difficulty and points for each I/O set.
    io_difficulty_specs: List of dictionaries with the specification for each
      I/O difficulty. Each one of these dictionaries must have a name for the
      difficulty, the time limit and a boolean indicating whether the result is
      public or not.
    base_index: Global index of the first I/O set of this problem among all I/O
      sets in the contest.

  Returns:
    A dictionary from I/O set name to a I/O specification, which is a dictionary
    with the I/O name, the input id within the problem, the points, the time
    limit and whether it's public or not.
  """
  problem_io_sets = []
  for input_io_set in io_sets:
    io_difficulty = input_io_set['difficulty']
    input_id = input_io_set['number']

    # Make a copy of the difficulty data and patch it with the information from
    # the I/O set.
    output_io_set = dict(io_difficulty_specs[io_difficulty])
    output_io_set['name'] = input_io_set['name']
    output_io_set['points'] = input_io_set['points']
    output_io_set['input_id'] = input_id
    output_io_set['global_index'] = base_index + input_id
    problem_io_sets.append(output_io_set)
  return problem_io_sets


def _GetProblems(host, cookie, contest_id):
  """Read the problems of the specified contest.

  Args:
    host: Host where the contest is running.
    cookie: Cookie that the user received when authenticating.
    contest_id: ID of the contest whose problems must be read.

  Returns:
    A tuple with two lists, the first with the problem IDs and the second
    with the problem names.

  Raises:
    error.NetworkError: If a network error occurs while communicating with the
      server.
    error.ServerError: If the server answers code distinct than 200 or the
      response is a malformed JSON.
  """
  # Send an HTTP request to get the problem list from the server.
  sys.stdout.write('Getting problem list of contest {0} from "{1}"...\n'.format(
      contest_id, host))
  request_referer = 'http://{0}/codejam/contest/dashboard?c={1}'.format(
      host, contest_id)
  request_arguments = {
      'cmd': 'GetProblems',
      'contest': contest_id,
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
    raise error.NetworkError('HTTP exception while retrieving problem '
                             'information from the Google Code Jam server: '
                             '{0}.\n'.format(e))

  # Check if the status is not good.
  if status != 200 or reason != 'OK':
    raise error.ServerError('Error while communicating with the server, cannot '
                            'get problem information. Check that the host, '
                            'username and contest id are valid.\n')

  # Parse the JSON response and extract each problem from it.
  try:
    problems = []
    json_response = json.loads(response)
    base_index = 0
    for problem in json_response:
      io_sets = _GetProblemIoSets(problem['io_sets'], _IO_DIFFICULTY_SPEC,
                                  base_index)
      io_set_name_to_index = dict((io_set['name'], index)
                                  for index, io_set in enumerate(io_sets))
      problems.append({'key': problem['key'],
                       'id': problem['id'],
                       'name': problem['name'],
                       'io_sets': io_sets,
                       'io_set_name_to_index': io_set_name_to_index})
      base_index += len(io_sets)
    return problems
  except (KeyError, ValueError) as e:
    raise error.ServerError('Invalid response received from the server, cannot '
                            'initialize contest. Check that the contest id is '
                            'valid: {0}.\n'.format(e))


def _ValidateContestDataOrRaise(middleware_tokens, problems):
  """Validate that all contest information is complete.

  Args:
    middleware_tokens: Dictionary with all retrieved middleware tokens.
    problems: Sequence with all retrieved problem information.

  Raises:
    error.ConfigurationError: If the contest data is invalid or incomplete.
  """
  needed_tokens = {
      'GetInitialValues': ('Cannot find middleware token to get contest '
                           'status.\n'),
      'GetInputFile': ('Cannot find middleware token to get input files, '
                       'please login again.\n'),
      'GetUserStatus': ('Cannot find middleware token to get user status, '
                        'please login again.\n'),
      'SubmitAnswer': ('Cannot find middleware token to submit answers, please '
                       'login again.\n'),
      }
  for token_name, user_reason in needed_tokens.iteritems():
    if token_name not in middleware_tokens:
      raise error.ConfigurationError(user_reason)

  if not problems:
    raise error.ConfigurationError('Cannot find problems in the contest, '
                                   'please check the contest id and try '
                                   'again.\n')


def _ValidateContestData(middleware_tokens, problems):
  """Validate that all contest information is complete.

  Args:
    middleware_tokens: Dictionary with all retrieved middleware tokens.
    problems: Sequence with all retrieved problem information.

  Returns:
    True if the contest data is valid and complete.
  """
  try:
    _ValidateContestDataOrRaise(middleware_tokens, problems)
    return True
  except error.ConfigurationError:
    return False


def Initialize(tournament_id, contest_id, password=None):
  """Initialize configuration for the specified tournament or contest.

  This function initializes the tool for a contest. If the contest is None,
  the tool will be initialized for the current contest of the specified
  tournament.

  Either one of tournament_id or contest_id must be not None.

  The retrieved data is stored in the current configuration file.

  Args:
    tournament_id: ID of the tournament whose current contest must be
      initialized.
    contest_id: ID of the contest to initialize. If None, the server will ask
      for the current contest of the specified tournament.
    password: Password specified by the user, if any.

  Raises:
    error.ConfigurationError: If the contest data is invalid or incomplete.
    error.UserError: If no contest was specified and there is no running contest
      for the specified tournament.
  """
  # Reset the current configuration file with the one provided by the user and
  # renew the cookie, so the middleware tokens are retrieved correctly.
  try:
    user_config_path = data_manager.ParametrizeConfigPath(
        constants.USER_CONFIG_PATH)
    current_config_path = data_manager.ParametrizeConfigPath(
        constants.CURRENT_CONFIG_PATH)
    shutil.copy(user_config_path, current_config_path)
    code_jam_login.Login(password)
  except OSError as e:
    raise error.InternalError('Configuration file {0} could not be created: '
                              '{1}.\n'.format(current_config_path, e))

  # Read the current configuration file and extract the host and the cookie.
  try:
    contest_data = data_manager.ReadData()
    host = contest_data['host']
    cookie = contest_data['cookie']
  except KeyError as e:
    # Indicate that no host or cookie was configured and exit with error.
    raise error.ConfigurationError('No host or login cookie found in the '
                                   'configuration file: {0}.\n'.format(e))

  # Get the current contest if no contest id was specified. If there is no
  # running contest show an error to the user.
  if contest_id is None:
    contest_id = GetCurrentContestId(host, cookie, tournament_id)
    if contest_id is None:
      raise error.UserError('No contest is running for tournament %s and no '
                            'contest id was specified.\n' % tournament_id)
    sys.stdout.write('Initializing tool for current contest with id %s.\n' %
                     contest_id)

  # Retrieve the problem list and validate the extracted contest data and exit
  # if there is any error.
  problems = _GetProblems(host, cookie, contest_id)
  _ValidateContestDataOrRaise(contest_data['middleware_tokens'], problems)

  # Add the contest id, the problems and the middleware tokens to the contest
  # data.
  contest_data['contest_id'] = contest_id
  contest_data['problems'] = problems

  # Finally, write the contest data to the current data file, and then
  # renew the cookie stored in the configuration.
  data_manager.WriteData(contest_data)
  sys.stdout.write('Contest {0} initialized successfully, {1} problem(s) '
                   'retrieved.\n'.format(contest_id, len(problems)))


def IsInitialized():
  """Check if the tool has been inititalized with a contest.

  This function checks that the current configuration file exists and it
  contains valid information, which includes a contest id, problem ids, problem
  names and middleware tokens.

  Returns:
    True if a contest has been initialized, false otherwise.
  """
  # Check if the current configuration file exists, otherwise the contest has
  # not been initialized yet.
  current_config_path = data_manager.ParametrizeConfigPath(
      constants.CURRENT_CONFIG_PATH)
  if not os.path.isfile(current_config_path):
    return False

  # Read the current config and check that all contest-related fields exist.
  current_config = data_manager.ReadData()
  if ('cookie' not in current_config or
      'middleware_tokens' not in current_config or
      'contest_id' not in current_config or
      'problems' not in current_config):
    return False

  # Use the contest validator to check the data, ignoring the error messages.
  return _ValidateContestData(current_config['middleware_tokens'],
                              current_config['problems'])


def ClearContest():
  # Erase the current configuration file if it exists and is a file, otherwise
  # show a warning if the configuration is not a regular file (should not happen
  # under normal conditions).
  try:
    current_config_path = data_manager.ParametrizeConfigPath(
        constants.CURRENT_CONFIG_PATH)
    if os.path.isfile(current_config_path):
      os.remove(current_config_path)
    elif os.path.exists(current_config_path):
      sys.stderr.write('Warning: Cannot erase current configuration file "{0}" '
                       'because it is not a regular file.\n'.format(
                           current_config_path))
  except OSError as e:
    raise error.InternalError('OS error happened while deleting file "{0}": '
                              '{1}.\n'.format(filename, e))


def GetCurrentContestId(host, cookie, tournament_id):
  # Send an HTTP request to get the problem list from the server.
  sys.stdout.write('Getting current contest of tournament {0} from '
                   '"{1}"...\n'.format(tournament_id, host))
  request_arguments = {
      't': tournament_id,
      'zx': str(int(time.time())),
      }
  request_headers = {
      'Referer': 'http://{0}/codejam',
      'Cookie': cookie,
      }
  try:
    status, reason, response = http_interface.Get(
        host, '/codejam/contest/microsite-info', request_arguments,
        request_headers)
  except httplib.HTTPException as e:
    raise error.NetworkError('HTTP exception while retrieving current contest '
                             'from the Google Code Jam server: '
                             '{0}.\n'.format(e))

  # Check if the status is not good.
  if status != 200 or reason != 'OK':
    raise error.ServerError('Error while communicating with the server, cannot '
                            'get current contest. Check that the host and '
                            'username are valid.\n')

  # Parse the JSON response and extract the contest status from it.
  try:
    json_response = json.loads(response)
    return json_response.get('contestId', None)
  except ValueError as e:
    raise error.ServerError('Invalid response received from the server, cannot '
                            'get current contest. Check that the tournament id '
                            'is valid: {0}.\n'.format(e))


def GetContestStatus(host, cookie, get_initial_values_token, contest_id):
  """Get the contest status of the specified contest.

  Args:
    host: Host where the contest is running.
    cookie: Cookie that the user received when authenticating.
    get_initial_values_token: Middleware token used to make the request.
    contest_id: ID of the contest whose problems must be read.

  Returns:
    The contest status.

  Raises:
    error.NetworkError: If a network error occurs while communicating with the
      server.
    error.ServerError: If the server answers code distinct than 200 or the
      response is a malformed JSON.
  """
  # Send an HTTP request to get the problem list from the server.
  sys.stdout.write('Getting status of contest {0} from "{1}"...\n'.format(
      contest_id, host))
  request_referer = 'http://{0}/codejam/contest/dashboard?c={1}'.format(
      host, contest_id)
  request_arguments = {
      'cmd': 'GetInitialValues',
      'contest': contest_id,
      'zx': str(int(time.time())),
      'csrfmiddlewaretoken': str(get_initial_values_token),
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
    raise error.NetworkError('HTTP exception while retrieving contest status '
                             'from the Google Code Jam server: '
                             '{0}.\n'.format(e))

  # Check if the status is not good.
  if status != 200 or reason != 'OK':
    raise error.ServerError('Error while communicating with the server, cannot '
                            'get contest status. Check that the host, username '
                            'and contest id are valid.\n')

  # Parse the JSON response and extract the contest status from it.
  try:
    json_response = json.loads(response)
    return json_response['cs']
  except (KeyError, ValueError) as e:
    raise error.ServerError('Invalid response received from the server, cannot '
                            'get contest status. Check that the contest id is '
                            'valid: {0}.\n'.format(e))


def CanSubmit(contest_status):
  """Check if a contest is accepting submissions given its status.

  Args:
    contest_status: Status of the contest to check.

  Returns:
    True if the contest is accepting and processing submissions.
  """
  return contest_status in [ACTIVE, PRACTICE]
