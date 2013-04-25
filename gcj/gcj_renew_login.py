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

"""This file implements the main function for the login agent, which uses
the CodeJamLogin class in the lib directory."""



import optparse
import os
import sys

from lib import code_jam_login
from lib import constants
from lib import error


def main():
  """Main function for the login agent script.

  This script receives no positional arguments.
  """
  try:
    # Create an option parser and use it to parse the supplied arguments.
    program_version = 'GCJ login agent {0}'.format(
        constants.VERSION)
    parser = optparse.OptionParser(usage='%prog [options]',
                                   version=program_version)
    parser.add_option('-p', '--passwd', action='store', dest='password',
                      help=('Password used to login in the server, will be '
                            'asked if not specified'))
    parser.add_option('--base_dir', action='store', dest='base_dir',
                      help=('Base directory used to parametrize configuration '
                            'file paths'))
    parser.set_defaults(base_dir=os.path.dirname(os.path.realpath(__file__)))
    options, args = parser.parse_args()

    # Store the script location in a runtime constant, so it can be used by
    # the library to locate the configuration files.
    constants.SetRuntimeConstant('base_dir', options.base_dir)

    # Check that the number of arguments is valid.
    if len(args) != 0:
      raise error.OptionError('need no positional arguments')

    # Login into the codejam servers.
    code_jam_login.Login(options.password)

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
