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

"""This file implements the main function for the output submitter, which uses
the OutputSubmitter class in the lib directory."""



import optparse
import os
import re
import sys

from lib import code_jam_login
from lib import constants
from lib import contest_manager
from lib import data_manager
from lib import error
from lib import google_login
from lib import output_submitter
from lib import user_status
from lib import utils


def main():
  """Main function for the output submitter script.

  This script receives three positional arguments, the problem letter, the
  input size and the submit id.
  """
  try:
    # Create an option parser and use it to parse the supplied arguments.
    program_version = 'GCJ solution submitter {0}'.format(
        constants.VERSION)
    parser = optparse.OptionParser(usage='%prog [options] problem input id',
                                   version=program_version)
    parser.add_option('-l', '--login', action='store_true', dest='renew_cookie',
                      help='Ignore the stored cookie and log in again')
    parser.add_option('-p', '--passwd', action='store', dest='password',
                      help=('Password used to log in. You will be prompted for '
                            'a password if one is required and this flag is '
                            'left empty and there is no password in the '
                            'configuration files'))
    parser.add_option('-f', '--force', action='store_true', dest='force',
                      help=('Skip check to verify if there is a running timer '
                            'and there is no submission if the input is large'))
    parser.add_option('-d', '--data-directory', action='store',
                      dest='data_directory',
                      help=('Directory with the I/O files and main source '
                            'files [default: ./source]'))
    parser.add_option('-o', '--output-name', action='store', dest='output_name',
                      help='Name of the file with the solution\'s output')
    parser.add_option('-a', '--add-source', action='append',
                      dest='extra_sources',
                      help='Add EXTRA_SOURCE to the submitted source files',
                      metavar='EXTRA_SOURCE')
    parser.add_option('-z', '--zip-sources', action='store_true',
                      dest='zip_sources',
                      help=('Put the source files into a zip file before '
                            'submitting'))
    parser.add_option('--ignore-zip', action='store_true', dest='ignore_zip',
                      help=('Ignore source zip files not specified directly '
                            'using the -a option'))
    parser.add_option('--ignore-default-source', action='store_true',
                      dest='ignore_def_source',
                      help=('Ignore files in the default source directory, '
                            'except for those specified using the -a option'))
    parser.add_option('--gzip-content', action='store_true',
                      dest='gzip_content',
                      help=('Send the output and source code using gzip '
                            'encoding (faster)'))
    parser.add_option('--nogzip-content', action='store_false',
                      dest='gzip_content',
                      help=('Send the output and sources using plain encoding '
                            '(slower)'))
    parser.add_option('--base_dir', action='store', dest='base_dir',
                      help=('Base directory used to parametrize configuration '
                            'file paths'))
    parser.set_defaults(renew_login=False, force=False, gzip_content=True,
                        zip_sources=False, ignore_zip=False,
                        ignore_def_source=False,
                        base_dir=os.path.dirname(os.path.realpath(__file__)))
    options, args = parser.parse_args()

    # Store the script location in a runtime constant, so it can be used by
    # the library to locate the configuration files.
    constants.SetRuntimeConstant('base_dir', options.base_dir)

    # Check that the number of arguments is valid.
    if len(args) != 3:
      raise error.OptionError('need 3 positional arguments')

    # Check that the problem idenfier is valid.
    problem_letter = args[0].upper()
    if len(problem_letter) != 1 or not problem_letter.isupper():
      raise error.OptionError(
          'invalid problem {0}, must be one uppercase letter'.format(
              problem_letter))

    # Check that the submit id is a valid identifier.
    id = args[2]
    if not re.match('^\w+$', id):
      raise error.OptionError('invalid id {0}, can only have numbers, letters '
                              'and underscores'.format(id))

    # Check that the contest has been initialized.
    if not contest_manager.IsInitialized():
      raise error.ConfigurationError(
          'Contest is not initialized, please initialize the contest before '
          'trying to submit output files.\n')

    # Read user and input information from the config file.
    try:
      current_config = data_manager.ReadData()
      host = current_config['host']
      user = current_config['user']
    except KeyError as e:
      raise error.ConfigurationError(
          'Cannot find all required user data in the configuration files: {0}. '
          'Please fill the missing fields in the user configuration '
          'file.\n'.format(e))

    # Read current contest information from the config file.
    try:
      middleware_tokens = current_config['middleware_tokens']
      cookie = None if options.renew_cookie else current_config['cookie']
      contest_id = current_config['contest_id']
      problems = current_config['problems']
    except KeyError as e:
      raise error.ConfigurationError(
          'Cannot find all required contest data in configuration files: {0}. '
          'Reinitializing the contest might solve this error.\n'.format(e))

    # Calculate the problem index and check if it is inside the range.
    problem_index = ord(problem_letter) - ord('A')
    if problem_index < 0 or problem_index >= len(problems):
      raise error.UserError(
          'Cannot find problem {0}; there are only {1} problem(s).\n'.format(
              problem_letter, len(problems)))

    # Get the problem specification and the targeted I/O set from it.
    problem = problems[problem_index]
    io_set_name = args[1].lower()
    io_set = utils.GetProblemIoSetByName(problem, io_set_name)
    if io_set is None:
      raise error.UserError(
          'Input type {0} not found for problem {1}, available types are: '
          '{2}.\n'.format(io_set_name, problem['name'],
                          ', '.join(io_set['name']
                                    for io_set in problem['io_sets'])))
    input_id = io_set['input_id']

    # Get the needed middleware tokens to submit solutions and check for running
    # attempts.
    try:
      get_initial_values_token = middleware_tokens['GetInitialValues']
      user_status_token = middleware_tokens['GetUserStatus']
      submit_output_token = middleware_tokens['SubmitAnswer']
    except KeyError as e:
      raise error.ConfigurationError(
          'Cannot find {0} token in configuration file. Reinitializing the '
          'contest might solve this error.\n'.format(e))

    # Get the data directory from the options, if not defined, get it from the
    # configuration, using './source' as the default value if not found. In the
    # same way, get the output filename format and the main source code filename
    # format.
    data_directory = (options.data_directory or
                      current_config.get('data_directory', './source'))
    output_name_format = (options.output_name or
                          current_config.get('output_name_format',
                                             '{problem}-{input}-{id}.out'))
    source_names_format = current_config.get('source_names_format')

    # There is no sensible default for the main source, so exit with error if no
    # value is found and it wasn't ignored.
    if not options.ignore_def_source and source_names_format is None:
      raise error.UserError(
          'No format found for the default sources file name. Specify '
          '"source_name_format" in the configuration file or ignore it passing '
          '--ignore-default-source.\n')

    # Generate the output file name using the specified format and then return.
    try:
      output_basename = output_name_format.format(
        problem=problem_letter, input=io_set_name, id=id)
      output_filename = os.path.normpath(os.path.join(data_directory,
                                                      output_basename))
    except KeyError as e:
      raise error.ConfigurationError(
          'Invalid output name format {0}, {1} is an invalid key, only use '
          '"problem", "input" and "id".\n'.format(input_name_format, e))

    # Create the list with all the source files and add the default source file
    # if it was requested.
    source_names = []
    if not options.ignore_def_source:
      try:
        # Process each source name in the source formats list.
        for source_name_format in source_names_format:
          # Generate the source file name using the specified format and append
          # it to the source list.
          def_source_basename = source_name_format.format(
              problem=problem_letter, input=io_set_name, id=id)
          def_source_filename = os.path.normpath(os.path.join(
              data_directory, def_source_basename))
          source_names.append(def_source_filename)
      except KeyError as e:
        raise error.ConfigurationError(
            'Invalid output name format {0}, {1} is an invalid key, only '
            'use "problem", "input" and "id".\n'.format(input_name_format, e))

    # Append any extra source file to the source list, normalizing their paths
    # for the current operative system.
    if options.extra_sources is not None:
      for extra_source_format in options.extra_sources:
        extra_source_file = extra_source_format.format(problem=problem_letter,
                                                       input=io_set_name, id=id)
        source_names.append(os.path.normpath(extra_source_file))

    # Print message indicating that an output is going to be submitted.
    print '-' * 79
    print '{0} output for "{1} - {2}" at "{3}"'.format(
      io_set['difficulty_name'].capitalize(), problem_letter, problem['name'],
      output_filename)
    print '-' * 79

    # Renew the cookie if the user requested a new login or the cookie has
    # expired.
    if google_login.CookieHasExpired(cookie):
      print 'Cookie has expired, logging into the Code Jam servers...'
      cookie = None
    if not cookie or options.renew_cookie:
      cookie = code_jam_login.Login(options.password)

    # Get the contest status and check if it is accepting submissions.
    contest_status = contest_manager.GetContestStatus(
        host, cookie, get_initial_values_token, contest_id)
    if not options.force and not contest_manager.CanSubmit(contest_status):
      raise error.UserError('Cannot submit solutions to this contest, its not '
                            'active or in practice mode.\n')

    # All problem inputs have public answers in practice mode.
    io_set_public = (io_set['public'] or
                     contest_status == contest_manager.PRACTICE)

    # Get the user status and check if it is participating or not.
    current_user_status = user_status.GetUserStatus(
        host, cookie, user_status_token, contest_id, problems)
    if (contest_status == contest_manager.ACTIVE and
        current_user_status is not None):
      # Check that there is a running timer for this problem input.
      problem_inputs = current_user_status.problem_inputs
      problem_input_state = problem_inputs[problem_index][input_id]
      if not options.force and problem_input_state.current_attempt == -1:
        raise error.UserError(
            'You cannot submit {0}-{1}, the timer expired or you did not '
            'download this input.\n'.format(problem_letter, io_set_name))

      # Ask for confirmation if user is trying to resubmit a non-public output.
      if not io_set_public and problem_input_state.submitted:
        submit_message = ('You already have submitted an output for {0}-{1}. '
                          'Resubmitting will override the previous one.'.format(
                              problem_letter, io_set_name))
        utils.AskConfirmationOrDie(submit_message, 'Submit', options.force)
        print 'Submitting new output and source files.'
      else:
        print 'Submitting output and source files.'
    else:
      print 'Submitting practice output and source files.'

    # Check if the contest is running and no source file is being included, show
    # a warning to the user indicating that he/she might be disqualified because
    # of this. This confirmation cannot be skipped by using --force.
    if contest_status == contest_manager.ACTIVE and not source_names:
      submit_message = ('You did not include source code files for this '
                        'attempt. Submitting output files without source code '
                        'can lead to disqualification.'.format(
                            problem_letter, io_set_name))
      utils.AskConfirmationOrDie(submit_message, 'Are you sure', False)
      print 'Submitting without source files.'

    # Create the output submitter and send the files.
    submitter = output_submitter.OutputSubmitter(
        host, cookie, submit_output_token, contest_id, problem['id'])
    submitter.Submit(input_id, output_filename, source_names, io_set_public,
      gzip_body=options.gzip_content, zip_sources=options.zip_sources,
      add_ignored_zips=not options.ignore_zip)

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
