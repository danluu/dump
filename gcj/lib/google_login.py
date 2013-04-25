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

"""This module exposes one function Login(), that authenticates user into the
Google services, returning an authentication token and a cookie."""



from datetime import datetime, timedelta
import time
import urllib
import urllib2


class AuthenticationError(urllib2.HTTPError):
  """Exception class to indicate an error when authenticating with Google's
  ClientLogin.
  """
  def __init__(self, url, code, message, headers, args):
    """Initialize the error with the specified arguments."""
    super(AuthenticationError, self).__init__(url, code, message,
                                              headers, None)
    self.args = args
    self.reason = args["Error"]


def _GetHTTPOpener():
  """Create an http opener used to interact with Google's ClientLogin.

  Returns:
    An http opener capable of handling anything needed to interact with
    Google's ClientLogin.
  """
  # Create an http opener capable of handling proxies, http and https.
  opener = urllib2.OpenerDirector()
  opener.add_handler(urllib2.ProxyHandler())
  opener.add_handler(urllib2.UnknownHandler())
  opener.add_handler(urllib2.HTTPHandler())
  opener.add_handler(urllib2.HTTPDefaultErrorHandler())
  opener.add_handler(urllib2.HTTPErrorProcessor())
  opener.add_handler(urllib2.HTTPSHandler())
  return opener


def _ParseBodyAsDict(body):
  """ Parse the specified body as a dictionary with each element in a line, and
  key value pairs separated by '='.

  Args:
    body: The string with the HTTP body to parse.

  Returns:
    A dictionary with the body contents.
  """
  return dict(line.split('=') for line in body.split('\n') if line)


def _GetGoogleAuthtoken(account_type, user, password, service, source):
  """This function authenticates the user in the specified service using
  the provided authentication data.

  Args:
    account_type: Type of the account to login, could be GOOGLE or any other
        string if the account is external.
    user: Name of the user to be logged in.
    password: Password of the user to be logged in.
    service: Service where the user wants to log in, for example, 'ah'.
    source: Name of the application requesting the user authentication.

  Returns:
    The authentatication token for the user if the supplied data is correct.

  Raises:
    lib.AuthenticationError: This exception is raised if the HTTP response is
       403 - Forbidden, in this case the error is parsed and returned to the
       user in the exception.

    urllib2.HTTPError: This exception is raised for any other HTTP error.
  """
  # Create a request for Google's Client login, with the specied data.
  auth_request_data_map = {
    'accountType': account_type,
    'Email': user,
    'Passwd': password,
    'service': service,
    'source': source
  }
  auth_request_data = urllib.urlencode(auth_request_data_map)
  auth_url = 'https://www.google.com/accounts/ClientLogin'
  auth_request = urllib2.Request(auth_url, auth_request_data)

  try:
    # Create a custom opener, make the request and extract the body.
    http_opener = _GetHTTPOpener()
    auth_response = http_opener.open(auth_request)
    auth_response_body = auth_response.read()

    # Parse the response data as a dictionary and return the 'Auth' key.
    auth_response_data = _ParseBodyAsDict(auth_response_body)
    return auth_response_data['Auth']

  except urllib2.HTTPError as e:
    # Check if the error was a 403 - Forbidden. In that case, forward the
    # exception as an authentication error. Otherwise, just forward the
    # exception.
    if e.code == 403:
      # Parse the error body as a dictionary and forward the exception as an
      # authentication error.
      response_dict = _ParseBodyAsDict(e.read())
      raise AuthenticationError(auth_request.get_full_url(), e.code, e.msg,
                                e.headers, response_dict)
    else:
      raise


def _GetGaeCookie(host, service, auth_token, secure):
  """This function creates a login cookie using the authentication token
  obtained after logging in successfully in the Google account.

  Args:
    host: Host where the user wants to login.
    service: Service code where the user wants to login.
    auth_token: Authentication token obtained from ClientLogin.
    secure: True if we want a secure cookie, false if not.

  Returns:
    A cookie for the specifed service.

  Raises:
    urllib2.HTTPError: This exception is raised when the cookie cannot be
        obtained and the user is redirected to another place.
  """
  # Create a request for Google's service with the authentication token.
  continue_location = 'http://localhost/'
  cookie_request_data_map = {
    'continue' : continue_location,
    'auth'     : auth_token,
  }
  cookie_request_data = urllib.urlencode(cookie_request_data_map)
  cookie_url = '{protocol}://{host}/_{service}/login?{data}'.format(
    protocol=('https' if secure else 'http'), host=host, service=service,
    data=cookie_request_data)
  cookie_request = urllib2.Request(cookie_url)

  try:
    # Create a custom opener, make the request and extract the body.
    http_opener = _GetHTTPOpener()
    cookie_response = http_opener.open(cookie_request)
  except urllib2.HTTPError as e:
    # Keep the error as the cookie response.
    cookie_response = e

  # Check that a redirection was made to the required continue location.
  # Otherwise, return an HTTP error.
  response_code = cookie_response.code
  if (response_code != 302 or
      cookie_response.info()['location'] != continue_location):
    raise urllib2.HTTPError(cookie_request.get_full_url(), response_code,
                            cookie_response.msg, cookie_response.headers,
                            cookie_response.fp)

  # Extract the cookie from the headers and remove 'HttpOnly' from it.
  cookie = cookie_response.headers.get('Set-Cookie')
  return cookie.replace('; HttpOnly', '')


def Login(host, account_type, user, password, service, source, secure):
  """Retrieve the authentication token and cookie from the specified service,
  using the given user and password to authenticate.

  Args:
    host: Host where the user wants to login.
    account_type: Type of the account to login, could be GOOGLE or any other
        string if the account is external.
    user: Name of the user to be logged in.
    password: Password of the user to be logged in.
    service: Service where the user wants to log in, for example, 'ah'.
    source: Name of the application requesting the user authentication.
    secure: True if we want a secure cookie, false if not.

  Returns:
    A tuple with the authentication token and a cookie for the specifed service.
  """
  auth_token = _GetGoogleAuthtoken(account_type, user, password, service,
                                   source)
  cookie = _GetGaeCookie(host, service, auth_token, secure)
  return auth_token, cookie


def _ParseCookieFields(cookie):
  # Fields inside the cookie are separated by a semicolon, so split the cookie
  # and process each token as a field.
  cookie_fields = {}
  for token in cookie.split(';'):
    # Keys and values are separated by a single equal in the field, or they
    # might be keys without values. In this case, use True as the field value.
    equal_index = token.find('=')
    if equal_index == -1:
      field_name = token.strip()
      field_value = True
    else:
      field_name = token[:equal_index].strip()
      field_value = token[equal_index + 1:].strip()
    cookie_fields[field_name] = field_value
  return cookie_fields


def GetCookieExpirationTime(cookie):
  """Extract and return the expiration time in the cookie.

  Args:
    cookie: String with the cookie whose expiration time must be retrieved.

  Returns:
    A string with the cookie expiration time, or None if the expiration field\
    was not found. The expiration time is returned in UTC.
  """
  # Parse the cookie fields and look for an expiration field, and return None if
  # the cookie has no expiration date.
  cookie_fields = _ParseCookieFields(cookie)
  return cookie_fields.get('expires')


def CookieHasExpired(cookie):
  """Checks whether the specified cookie expired or not.

  Args:
    cookie: String with the cookie information.

  Returns:
    True if the cookie has expired, false otherwise.
  """
  # Get the cookie expiration time, if it is not found just assume the cookie
  # has not expired yet.
  expiration_time_string = GetCookieExpirationTime(cookie)
  if expiration_time_string is None:
    return False

  # Parse the cookie expiration time and check if there are at least 5 minutes
  # before expiration, otherwise the cookie might expire after this function
  # exits but before the user action is complete.
  expiration_time = datetime.strptime(expiration_time_string,
                                      '%a, %d-%b-%Y %H:%M:%S %Z')
  offset = time.altzone if time.daylight else time.timezone
  today_gmt_time = datetime.today() + timedelta(seconds=offset)
  time_left = expiration_time - today_gmt_time
  return time_left < timedelta(minutes=5)
