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

"""This module exposes a class to submit solutions to the codejam server."""



import glob
import httplib
import json
import os
import random
import shutil
import sys

from lib import constants
from lib import error
from lib import http_interface
from lib import multipart_data
from lib import zip_utils


class OutputSubmitter(object):
  """Class to submit outputs from a specific problem."""
  def __init__(self, host, cookie, middleware_token, contest_id, problem_id):
    """Initialize an output submitter for a specific problem.

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

  def _PrepareSourceFiles(self, source_patterns):
    """Zip all source directories into files and return them.

    The returned list will contain (filename, file_data) tuples, where file_data
    will be None for files that have not been read yet.

    Args:
      source_patterns: List with all the file patterns to include with the
        solution. These file patterns will be expanded using python's glob
        module.

    Returns:
      A (source_files, ignored_zips) tuple, where source_files is a list of
      (filename, file_data) tuples with the files to submits, and ignored_zips
      is a set with all zip files found within zipped directories.
    """
    # Initialze set for the source names, the ignored zip files and all
    # temporary created files.
    source_files = []
    ignored_zips = set()

    # Process each source pattern specified by the user, expanding them using
    # the python's glob module.
    for source_pattern in source_patterns:
      for source in glob.iglob(source_pattern):
        # Check if the source is a directory or a file.
        if os.path.isdir(source):
          # Create a zip file in memory for the directory, add it to the source
          # files and update the ignored_zips set.
          sys.stdout.write('Compressing directory "{0}"...\n'.format(source))
          zipped_contents, newly_ignored_zips = (
              zip_utils.MakeZipFileInMemory([source], ignore_exts=['.zip']))
          ignored_zips.update(newly_ignored_zips)
          flat_source_name = source.replace('\\', '_').replace('/', '_')
          zip_filename = '{1}_{0}.zip'.format(random.randrange(0, 2**31 - 1),
                                              flat_source_name)
          source_files.append((zip_filename, zipped_contents))
        else:
          # Add files directly to the prepared sources.
          source_files.append((source, None))

    # Return all generated sets.
    return source_files, ignored_zips

  def _ParseResult(self, response_data, io_set_public):
    """Extract the result from the server response data.

    Args:
      response_data: The response body obtained from the server, which is
        formatted like a python dictionary.
      io_set_public: Boolean indicating whether the answer is public or not.

    Returns:
      The returned message from the server, or the string 'No message found' if
      there was no answer message.

    Raises:
      error.ServerError: If the server response is malformed.
    """
    # Convert the response data to a dictionary and return the message.
    try:
      result = json.loads(response_data)
      msg = result.get('msg', 'No message found')
      if not result.get('hasAnswer', False):
        return 'Rejected: ' + msg
      elif not io_set_public:
        return 'Submitted: ' + msg
      elif result.get('ok', False):
        return 'Correct: ' + msg
      else:
        return 'Incorrect: ' + msg
    except ValueError as e:
      raise error.ServerError('Invalid response received from the server, '
                              'cannot submit solution. Check that the host, '
                              'user and contest id are valid: {0}.\n'.format(e))

  def Submit(self, input_id, output_name, source_patterns, io_set_public,
             gzip_body=True, zip_sources=False, add_ignored_zips=False):
    """Submit the specified output and sources file to the problem.

    Args:
      input_id: Identifier of the output to submit ('0' for the small output,
        '1' for the large output).
      output_name: Name of the file with the output data.
      source_patterns: Name patterns of the source files to be included with the
        output. These patterns will be expanded using Python's glob module.
      io_set_public: Boolean indicating whether the answer is public or not.
      gzip_body: Boolean indicating whether the body has to be gzipped or not.
      zip_sources: Boolean indicating whether all sources should be put inside a
        zip file or not.
      add_ignored_zips: Boolean indicating whether zip files that are not
        included directly but are inside a included directory should be
        submitted or not.

    Raises:
      error.InternalError: If an error occurs while copying ignored zip files
        to the final location.
      error.NetworkError: If a network error occurs while communicating with the
        server.
      error.ServerError: If the server answers code distinct than 200.
    """
    # Prepare the source files (zipping all directories). After this,
    # source_files will only contain text files and zip files specified directly
    # or by compressing a directory.
    source_files, ignored_zips = self._PrepareSourceFiles(set(source_patterns))

    # Check if the user requested to zip source files.
    if zip_sources:
      # Extract all files to zip into a list and remove them from the
      # source files list.
      sources_to_zip = [filename
                        for filename, file_data in source_files
                        if file_data is None]
      source_files = [(filename, file_data)
                      for filename, file_data in source_files
                      if file_data is not None]

      # Generate a zip file with all the flat source files.
      sys.stdout.write('Compressing files "{0}"...\n'.format(
          ', '.join(sources_to_zip)))
      zipped_sources, _ = zip_utils.MakeZipFileInMemory(
          sources_to_zip, ignore_exts=['.zip'])

      # Generate a random name for the zipped source files and add it to the
      # source files to send.
      zip_filename = '__plain_files_{0}.zip'.format(
          random.randrange(0, 2**31 - 1))
      source_files.append((zip_filename, zipped_sources))

    # Check if the user requested to add the ignored zip files inside included
    # directories.
    if add_ignored_zips:
      # Copy and add each ignored file to the source list.
      for ignored_zip in ignored_zips:
        # Read the contents of the ignored zip file.
        try:
          zip_file = open(ignored_zip, 'rb')
          zip_file_contents = zip_file.read()
          zip_file.close()
        except IOError as e:
          raise error.InternalError('I/O error happened while read zip file '
                                    '"{0}": {1}.\n'.format(ignored_zip, e))

        # Generate the zip flat filename by substituting path with underscores
        # and adding a random number to prevent collisions. Then use it to add
        # the zip file and its contents into the source files to send.
        path, ext = os.path.splitext(ignored_zip)
        zip_flat_filename = '{1}_{0}{2}'.format(
            random.randrange(0, 2**31 - 1),
            path.replace('\\', '_').replace('/', '_'), ext)
        source_files.append((zip_flat_filename, zip_file_contents))

    # Print message and check that at least one source file was included.
    if source_files:
      sources_str = ', '.join('"{0}"'.format(filename)
                              for filename, _ in source_files)
      sys.stdout.write('Sending output file "{0}" and source(s) {1} to "{2}"'
                       '...\n'.format(output_name, sources_str, self.host))
    else:
      # Print warning saying that no source file is being included, this might
      # cause disqualification in a real contest.
      sys.stdout.write('Warning, no source files are being sent for output '
                       'file "{0}"!\n'.format(output_name))
      sys.stdout.write('Sending output file "{0}" to "{1}"...\n'.format(
          output_name, self.host))

    # Generate a random boundary string to separate multipart data and
    # create a multipart data object with it. Then fill it with the necessary
    # arguments.
    multipart_boundary = '----gcjMultipartBoundary{0}'.format(
        random.randrange(0, 2**31 - 1))
    body_data = multipart_data.MultipartData(multipart_boundary)
    body_data.AddString('csrfmiddlewaretoken', self.middleware_token)
    body_data.AddFile('answer', output_name)
    for i, (filename, file_data) in enumerate(source_files):
      body_data.AddFile('source-file{0}'.format(i), filename, file_data)
      body_data.AddString('source-file-name{0}'.format(i), filename)
    body_data.AddString('cmd', 'SubmitAnswer')
    body_data.AddString('contest', self.contest_id)
    body_data.AddString('problem', self.problem_id)
    body_data.AddString('input_id', input_id)
    body_data.AddString('num_source_files', str(len(source_files)))
    body_data.AddString('agent', constants.CODEJAM_AGENT_NAME)

    # Get the message body and check if compression was requested.
    request_body = str(body_data)
    if gzip_body:
      compressed_body = zip_utils.ZipData(request_body)
      sys.stdout.write('Sending {0} bytes to server ({1} uncompressed)'
                       '...\n'.format(len(compressed_body),
                                      len(request_body)))
      request_body = compressed_body
    else:
      sys.stdout.write('Sending {0} bytes to server...\n'.format(
          len(request_body)))

    # Send an HTTP request with the output file and the source files.
    request_url = '/codejam/contest/dashboard/do'
    request_referer = 'http://{0}/codejam/contest/dashboard?c={1}'.format(
        self.host, self.contest_id)
    request_arguments = {}
    request_headers = {
        'Content-Encoding': 'gzip' if gzip_body else 'text/plain',
        'Content-Type': 'multipart/form-data; boundary={0}'.format(
            multipart_boundary),
        'Referer': request_referer,
        'Cookie': self.cookie,
        }
    try:
      status, reason, response = http_interface.Post(
          self.host, request_url, request_arguments, request_headers,
          request_body)
    except httplib.HTTPException as e:
      raise error.NetworkError('HTTP exception while sending solution to the '
                               'Google Code Jam server: {0}.\n'.format(e))

    # Check if the status is not good.
    if status != 200 or reason != 'OK':
      raise error.ServerError('Error while communicating with the server, '
                              'cannot submit solution. Check that the host, '
                              'username and contest id are valid.\n')

    # Check if the server accepted the input or just ignored it. If it
    # accepted it, parse the response and print the submission result.
    if response:
      submit_result = self._ParseResult(response, io_set_public)
      sys.stdout.write('{0}\n'.format(submit_result))
    else:
      raise error.ServerError(
          'No response received from the server. This generally happens if '
          'you try to submit the large output before solving the small '
          'input.\n')
