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

"""This module exposes a class that provides functionality to download an
input from a codejam problem."""



import httplib
import sys

from lib import constants
from lib import error
from lib import http_interface


class InputDownloader(object):
  """Class to download inputs from a specific problem."""
  def __init__(self, host, cookie, middleware_token, contest_id, problem_id):
    """Initialize an input downloader for a specific problem.

    Args:
      host: Name of the server running the contest.
      cookie: Cookie obtained when the user authenticated in the server.
      middleware_token: Input token scrapped from the dashboard.
      contest_id: Identifier of the running contest.
      problem_id: Identifier of the problem whose input must be downloaded.
    """
    self.host = host
    self.cookie = cookie
    self.middleware_token = middleware_token
    self.contest_id = contest_id
    self.problem_id = problem_id

  def Download(self, input_id, filename):
    """Download the specified input and store it in the specified file.

    Args:
      input_id: Identifier of the input to download ('0' for the small input
          and '1' for the large input).
      filename: Name of the file where the input data must be stored.
    """
    # Send an HTTP request to get the input file from the server.
    sys.stdout.write('Getting input file "{0}" from "{1}"...\n'.format(
        filename, self.host))
    request_url = '/codejam/contest/dashboard/do/{0}'.format(filename)
    request_referer = 'http://{0}/codejam/contest/dashboard?c={1}'.format(
        self.host, self.contest_id)
    request_arguments = {
        'cmd': 'GetInputFile',
        'contest': self.contest_id,
        'problem': str(self.problem_id),
        'input_id': input_id,
        'filename': filename,
        'input_file_type': '0',
        'csrfmiddlewaretoken': self.middleware_token,
        'agent': constants.CODEJAM_AGENT_NAME,
        }
    request_headers = {
        'Referer': request_referer,
        'Cookie': self.cookie,
        }
    try:
      status, reason, response = http_interface.Get(
          self.host, request_url, request_arguments, request_headers)
    except httplib.HTTPException as e:
      raise error.NetworkError('HTTP exception while getting input file: '
                               '{0}.\n'.format(e))

    # Check if the status is not good.
    if status != 200 or reason != 'OK':
      raise error.ServerError('Error while communicating with the server, '
                              'cannot download input. Check that the host, '
                              'username and contest id are valid.\n')

    # No response from the server, output warning.
    if not response:
      raise error.ServerError(
          'No response received from the server. This generally happens when:\n'
          '  - You try to download a small input but it is already solved.\n'
          '  - You try to download an input before solving the previous ones.\n'
          '  - You try to redownload the large but its timer already '
          'expired.\n')

    # Write response to the desired file.
    try:
      input_file = open(filename, 'wt')
      input_file.write(response)
      input_file.close()
      sys.stdout.write('File "{0}" downloaded successfully.\n'.format(filename))
    except IOError as e:
      raise error.InternalError('I/O error while writing file "{0}": '
                                '{1}.\n'.format(filename, e))
