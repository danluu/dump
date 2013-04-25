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

"""This module contains functions used to zip or unzip data."""



import StringIO
import gzip
import os
import zipfile

from lib import error


def UnzipData(zipped_data):
  """Unzip the specified data using a temporary file and the gzip library.

  Args:
    A byte array with the zipped data.

  Returns:
    A byte array with the unzipped data.

  Raises:
    error.InternalError: If any I/O or Unicode error occurs while unzipping the
      data.
  """
  # Uncompress the zipped data using a memory-mapped file.
  try:
    zipped_memfile = StringIO.StringIO(zipped_data)
    unzipped_file = gzip.GzipFile(fileobj=zipped_memfile, mode='rb')
    unzipped_data = unzipped_file.read()
    unzipped_file.close()
    zipped_memfile.close()
    return unzipped_data

  except UnicodeError as e:
    raise error.InternalError('Unicode error while parsing zipped data: '
                              '{0}.\n'.format(e))
  except IOError as e:
    raise error.InternalError('I/O error while decompressing unzipped data: '
                              '{0}.\n'.format(e))


def ZipData(unzipped_data):
  """Zip the specified data using a temporary file and the gzip library.

  Args:
    A byte array with the unzipped data.

  Returns:
    A byte array with the zipped data.

  Raises:
    error.InternalError: If any I/O or Unicode error occurs while unzipping the
      data.
  """
  try:
    # Compress the unzipped data into a memory-mapped file.
    zipped_memfile = StringIO.StringIO()
    zipped_file = gzip.GzipFile(fileobj=zipped_memfile, mode='wb')
    zipped_file.write(unzipped_data)
    zipped_file.close()

    # Extract the zipped data from the memory-mapped file, release it and
    # return the zipped data.
    zipped_data = zipped_memfile.getvalue()
    zipped_memfile.close()
    return zipped_data

  except UnicodeError as e:
    raise error.InternalError('Unicode error while parsing zipped data: '
                              '{0}.\n'.format(e))
  except IOError as e:
    raise error.InternalError('I/O error while decompressing unzipped data: '
                              '{0}.\n'.format(e))


def MakeZipFile(source_files, output_file, ignore_exts=None):
  """Create a zip file with the specified source files.

  The source_files sequence can include directories, which will be traversed and
  added recursively to the output file, ignoring those with banned extensions.

  Args:
    source_files: A collection with all source files or directories to zip.
    output_file: Name or file-like object where the zip file must be generated.
    ignore_exts: A collection with all the extensions to ignore.

  Returns:
    A list with all the ignored files during the zip file creation.

  Raises:
    error.InternalError: If any I/O or OS error occurs while zipping the data.
  """
  if ignore_exts is None:
    ignore_exts = []

  try:
    # Open the destination zip file and initialize the ignored files set.
    zip_file = zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED)
    ignored_files = set()

    # Put all specified sources in the zip file, ignoring files with the
    # specified extensions.
    for source_filename in source_files:
      # If the source is a directory, walk over it, adding each file inside it.
      if os.path.isdir(source_filename):
        # Walk over the specified directory.
        for dirpath, dirnames, filenames in os.walk(source_filename):
          # Create the directory inside the zip file and process all
          # files in the current directory.
          zip_file.write(dirpath)
          for filename in filenames:
            # Create the base filename and check if it extension is not in the
            # extenstions ignore list. Otherwise, add it to the ignored files
            # set.
            base_filename = os.path.join(dirpath, filename)
            if os.path.splitext(filename)[1] not in ignore_exts:
              zip_file.write(base_filename)
            else:
              ignored_files.add(base_filename)
      else:
        # Add a file to the zip if and only if it extension is not in the
        # ignore list. Otherwise, add it to the ignored files set.
        if os.path.splitext(source_filename)[1] not in ignore_exts:
          zip_file.write(source_filename)
        else:
          ignored_files.add(source_filename)

    # Close the zip file and return the ignored files set.
    zip_file.close()
    return ignored_files

  except IOError as e:
    raise error.InternalError('I/O error while creating zip file: '
                              '{0}.\n'.format(e))

  except OSError as e:
    raise error.InternalError('OS error while creating zip file: '
                              '{0}.\n'.format(e))


def MakeZipFileInMemory(source_files, ignore_exts=None):
  """Create a zip file with the specified source files in memory.

  The source_files sequence can include directories, which will be traversed and
  added recursively to the output file, ignoring those with banned extensions.

  Args:
    source_files: A collection with all source files or directories to zip.
    ignore_exts: A collection with all the extensions to ignore.

  Returns:
    A (zip_output, ignored_files) tuple, where zip_output are the contents of
    the generated zip file and ignored_files is a list with all the ignored
    files during the zip file creation.

  Raises:
    error.InternalError: If any Unicode error occurs while zipping the data.
  """
  # Create a memory-mapped file and create the zip file on it. Then, get its
  # contents, close the file and return.
  try:
    output_file = StringIO.StringIO()
    ignored_files = MakeZipFile(source_files, output_file, ignore_exts)
    zip_output = output_file.getvalue()
    output_file.close()
    return zip_output, ignored_files

  except UnicodeError as e:
    raise error.InternalError('Unicode error while parsing zipped data: '
                              '{0}.\n'.format(e))
