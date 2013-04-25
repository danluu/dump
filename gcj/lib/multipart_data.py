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



import mimetypes

from lib import error


class MultipartData(object):
  """Class to manage multipart data in HTTP requests."""
  def __init__(self, boundary):
    """Initialize the object data empty and store the used boundary.

    Args:
      boundary: Boundary used to separate multipart data elements.
    """
    self.data = []
    self.boundary = boundary

  def __str__(self):
    """Convert this multipart data to a readable string.

    Returns:
      A string with the body of the HTTP packet that will contain the multipart
      data.
    """
    return "\r\n".join(self.data + ['--' + self.boundary + '--', ''])

  def _GetContentType(self, filename):
    """Guess the content type of a file given its name.

    Args:
      filename: Name of the file whose mimetype should be guessed.

    Returns:
      The guessed mimetype for the file, or 'application/octet-stream' if no
      guess could be made.
    """
    guessed_type = mimetypes.guess_type(filename)[0]
    return guessed_type if guessed_type != None else 'application/octet-stream'

  def AddFile(self, name, filename, file_data=None):
    """Add a file's contents to this multipart data.

    Args:
      name: Name of the element to add to the multipart data.
      filename: Name of the file with the contents to add to the multipart data.
      file_data: Data of the file to be added. If None, the data will be read
          from this file instead. This parameter is here to support
          memory-mapped files.

    Raises:
      error.InternalError: If a problem occurs when reading the file.
    """
    # Read the data from the specified file.
    if file_data is None:
      try:
        file_obj = open(filename, 'rb')
        file_data = file_obj.read()
        file_obj.close()
      except IOError as e:
        raise error.InternalError('I/O error while reading file "{0}": '
                                  '{1}.\n'.format(filename, e))

    # Append the metadata and then the read file data. Finally, complete with
    # a closing boundary.
    self.data.append('--' + self.boundary)
    self.data.append('Content-Disposition: form-data; name="{0}"; '
                     'filename="{1}"'.format(name, filename))
    self.data.append('Content-Type: {0}'.format(
        self._GetContentType(filename)))
    self.data.append('')
    self.data.append(file_data)

  def AddString(self, name, value):
    """Add a string value to this multipart data.

    Args:
      name: Name of the element to add to the multipart data.
      value: String with the contents to add to the multipart data.
    """
    # Append the field metadata and then the value. Finally, complete with a
    # closing boundary.
    self.data.append('--' + self.boundary);
    self.data.append('Content-Disposition: form-data; name="{0}"'.format(name))
    self.data.append('')
    self.data.append(str(value))
