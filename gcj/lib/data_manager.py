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

"""This module exposes two public function ReadData() and WriteData(), that
can be used to retrieve or put data into the configuration files."""



import re
import sys

from lib import constants
from lib import error

_INPUT_NAME_REGEXP = re.compile(r'^[a-z0-9_]+$')

_DEFAULT_DATA = {}


def _PrepareFileData(file_lines):
  # For each line, remove comments and trim all spaces at beginning and the end.
  for i in xrange(len(file_lines)):
    comment_index = file_lines[i].find('#')
    if comment_index != -1:
      file_lines[i] = file_lines[i][:comment_index]
    file_lines[i] = file_lines[i].strip()

  # Join all lines into a single string, being careful to remove empty lines.
  return '\n'.join(line for line in file_lines if line)


def _ReadDataImpl(filename):
  """Read the persistent data from the specified file, which should be
  formatted as a python dict.

  Args:
    filename: Name of the file with the data to load.

  Returns:
    A python dictionary with the file contents.

  Raises:
    error.InternalError: If there is any error while reading the data from the
      file.
  """
  try:
    # Open the configuration file and read all lines from it.
    file = open(filename, 'rt')
    file_lines = file.readlines()
    file.close()

    # Prepare the file data to prevent mistakes and evaluate it as if it were a
    # python dictionary.
    file_data = _PrepareFileData(file_lines)
    return eval(file_data, {}, {})
  except IOError as e:
    raise error.InternalError('IO error happened while reading data from file '
                              '"{0}" : {1}.\n'.format(filename, e))


def _WriteDataImpl(data, filename):
  """Write the specified data to the specified file, which will
  be formatted as a python dict.

  Args:
    data: Python dictionary with the data to write to the file.
    filename: Name of the file where the data should be written.

  Raises:
    error.InternalError: If there is any error while writing the data to the
      file.
  """
  try:
    # Calculate the space needed for the keys and create a format string
    # for each data item.
    key_width = max(len(repr(key)) for key in data.iterkeys())
    item_format = '{0:%d} : {1},' % key_width

    # Open the file and store each item inside it.
    file = open(filename, 'wt')
    file.write('# -*- coding: utf-8 -*-\n')
    file.write('{\n')
    for key, value in sorted(data.iteritems()):
      item_line = item_format.format(repr(key), repr(value))
      file.write('{0}\n'.format(item_line))
    file.write('}\n')
    file.close()
  except IOError as e:
    raise error.InternalError('IO error happened while writing data to file '
                              '"{0}" : {1}.\n'.format(filename, e))


def _ValidateData(data):
  """Check that all configuration data is valid.

  Args:
    data: Dictionary with the configuration data to validate.

  Raises:
    error.ConfigurationError: If there is any invalid field in the
      configuration.
  """
  # There should be an user and it cannot be the default value.
  if 'user' not in data:
    raise error.ConfigurationError('Username was not found in user data '
                                   'file.\n')
  if data['user'] == 'your-name-here@gmail.com':
    user_config_path = ParametrizeConfigPath(constants.USER_CONFIG_PATH)
    raise error.ConfigurationError('Remember to set your username in the user '
                                   'configuration file "{0}".\n'.format(
                                       user_config_path))


def ParametrizeConfigPath(config_path):
  """Fill in arguments in the config_path and return the result.

  Args:
    config_path: Path to be parametrized.

  Returns:
    The config_path with the arguments filled.
  """
  base_dir = constants.GetRuntimeConstant('base_dir', '.')
  return config_path.format(base_dir=base_dir)


def ReadData(default_data=None):
  """Read tool configuration data.

  Args:
    default_data: Dictionary with default values for fields that do not appear
      in both configuration files.

  Returns:
    A dictionary with the validated configuration data.

  Raises:
    error.InternalError: If there is any problem while reading the user
      configuration file.
  """
  # Read the user data and check if it was read successfully.
  try:
    user_config_path = ParametrizeConfigPath(constants.USER_CONFIG_PATH)
    user_data = _ReadDataImpl(user_config_path)
  except error.InternalError:
    raise error.InternalError('Unable to read used data.\n')

  # Read the current contest data and show warning if not read successfully.
  try:
    current_config_path = ParametrizeConfigPath(constants.CURRENT_CONFIG_PATH)
    current_data = _ReadDataImpl(current_config_path)
  except error.InternalError:
    sys.stderr.write('Warning: Cannot read current data.\n')
    current_data = {}

  # Start with the default data, patch it with the current data and then with
  # the user's data, so the latter ones have more priority. Then validate and
  # return the data.
  final_data = dict(default_data or _DEFAULT_DATA)
  final_data.update(current_data)
  final_data.update(user_data)
  _ValidateData(final_data)
  return final_data


def WriteData(data):
  """Write tool configuration data into the current file.

  Args:
    data: Dictionary with tool configuration.

  Raises:
    error.InternalError: If there is any problem while writing the current
      configuration file.
  """
  # Just forward the data to the current configuration file, the user
  # configuration should not be changed by the tool.
  try:
    current_config_path = ParametrizeConfigPath(constants.CURRENT_CONFIG_PATH)
    _WriteDataImpl(data, current_config_path)
  except error.InternalError:
    raise error.InternalError('Cannot write data to the current '
                              'configuration.\n')
