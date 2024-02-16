#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="EditMetadata2Request.py">
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


class EditMetadata2Request(CadRequest):
    """
    Request model for edit_metadata2 operation.
    Initializes a new instance.

    :param drawing Input drawing
    :param metadata_component Drawing components in string Json format that can be edited.
    """

    def __init__(self, drawing, metadata_component):
        CadRequest.__init__(self)
        self.drawing = drawing
        self.metadata_component = metadata_component

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: http_request configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing' is set
        if self.drawing is None:
            raise ValueError("Missing the required parameter `drawing` when calling `edit_metadata2`")
        # verify the required parameter 'metadata_component' is set
        if self.metadata_component is None:
            raise ValueError("Missing the required parameter `metadata_component` when calling `edit_metadata2`")

        collection_formats = {}
        path = '/cad/editMetadata'
        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing is not None:
            local_var_files.append((self._lowercase_first_letter('drawing'), self.drawing))
        if self.metadata_component is not None:
            form_params.append((self._lowercase_first_letter('metadataComponent'), self.metadata_component))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['application/octet-stream', 'multipart/form-data'])

        # Authentication setting
        auth_settings = ['JWT']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
