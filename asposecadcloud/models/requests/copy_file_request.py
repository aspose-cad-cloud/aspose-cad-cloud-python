#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="CopyFileRequest.py">
#    Copyright (c) 2018-2019 Aspose Pty Ltd. All rights reserved.
#  </copyright>
#  <summary>
#    Permission is hereby granted, free of charge, to any person obtaining a
#   copy  of this software and associated documentation files (the "Software"),
#   to deal  in the Software without restriction, including without limitation
#   the rights  to use, copy, modify, merge, publish, distribute, sublicense,
#   and/or sell  copies of the Software, and to permit persons to whom the
#   Software is  furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in
#   all  copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#   FROM,  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#   DEALINGS IN THE SOFTWARE.
#  </summary>
#  -----------------------------------------------------------------

from asposecadcloud.models.requests.cad_request import CadRequest
from asposecadcloud.models.requests.http_request import HttpRequest


class CopyFileRequest(CadRequest):
    """
    Request model for copy_file operation.
    Initializes a new instance.

    :param src_path Source file path e.g. '/folder/file.ext'
    :param dest_path Destination file path
    :param src_storage_name Source storage name
    :param dest_storage_name Destination storage name
    :param version_id File version ID to copy
    """

    def __init__(self, src_path, dest_path, src_storage_name=None, dest_storage_name=None, version_id=None):
        CadRequest.__init__(self)
        self.src_path = src_path
        self.dest_path = dest_path
        self.src_storage_name = src_storage_name
        self.dest_storage_name = dest_storage_name
        self.version_id = version_id

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: http_request configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'src_path' is set
        if self.src_path is None:
            raise ValueError("Missing the required parameter `src_path` when calling `copy_file`")
        # verify the required parameter 'dest_path' is set
        if self.dest_path is None:
            raise ValueError("Missing the required parameter `dest_path` when calling `copy_file`")

        collection_formats = {}
        path = '/cad/storage/file/copy/{srcPath}'
        path_params = {}
        if self.src_path is not None:
            path_params[self._lowercase_first_letter('srcPath')] = self.src_path

        query_params = []
        if self._lowercase_first_letter('destPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('destPath' + '}'), self.dest_path if self.dest_path is not None else '')
        else:
            if self.dest_path is not None:
                query_params.append((self._lowercase_first_letter('destPath'), self.dest_path))
        if self._lowercase_first_letter('srcStorageName') in path:
            path = path.replace('{' + self._lowercase_first_letter('srcStorageName' + '}'), self.src_storage_name if self.src_storage_name is not None else '')
        else:
            if self.src_storage_name is not None:
                query_params.append((self._lowercase_first_letter('srcStorageName'), self.src_storage_name))
        if self._lowercase_first_letter('destStorageName') in path:
            path = path.replace('{' + self._lowercase_first_letter('destStorageName' + '}'), self.dest_storage_name if self.dest_storage_name is not None else '')
        else:
            if self.dest_storage_name is not None:
                query_params.append((self._lowercase_first_letter('destStorageName'), self.dest_storage_name))
        if self._lowercase_first_letter('versionId') in path:
            path = path.replace('{' + self._lowercase_first_letter('versionId' + '}'), self.version_id if self.version_id is not None else '')
        else:
            if self.version_id is not None:
                query_params.append((self._lowercase_first_letter('versionId'), self.version_id))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
