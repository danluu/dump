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

"""This file implements the main function for the status grabber."""



import itertools
import optparse
import os
import sys

from lib import code_jam_login
from lib import constants
from lib import data_manager
from lib import error
from lib import google_login
from lib import user_status
from lib import user_submissions


def FormatProblemInputStatus(status):
  """Format a problem input status into a human readable string.

  Args:
    status: user_status.ProblemInputStatus instance to be formatted.

  Returns:
    A human-readable string with the user status.
  """
  # Construct strings for the input type and the solved time for this input.
  input_type_str = '{0}:'.format(status.input_type)
  solved_time_str = '--:--:--'
  if status.solved_time != -1:
    seconds = status.solved_time % 60
    minutes = (status.solved_time // 60) % 60
    hours = status.solved_time // 3600
    solved_time_str = '{0:02d}:{1:02d}:{2:02d}'.format(hours, minutes, seconds)

  # Construct string with tne number of wrong tries for this input.
  wrong_tries_str = None
  if status.wrong_tries == 1:
    wrong_tries_str = '(1 wrong try)'
  elif status.wrong_tries > 1:
    wrong_tries_str = '({0} wrong tries)'.format(status.wrong_tries)

  # Construct string with the time left for the current attempt.
  current_attempt_str = None
  if status.current_attempt != -1:
    seconds = status.current_attempt % 60
    minutes = status.current_attempt // 60
    current_attempt_str = '<< {0}:{1:02d} left'.format(minutes, seconds)

  # Join all parts into a simple string.
  final_str_parts = [input_type_str, solved_time_str]
  if wrong_tries_str is not None:
    final_str_parts.append(wrong_tries_str)
  if current_attempt_str is not None:
    final_str_parts.append(current_attempt_str)
  return ' '.join(final_str_parts)


def main():
  """Main function for the status grabber script.

  This script receives no positional arguments.
  """
  try:
    # Create an option parser and use it to parse the supplied arguments.
    program_version = 'GCJ status grabber {0}'.format(
        constants.VERSION)
    parser = optparse.OptionParser(usage='%prog [options]',
                                   version=program_version)
    parser.add_option('-l', '--login', action='store_true', dest='renew_cookie',
                      help='Ignore the stored cookie, and log in again')
    parser.add_option('-p', '--passwd', action='store', dest='password',
                      help=('Password used to log in. You will be prompted for '
                            'a password if one is required and this flag is '
                            'left empty and there is no password in the '
                            'configuration files'))
    parser.add_option('--base_dir', action='store', dest='base_dir',
                      help=('Base directory used to parametrize configuration '
                            'file paths'))
    parser.set_defaults(renew_cookie=False,
                        base_dir=os.path.dirname(os.path.realpath(__file__)))
    options, args = parser.parse_args()

    # Store the script location in a runtime constant, so it can be used by
    # the library to locate the configuration files.
    constants.SetRuntimeConstant('base_dir', options.base_dir)

    # Check that the number of arguments is valid.
    if len(args) != 0:
      raise error.OptionError('need no positional arguments')

    # Read user information from the config file.
    try:
      current_config = data_manager.ReadData()
      host = current_config['host']
      middleware_tokens = current_config['middleware_tokens']
      cookie = current_config['cookie']
      contest_id = current_config['contest_id']
      problems = current_config['problems']
    except KeyError as e:
      raise error.ConfigurationError(
          'Cannot find field {0} in the configuration files. Please fill the '
          'missing fields in the user configuration file.\n'.format(e))

    # Get the get middleware token used to request the user status.
    try:
      user_status_token = middleware_tokens['GetUserStatus']
    except KeyError:
      raise error.ConfigurationError(
          'Cannot find "GetUserStatus" token in configuration file. '
          'Reinitializing the contest might solve this error.\n')

    # Renew the cookie if the user requested a new login or the cookie has
    # expired.
    if google_login.CookieHasExpired(cookie):
      print 'Cookie has expired, logging into the Code Jam servers...'
      cookie = None
    if not cookie or options.renew_cookie:
      cookie = code_jam_login.Login(options.password)

    # Get user's status and check if he/she is participating.
    status = user_status.GetUserStatus(host, cookie, user_status_token,
                                       contest_id, problems)
    if status is not None:
      # Get user's submissions and use them to fix the user's status.
      submissions = user_submissions.GetUserSubmissions(host, cookie,
                                                        contest_id, problems)
      user_status.FixStatusWithSubmissions(status, submissions)

      # Show each problem input status to the user.
      print '-' * 79
      print 'User status at contest {0}'.format(contest_id)
      print '-' * 79
      print 'Rank: {0} ({1} points)'.format(status.rank, status.points)
      for problem, problem_status in itertools.izip(problems,
                                                    status.problem_inputs):
        print 'Problem: {0}'.format(problem['name'])
        for input_status in problem_status:
          print '  {0}'.format(FormatProblemInputStatus(input_status))
    else:
      # Show error message, user is not participating in the contest.
      print 'User status not found at contest {0}'.format(contest_id)

  except error.OptionError as e:
    parser.print_usage()
    program_basename = os.path.basename(sys.argv[0])
    sys.stderr.write('{0}: error: {1}\n'.format(program_basename, e))
    sys.exit(1)

  except error.UserError as e:
    sys.stderr.write(str(e))
    sys.exit(1)

  except error.CommandlineError as e:
    sys.stderr.write('{0}: {1}'.format(e.__class__.__name__, e))
    sys.exit(1)


if __name__ == '__main__':
  main()
