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

"""This module declares the base exception for all used exceptions."""




class CommandlineError(Exception):
  """Base exception used in the commandline tool."""
  pass


class AuthenticationError(CommandlineError):
  """Exception used when there is an error while autenticating."""
  pass


class ConfigurationError(CommandlineError):
  """Exception used for all configuration errors."""
  pass


class InternalError(CommandlineError):
  """Exception used for all internal errors."""
  pass


class NetworkError(CommandlineError):
  """Exception used for all network errors."""
  pass


class OptionError(CommandlineError):
  """Exception used for all error in the scripts' options."""
  pass


class ServerError(CommandlineError):
  """Exception used for all server errors."""
  pass


class UserError(CommandlineError):
  """Exception used for all user errors."""
  pass
