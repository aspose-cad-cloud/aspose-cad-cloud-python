#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="cad_api.py">
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
#  ----------------------------------------------------------------------------

from __future__ import absolute_import

import six

from asposecadcloud.api_client import ApiClient
from asposecadcloud.configuration import Configuration
from asposecadcloud.rest import ApiException


class CadApi(object):
    """
    Aspose.CAD Cloud API

    """

    def __init__(self, app_key=None, app_sid=None, base_url=None,
                 api_version=None, debug=False, proxy=None):
        """
        Initializes a new instance of the CadApi class.

        :param app_key: The app key.
        :param app_sid: The app sid.
        :param base_url: The base URL.
        :param api_version: API version.
        :param debug: If debug mode is enabled. False by default.
		:param proxy: proxy url if needed.
        :param on_premise:
            True for on-premise solution with metered license usage.
            False for Aspose Cloud-hosted solution usage, default.
        """
        configuration = Configuration(app_key=app_key,
                                      app_sid=app_sid,
                                      base_url=base_url,
                                      api_version=api_version,
                                      debug=debug,
									  proxy=proxy)
        self.api_client = ApiClient(configuration)

    def convert(self, request):
        """Convert CAD drawing to DXF, DWG, DGN, DWF, DWFX, IFC, STL, STP, STEP, CGM, GLB, GLTF, DWT, IGES, PLT, CF2, OBJ, HPGL, IGS, PCL, FBX, PDF, SVG format.


        :param request convert_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def convert_async(self, request):
        """Convert CAD drawing to DXF, DWG, DGN, DWF, DWFX, IFC, STL, STP, STEP, CGM, GLB, GLTF, DWT, IGES, PLT, CF2, OBJ, HPGL, IGS, PCL, FBX, PDF, SVG format.


        :param request convert_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def copy_file(self, request):
        """Copy file


        :param request copy_file_request object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', None)

    def copy_file_async(self, request):
        """Copy file


        :param request copy_file_request object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', None)

    def copy_folder(self, request):
        """Copy folder


        :param request copy_folder_request object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', None)

    def copy_folder_async(self, request):
        """Copy folder


        :param request copy_folder_request object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', None)

    def create_folder(self, request):
        """Create the folder


        :param request create_folder_request object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', None)

    def create_folder_async(self, request):
        """Create the folder


        :param request create_folder_request object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', None)

    def delete_file(self, request):
        """Delete file


        :param request delete_file_request object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'DELETE', None)

    def delete_file_async(self, request):
        """Delete file


        :param request delete_file_request object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'DELETE', None)

    def delete_folder(self, request):
        """Delete folder


        :param request delete_folder_request object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'DELETE', None)

    def delete_folder_async(self, request):
        """Delete folder


        :param request delete_folder_request object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'DELETE', None)

    def download_file(self, request):
        """Download file


        :param request download_file_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'GET', 'file')

    def download_file_async(self, request):
        """Download file


        :param request download_file_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'GET', 'file')

    def edit_metadata(self, request):
        """Get Metadata info


        :param request edit_metadata_request object with parameters
        :return: str
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'str')

    def edit_metadata_async(self, request):
        """Get Metadata info


        :param request edit_metadata_request object with parameters
        :return: str
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'str')

    def extract_metadata(self, request):
        """Extract Metadata from CAD drawing to txt, xml or json file.


        :param request extract_metadata_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def extract_metadata_async(self, request):
        """Extract Metadata from CAD drawing to txt, xml or json file.


        :param request extract_metadata_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def extract_text(self, request):
        """Extract Text from CAD drawing to txt file


        :param request extract_text_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def extract_text_async(self, request):
        """Extract Text from CAD drawing to txt file


        :param request extract_text_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def get_disc_usage(self, request):
        """Get disc usage


        :param request get_disc_usage_request object with parameters
        :return: DiscUsage
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'GET', 'DiscUsage')

    def get_disc_usage_async(self, request):
        """Get disc usage


        :param request get_disc_usage_request object with parameters
        :return: DiscUsage
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'GET', 'DiscUsage')

    def get_drawing_properties(self, request):
        """Retrieves info about an existing drawing.             


        :param request get_drawing_properties_request object with parameters
        :return: CadResponse
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'GET', 'CadResponse')

    def get_drawing_properties_async(self, request):
        """Retrieves info about an existing drawing.             


        :param request get_drawing_properties_request object with parameters
        :return: CadResponse
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'GET', 'CadResponse')

    def get_drawing_resize(self, request):
        """Resize an existing drawing.


        :param request get_drawing_resize_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'GET', 'file')

    def get_drawing_resize_async(self, request):
        """Resize an existing drawing.


        :param request get_drawing_resize_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'GET', 'file')

    def get_drawing_rotate_flip(self, request):
        """Rotate/flip an existing drawing.


        :param request get_drawing_rotate_flip_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'GET', 'file')

    def get_drawing_rotate_flip_async(self, request):
        """Rotate/flip an existing drawing.


        :param request get_drawing_rotate_flip_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'GET', 'file')

    def get_drawing_save_as(self, request):
        """Export an existing drawing to another format.


        :param request get_drawing_save_as_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'GET', 'file')

    def get_drawing_save_as_async(self, request):
        """Export an existing drawing to another format.


        :param request get_drawing_save_as_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'GET', 'file')

    def get_file_versions(self, request):
        """Get file versions


        :param request get_file_versions_request object with parameters
        :return: FileVersions
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'GET', 'FileVersions')

    def get_file_versions_async(self, request):
        """Get file versions


        :param request get_file_versions_request object with parameters
        :return: FileVersions
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'GET', 'FileVersions')

    def get_files_list(self, request):
        """Get all files and folders within a folder


        :param request get_files_list_request object with parameters
        :return: FilesList
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'GET', 'FilesList')

    def get_files_list_async(self, request):
        """Get all files and folders within a folder


        :param request get_files_list_request object with parameters
        :return: FilesList
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'GET', 'FilesList')

    def move_file(self, request):
        """Move file


        :param request move_file_request object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', None)

    def move_file_async(self, request):
        """Move file


        :param request move_file_request object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', None)

    def move_folder(self, request):
        """Move folder


        :param request move_folder_request object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', None)

    def move_folder_async(self, request):
        """Move folder


        :param request move_folder_request object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', None)

    def object_exists(self, request):
        """Check if file or folder exists


        :param request object_exists_request object with parameters
        :return: ObjectExist
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'GET', 'ObjectExist')

    def object_exists_async(self, request):
        """Check if file or folder exists


        :param request object_exists_request object with parameters
        :return: ObjectExist
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'GET', 'ObjectExist')

    def paper_to_cad(self, request):
        """Convert bitmap image to DXF, DWG, DGN, DWF, DWFX, IFC, STL, STP, STEP, CGM, GLB, GLTF, DWT, IGES, PLT, CF2, OBJ, HPGL, IGS, PCL, FBX, SVG format.


        :param request paper_to_cad_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def paper_to_cad_async(self, request):
        """Convert bitmap image to DXF, DWG, DGN, DWF, DWFX, IFC, STL, STP, STEP, CGM, GLB, GLTF, DWT, IGES, PLT, CF2, OBJ, HPGL, IGS, PCL, FBX, SVG format.


        :param request paper_to_cad_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_bmp(self, request):
        """Export an existing drawing to BMP format with export settings specified.


        :param request post_drawing_bmp_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_bmp_async(self, request):
        """Export an existing drawing to BMP format with export settings specified.


        :param request post_drawing_bmp_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_cgm(self, request):
        """Export an existing drawing to CGM format with export settings specified.


        :param request post_drawing_cgm_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_cgm_async(self, request):
        """Export an existing drawing to CGM format with export settings specified.


        :param request post_drawing_cgm_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_dicom(self, request):
        """Export an existing drawing to Dicom format with export settings specified.


        :param request post_drawing_dicom_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_dicom_async(self, request):
        """Export an existing drawing to Dicom format with export settings specified.


        :param request post_drawing_dicom_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_dwf(self, request):
        """Export an existing drawing to Dwf format with export settings specified.


        :param request post_drawing_dwf_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_dwf_async(self, request):
        """Export an existing drawing to Dwf format with export settings specified.


        :param request post_drawing_dwf_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_dxf(self, request):
        """Export an existing drawing to DXF format with export settings specified.


        :param request post_drawing_dxf_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_dxf_async(self, request):
        """Export an existing drawing to DXF format with export settings specified.


        :param request post_drawing_dxf_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_fbx(self, request):
        """Export an existing drawing to Fbx format with export settings specified.


        :param request post_drawing_fbx_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_fbx_async(self, request):
        """Export an existing drawing to Fbx format with export settings specified.


        :param request post_drawing_fbx_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_gif(self, request):
        """Export an existing drawing into GIF format with export settings specified.


        :param request post_drawing_gif_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_gif_async(self, request):
        """Export an existing drawing into GIF format with export settings specified.


        :param request post_drawing_gif_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_glb(self, request):
        """Export an existing drawing to GLB format with export settings specified.


        :param request post_drawing_glb_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_glb_async(self, request):
        """Export an existing drawing to GLB format with export settings specified.


        :param request post_drawing_glb_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_gltf(self, request):
        """Export an existing drawing to GLTF format with export settings specified.


        :param request post_drawing_gltf_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_gltf_async(self, request):
        """Export an existing drawing to GLTF format with export settings specified.


        :param request post_drawing_gltf_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_jpeg(self, request):
        """Export an existing drawing into JPEG format with export settings specified.


        :param request post_drawing_jpeg_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_jpeg_async(self, request):
        """Export an existing drawing into JPEG format with export settings specified.


        :param request post_drawing_jpeg_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_jpeg2000(self, request):
        """Export an existing drawing into JPEG2000 format with export settings specified.


        :param request post_drawing_jpeg2000_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_jpeg2000_async(self, request):
        """Export an existing drawing into JPEG2000 format with export settings specified.


        :param request post_drawing_jpeg2000_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_obj(self, request):
        """Export an existing drawing to Obj format with export settings specified.


        :param request post_drawing_obj_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_obj_async(self, request):
        """Export an existing drawing to Obj format with export settings specified.


        :param request post_drawing_obj_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_pdf(self, request):
        """Export an existing drawing to PDF format with export settings specified.


        :param request post_drawing_pdf_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_pdf_async(self, request):
        """Export an existing drawing to PDF format with export settings specified.


        :param request post_drawing_pdf_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_png(self, request):
        """Export an existing drawing into PNG format with export settings specified.


        :param request post_drawing_png_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_png_async(self, request):
        """Export an existing drawing into PNG format with export settings specified.


        :param request post_drawing_png_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_properties(self, request):
        """Retrieves info about drawing which is passed as a zero-indexed multipart/form-data content or as raw body stream.


        :param request post_drawing_properties_request object with parameters
        :return: CadResponse
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'CadResponse')

    def post_drawing_properties_async(self, request):
        """Retrieves info about drawing which is passed as a zero-indexed multipart/form-data content or as raw body stream.


        :param request post_drawing_properties_request object with parameters
        :return: CadResponse
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'CadResponse')

    def post_drawing_psd(self, request):
        """Export an existing drawing into PSD format with export settings specified.


        :param request post_drawing_psd_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_psd_async(self, request):
        """Export an existing drawing into PSD format with export settings specified.


        :param request post_drawing_psd_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_resize(self, request):
        """Resize a drawing. Drawing data is passed as a zero-indexed multipart/form-data content or as raw body stream.


        :param request post_drawing_resize_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_resize_async(self, request):
        """Resize a drawing. Drawing data is passed as a zero-indexed multipart/form-data content or as raw body stream.


        :param request post_drawing_resize_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_rotate_flip(self, request):
        """Rotate/flip a drawing. Drawing data is passed as a zero-indexed multipart/form-data content or as raw body stream.


        :param request post_drawing_rotate_flip_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_rotate_flip_async(self, request):
        """Rotate/flip a drawing. Drawing data is passed as a zero-indexed multipart/form-data content or as raw body stream.


        :param request post_drawing_rotate_flip_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_save_as(self, request):
        """Export existing drawing to another format. Drawing data is passed as zero-indexed multipart/form-data content or as raw body stream.             


        :param request post_drawing_save_as_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_save_as_async(self, request):
        """Export existing drawing to another format. Drawing data is passed as zero-indexed multipart/form-data content or as raw body stream.             


        :param request post_drawing_save_as_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_stp(self, request):
        """Export an existing drawing to STP format with export settings specified.


        :param request post_drawing_stp_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_stp_async(self, request):
        """Export an existing drawing to STP format with export settings specified.


        :param request post_drawing_stp_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_svg(self, request):
        """Export an existing drawing to SVG format with export settings specified.


        :param request post_drawing_svg_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_svg_async(self, request):
        """Export an existing drawing to SVG format with export settings specified.


        :param request post_drawing_svg_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_three_ds(self, request):
        """Export an existing drawing to 3ds format with export settings specified.


        :param request post_drawing_three_ds_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_three_ds_async(self, request):
        """Export an existing drawing to 3ds format with export settings specified.


        :param request post_drawing_three_ds_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_tiff(self, request):
        """Export an existing drawing into TIFF format with export settings specified.


        :param request post_drawing_tiff_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_tiff_async(self, request):
        """Export an existing drawing into TIFF format with export settings specified.


        :param request post_drawing_tiff_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_u3d(self, request):
        """Export an existing drawing to U3d format with export settings specified.


        :param request post_drawing_u3d_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_u3d_async(self, request):
        """Export an existing drawing to U3d format with export settings specified.


        :param request post_drawing_u3d_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_webp(self, request):
        """Export an existing drawing to Webp format with export settings specified.


        :param request post_drawing_webp_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_webp_async(self, request):
        """Export an existing drawing to Webp format with export settings specified.


        :param request post_drawing_webp_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_wmf(self, request):
        """Export an existing drawing to WMF format with export settings specified.


        :param request post_drawing_wmf_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_wmf_async(self, request):
        """Export an existing drawing to WMF format with export settings specified.


        :param request post_drawing_wmf_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def put_drawing_bmp(self, request):
        """Export drawing to BMP format. Drawing data is passed as zero-indexed multipart/form-data as well as export BMP options serialized as JSON. Order of drawing data and BMP options could vary.


        :param request put_drawing_bmp_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_bmp_async(self, request):
        """Export drawing to BMP format. Drawing data is passed as zero-indexed multipart/form-data as well as export BMP options serialized as JSON. Order of drawing data and BMP options could vary.


        :param request put_drawing_bmp_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_cgm(self, request):
        """Export drawing to CGM format. Drawing data is passed as zero-indexed multipart/form-data as well as export CGM options serialized as JSON. Order of drawing data and CGM options could vary.


        :param request put_drawing_cgm_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_cgm_async(self, request):
        """Export drawing to CGM format. Drawing data is passed as zero-indexed multipart/form-data as well as export CGM options serialized as JSON. Order of drawing data and CGM options could vary.


        :param request put_drawing_cgm_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_dicom(self, request):
        """Export drawing to Dicom format. Drawing data is passed as zero-indexed multipart/form-data as well as export Dicom options serialized as JSON. Order of drawing data and Dicom options could vary.


        :param request put_drawing_dicom_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_dicom_async(self, request):
        """Export drawing to Dicom format. Drawing data is passed as zero-indexed multipart/form-data as well as export Dicom options serialized as JSON. Order of drawing data and Dicom options could vary.


        :param request put_drawing_dicom_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_dwf(self, request):
        """Export drawing to Dwf format. Drawing data is passed as zero-indexed multipart/form-data as well as export Dwf options serialized as JSON. Order of drawing data and Dwf options could vary.


        :param request put_drawing_dwf_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_dwf_async(self, request):
        """Export drawing to Dwf format. Drawing data is passed as zero-indexed multipart/form-data as well as export Dwf options serialized as JSON. Order of drawing data and Dwf options could vary.


        :param request put_drawing_dwf_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_dxf(self, request):
        """Export drawing to DXF format. Drawing data is passed as zero-indexed multipart/form-data as well as export DXF options serialized as JSON. Order of drawing data and DXF options could vary.


        :param request put_drawing_dxf_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_dxf_async(self, request):
        """Export drawing to DXF format. Drawing data is passed as zero-indexed multipart/form-data as well as export DXF options serialized as JSON. Order of drawing data and DXF options could vary.


        :param request put_drawing_dxf_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_fbx(self, request):
        """Export drawing to Fbx format. Drawing data is passed as zero-indexed multipart/form-data as well as export Fbx options serialized as JSON. Order of drawing data and Fbx options could vary.


        :param request put_drawing_fbx_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_fbx_async(self, request):
        """Export drawing to Fbx format. Drawing data is passed as zero-indexed multipart/form-data as well as export Fbx options serialized as JSON. Order of drawing data and Fbx options could vary.


        :param request put_drawing_fbx_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_gif(self, request):
        """Export drawing to GIF format. Drawing data is passed as zero-indexed multipart/form-data as well as export GIF options serialized as JSON. Order of drawing data and GIF options could vary.


        :param request put_drawing_gif_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_gif_async(self, request):
        """Export drawing to GIF format. Drawing data is passed as zero-indexed multipart/form-data as well as export GIF options serialized as JSON. Order of drawing data and GIF options could vary.


        :param request put_drawing_gif_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_glb(self, request):
        """Export drawing to GLB format. Drawing data is passed as zero-indexed multipart/form-data as well as export GLB options serialized as JSON. Order of drawing data and GLB options could vary.


        :param request put_drawing_glb_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_glb_async(self, request):
        """Export drawing to GLB format. Drawing data is passed as zero-indexed multipart/form-data as well as export GLB options serialized as JSON. Order of drawing data and GLB options could vary.


        :param request put_drawing_glb_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_gltf(self, request):
        """Export drawing to GLTF format. Drawing data is passed as zero-indexed multipart/form-data as well as export GLTF options serialized as JSON. Order of drawing data and GLTF options could vary.


        :param request put_drawing_gltf_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_gltf_async(self, request):
        """Export drawing to GLTF format. Drawing data is passed as zero-indexed multipart/form-data as well as export GLTF options serialized as JSON. Order of drawing data and GLTF options could vary.


        :param request put_drawing_gltf_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_jpeg(self, request):
        """Export drawing to JPEG format. Drawing data is passed as zero-indexed multipart/form-data as well as export JPEG options serialized as JSON. Order of drawing data and JPEG options could vary.


        :param request put_drawing_jpeg_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_jpeg_async(self, request):
        """Export drawing to JPEG format. Drawing data is passed as zero-indexed multipart/form-data as well as export JPEG options serialized as JSON. Order of drawing data and JPEG options could vary.


        :param request put_drawing_jpeg_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_jpeg2000(self, request):
        """Export drawing to JPEG2000 format. Drawing data is passed as zero-indexed multipart/form-data as well as export JPEG2000 options serialized as JSON. Order of drawing data and JPEG2000 options could vary.


        :param request put_drawing_jpeg2000_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_jpeg2000_async(self, request):
        """Export drawing to JPEG2000 format. Drawing data is passed as zero-indexed multipart/form-data as well as export JPEG2000 options serialized as JSON. Order of drawing data and JPEG2000 options could vary.


        :param request put_drawing_jpeg2000_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_obj(self, request):
        """Export drawing to Obj format. Drawing data is passed as zero-indexed multipart/form-data as well as export Obj options serialized as JSON. Order of drawing data and Obj options could vary.


        :param request put_drawing_obj_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_obj_async(self, request):
        """Export drawing to Obj format. Drawing data is passed as zero-indexed multipart/form-data as well as export Obj options serialized as JSON. Order of drawing data and Obj options could vary.


        :param request put_drawing_obj_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_pdf(self, request):
        """Export drawing to PDF format. Drawing data is passed as zero-indexed multipart/form-data as well as export PDF options serialized as JSON. Order of drawing data and PDF options could vary.


        :param request put_drawing_pdf_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_pdf_async(self, request):
        """Export drawing to PDF format. Drawing data is passed as zero-indexed multipart/form-data as well as export PDF options serialized as JSON. Order of drawing data and PDF options could vary.


        :param request put_drawing_pdf_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_png(self, request):
        """Export drawing to PNG format. Drawing data is passed as zero-indexed multipart/form-data as well as export PNG options serialized as JSON. Order of drawing data and PNG options could vary.


        :param request put_drawing_png_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_png_async(self, request):
        """Export drawing to PNG format. Drawing data is passed as zero-indexed multipart/form-data as well as export PNG options serialized as JSON. Order of drawing data and PNG options could vary.


        :param request put_drawing_png_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_psd(self, request):
        """Export drawing to PSD format. Drawing data is passed as zero-indexed multipart/form-data as well as export PSD options serialized as JSON. Order of drawing data and PSD options could vary.


        :param request put_drawing_psd_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_psd_async(self, request):
        """Export drawing to PSD format. Drawing data is passed as zero-indexed multipart/form-data as well as export PSD options serialized as JSON. Order of drawing data and PSD options could vary.


        :param request put_drawing_psd_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_stp(self, request):
        """Export drawing to Stp format. Drawing data is passed as zero-indexed multipart/form-data as well as export Stp options serialized as JSON. Order of drawing data and Stp options could vary.


        :param request put_drawing_stp_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_stp_async(self, request):
        """Export drawing to Stp format. Drawing data is passed as zero-indexed multipart/form-data as well as export Stp options serialized as JSON. Order of drawing data and Stp options could vary.


        :param request put_drawing_stp_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_svg(self, request):
        """Export drawing to SVG format. Drawing data is passed as zero-indexed multipart/form-data as well as export SVG options serialized as JSON. Order of drawing data and SVG options could vary.


        :param request put_drawing_svg_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_svg_async(self, request):
        """Export drawing to SVG format. Drawing data is passed as zero-indexed multipart/form-data as well as export SVG options serialized as JSON. Order of drawing data and SVG options could vary.


        :param request put_drawing_svg_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_three_ds(self, request):
        """Export drawing to 3ds format. Drawing data is passed as zero-indexed multipart/form-data as well as export 3ds options serialized as JSON. Order of drawing data and 3ds options could vary.


        :param request put_drawing_three_ds_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_three_ds_async(self, request):
        """Export drawing to 3ds format. Drawing data is passed as zero-indexed multipart/form-data as well as export 3ds options serialized as JSON. Order of drawing data and 3ds options could vary.


        :param request put_drawing_three_ds_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_tiff(self, request):
        """Export drawing to TIFF format. Drawing data is passed as zero-indexed multipart/form-data as well as export TIFF options serialized as JSON. Order of drawing data and TIFF options could vary.


        :param request put_drawing_tiff_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_tiff_async(self, request):
        """Export drawing to TIFF format. Drawing data is passed as zero-indexed multipart/form-data as well as export TIFF options serialized as JSON. Order of drawing data and TIFF options could vary.


        :param request put_drawing_tiff_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_u3d(self, request):
        """Export drawing to U3d format. Drawing data is passed as zero-indexed multipart/form-data as well as export U3d options serialized as JSON. Order of drawing data and U3d options could vary.


        :param request put_drawing_u3d_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_u3d_async(self, request):
        """Export drawing to U3d format. Drawing data is passed as zero-indexed multipart/form-data as well as export U3d options serialized as JSON. Order of drawing data and U3d options could vary.


        :param request put_drawing_u3d_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_webp(self, request):
        """Export drawing to Webp format. Drawing data is passed as zero-indexed multipart/form-data as well as export Webp options serialized as JSON. Order of drawing data and Webp options could vary.


        :param request put_drawing_webp_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_webp_async(self, request):
        """Export drawing to Webp format. Drawing data is passed as zero-indexed multipart/form-data as well as export Webp options serialized as JSON. Order of drawing data and Webp options could vary.


        :param request put_drawing_webp_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_wmf(self, request):
        """Export drawing to WMF format. Drawing data is passed as zero-indexed multipart/form-data as well as export WMF options serialized as JSON. Order of drawing data and WMF options could vary.


        :param request put_drawing_wmf_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_wmf_async(self, request):
        """Export drawing to WMF format. Drawing data is passed as zero-indexed multipart/form-data as well as export WMF options serialized as JSON. Order of drawing data and WMF options could vary.


        :param request put_drawing_wmf_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_edit_metadata(self, request):
        """Save Metadata


        :param request put_edit_metadata_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_edit_metadata_async(self, request):
        """Save Metadata


        :param request put_edit_metadata_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def storage_exists(self, request):
        """Check if storage exists


        :param request storage_exists_request object with parameters
        :return: StorageExist
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'GET', 'StorageExist')

    def storage_exists_async(self, request):
        """Check if storage exists


        :param request storage_exists_request object with parameters
        :return: StorageExist
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'GET', 'StorageExist')

    def upload_file(self, request):
        """Upload file


        :param request upload_file_request object with parameters
        :return: FilesUploadResult
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'FilesUploadResult')

    def upload_file_async(self, request):
        """Upload file


        :param request upload_file_request object with parameters
        :return: FilesUploadResult
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'FilesUploadResult')

    def viewer(self, request):
        """Return file for viewer


        :param request viewer_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def viewer_async(self, request):
        """Return file for viewer


        :param request viewer_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def watermark(self, request):
        """Add watermark to drawing


        :param request watermark_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def watermark_async(self, request):
        """Add watermark to drawing


        :param request watermark_request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def __make_request(self, HttpRequest, method, return_type):
        def call_api():
            return self.api_client.call_api(
                resource_path=HttpRequest.resource_path,
                method=method,
                path_params=HttpRequest.path_params,
                query_params=HttpRequest.query_params,
                header_params=HttpRequest.header_params,
                body=HttpRequest.body_params,
                post_params=HttpRequest.form_params,
                files=HttpRequest.files,
                response_type=return_type,
                auth_settings=HttpRequest.auth_settings,
                _return_http_data_only=HttpRequest.return_http_data_only,
                _preload_content=HttpRequest.preload_content,
                _request_timeout=HttpRequest.request_timeout,
                collection_formats=HttpRequest.collection_formats)

        try:
            return call_api()
        except ApiException as ex:
            if ex.code == 401:
                self.__request_token()
                return call_api()
            raise

    def __make_request_async(self, HttpRequest, method, return_type):
        def call_api_async():
            self.api_client.call_api_async(
                resource_path=HttpRequest.resource_path,
                method=method,
                path_params=HttpRequest.path_params,
                query_params=HttpRequest.query_params,
                header_params=HttpRequest.header_params,
                body=HttpRequest.body_params,
                post_params=HttpRequest.form_params,
                files=HttpRequest.files,
                response_type=return_type,
                auth_settings=HttpRequest.auth_settings,
                _return_http_data_only=HttpRequest.return_http_data_only,
                _preload_content=HttpRequest.preload_content,
                _request_timeout=HttpRequest.request_timeout,
                collection_formats=HttpRequest.collection_formats)

        try:
            return call_api_async()
        except ApiException as ex:
            if ex.code == 401:
                self.__request_token()
                return call_api_async()
            raise

    def __request_token(self):
        config = self.api_client.configuration
        request_url = "/connect/token"
        form_params = [('grant_type', 'client_credentials'), ('client_id', config.api_key['app_sid']),
                       ('client_secret', config.api_key['api_key'])]

        header_params = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}

        api_version = self.api_client.configuration.api_version
        self.api_client.configuration.api_version = ''

        data = self.api_client.call_api(request_url, 'POST',
                                        {},
                                        [],
                                        header_params,
                                        post_params=form_params,
                                        response_type='object',
                                        files={}, _return_http_data_only=True)
        access_token = data['access_token'] if six.PY3 else data['access_token'].encode('utf8')
        self.api_client.configuration.access_token = access_token

        self.api_client.configuration.api_version = api_version

#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="convert_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class convert_request(CadRequest):
    """
    Request model for convert operation.
    Initializes a new instance.

    :param output_format Output DXF, DWG, DGN, DWF, DWFX, IFC, STL, STP, STEP, CGM, GLB, GLTF, DWT, IGES, PLT, CF2, OBJ, HPGL, IGS, PCL, FBX, PDF, SVG, PNG, BMP, DIB, TIFF, TIF, JPEG, GIF, PSD, JPG, JPE, JIF, JFIF, PSD, WEBP, DCM, DICOM, JP2, J2K, JPF, JPM, JPG2, J2C, JPC, JPX, MJ2 , DJVU file format.
    :param drawing Form-data file
    :param output_type_ext For output pdf format: PDF_15, PDFa_1a OR PDFa_1b. Null for another format
    """

    def __init__(self, output_format, drawing=None, output_type_ext=None):
        CadRequest.__init__(self)
        self.output_format = output_format
        self.drawing = drawing
        self.output_type_ext = output_type_ext

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'output_format' is set
        if self.output_format is None:
            raise ValueError("Missing the required parameter `output_format` when calling `convert`")

        collection_formats = {}
        path = '/cad/Convert'
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

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['multipart/form-data', 'application/octet-stream'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="copy_file_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class copy_file_request(CadRequest):
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
        :return: HttpRequest configured http request
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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="copy_folder_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class copy_folder_request(CadRequest):
    """
    Request model for copy_folder operation.
    Initializes a new instance.

    :param src_path Source folder path e.g. '/src'
    :param dest_path Destination folder path e.g. '/dst'
    :param src_storage_name Source storage name
    :param dest_storage_name Destination storage name
    """

    def __init__(self, src_path, dest_path, src_storage_name=None, dest_storage_name=None):
        CadRequest.__init__(self)
        self.src_path = src_path
        self.dest_path = dest_path
        self.src_storage_name = src_storage_name
        self.dest_storage_name = dest_storage_name

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'src_path' is set
        if self.src_path is None:
            raise ValueError("Missing the required parameter `src_path` when calling `copy_folder`")
        # verify the required parameter 'dest_path' is set
        if self.dest_path is None:
            raise ValueError("Missing the required parameter `dest_path` when calling `copy_folder`")

        collection_formats = {}
        path = '/cad/storage/folder/copy/{srcPath}'
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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="create_folder_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class create_folder_request(CadRequest):
    """
    Request model for create_folder operation.
    Initializes a new instance.

    :param path Folder path to create e.g. 'folder_1/folder_2/'
    :param storage_name Storage name
    """

    def __init__(self, path, storage_name=None):
        CadRequest.__init__(self)
        self.path = path
        self.storage_name = storage_name

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'path' is set
        if self.path is None:
            raise ValueError("Missing the required parameter `path` when calling `create_folder`")

        collection_formats = {}
        path = '/cad/storage/folder/{path}'
        path_params = {}
        if self.path is not None:
            path_params[self._lowercase_first_letter('path')] = self.path

        query_params = []
        if self._lowercase_first_letter('storageName') in path:
            path = path.replace('{' + self._lowercase_first_letter('storageName' + '}'), self.storage_name if self.storage_name is not None else '')
        else:
            if self.storage_name is not None:
                query_params.append((self._lowercase_first_letter('storageName'), self.storage_name))

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="delete_file_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class delete_file_request(CadRequest):
    """
    Request model for delete_file operation.
    Initializes a new instance.

    :param path File path e.g. '/folder/file.ext'
    :param storage_name Storage name
    :param version_id File version ID to delete
    """

    def __init__(self, path, storage_name=None, version_id=None):
        CadRequest.__init__(self)
        self.path = path
        self.storage_name = storage_name
        self.version_id = version_id

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'path' is set
        if self.path is None:
            raise ValueError("Missing the required parameter `path` when calling `delete_file`")

        collection_formats = {}
        path = '/cad/storage/file/{path}'
        path_params = {}
        if self.path is not None:
            path_params[self._lowercase_first_letter('path')] = self.path

        query_params = []
        if self._lowercase_first_letter('storageName') in path:
            path = path.replace('{' + self._lowercase_first_letter('storageName' + '}'), self.storage_name if self.storage_name is not None else '')
        else:
            if self.storage_name is not None:
                query_params.append((self._lowercase_first_letter('storageName'), self.storage_name))
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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="delete_folder_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class delete_folder_request(CadRequest):
    """
    Request model for delete_folder operation.
    Initializes a new instance.

    :param path Folder path e.g. '/folder'
    :param storage_name Storage name
    :param recursive Enable to delete folders, subfolders and files
    """

    def __init__(self, path, storage_name=None, recursive=None):
        CadRequest.__init__(self)
        self.path = path
        self.storage_name = storage_name
        self.recursive = recursive

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'path' is set
        if self.path is None:
            raise ValueError("Missing the required parameter `path` when calling `delete_folder`")

        collection_formats = {}
        path = '/cad/storage/folder/{path}'
        path_params = {}
        if self.path is not None:
            path_params[self._lowercase_first_letter('path')] = self.path

        query_params = []
        if self._lowercase_first_letter('storageName') in path:
            path = path.replace('{' + self._lowercase_first_letter('storageName' + '}'), self.storage_name if self.storage_name is not None else '')
        else:
            if self.storage_name is not None:
                query_params.append((self._lowercase_first_letter('storageName'), self.storage_name))
        if self._lowercase_first_letter('recursive') in path:
            path = path.replace('{' + self._lowercase_first_letter('recursive' + '}'), self.recursive if self.recursive is not None else '')
        else:
            if self.recursive is not None:
                query_params.append((self._lowercase_first_letter('recursive'), self.recursive))

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="download_file_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class download_file_request(CadRequest):
    """
    Request model for download_file operation.
    Initializes a new instance.

    :param path File path e.g. '/folder/file.ext'
    :param storage_name Storage name
    :param version_id File version ID to download
    """

    def __init__(self, path, storage_name=None, version_id=None):
        CadRequest.__init__(self)
        self.path = path
        self.storage_name = storage_name
        self.version_id = version_id

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'path' is set
        if self.path is None:
            raise ValueError("Missing the required parameter `path` when calling `download_file`")

        collection_formats = {}
        path = '/cad/storage/file/{path}'
        path_params = {}
        if self.path is not None:
            path_params[self._lowercase_first_letter('path')] = self.path

        query_params = []
        if self._lowercase_first_letter('storageName') in path:
            path = path.replace('{' + self._lowercase_first_letter('storageName' + '}'), self.storage_name if self.storage_name is not None else '')
        else:
            if self.storage_name is not None:
                query_params.append((self._lowercase_first_letter('storageName'), self.storage_name))
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
            ['multipart/form-data'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="edit_metadata_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class edit_metadata_request(CadRequest):
    """
    Request model for edit_metadata operation.
    Initializes a new instance.

    :param drawing 
    """

    def __init__(self, drawing=None):
        CadRequest.__init__(self)
        self.drawing = drawing

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """

        collection_formats = {}
        path = '/cad/EditMetadata'
        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing is not None:
            local_var_files.append((self._lowercase_first_letter('drawing'), self.drawing))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['multipart/form-data', 'application/octet-stream', 'multipart/form-data'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="extract_metadata_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class extract_metadata_request(CadRequest):
    """
    Request model for extract_metadata operation.
    Initializes a new instance.

    :param output_format Output TXT, XML or JSON file format.
    :param drawing Form-data file
    """

    def __init__(self, output_format, drawing=None):
        CadRequest.__init__(self)
        self.output_format = output_format
        self.drawing = drawing

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'output_format' is set
        if self.output_format is None:
            raise ValueError("Missing the required parameter `output_format` when calling `extract_metadata`")

        collection_formats = {}
        path = '/cad/ExtractMetadata'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outputFormat') in path:
            path = path.replace('{' + self._lowercase_first_letter('outputFormat' + '}'), self.output_format if self.output_format is not None else '')
        else:
            if self.output_format is not None:
                query_params.append((self._lowercase_first_letter('outputFormat'), self.output_format))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing is not None:
            local_var_files.append((self._lowercase_first_letter('drawing'), self.drawing))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['multipart/form-data', 'application/octet-stream'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="extract_text_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class extract_text_request(CadRequest):
    """
    Request model for extract_text operation.
    Initializes a new instance.

    :param drawing 
    """

    def __init__(self, drawing=None):
        CadRequest.__init__(self)
        self.drawing = drawing

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """

        collection_formats = {}
        path = '/cad/ExtractText'
        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing is not None:
            local_var_files.append((self._lowercase_first_letter('drawing'), self.drawing))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['multipart/form-data', 'application/octet-stream'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="get_disc_usage_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class get_disc_usage_request(CadRequest):
    """
    Request model for get_disc_usage operation.
    Initializes a new instance.

    :param storage_name Storage name
    """

    def __init__(self, storage_name=None):
        CadRequest.__init__(self)
        self.storage_name = storage_name

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """

        collection_formats = {}
        path = '/cad/storage/disc'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('storageName') in path:
            path = path.replace('{' + self._lowercase_first_letter('storageName' + '}'), self.storage_name if self.storage_name is not None else '')
        else:
            if self.storage_name is not None:
                query_params.append((self._lowercase_first_letter('storageName'), self.storage_name))

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="get_drawing_properties_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class get_drawing_properties_request(CadRequest):
    """
    Request model for get_drawing_properties operation.
    Initializes a new instance.

    :param name Filename of an input drawing on a storage.
    :param folder Folder with a drawing to get properties for.
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, folder=None, storage=None):
        CadRequest.__init__(self)
        self.name = name
        self.folder = folder
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_drawing_properties`")

        collection_formats = {}
        path = '/cad/{name}/properties'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="get_drawing_resize_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class get_drawing_resize_request(CadRequest):
    """
    Request model for get_drawing_resize operation.
    Initializes a new instance.

    :param name Filename of a drawing.
    :param output_format Resulting file format.
    :param new_width New width.
    :param new_height New height.
    :param folder Folder with a drawing to process.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, output_format, new_width, new_height, folder=None, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.name = name
        self.output_format = output_format
        self.new_width = new_width
        self.new_height = new_height
        self.folder = folder
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_drawing_resize`")
        # verify the required parameter 'output_format' is set
        if self.output_format is None:
            raise ValueError("Missing the required parameter `output_format` when calling `get_drawing_resize`")
        # verify the required parameter 'new_width' is set
        if self.new_width is None:
            raise ValueError("Missing the required parameter `new_width` when calling `get_drawing_resize`")
        # verify the required parameter 'new_height' is set
        if self.new_height is None:
            raise ValueError("Missing the required parameter `new_height` when calling `get_drawing_resize`")

        collection_formats = {}
        path = '/cad/{name}/resize'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('outputFormat') in path:
            path = path.replace('{' + self._lowercase_first_letter('outputFormat' + '}'), self.output_format if self.output_format is not None else '')
        else:
            if self.output_format is not None:
                query_params.append((self._lowercase_first_letter('outputFormat'), self.output_format))
        if self._lowercase_first_letter('newWidth') in path:
            path = path.replace('{' + self._lowercase_first_letter('newWidth' + '}'), self.new_width if self.new_width is not None else '')
        else:
            if self.new_width is not None:
                query_params.append((self._lowercase_first_letter('newWidth'), self.new_width))
        if self._lowercase_first_letter('newHeight') in path:
            path = path.replace('{' + self._lowercase_first_letter('newHeight' + '}'), self.new_height if self.new_height is not None else '')
        else:
            if self.new_height is not None:
                query_params.append((self._lowercase_first_letter('newHeight'), self.new_height))
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="get_drawing_rotate_flip_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class get_drawing_rotate_flip_request(CadRequest):
    """
    Request model for get_drawing_rotate_flip operation.
    Initializes a new instance.

    :param name Filename of a drawing.
    :param output_format Resulting file format.
    :param rotate_flip_type Rotate/flip operation to apply. Possible values: RotateNoneFlipNone, Rotate90FlipNone, Rotate180FlipNone, Rotate270FlipNone, RotateNoneFlipX, Rotate90FlipX, Rotate180FlipX, Rotate270FlipX, RotateNoneFlipY, Rotate90FlipY, Rotate180FlipY, Rotate270FlipY, RotateNoneFlipXY, Rotate90FlipXY, Rotate180FlipXY, Rotate270FlipXY
    :param folder Folder with a drawing to process.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, output_format, rotate_flip_type, folder=None, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.name = name
        self.output_format = output_format
        self.rotate_flip_type = rotate_flip_type
        self.folder = folder
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_drawing_rotate_flip`")
        # verify the required parameter 'output_format' is set
        if self.output_format is None:
            raise ValueError("Missing the required parameter `output_format` when calling `get_drawing_rotate_flip`")
        # verify the required parameter 'rotate_flip_type' is set
        if self.rotate_flip_type is None:
            raise ValueError("Missing the required parameter `rotate_flip_type` when calling `get_drawing_rotate_flip`")

        collection_formats = {}
        path = '/cad/{name}/rotateflip'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('outputFormat') in path:
            path = path.replace('{' + self._lowercase_first_letter('outputFormat' + '}'), self.output_format if self.output_format is not None else '')
        else:
            if self.output_format is not None:
                query_params.append((self._lowercase_first_letter('outputFormat'), self.output_format))
        if self._lowercase_first_letter('rotateFlipType') in path:
            path = path.replace('{' + self._lowercase_first_letter('rotateFlipType' + '}'), self.rotate_flip_type if self.rotate_flip_type is not None else '')
        else:
            if self.rotate_flip_type is not None:
                query_params.append((self._lowercase_first_letter('rotateFlipType'), self.rotate_flip_type))
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="get_drawing_save_as_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class get_drawing_save_as_request(CadRequest):
    """
    Request model for get_drawing_save_as operation.
    Initializes a new instance.

    :param name Filename of an input drawing on a storage.
    :param output_format Resulting file format.
    :param folder Folder with a drawing to process.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, output_format, folder=None, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.name = name
        self.output_format = output_format
        self.folder = folder
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_drawing_save_as`")
        # verify the required parameter 'output_format' is set
        if self.output_format is None:
            raise ValueError("Missing the required parameter `output_format` when calling `get_drawing_save_as`")

        collection_formats = {}
        path = '/cad/{name}/saveAs/{outputFormat}'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name
        if self.output_format is not None:
            path_params[self._lowercase_first_letter('outputFormat')] = self.output_format

        query_params = []
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="get_file_versions_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class get_file_versions_request(CadRequest):
    """
    Request model for get_file_versions operation.
    Initializes a new instance.

    :param path File path e.g. '/file.ext'
    :param storage_name Storage name
    """

    def __init__(self, path, storage_name=None):
        CadRequest.__init__(self)
        self.path = path
        self.storage_name = storage_name

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'path' is set
        if self.path is None:
            raise ValueError("Missing the required parameter `path` when calling `get_file_versions`")

        collection_formats = {}
        path = '/cad/storage/version/{path}'
        path_params = {}
        if self.path is not None:
            path_params[self._lowercase_first_letter('path')] = self.path

        query_params = []
        if self._lowercase_first_letter('storageName') in path:
            path = path.replace('{' + self._lowercase_first_letter('storageName' + '}'), self.storage_name if self.storage_name is not None else '')
        else:
            if self.storage_name is not None:
                query_params.append((self._lowercase_first_letter('storageName'), self.storage_name))

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="get_files_list_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class get_files_list_request(CadRequest):
    """
    Request model for get_files_list operation.
    Initializes a new instance.

    :param path Folder path e.g. '/folder'
    :param storage_name Storage name
    """

    def __init__(self, path, storage_name=None):
        CadRequest.__init__(self)
        self.path = path
        self.storage_name = storage_name

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'path' is set
        if self.path is None:
            raise ValueError("Missing the required parameter `path` when calling `get_files_list`")

        collection_formats = {}
        path = '/cad/storage/folder/{path}'
        path_params = {}
        if self.path is not None:
            path_params[self._lowercase_first_letter('path')] = self.path

        query_params = []
        if self._lowercase_first_letter('storageName') in path:
            path = path.replace('{' + self._lowercase_first_letter('storageName' + '}'), self.storage_name if self.storage_name is not None else '')
        else:
            if self.storage_name is not None:
                query_params.append((self._lowercase_first_letter('storageName'), self.storage_name))

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="move_file_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class move_file_request(CadRequest):
    """
    Request model for move_file operation.
    Initializes a new instance.

    :param src_path Source file path e.g. '/src.ext'
    :param dest_path Destination file path e.g. '/dest.ext'
    :param src_storage_name Source storage name
    :param dest_storage_name Destination storage name
    :param version_id File version ID to move
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
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'src_path' is set
        if self.src_path is None:
            raise ValueError("Missing the required parameter `src_path` when calling `move_file`")
        # verify the required parameter 'dest_path' is set
        if self.dest_path is None:
            raise ValueError("Missing the required parameter `dest_path` when calling `move_file`")

        collection_formats = {}
        path = '/cad/storage/file/move/{srcPath}'
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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="move_folder_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class move_folder_request(CadRequest):
    """
    Request model for move_folder operation.
    Initializes a new instance.

    :param src_path Folder path to move e.g. '/folder'
    :param dest_path Destination folder path to move to e.g '/dst'
    :param src_storage_name Source storage name
    :param dest_storage_name Destination storage name
    """

    def __init__(self, src_path, dest_path, src_storage_name=None, dest_storage_name=None):
        CadRequest.__init__(self)
        self.src_path = src_path
        self.dest_path = dest_path
        self.src_storage_name = src_storage_name
        self.dest_storage_name = dest_storage_name

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'src_path' is set
        if self.src_path is None:
            raise ValueError("Missing the required parameter `src_path` when calling `move_folder`")
        # verify the required parameter 'dest_path' is set
        if self.dest_path is None:
            raise ValueError("Missing the required parameter `dest_path` when calling `move_folder`")

        collection_formats = {}
        path = '/cad/storage/folder/move/{srcPath}'
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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="object_exists_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class object_exists_request(CadRequest):
    """
    Request model for object_exists operation.
    Initializes a new instance.

    :param path File or folder path e.g. '/file.ext' or '/folder'
    :param storage_name Storage name
    :param version_id File version ID
    """

    def __init__(self, path, storage_name=None, version_id=None):
        CadRequest.__init__(self)
        self.path = path
        self.storage_name = storage_name
        self.version_id = version_id

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'path' is set
        if self.path is None:
            raise ValueError("Missing the required parameter `path` when calling `object_exists`")

        collection_formats = {}
        path = '/cad/storage/exist/{path}'
        path_params = {}
        if self.path is not None:
            path_params[self._lowercase_first_letter('path')] = self.path

        query_params = []
        if self._lowercase_first_letter('storageName') in path:
            path = path.replace('{' + self._lowercase_first_letter('storageName' + '}'), self.storage_name if self.storage_name is not None else '')
        else:
            if self.storage_name is not None:
                query_params.append((self._lowercase_first_letter('storageName'), self.storage_name))
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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="paper_to_cad_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class paper_to_cad_request(CadRequest):
    """
    Request model for paper_to_cad operation.
    Initializes a new instance.

    :param output_format Output DXF, DWG, DGN, DWF, DWFX, IFC, STL, STP, STEP, CGM, GLB, GLTF, DWT, IGES, PLT, CF2, OBJ, HPGL, IGS, PCL, FBX, SVG file format.
    :param drawing Form-data file
    """

    def __init__(self, output_format, drawing=None):
        CadRequest.__init__(self)
        self.output_format = output_format
        self.drawing = drawing

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'output_format' is set
        if self.output_format is None:
            raise ValueError("Missing the required parameter `output_format` when calling `paper_to_cad`")

        collection_formats = {}
        path = '/cad/paper-to-cad'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outputFormat') in path:
            path = path.replace('{' + self._lowercase_first_letter('outputFormat' + '}'), self.output_format if self.output_format is not None else '')
        else:
            if self.output_format is not None:
                query_params.append((self._lowercase_first_letter('outputFormat'), self.output_format))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing is not None:
            local_var_files.append((self._lowercase_first_letter('drawing'), self.drawing))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['multipart/form-data', 'application/octet-stream'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="post_drawing_bmp_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class post_drawing_bmp_request(CadRequest):
    """
    Request model for post_drawing_bmp operation.
    Initializes a new instance.

    :param name Filename of an input drawing on a storage.
    :param options Export BMP options passed as a JSON on a request body.
    :param folder Folder with a drawing to process.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, options, folder=None, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.name = name
        self.options = options
        self.folder = folder
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_bmp`")
        # verify the required parameter 'options' is set
        if self.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_bmp`")

        collection_formats = {}
        path = '/cad/{name}/bmp'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if self.options is not None:
            body_params = self.options

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="post_drawing_cgm_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class post_drawing_cgm_request(CadRequest):
    """
    Request model for post_drawing_cgm operation.
    Initializes a new instance.

    :param name Filename of an input drawing on a storage.
    :param options Export CGM options passed as a JSON on a request body.
    :param folder Folder with a drawing to process.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, options, folder=None, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.name = name
        self.options = options
        self.folder = folder
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_cgm`")
        # verify the required parameter 'options' is set
        if self.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_cgm`")

        collection_formats = {}
        path = '/cad/{name}/cgm'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if self.options is not None:
            body_params = self.options

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="post_drawing_dicom_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class post_drawing_dicom_request(CadRequest):
    """
    Request model for post_drawing_dicom operation.
    Initializes a new instance.

    :param name Filename of an input drawing on a storage.
    :param options Export Dicom options passed as a JSON on a request body.
    :param folder Folder with a drawing to process.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, options, folder=None, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.name = name
        self.options = options
        self.folder = folder
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_dicom`")
        # verify the required parameter 'options' is set
        if self.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_dicom`")

        collection_formats = {}
        path = '/cad/{name}/dicom'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if self.options is not None:
            body_params = self.options

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="post_drawing_dwf_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class post_drawing_dwf_request(CadRequest):
    """
    Request model for post_drawing_dwf operation.
    Initializes a new instance.

    :param name Filename of an input drawing on a storage.
    :param options Export Dwf options passed as a JSON on a request body.
    :param folder Folder with a drawing to process.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, options, folder=None, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.name = name
        self.options = options
        self.folder = folder
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_dwf`")
        # verify the required parameter 'options' is set
        if self.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_dwf`")

        collection_formats = {}
        path = '/cad/{name}/dwf'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if self.options is not None:
            body_params = self.options

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="post_drawing_dxf_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class post_drawing_dxf_request(CadRequest):
    """
    Request model for post_drawing_dxf operation.
    Initializes a new instance.

    :param name Filename of an input drawing on a storage.
    :param options Export DXF options passed as a JSON on a request body.
    :param folder Folder with a drawing to process.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, options, folder=None, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.name = name
        self.options = options
        self.folder = folder
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_dxf`")
        # verify the required parameter 'options' is set
        if self.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_dxf`")

        collection_formats = {}
        path = '/cad/{name}/dxf'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if self.options is not None:
            body_params = self.options

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="post_drawing_fbx_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class post_drawing_fbx_request(CadRequest):
    """
    Request model for post_drawing_fbx operation.
    Initializes a new instance.

    :param name Filename of an input drawing on a storage.
    :param options Export Fbx options passed as a JSON on a request body.
    :param folder Folder with a drawing to process.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, options, folder=None, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.name = name
        self.options = options
        self.folder = folder
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_fbx`")
        # verify the required parameter 'options' is set
        if self.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_fbx`")

        collection_formats = {}
        path = '/cad/{name}/fbx'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if self.options is not None:
            body_params = self.options

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="post_drawing_gif_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class post_drawing_gif_request(CadRequest):
    """
    Request model for post_drawing_gif operation.
    Initializes a new instance.

    :param name Filename of an input drawing on a storage.
    :param options Export GIF options passed as a JSON on a request body.
    :param folder Folder with a drawing to process.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, options, folder=None, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.name = name
        self.options = options
        self.folder = folder
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_gif`")
        # verify the required parameter 'options' is set
        if self.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_gif`")

        collection_formats = {}
        path = '/cad/{name}/gif'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if self.options is not None:
            body_params = self.options

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="post_drawing_glb_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class post_drawing_glb_request(CadRequest):
    """
    Request model for post_drawing_glb operation.
    Initializes a new instance.

    :param name Filename of an input drawing on a storage.
    :param options Export GLB options passed as a JSON on a request body.
    :param folder Folder with a drawing to process.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, options, folder=None, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.name = name
        self.options = options
        self.folder = folder
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_glb`")
        # verify the required parameter 'options' is set
        if self.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_glb`")

        collection_formats = {}
        path = '/cad/{name}/glb'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if self.options is not None:
            body_params = self.options

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="post_drawing_gltf_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class post_drawing_gltf_request(CadRequest):
    """
    Request model for post_drawing_gltf operation.
    Initializes a new instance.

    :param name Filename of an input drawing on a storage.
    :param options Export GLTF options passed as a JSON on a request body.
    :param folder Folder with a drawing to process.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, options, folder=None, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.name = name
        self.options = options
        self.folder = folder
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_gltf`")
        # verify the required parameter 'options' is set
        if self.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_gltf`")

        collection_formats = {}
        path = '/cad/{name}/gltf'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if self.options is not None:
            body_params = self.options

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="post_drawing_jpeg_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class post_drawing_jpeg_request(CadRequest):
    """
    Request model for post_drawing_jpeg operation.
    Initializes a new instance.

    :param name Filename of an input drawing on a storage.
    :param options Export JPEG options passed as a JSON on a request body.
    :param folder Folder with a drawing to process.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, options, folder=None, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.name = name
        self.options = options
        self.folder = folder
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_jpeg`")
        # verify the required parameter 'options' is set
        if self.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_jpeg`")

        collection_formats = {}
        path = '/cad/{name}/jpeg'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if self.options is not None:
            body_params = self.options

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="post_drawing_jpeg2000_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class post_drawing_jpeg2000_request(CadRequest):
    """
    Request model for post_drawing_jpeg2000 operation.
    Initializes a new instance.

    :param name Filename of an input drawing on a storage.
    :param options Export JPEG2000 options passed as a JSON on a request body.
    :param folder Folder with a drawing to process.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, options, folder=None, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.name = name
        self.options = options
        self.folder = folder
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_jpeg2000`")
        # verify the required parameter 'options' is set
        if self.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_jpeg2000`")

        collection_formats = {}
        path = '/cad/{name}/jpeg2000'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if self.options is not None:
            body_params = self.options

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="post_drawing_obj_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class post_drawing_obj_request(CadRequest):
    """
    Request model for post_drawing_obj operation.
    Initializes a new instance.

    :param name Filename of an input drawing on a storage.
    :param options Export Obj options passed as a JSON on a request body.
    :param folder Folder with a drawing to process.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, options, folder=None, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.name = name
        self.options = options
        self.folder = folder
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_obj`")
        # verify the required parameter 'options' is set
        if self.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_obj`")

        collection_formats = {}
        path = '/cad/{name}/obj'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if self.options is not None:
            body_params = self.options

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="post_drawing_pdf_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class post_drawing_pdf_request(CadRequest):
    """
    Request model for post_drawing_pdf operation.
    Initializes a new instance.

    :param name Filename of an input drawing on a storage.
    :param options Export PDF options passed as a JSON on a request body.
    :param folder Folder with a drawing to process.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, options, folder=None, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.name = name
        self.options = options
        self.folder = folder
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_pdf`")
        # verify the required parameter 'options' is set
        if self.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_pdf`")

        collection_formats = {}
        path = '/cad/{name}/pdf'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if self.options is not None:
            body_params = self.options

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="post_drawing_png_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class post_drawing_png_request(CadRequest):
    """
    Request model for post_drawing_png operation.
    Initializes a new instance.

    :param name Filename of an input drawing on a storage.
    :param options Export PNG options passed as a JSON on a request body.
    :param folder Folder with a drawing to process.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, options, folder=None, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.name = name
        self.options = options
        self.folder = folder
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_png`")
        # verify the required parameter 'options' is set
        if self.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_png`")

        collection_formats = {}
        path = '/cad/{name}/png'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if self.options is not None:
            body_params = self.options

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="post_drawing_properties_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class post_drawing_properties_request(CadRequest):
    """
    Request model for post_drawing_properties operation.
    Initializes a new instance.

    :param drawing_data Input drawing
    """

    def __init__(self, drawing_data):
        CadRequest.__init__(self)
        self.drawing_data = drawing_data

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing_data' is set
        if self.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `post_drawing_properties`")

        collection_formats = {}
        path = '/cad/properties'
        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing_data is not None:
            local_var_files.append((self._lowercase_first_letter('drawingData'), self.drawing_data))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['multipart/form-data', 'application/octet-stream'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="post_drawing_psd_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class post_drawing_psd_request(CadRequest):
    """
    Request model for post_drawing_psd operation.
    Initializes a new instance.

    :param name Filename of an input drawing on a storage.
    :param options Export PSD options passed as a JSON on a request body.
    :param folder Folder with a drawing to process.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, options, folder=None, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.name = name
        self.options = options
        self.folder = folder
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_psd`")
        # verify the required parameter 'options' is set
        if self.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_psd`")

        collection_formats = {}
        path = '/cad/{name}/psd'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if self.options is not None:
            body_params = self.options

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="post_drawing_resize_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class post_drawing_resize_request(CadRequest):
    """
    Request model for post_drawing_resize operation.
    Initializes a new instance.

    :param drawing_data Input drawing
    :param output_format Resulting file format.
    :param new_width New width.
    :param new_height New height.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, drawing_data, output_format, new_width, new_height, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.drawing_data = drawing_data
        self.output_format = output_format
        self.new_width = new_width
        self.new_height = new_height
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing_data' is set
        if self.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `post_drawing_resize`")
        # verify the required parameter 'output_format' is set
        if self.output_format is None:
            raise ValueError("Missing the required parameter `output_format` when calling `post_drawing_resize`")
        # verify the required parameter 'new_width' is set
        if self.new_width is None:
            raise ValueError("Missing the required parameter `new_width` when calling `post_drawing_resize`")
        # verify the required parameter 'new_height' is set
        if self.new_height is None:
            raise ValueError("Missing the required parameter `new_height` when calling `post_drawing_resize`")

        collection_formats = {}
        path = '/cad/resize'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outputFormat') in path:
            path = path.replace('{' + self._lowercase_first_letter('outputFormat' + '}'), self.output_format if self.output_format is not None else '')
        else:
            if self.output_format is not None:
                query_params.append((self._lowercase_first_letter('outputFormat'), self.output_format))
        if self._lowercase_first_letter('newWidth') in path:
            path = path.replace('{' + self._lowercase_first_letter('newWidth' + '}'), self.new_width if self.new_width is not None else '')
        else:
            if self.new_width is not None:
                query_params.append((self._lowercase_first_letter('newWidth'), self.new_width))
        if self._lowercase_first_letter('newHeight') in path:
            path = path.replace('{' + self._lowercase_first_letter('newHeight' + '}'), self.new_height if self.new_height is not None else '')
        else:
            if self.new_height is not None:
                query_params.append((self._lowercase_first_letter('newHeight'), self.new_height))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing_data is not None:
            local_var_files.append((self._lowercase_first_letter('drawingData'), self.drawing_data))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['application/octet-stream', 'multipart/form-data'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="post_drawing_rotate_flip_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class post_drawing_rotate_flip_request(CadRequest):
    """
    Request model for post_drawing_rotate_flip operation.
    Initializes a new instance.

    :param drawing_data Input drawing
    :param output_format Resulting file format.
    :param rotate_flip_type Rotate/flip operation to apply. Possible values: RotateNoneFlipNone, Rotate90FlipNone, Rotate180FlipNone, Rotate270FlipNone, RotateNoneFlipX, Rotate90FlipX, Rotate180FlipX, Rotate270FlipX, RotateNoneFlipY, Rotate90FlipY, Rotate180FlipY, Rotate270FlipY, RotateNoneFlipXY, Rotate90FlipXY, Rotate180FlipXY, Rotate270FlipXY
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, drawing_data, output_format, rotate_flip_type, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.drawing_data = drawing_data
        self.output_format = output_format
        self.rotate_flip_type = rotate_flip_type
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing_data' is set
        if self.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `post_drawing_rotate_flip`")
        # verify the required parameter 'output_format' is set
        if self.output_format is None:
            raise ValueError("Missing the required parameter `output_format` when calling `post_drawing_rotate_flip`")
        # verify the required parameter 'rotate_flip_type' is set
        if self.rotate_flip_type is None:
            raise ValueError("Missing the required parameter `rotate_flip_type` when calling `post_drawing_rotate_flip`")

        collection_formats = {}
        path = '/cad/rotateflip'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outputFormat') in path:
            path = path.replace('{' + self._lowercase_first_letter('outputFormat' + '}'), self.output_format if self.output_format is not None else '')
        else:
            if self.output_format is not None:
                query_params.append((self._lowercase_first_letter('outputFormat'), self.output_format))
        if self._lowercase_first_letter('rotateFlipType') in path:
            path = path.replace('{' + self._lowercase_first_letter('rotateFlipType' + '}'), self.rotate_flip_type if self.rotate_flip_type is not None else '')
        else:
            if self.rotate_flip_type is not None:
                query_params.append((self._lowercase_first_letter('rotateFlipType'), self.rotate_flip_type))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing_data is not None:
            local_var_files.append((self._lowercase_first_letter('drawingData'), self.drawing_data))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['application/octet-stream', 'multipart/form-data'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="post_drawing_save_as_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class post_drawing_save_as_request(CadRequest):
    """
    Request model for post_drawing_save_as operation.
    Initializes a new instance.

    :param drawing_data Input drawing
    :param output_format Resulting file format.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, drawing_data, output_format, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.drawing_data = drawing_data
        self.output_format = output_format
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing_data' is set
        if self.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `post_drawing_save_as`")
        # verify the required parameter 'output_format' is set
        if self.output_format is None:
            raise ValueError("Missing the required parameter `output_format` when calling `post_drawing_save_as`")

        collection_formats = {}
        path = '/cad/saveAs/{outputFormat}'
        path_params = {}
        if self.output_format is not None:
            path_params[self._lowercase_first_letter('outputFormat')] = self.output_format

        query_params = []
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing_data is not None:
            local_var_files.append((self._lowercase_first_letter('drawingData'), self.drawing_data))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['application/octet-stream', 'multipart/form-data'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="post_drawing_stp_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class post_drawing_stp_request(CadRequest):
    """
    Request model for post_drawing_stp operation.
    Initializes a new instance.

    :param name Filename of an input drawing on a storage.
    :param options Export STP options passed as a JSON on a request body.
    :param folder Folder with a drawing to process.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, options, folder=None, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.name = name
        self.options = options
        self.folder = folder
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_stp`")
        # verify the required parameter 'options' is set
        if self.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_stp`")

        collection_formats = {}
        path = '/cad/{name}/stp'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if self.options is not None:
            body_params = self.options

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="post_drawing_svg_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class post_drawing_svg_request(CadRequest):
    """
    Request model for post_drawing_svg operation.
    Initializes a new instance.

    :param name Filename of an input drawing on a storage.
    :param options Export SVG options passed as a JSON on a request body.
    :param folder Folder with a drawing to process.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, options, folder=None, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.name = name
        self.options = options
        self.folder = folder
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_svg`")
        # verify the required parameter 'options' is set
        if self.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_svg`")

        collection_formats = {}
        path = '/cad/{name}/svg'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if self.options is not None:
            body_params = self.options

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="post_drawing_three_ds_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class post_drawing_three_ds_request(CadRequest):
    """
    Request model for post_drawing_three_ds operation.
    Initializes a new instance.

    :param name Filename of an input drawing on a storage.
    :param options Export 3ds options passed as a JSON on a request body.
    :param folder Folder with a drawing to process.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, options, folder=None, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.name = name
        self.options = options
        self.folder = folder
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_three_ds`")
        # verify the required parameter 'options' is set
        if self.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_three_ds`")

        collection_formats = {}
        path = '/cad/{name}/3ds'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if self.options is not None:
            body_params = self.options

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="post_drawing_tiff_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class post_drawing_tiff_request(CadRequest):
    """
    Request model for post_drawing_tiff operation.
    Initializes a new instance.

    :param name Filename of an input drawing on a storage.
    :param options Export TIFF options passed as a JSON on a request body.
    :param folder Folder with a drawing to process.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, options, folder=None, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.name = name
        self.options = options
        self.folder = folder
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_tiff`")
        # verify the required parameter 'options' is set
        if self.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_tiff`")

        collection_formats = {}
        path = '/cad/{name}/tiff'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if self.options is not None:
            body_params = self.options

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="post_drawing_u3d_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class post_drawing_u3d_request(CadRequest):
    """
    Request model for post_drawing_u3d operation.
    Initializes a new instance.

    :param name Filename of an input drawing on a storage.
    :param options Export U3d options passed as a JSON on a request body.
    :param folder Folder with a drawing to process.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, options, folder=None, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.name = name
        self.options = options
        self.folder = folder
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_u3d`")
        # verify the required parameter 'options' is set
        if self.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_u3d`")

        collection_formats = {}
        path = '/cad/{name}/u3d'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if self.options is not None:
            body_params = self.options

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="post_drawing_webp_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class post_drawing_webp_request(CadRequest):
    """
    Request model for post_drawing_webp operation.
    Initializes a new instance.

    :param name Filename of an input drawing on a storage.
    :param options Export Webp options passed as a JSON on a request body.
    :param folder Folder with a drawing to process.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, options, folder=None, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.name = name
        self.options = options
        self.folder = folder
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_webp`")
        # verify the required parameter 'options' is set
        if self.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_webp`")

        collection_formats = {}
        path = '/cad/{name}/webp'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if self.options is not None:
            body_params = self.options

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="post_drawing_wmf_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class post_drawing_wmf_request(CadRequest):
    """
    Request model for post_drawing_wmf operation.
    Initializes a new instance.

    :param name Filename of an input drawing on a storage.
    :param options Export WMF options passed as a JSON on a request body.
    :param folder Folder with a drawing to process.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, name, options, folder=None, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.name = name
        self.options = options
        self.folder = folder
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'name' is set
        if self.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_wmf`")
        # verify the required parameter 'options' is set
        if self.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_wmf`")

        collection_formats = {}
        path = '/cad/{name}/wmf'
        path_params = {}
        if self.name is not None:
            path_params[self._lowercase_first_letter('name')] = self.name

        query_params = []
        if self._lowercase_first_letter('folder') in path:
            path = path.replace('{' + self._lowercase_first_letter('folder' + '}'), self.folder if self.folder is not None else '')
        else:
            if self.folder is not None:
                query_params.append((self._lowercase_first_letter('folder'), self.folder))
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if self.options is not None:
            body_params = self.options

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="put_drawing_bmp_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class put_drawing_bmp_request(CadRequest):
    """
    Request model for put_drawing_bmp operation.
    Initializes a new instance.

    :param drawing_data Input drawing
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param export_options JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/BmpOptionsDTO model definition.
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, drawing_data, out_path=None, export_options=None, storage=None):
        CadRequest.__init__(self)
        self.drawing_data = drawing_data
        self.out_path = out_path
        self.export_options = export_options
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing_data' is set
        if self.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_bmp`")

        collection_formats = {}
        path = '/cad/bmp'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing_data is not None:
            local_var_files.append((self._lowercase_first_letter('drawingData'), self.drawing_data))
        if self.export_options is not None:
            form_params.append((self._lowercase_first_letter('exportOptions'), self.export_options))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['application/octet-stream', 'multipart/form-data'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="put_drawing_cgm_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class put_drawing_cgm_request(CadRequest):
    """
    Request model for put_drawing_cgm operation.
    Initializes a new instance.

    :param drawing_data Input drawing
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param export_options JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/CgmOptionsDTO model definition.
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, drawing_data, out_path=None, export_options=None, storage=None):
        CadRequest.__init__(self)
        self.drawing_data = drawing_data
        self.out_path = out_path
        self.export_options = export_options
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing_data' is set
        if self.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_cgm`")

        collection_formats = {}
        path = '/cad/cgm'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing_data is not None:
            local_var_files.append((self._lowercase_first_letter('drawingData'), self.drawing_data))
        if self.export_options is not None:
            form_params.append((self._lowercase_first_letter('exportOptions'), self.export_options))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['multipart/form-data', 'application/octet-stream'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="put_drawing_dicom_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class put_drawing_dicom_request(CadRequest):
    """
    Request model for put_drawing_dicom operation.
    Initializes a new instance.

    :param drawing_data Input drawing
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param export_options JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/DicomOptionsDTO model definition.
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, drawing_data, out_path=None, export_options=None, storage=None):
        CadRequest.__init__(self)
        self.drawing_data = drawing_data
        self.out_path = out_path
        self.export_options = export_options
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing_data' is set
        if self.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_dicom`")

        collection_formats = {}
        path = '/cad/dicom'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing_data is not None:
            local_var_files.append((self._lowercase_first_letter('drawingData'), self.drawing_data))
        if self.export_options is not None:
            form_params.append((self._lowercase_first_letter('exportOptions'), self.export_options))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['application/octet-stream', 'multipart/form-data'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="put_drawing_dwf_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class put_drawing_dwf_request(CadRequest):
    """
    Request model for put_drawing_dwf operation.
    Initializes a new instance.

    :param drawing_data Input drawing
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param export_options JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/DwfOptionsDTO model definition.
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, drawing_data, out_path=None, export_options=None, storage=None):
        CadRequest.__init__(self)
        self.drawing_data = drawing_data
        self.out_path = out_path
        self.export_options = export_options
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing_data' is set
        if self.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_dwf`")

        collection_formats = {}
        path = '/cad/dwf'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing_data is not None:
            local_var_files.append((self._lowercase_first_letter('drawingData'), self.drawing_data))
        if self.export_options is not None:
            form_params.append((self._lowercase_first_letter('exportOptions'), self.export_options))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['multipart/form-data', 'application/octet-stream'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="put_drawing_dxf_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class put_drawing_dxf_request(CadRequest):
    """
    Request model for put_drawing_dxf operation.
    Initializes a new instance.

    :param drawing_data Input drawing
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param export_options JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/DxfOptionsDTO model definition.
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, drawing_data, out_path=None, export_options=None, storage=None):
        CadRequest.__init__(self)
        self.drawing_data = drawing_data
        self.out_path = out_path
        self.export_options = export_options
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing_data' is set
        if self.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_dxf`")

        collection_formats = {}
        path = '/cad/dxf'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing_data is not None:
            local_var_files.append((self._lowercase_first_letter('drawingData'), self.drawing_data))
        if self.export_options is not None:
            form_params.append((self._lowercase_first_letter('exportOptions'), self.export_options))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['multipart/form-data', 'application/octet-stream'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="put_drawing_fbx_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class put_drawing_fbx_request(CadRequest):
    """
    Request model for put_drawing_fbx operation.
    Initializes a new instance.

    :param drawing_data Input drawing
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param export_options JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/FbxOptionsDTO model definition.
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, drawing_data, out_path=None, export_options=None, storage=None):
        CadRequest.__init__(self)
        self.drawing_data = drawing_data
        self.out_path = out_path
        self.export_options = export_options
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing_data' is set
        if self.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_fbx`")

        collection_formats = {}
        path = '/cad/fbx'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing_data is not None:
            local_var_files.append((self._lowercase_first_letter('drawingData'), self.drawing_data))
        if self.export_options is not None:
            form_params.append((self._lowercase_first_letter('exportOptions'), self.export_options))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['multipart/form-data', 'application/octet-stream'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="put_drawing_gif_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class put_drawing_gif_request(CadRequest):
    """
    Request model for put_drawing_gif operation.
    Initializes a new instance.

    :param drawing_data Input drawing
    :param export_options JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/GifOptionsDTO model definition.
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, drawing_data, export_options=None, out_path=None, storage=None):
        CadRequest.__init__(self)
        self.drawing_data = drawing_data
        self.export_options = export_options
        self.out_path = out_path
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing_data' is set
        if self.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_gif`")

        collection_formats = {}
        path = '/cad/gif'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing_data is not None:
            local_var_files.append((self._lowercase_first_letter('drawingData'), self.drawing_data))
        if self.export_options is not None:
            form_params.append((self._lowercase_first_letter('exportOptions'), self.export_options))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['multipart/form-data', 'application/octet-stream'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="put_drawing_glb_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class put_drawing_glb_request(CadRequest):
    """
    Request model for put_drawing_glb operation.
    Initializes a new instance.

    :param drawing_data Input drawing
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param export_options JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/GlbOptionsDTO model definition.
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, drawing_data, out_path=None, export_options=None, storage=None):
        CadRequest.__init__(self)
        self.drawing_data = drawing_data
        self.out_path = out_path
        self.export_options = export_options
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing_data' is set
        if self.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_glb`")

        collection_formats = {}
        path = '/cad/glb'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing_data is not None:
            local_var_files.append((self._lowercase_first_letter('drawingData'), self.drawing_data))
        if self.export_options is not None:
            form_params.append((self._lowercase_first_letter('exportOptions'), self.export_options))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['multipart/form-data', 'application/octet-stream'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="put_drawing_gltf_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class put_drawing_gltf_request(CadRequest):
    """
    Request model for put_drawing_gltf operation.
    Initializes a new instance.

    :param drawing_data Input drawing
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param export_options JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/GltfOptionsDTO model definition.
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, drawing_data, out_path=None, export_options=None, storage=None):
        CadRequest.__init__(self)
        self.drawing_data = drawing_data
        self.out_path = out_path
        self.export_options = export_options
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing_data' is set
        if self.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_gltf`")

        collection_formats = {}
        path = '/cad/gltf'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing_data is not None:
            local_var_files.append((self._lowercase_first_letter('drawingData'), self.drawing_data))
        if self.export_options is not None:
            form_params.append((self._lowercase_first_letter('exportOptions'), self.export_options))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['multipart/form-data', 'application/octet-stream'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="put_drawing_jpeg_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class put_drawing_jpeg_request(CadRequest):
    """
    Request model for put_drawing_jpeg operation.
    Initializes a new instance.

    :param drawing_data Input drawing
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param export_options JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/JpegOptionsDTO model definition.
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, drawing_data, out_path=None, export_options=None, storage=None):
        CadRequest.__init__(self)
        self.drawing_data = drawing_data
        self.out_path = out_path
        self.export_options = export_options
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing_data' is set
        if self.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_jpeg`")

        collection_formats = {}
        path = '/cad/jpeg'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing_data is not None:
            local_var_files.append((self._lowercase_first_letter('drawingData'), self.drawing_data))
        if self.export_options is not None:
            form_params.append((self._lowercase_first_letter('exportOptions'), self.export_options))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['multipart/form-data', 'application/octet-stream'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="put_drawing_jpeg2000_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class put_drawing_jpeg2000_request(CadRequest):
    """
    Request model for put_drawing_jpeg2000 operation.
    Initializes a new instance.

    :param drawing_data Input drawing
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param export_options JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/Jpeg2000OptionsDTO model definition.
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, drawing_data, out_path=None, export_options=None, storage=None):
        CadRequest.__init__(self)
        self.drawing_data = drawing_data
        self.out_path = out_path
        self.export_options = export_options
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing_data' is set
        if self.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_jpeg2000`")

        collection_formats = {}
        path = '/cad/jpeg2000'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing_data is not None:
            local_var_files.append((self._lowercase_first_letter('drawingData'), self.drawing_data))
        if self.export_options is not None:
            form_params.append((self._lowercase_first_letter('exportOptions'), self.export_options))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['multipart/form-data', 'application/octet-stream'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="put_drawing_obj_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class put_drawing_obj_request(CadRequest):
    """
    Request model for put_drawing_obj operation.
    Initializes a new instance.

    :param drawing_data Input drawing
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param export_options JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/ObjOptionsDTO model definition.
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, drawing_data, out_path=None, export_options=None, storage=None):
        CadRequest.__init__(self)
        self.drawing_data = drawing_data
        self.out_path = out_path
        self.export_options = export_options
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing_data' is set
        if self.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_obj`")

        collection_formats = {}
        path = '/cad/obj'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing_data is not None:
            local_var_files.append((self._lowercase_first_letter('drawingData'), self.drawing_data))
        if self.export_options is not None:
            form_params.append((self._lowercase_first_letter('exportOptions'), self.export_options))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['multipart/form-data', 'application/octet-stream'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="put_drawing_pdf_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class put_drawing_pdf_request(CadRequest):
    """
    Request model for put_drawing_pdf operation.
    Initializes a new instance.

    :param drawing_data Input drawing
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param export_options JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/PdfOptionsDTO model definition.
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, drawing_data, out_path=None, export_options=None, storage=None):
        CadRequest.__init__(self)
        self.drawing_data = drawing_data
        self.out_path = out_path
        self.export_options = export_options
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing_data' is set
        if self.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_pdf`")

        collection_formats = {}
        path = '/cad/pdf'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing_data is not None:
            local_var_files.append((self._lowercase_first_letter('drawingData'), self.drawing_data))
        if self.export_options is not None:
            form_params.append((self._lowercase_first_letter('exportOptions'), self.export_options))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['multipart/form-data', 'application/octet-stream'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="put_drawing_png_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class put_drawing_png_request(CadRequest):
    """
    Request model for put_drawing_png operation.
    Initializes a new instance.

    :param drawing_data Input drawing
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param export_options JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/PngOptionsDTO model definition.
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, drawing_data, out_path=None, export_options=None, storage=None):
        CadRequest.__init__(self)
        self.drawing_data = drawing_data
        self.out_path = out_path
        self.export_options = export_options
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing_data' is set
        if self.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_png`")

        collection_formats = {}
        path = '/cad/png'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing_data is not None:
            local_var_files.append((self._lowercase_first_letter('drawingData'), self.drawing_data))
        if self.export_options is not None:
            form_params.append((self._lowercase_first_letter('exportOptions'), self.export_options))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['multipart/form-data', 'application/octet-stream'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="put_drawing_psd_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class put_drawing_psd_request(CadRequest):
    """
    Request model for put_drawing_psd operation.
    Initializes a new instance.

    :param drawing_data Input drawing
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param export_options JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/PsdOptionsDTO model definition.
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, drawing_data, out_path=None, export_options=None, storage=None):
        CadRequest.__init__(self)
        self.drawing_data = drawing_data
        self.out_path = out_path
        self.export_options = export_options
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing_data' is set
        if self.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_psd`")

        collection_formats = {}
        path = '/cad/psd'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing_data is not None:
            local_var_files.append((self._lowercase_first_letter('drawingData'), self.drawing_data))
        if self.export_options is not None:
            form_params.append((self._lowercase_first_letter('exportOptions'), self.export_options))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['multipart/form-data', 'application/octet-stream'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="put_drawing_stp_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class put_drawing_stp_request(CadRequest):
    """
    Request model for put_drawing_stp operation.
    Initializes a new instance.

    :param drawing_data Input drawing
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param export_options JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/StpOptionsDTO model definition.
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, drawing_data, out_path=None, export_options=None, storage=None):
        CadRequest.__init__(self)
        self.drawing_data = drawing_data
        self.out_path = out_path
        self.export_options = export_options
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing_data' is set
        if self.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_stp`")

        collection_formats = {}
        path = '/cad/stp'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing_data is not None:
            local_var_files.append((self._lowercase_first_letter('drawingData'), self.drawing_data))
        if self.export_options is not None:
            form_params.append((self._lowercase_first_letter('exportOptions'), self.export_options))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['multipart/form-data', 'application/octet-stream'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="put_drawing_svg_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class put_drawing_svg_request(CadRequest):
    """
    Request model for put_drawing_svg operation.
    Initializes a new instance.

    :param drawing_data Input drawing
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param export_options JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/SvgOptionsDTO model definition.
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, drawing_data, out_path=None, export_options=None, storage=None):
        CadRequest.__init__(self)
        self.drawing_data = drawing_data
        self.out_path = out_path
        self.export_options = export_options
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing_data' is set
        if self.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_svg`")

        collection_formats = {}
        path = '/cad/svg'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing_data is not None:
            local_var_files.append((self._lowercase_first_letter('drawingData'), self.drawing_data))
        if self.export_options is not None:
            form_params.append((self._lowercase_first_letter('exportOptions'), self.export_options))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['multipart/form-data', 'application/octet-stream'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="put_drawing_three_ds_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class put_drawing_three_ds_request(CadRequest):
    """
    Request model for put_drawing_three_ds operation.
    Initializes a new instance.

    :param drawing_data Input drawing
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param export_options JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/ThreeDSOptionsDTO model definition.
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, drawing_data, out_path=None, export_options=None, storage=None):
        CadRequest.__init__(self)
        self.drawing_data = drawing_data
        self.out_path = out_path
        self.export_options = export_options
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing_data' is set
        if self.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_three_ds`")

        collection_formats = {}
        path = '/cad/3ds'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing_data is not None:
            local_var_files.append((self._lowercase_first_letter('drawingData'), self.drawing_data))
        if self.export_options is not None:
            form_params.append((self._lowercase_first_letter('exportOptions'), self.export_options))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['application/octet-stream', 'multipart/form-data'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="put_drawing_tiff_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class put_drawing_tiff_request(CadRequest):
    """
    Request model for put_drawing_tiff operation.
    Initializes a new instance.

    :param drawing_data Input drawing
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param export_options JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/TiffOptionsDTO model definition.
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, drawing_data, out_path=None, export_options=None, storage=None):
        CadRequest.__init__(self)
        self.drawing_data = drawing_data
        self.out_path = out_path
        self.export_options = export_options
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing_data' is set
        if self.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_tiff`")

        collection_formats = {}
        path = '/cad/tiff'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing_data is not None:
            local_var_files.append((self._lowercase_first_letter('drawingData'), self.drawing_data))
        if self.export_options is not None:
            form_params.append((self._lowercase_first_letter('exportOptions'), self.export_options))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['multipart/form-data', 'application/octet-stream'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="put_drawing_u3d_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class put_drawing_u3d_request(CadRequest):
    """
    Request model for put_drawing_u3d operation.
    Initializes a new instance.

    :param drawing_data Input drawing
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param export_options JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/U3dOptionsDTO model definition.
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, drawing_data, out_path=None, export_options=None, storage=None):
        CadRequest.__init__(self)
        self.drawing_data = drawing_data
        self.out_path = out_path
        self.export_options = export_options
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing_data' is set
        if self.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_u3d`")

        collection_formats = {}
        path = '/cad/u3d'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing_data is not None:
            local_var_files.append((self._lowercase_first_letter('drawingData'), self.drawing_data))
        if self.export_options is not None:
            form_params.append((self._lowercase_first_letter('exportOptions'), self.export_options))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['application/octet-stream', 'multipart/form-data'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="put_drawing_webp_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class put_drawing_webp_request(CadRequest):
    """
    Request model for put_drawing_webp operation.
    Initializes a new instance.

    :param drawing_data Input drawing
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param export_options JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/WebpOptionsDTO model definition.
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, drawing_data, out_path=None, export_options=None, storage=None):
        CadRequest.__init__(self)
        self.drawing_data = drawing_data
        self.out_path = out_path
        self.export_options = export_options
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing_data' is set
        if self.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_webp`")

        collection_formats = {}
        path = '/cad/webp'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing_data is not None:
            local_var_files.append((self._lowercase_first_letter('drawingData'), self.drawing_data))
        if self.export_options is not None:
            form_params.append((self._lowercase_first_letter('exportOptions'), self.export_options))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['application/octet-stream', 'multipart/form-data'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="put_drawing_wmf_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class put_drawing_wmf_request(CadRequest):
    """
    Request model for put_drawing_wmf operation.
    Initializes a new instance.

    :param drawing_data Input drawing
    :param out_path Path to updated file (if this is empty, response contains streamed file).
    :param export_options JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/WmfOptionsDTO model definition.
    :param storage Your Aspose Cloud Storage name.
    """

    def __init__(self, drawing_data, out_path=None, export_options=None, storage=None):
        CadRequest.__init__(self)
        self.drawing_data = drawing_data
        self.out_path = out_path
        self.export_options = export_options
        self.storage = storage

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'drawing_data' is set
        if self.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_wmf`")

        collection_formats = {}
        path = '/cad/wmf'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outPath') in path:
            path = path.replace('{' + self._lowercase_first_letter('outPath' + '}'), self.out_path if self.out_path is not None else '')
        else:
            if self.out_path is not None:
                query_params.append((self._lowercase_first_letter('outPath'), self.out_path))
        if self._lowercase_first_letter('storage') in path:
            path = path.replace('{' + self._lowercase_first_letter('storage' + '}'), self.storage if self.storage is not None else '')
        else:
            if self.storage is not None:
                query_params.append((self._lowercase_first_letter('storage'), self.storage))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing_data is not None:
            local_var_files.append((self._lowercase_first_letter('drawingData'), self.drawing_data))
        if self.export_options is not None:
            form_params.append((self._lowercase_first_letter('exportOptions'), self.export_options))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['multipart/form-data', 'application/octet-stream'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="put_edit_metadata_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class put_edit_metadata_request(CadRequest):
    """
    Request model for put_edit_metadata operation.
    Initializes a new instance.

    :param drawing 
    :param metadata_component 
    """

    def __init__(self, drawing=None, metadata_component=None):
        CadRequest.__init__(self)
        self.drawing = drawing
        self.metadata_component = metadata_component

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """

        collection_formats = {}
        path = '/cad/EditMetadata'
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
            ['multipart/form-data', 'application/octet-stream'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="storage_exists_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class storage_exists_request(CadRequest):
    """
    Request model for storage_exists operation.
    Initializes a new instance.

    :param storage_name Storage name
    """

    def __init__(self, storage_name):
        CadRequest.__init__(self)
        self.storage_name = storage_name

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'storage_name' is set
        if self.storage_name is None:
            raise ValueError("Missing the required parameter `storage_name` when calling `storage_exists`")

        collection_formats = {}
        path = '/cad/storage/{storageName}/exist'
        path_params = {}
        if self.storage_name is not None:
            path_params[self._lowercase_first_letter('storageName')] = self.storage_name

        query_params = []

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
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="upload_file_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class upload_file_request(CadRequest):
    """
    Request model for upload_file operation.
    Initializes a new instance.

    :param path Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext             If the content is multipart and path does not contains the file name it tries to get them from filename parameter             from Content-Disposition header.             
    :param file File to upload
    :param storage_name Storage name
    """

    def __init__(self, path, file, storage_name=None):
        CadRequest.__init__(self)
        self.path = path
        self.file = file
        self.storage_name = storage_name

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'path' is set
        if self.path is None:
            raise ValueError("Missing the required parameter `path` when calling `upload_file`")
        # verify the required parameter 'file' is set
        if self.file is None:
            raise ValueError("Missing the required parameter `file` when calling `upload_file`")

        collection_formats = {}
        path = '/cad/storage/file/{path}'
        path_params = {}
        if self.path is not None:
            path_params[self._lowercase_first_letter('path')] = self.path

        query_params = []
        if self._lowercase_first_letter('storageName') in path:
            path = path.replace('{' + self._lowercase_first_letter('storageName' + '}'), self.storage_name if self.storage_name is not None else '')
        else:
            if self.storage_name is not None:
                query_params.append((self._lowercase_first_letter('storageName'), self.storage_name))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.file is not None:
            local_var_files.append((self._lowercase_first_letter('File'), self.file))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['multipart/form-data'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="viewer_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class viewer_request(CadRequest):
    """
    Request model for viewer operation.
    Initializes a new instance.

    :param output_format 
    :param drawing 
    """

    def __init__(self, output_format, drawing=None):
        CadRequest.__init__(self)
        self.output_format = output_format
        self.drawing = drawing

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'output_format' is set
        if self.output_format is None:
            raise ValueError("Missing the required parameter `output_format` when calling `viewer`")

        collection_formats = {}
        path = '/cad/Viewer'
        path_params = {}

        query_params = []
        if self._lowercase_first_letter('outputFormat') in path:
            path = path.replace('{' + self._lowercase_first_letter('outputFormat' + '}'), self.output_format if self.output_format is not None else '')
        else:
            if self.output_format is not None:
                query_params.append((self._lowercase_first_letter('outputFormat'), self.output_format))

        header_params = {}

        form_params = []
        local_var_files = []
        if self.drawing is not None:
            local_var_files.append((self._lowercase_first_letter('drawing'), self.drawing))

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self._select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = 'multipart/form-data' if form_params or local_var_files else self._select_header_content_type(
            ['multipart/form-data', 'application/octet-stream'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)
#  coding: utf-8
#  ----------------------------------------------------------------
#  <copyright company="Aspose" file="watermark_request.py">
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
from asposecadcloud.models.requests.HttpRequest import HttpRequest


class watermark_request(CadRequest):
    """
    Request model for watermark operation.
    Initializes a new instance.

    :param output_format 
    :param drawing 
    :param watermark_rgb 
    :param output_type_ext 
    """

    def __init__(self, output_format, drawing=None, watermark_rgb=None, output_type_ext=None):
        CadRequest.__init__(self)
        self.output_format = output_format
        self.drawing = drawing
        self.watermark_rgb = watermark_rgb
        self.output_type_ext = output_type_ext

    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        # verify the required parameter 'output_format' is set
        if self.output_format is None:
            raise ValueError("Missing the required parameter `output_format` when calling `watermark`")

        collection_formats = {}
        path = '/cad/Watermark'
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
            ['multipart/form-data', 'application/octet-stream'])

        # Authentication setting
        auth_settings = ['Bearer']

        return HttpRequest(path, path_params, query_params, header_params, form_params, body_params, local_var_files,
                           collection_formats, auth_settings)

#  coding: utf-8
#  --------------------------------------------------------------
#  <copyright company="Aspose" file="cad_request.py">
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
#  --------------------------------------------------------------

from abc import ABCMeta, abstractmethod


class cad_request(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def to_http_info(self, config):
        """
        Prepares initial info for HTTP request

        :param config: CAD API configuration.
        :type: asposecadcloud.Configuration
        :return: HttpRequest configured http request
        :rtype: Configuration.models.requests.HttpRequest
        """
        pass

    @staticmethod
    def _select_header_accept(accepts):
        """Returns `Accept` based on an array of accepts provided.

        :param accepts: List of headers.
        :return: Accept (e.g. application/json).
        """
        if not accepts:
            return None

        accepts = [x.lower() for x in accepts]

        if 'application/json' in accepts:
            return 'application/json'

        return ', '.join(accepts)

    @staticmethod
    def _select_header_content_type(content_types):
        """Returns `Content-Type` based on an array of content_types provided.

        :param content_types: List of content-types.
        :return: Content-Type (e.g. application/json).
        """
        if not content_types:
            return 'application/json'

        content_types = [x.lower() for x in content_types]

        if 'application/json' in content_types or '*/*' in content_types:
            return 'application/json'

        return content_types[0]

    @staticmethod
    def _lowercase_first_letter(string):
        """
        Converts first letter of the string to lowercase

        :param string: initial string
        :return: initial string with first character in lowercase
        """
        if not string:
            return string

        return string[0].lower() + string[1:]
