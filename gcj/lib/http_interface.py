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

"""This module generates utility methods to make HTTP requests."""



import httplib
import sys
import urllib

from lib import constants
from lib import zip_utils

_DEFAULT_REQUEST_HEADERS = {
    'Accept': 'application/xml,application/xhtml+xml,text/html,text/plain',
    'Accept-Encoding': 'gzip',
    'Accept-Language': 'en',
    'Accept-Charset': 'utf-8',
    'User-Agent': 'Mozilla/5.0 GCJ_Commandline/{0}'.format(constants.VERSION),
}


def _AssembleRequestHeaders(extra_headers):
  """Get the final request headers given client's additional headers.

  Args:
    extra_headers: Dictionary with additional headers for the request. These are
        patched into a copy of the default headers. This argument can be None.

  Returns:
    The final headers for the http request.
  """
  headers = dict(_DEFAULT_REQUEST_HEADERS)
  if extra_headers is not None:
    headers.update(extra_headers)
  return headers


def _MakeRequest(host, method, url, arguments, headers=None, body=''):
  """Send an HTTP request and return the server response.

  Args:
    host: Name of the host that will receive the request.
    method: The method used for the request (either 'GET' or 'POST').
    url: Selector inside that host that should receive the request.
    arguments: Dictionary with all arguments to pass.
    headers: Dictionary with additional headers for the request.
    body: String with the request contents.

  Returns:
    A (status, reason, response) tuple, where status and reason are the ones
    in the HTTP response and response is its body.
  """
  # Get the final request headers and attach the arguments to the url if
  # necessary.
  request_headers = _AssembleRequestHeaders(headers)
  if arguments:
    request_arguments = urllib.urlencode(arguments)
    url = '{0}?{1}'.format(url, request_arguments)

  # Create a connection to the server and get the response, then process it
  # accordingly to the content encoding.
  http_connection = httplib.HTTPConnection(host)
  http_connection.request(method, url, body, request_headers)
  http_response = http_connection.getresponse()
  content_encoding = http_response.getheader('Content-Encoding', 'text/plain')
  response = http_response.read()
  if content_encoding == 'gzip':
    # Unzip response if encoding is gzip, otherwise assume its plain text.
    zipped_response_size = len(response)
    response = zip_utils.UnzipData(response)
    sys.stdout.write('{0} {1}, {2} bytes read from server ({3} '
                     'uncompressed).\n'.format(
                         http_response.status, http_response.reason,
                         zipped_response_size, len(response)))
  else:
    sys.stdout.write('{0} {1}, {2} bytes read from server.\n'.format(
        http_response.status, http_response.reason, len(response)))
  http_response.close()
  return http_response.status, http_response.reason, response


def Get(host, url, arguments, headers=None, body=''):
  """Send a GET HTTP request to the specified server."""
  return _MakeRequest(host, 'GET', url, arguments, headers, body)


def Post(host, url, arguments, headers=None, body=''):
  """Send a POST HTTP request to the specified server."""
  return _MakeRequest(host, 'POST', url, arguments, headers, body)
