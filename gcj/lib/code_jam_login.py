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

"""This module exposes one public function Login(), that given the password of
the Code Jam contestant should log him in and return a cookie."""



from datetime import datetime, timedelta

import BaseHTTPServer
import getpass
import httplib
import json
import sys
import time
import urllib2

from lib import constants
from lib import data_manager
from lib import error
from lib import google_login
from lib import http_interface


def CheckToolVersion(host, tool_version):
  """Check if the specified tool_version is accepted by the host.

  Args:
    host: Host where the contest is running.
    tool_version: String with this tool's version.

  Raises:
    error.InternalError: If the tool's version is not accepted by the host.
    error.NetworkError: If a network error occurs while communicating with the
      server.
    error.ServerError: If the server answers code distinct than 200 or the
      response is a malformed JSON.
  """
  # Send an HTTP request to get the problem list from the server.
  sys.stdout.write('Checking tool version for "{0}"...\n'.format(host))
  request_referer = 'http://{0}/codejam'.format(host)
  request_arguments = {
      'cmd': 'CheckVersion',
      'version': tool_version,
      }
  request_headers = {
      'Referer': request_referer,
      }
  try:
    status, reason, response = http_interface.Get(
        host, '/codejam/cmdline', request_arguments, request_headers)
  except httplib.HTTPException as e:
    raise error.NetworkError('HTTP exception while checking tool version with '
                             'the Google Code Jam server: {0}\n'.format(e))

  # The current server version might not support this yet. Print a warning
  # message and skip validation.
  if status == 404:
    print 'WARNING: Cannot check commandline version with the server.'
    return

  # Check if the status is not good.
  if status != 200 or reason != 'OK':
    raise error.ServerError('Error while communicating with the server, cannot '
                            'check tool version. Check that the host is '
                            'valid.\n')

  # Extract token information from server response.
  try:
    validation_info = json.loads(response)
    if validation_info['msg']:
      print validation_info['msg']
    if not validation_info['valid']:
      raise error.InternalError('This tool\'s version is not accepted by host '
                                '{0}, please update to the latest '
                                'version.\n'.format(host, tool_version))
  except (KeyError, ValueError) as e:
    raise error.ServerError('Invalid response received from the server, cannot '
                            'initialize contest. Check that the contest id is '
                            'valid: {0}.\n'.format(e))


def AskForPassword(user):
  """Ask the user for his or her password.

  Args:
    user: Name of the user whose password must be retrieved.

  Returns:
    A password entered by the user.
  """
  return getpass.getpass('Password for {0}: '.format(user))


def _GetUserPassword(user, contest_data):
  """Get the user password from a possible input string, a value inside the
  configuration file or directly from the user.

  Args:
    user: Name of the user whose password must be retrieved.
    contest_data: Data of the actual contest in a Python dict.

  Returns:
    The password of the specified user. This password might come from the
    configuration file or the standard input.
  """
  # Retrieve the password from the contest data if it is there.
  if 'password' in contest_data:
    return contest_data['password']

  # No password was specified in the command line or the configuration file,
  # read it from the user.
  print 'Cannot find password for user {0}.'.format(user)
  return AskForPassword(user)


def MakeLogin(host, user, password=None):
  """Retrieve the authentication token and cookie from the code jam server,
  using the given user and password to authenticate.

  Args:
    host: Name of the host that runs the competition.
    user: User to authenticate in the Code Jam servers.
    password: Password of the user. If None it will be read from the user.

  Returns:
    A tuple with the authentication token and the login cookie.

  Raises:
    error.AuthenticationError: If the server answers with an authentication
      error, as specified in the GoogleLogin protocol.
    error.NetworkError: If there was a problem while communicating with the
      server.
  """
  try:
    # Ask the user for the password if it wasn't provided.
    if password is None:
      sys.stdout.write('Logging into "{0}" with user "{1}"...\n'.format(
          host, user))
      password = AskForPassword(user)

    # Get the authentication token and gae cookie using the GoogleLogin module.
    application_name = 'gcj_commandline-{0}'.format(constants.VERSION)
    auth_token, cookie = google_login.Login(
        host, 'HOSTED_OR_GOOGLE', user, password, 'ah', application_name, False)
    sys.stdout.write('Successfully logged into "{0}" with user "{1}".\n'.format(
        host, user))
    return auth_token, cookie

  except google_login.AuthenticationError as e:
    # Return a exception with a human-readable error based on the error and exit
    # with an error code.
    if e.reason == 'BadAuthentication':
      raise error.AuthenticationError('Invalid username or password.\n')
    elif e.reason == 'CaptchaRequired':
      raise error.AuthenticationError(
          'Please go to https://www.google.com/accounts/DisplayUnlockCaptcha '
          'and verify you are a human. Then try again.\n')
    elif e.reason == 'NotVerified':
      raise error.AuthenticationError('Account not verified.')
    elif e.reason == 'TermsNotAgreed':
      raise error.AuthenticationError('User has not agreed to TOS.')
    elif e.reason == 'AccountDeleted':
      raise error.AuthenticationError('The user account has been deleted.')
    elif e.reason == 'AccountDisabled':
      raise error.AuthenticationError('The user account has been disabled.')
    elif e.reason == 'ServiceDisabled':
      raise error.AuthenticationError('The user\'s access to the service has '
                                      'been disabled.')
    elif e.reason == 'ServiceUnavailable':
      raise error.AuthenticationError('The service is not available, try again '
                                      'later.')
    else:
      raise error.AuthenticationError('Unrecognized authentication error. '
                                      'Reason: %s' % e.reason)

  except urllib2.HTTPError as e:
    explanation = BaseHTTPServer.BaseHTTPRequestHandler.responses[e.code][0]
    raise error.NetworkError('HTTP error while logging into the Google Code '
                             'Jam server ({0}): {1}\n'.format(e.code,
                                                              explanation))


# TODO(user): Update the commandline tool to adapt to the fact that we only
# need one middleware token now. This should be a simplification.
def _GetMiddlewareTokens(host, cookie):
  """Get needed middleware tokens for the specified host.

  Args:
    host: Host where the contest is running.
    cookie: Cookie that the user received when authenticating.

  Returns:
    A tuple two elements: a dictionary containing all the middleware tokens,
    and the tokens expiration date.

  Raises:
    error.NetworkError: If a network error occurs while communicating with the
      server.
    error.ServerError: If the server answers code distinct than 200 or the
      response is a malformed JSON.
  """
  # Send an HTTP request to get the problem list from the server.
  sys.stdout.write('Getting middleware tokens from "{0}"...\n'.format(host))
  request_referer = 'http://{0}/codejam'.format(host)
  request_arguments = {
      'cmd': 'GetMiddlewareTokens',
      'actions': 'GetInitialValues,GetInputFile,GetUserStatus,SubmitAnswer',
      }
  request_headers = {
      'Referer': request_referer,
      'Cookie': cookie,
      }
  try:
    status, reason, response = http_interface.Get(
        host, '/codejam/middleware', request_arguments, request_headers)
  except httplib.HTTPException as e:
    raise error.NetworkError('HTTP exception while retrieving middleware '
                             'tokens from the Google Code Jam server: '
                             '{0}\n'.format(e))

  # Check if the status is not good.
  if status != 200 or reason != 'OK':
    raise error.ServerError('Error while communicating with the server, cannot '
                            'get middleware tokens. Check that the host, '
                            'username and contest id are valid.\n')

  # Extract token information from server response.
  try:
    tokens_info = json.loads(response)
    return tokens_info['tokens'], tokens_info['expire']
  except (KeyError, ValueError) as e:
    raise error.ServerError('Invalid response received from the server, cannot '
                            'initialize contest. Check that the contest id is '
                            'valid: {0}.\n'.format(e))


def _UTCToLocalDatetime(date_string, input_format, output_format=None):
  """Convert a date string to UTC into a possible different format.

  Args:
    date_string: String with the datetime to be converted.
    input_format: Format used to parse date_string, as expected by strptime.
    output_format: Format used to format the converted datetime. If None,
      input_format is used.

  Returns:
    The date string converted to UTC and formatted with output_format (or
    input_format if output_format is None).
  """
  if output_format is None:
    output_format = input_format
  parsed_utc_datetime = datetime.strptime(date_string, input_format)
  offset = time.altzone if time.daylight else time.timezone
  local_datetime = parsed_utc_datetime - timedelta(seconds=offset)
  return local_datetime.strftime(output_format)


def Login(password=None):
  """Renew contest cookie for the specified user in the host.

  Args:
    password: Password of the code jam contestant. If None, then the password
        will be retrieved using the GetUserPassword() function.

  Returns:
    The new contest cookie for the contestant.

  Raises:
    error.ConfigurationError: If the configuration file is missing or
      incomplete.
  """
  # Read the current configuration file and extract the host and username.
  try:
    contest_data = data_manager.ReadData()
    host = contest_data['host']
    user = contest_data['user']
  except KeyError as e:
    raise error.ConfigurationError('No host or username was found in the user '
                                   'configuration file: {0}.\n'.format(e))

  # Before doing anything, check that this tool version is valid.
  CheckToolVersion(host, constants.VERSION)

  # Retrieve the password from elsewhere, as the user didn't provide one.
  if password is None:
    password = _GetUserPassword(user, contest_data)

  # Log in into Google servers using ClientLogin and show the cookie expiration
  # date in localtime.
  _, cookie = MakeLogin(host, user, password)
  cookie_expiration_time = google_login.GetCookieExpirationTime(cookie)
  if cookie_expiration_time is not None:
    sys.stdout.write('Login cookie will expire at {0}.\n'.format(
        _UTCToLocalDatetime(cookie_expiration_time,
                            '%a, %d-%b-%Y %H:%M:%S %Z',
                            '%Y-%m-%d %H:%M:%S')))
  else:
    sys.stdout.write('Login cookie expiration time not found.\n')

  # Get new middleware tokens and show the expiration date in localtime.
  middleware_tokens, tokens_expiration_time = _GetMiddlewareTokens(host, cookie)
  sys.stdout.write('Middleware tokens will expire at {0}.\n'.format(
      _UTCToLocalDatetime(tokens_expiration_time, '%Y-%m-%d %H:%M:%S')))

  # Store cookie and middleware tokens in the current configuration file.
  contest_data['cookie'] = cookie
  contest_data['middleware_tokens'] = middleware_tokens
  contest_data['tokens_expiration_time'] = tokens_expiration_time

  # Finally, write the contest data to the current data file and return the
  # cookie.
  data_manager.WriteData(contest_data)
  return cookie
