#!/usr/bin/env python
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

"""This file implements the a tool to change the hashbang line of a bulk of
python files."""



import optparse
import os
import sys


def ChangeFileHashbang(filename, new_hashbang_line):
  """Change the specified file hashbang line.

  This function assumes that the specified filename is a python file.

  Args:
    filename: String with the name of the file to modify.
    new_hashbang_line: String with the new hashbang line to put in the file.
  """
  # Open the file and read all lines from it.
  with open(filename, 'rt') as file_obj:
    file_lines = file_obj.readlines()

  # Substitute the first line if it's an existing hashbang. Otherwise add the
  # new hashbang at the top of the file.
  complete_hashbang_line = '#!{0}\n'.format(new_hashbang_line.strip())
  if len(file_lines) > 0 and file_lines[0].startswith('#!'):
    file_lines[0] = complete_hashbang_line
  else:
    file_lines[0:1] = [complete_hashbang_line]

  # Write the processed lines to the file.
  with open(filename, 'wt') as file_obj:
    file_obj.write(''.join(file_lines))


def ProcessFile(target, new_hashbang_line):
  """Change the hashbang line of the specified target if it's a python file.

  Args:
    target: String with the file to modify.
    new_hashbang_line: String with the new hashbang line to put in the target.
  """
  # Only process a target if it's a python file.
  if os.path.isfile(target):
    extension = os.path.splitext(target)[1]
    if extension == '.py':
      print 'Adding hashbang to {0}.'.format(target)
      ChangeFileHashbang(target, new_hashbang_line)
    else:
      print 'Ignoring {0}, it\'s not a python file.'.format(target)
  elif not os.path.isdir(target):
    print 'Ignoring {0}, it\'s not a file.'.format(target)


def ProcessTarget(target, new_hashbang_line, recursive):
  """Process a target, which might be a directory or a regular file.

  Args:
    target: Name of the directory or file to process.
    new_hashbang_line: String with the new hashbang line to put in the target.
    recursive: Flag indicating whether directories should be processed
      recursively or not.
  """
  # Process directories recursively or not depending on the recursive flag, if
  # the recursive flag is False then only directly inside the target are
  # processed. Target files are processed directly.
  target_files = []
  if os.path.isdir(target):
    if recursive:
      for dirpath, dirnames, filenames in os.walk(target):
        target_files.extend(os.path.join(dirpath, filename)
                            for filename in filenames)
    else:
      target_files.extend(os.path.join(target, filename)
                          for filename in os.listdir(target))
  else:
    target_files.append(target)

  # Process each target file independently.
  for filename in target_files:
    ProcessFile(filename, new_hashbang_line)


def main():
  """Main function for the update hashbang script.

  This script receives two positional arguments or: the new hashbang to assign
  to all python files and a list of one or more directories with all the files
  to modify.
  """
  # Create an option parser and use it to parse the supplied arguments.
  program_version = 'GCJ hashbang tool'
  parser = optparse.OptionParser(usage='%prog [options]',
                                 version=program_version)
  parser.add_option('-r', action='store_true', dest='recursive',
                    help=('Process all directories recursively'))
  parser.set_defaults(recursive=False)
  options, args = parser.parse_args()

  # Check that the number of arguments is valid.
  if len(args) < 2:
    sys.stderr.write('need at least two positional arguments\n')
    sys.exit(1)

  # Modify all targets applying the new hashbang line.
  new_hashbang_line = args[0]
  for target in args[1:]:
    ProcessTarget(target, new_hashbang_line, options.recursive)


if __name__ == '__main__':
  main()
