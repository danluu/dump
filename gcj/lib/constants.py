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

"""This module exposes constants used inside the tool."""



VERSION = 'v1.2-beta1'
CODEJAM_AGENT_NAME = 'cmdline-%s' % VERSION
USER_CONFIG_PATH = '{base_dir}/config/user_config.py'
CURRENT_CONFIG_PATH = '{base_dir}/config/current_config.py'


_runtime_constants = {}


def GetRuntimeConstant(key, default_value=None):
  """Get a constant from the runtime_constants dictionary.

  Args:
    key: Key used to index the dictionary when retrieving the stored value.
    default_value: Value to be returned if the key is not in the dictionary.
  """
  return _runtime_constants.get(key, default_value)


def SetRuntimeConstant(key, value):
  """Store a constant into the runtime_constants dictionary.

  Args:
    key: Key used to index the dictionary when retrieving the stored value.
    value: Value to store in the dictionary.
  """
  _runtime_constants[key] = value
