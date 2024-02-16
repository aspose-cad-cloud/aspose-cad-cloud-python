#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="WatermarkRequest.py">
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


class WatermarkRequest(CadRequest):
    """
    Request model for watermark operation.
    Initializes a new instance.

    :param drawing Input drawing
    :param output_format Output DXF, DWG, DGN, DWF, DWFX, IFC, STL, STP, STEP, CGM, GLB, GLTF, DWT, IGES, PLT, CF2, OBJ, HPGL, IGS, PCL, FBX, PDF, SVG, PNG, BMP, DIB, TIFF, TIF, JPEG, GIF, PSD, JPG, JPE, JIF, JFIF, PSD, WEBP, DCM, DICOM, JP2, J2K, JPF, JPM, JPG2, J2C, JPC, JPX, MJ2 , DJVU file format.
    :param watermark_rgb String Json model
    :param output_type_ext For output pdf format: PDF_15, PDFa_1a OR PDFa_1b. Null for another format.
    """

    def __init__(self, drawing, output_format, watermark_rgb, output_type_ext=None):
        CadRequest.__init__(self)
        self.drawing = drawing
        self.output_format = output_format
        self.watermark_rgb = watermark_rgb
        self.output_type_ext = output_type_ext

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
            raise ValueError("Missing the required parameter `drawing` when calling `watermark`")
        # verify the required parameter 'output_format' is set
        if self.output_format is None:
            raise ValueError("Missing the required parameter `output_format` when calling `watermark`")
        # verify the required parameter 'watermark_rgb' is set
        if self.watermark_rgb is None:
            raise ValueError("Missing the required parameter `watermark_rgb` when calling `watermark`")

        collection_formats = {}
        path = '/cad/watermark'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outputFormat') in path:
            path = path.replace('{' + self._lowercase_first_letter('outputFormat' + '}'), self.output_format if self.output_format is not None else '')
        else:
            if self.output_format is not None:
                query_params.append((self._lowercase_first_letter('outputFormat'), self.output_format))
        if self._lowercase_first_letter('outputTypeExt') in path:
            path = path.replace('{' + self._lowercase_first_letter('outputTypeExt' + '}'), self.output_type_ext if self.output_type_ext is not None else '')
        else:
            if self.output_type_ext is not None:
                query_params.append((self._lowercase_first_letter('outputTypeExt'), self.output_type_ext))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing is not None:
            local_var_files.append((self._lowercase_first_letter('drawing'), self.drawing))
        if self.watermark_rgb is not None:
            form_params.append((self._lowercase_first_letter('watermarkRgb'), self.watermark_rgb))

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

