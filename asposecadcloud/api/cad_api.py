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


        :param request ConvertRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def convert_async(self, request):
        """Convert CAD drawing to DXF, DWG, DGN, DWF, DWFX, IFC, STL, STP, STEP, CGM, GLB, GLTF, DWT, IGES, PLT, CF2, OBJ, HPGL, IGS, PCL, FBX, PDF, SVG format.


        :param request ConvertRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def copy_file(self, request):
        """Copy file


        :param request CopyFileRequest object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', None)

    def copy_file_async(self, request):
        """Copy file


        :param request CopyFileRequest object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', None)

    def copy_folder(self, request):
        """Copy folder


        :param request CopyFolderRequest object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', None)

    def copy_folder_async(self, request):
        """Copy folder


        :param request CopyFolderRequest object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', None)

    def create_folder(self, request):
        """Create the folder


        :param request CreateFolderRequest object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', None)

    def create_folder_async(self, request):
        """Create the folder


        :param request CreateFolderRequest object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', None)

    def delete_file(self, request):
        """Delete file


        :param request DeleteFileRequest object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'DELETE', None)

    def delete_file_async(self, request):
        """Delete file


        :param request DeleteFileRequest object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'DELETE', None)

    def delete_folder(self, request):
        """Delete folder


        :param request DeleteFolderRequest object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'DELETE', None)

    def delete_folder_async(self, request):
        """Delete folder


        :param request DeleteFolderRequest object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'DELETE', None)

    def download_file(self, request):
        """Download file


        :param request DownloadFileRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'GET', 'file')

    def download_file_async(self, request):
        """Download file


        :param request DownloadFileRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'GET', 'file')

    def edit_metadata(self, request):
        """Get Metadata info.


        :param request EditMetadataRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def edit_metadata_async(self, request):
        """Get Metadata info.


        :param request EditMetadataRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def edit_metadata2(self, request):
        """Save Metadata.


        :param request EditMetadata2Request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def edit_metadata2_async(self, request):
        """Save Metadata.


        :param request EditMetadata2Request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def extract_metadata(self, request):
        """Extract Metadata from CAD drawing to txt, xml or json file.


        :param request ExtractMetadataRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def extract_metadata_async(self, request):
        """Extract Metadata from CAD drawing to txt, xml or json file.


        :param request ExtractMetadataRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def extract_text(self, request):
        """Extract Text from CAD drawing to txt file.


        :param request ExtractTextRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def extract_text_async(self, request):
        """Extract Text from CAD drawing to txt file.


        :param request ExtractTextRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def get_disc_usage(self, request):
        """Get disc usage


        :param request GetDiscUsageRequest object with parameters
        :return: DiscUsage
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'GET', 'DiscUsage')

    def get_disc_usage_async(self, request):
        """Get disc usage


        :param request GetDiscUsageRequest object with parameters
        :return: DiscUsage
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'GET', 'DiscUsage')

    def get_drawing_properties(self, request):
        """Retrieves info about an existing drawing.             


        :param request GetDrawingPropertiesRequest object with parameters
        :return: CadResponse
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'GET', 'CadResponse')

    def get_drawing_properties_async(self, request):
        """Retrieves info about an existing drawing.             


        :param request GetDrawingPropertiesRequest object with parameters
        :return: CadResponse
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'GET', 'CadResponse')

    def get_drawing_resize(self, request):
        """Resize an existing drawing.


        :param request GetDrawingResizeRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'GET', 'file')

    def get_drawing_resize_async(self, request):
        """Resize an existing drawing.


        :param request GetDrawingResizeRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'GET', 'file')

    def get_drawing_rotate_flip(self, request):
        """Rotate/flip an existing drawing.


        :param request GetDrawingRotateFlipRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'GET', 'file')

    def get_drawing_rotate_flip_async(self, request):
        """Rotate/flip an existing drawing.


        :param request GetDrawingRotateFlipRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'GET', 'file')

    def get_drawing_save_as(self, request):
        """Export an existing drawing to another format.


        :param request GetDrawingSaveAsRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'GET', 'file')

    def get_drawing_save_as_async(self, request):
        """Export an existing drawing to another format.


        :param request GetDrawingSaveAsRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'GET', 'file')

    def get_file_versions(self, request):
        """Get file versions


        :param request GetFileVersionsRequest object with parameters
        :return: FileVersions
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'GET', 'FileVersions')

    def get_file_versions_async(self, request):
        """Get file versions


        :param request GetFileVersionsRequest object with parameters
        :return: FileVersions
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'GET', 'FileVersions')

    def get_files_list(self, request):
        """Get all files and folders within a folder


        :param request GetFilesListRequest object with parameters
        :return: FilesList
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'GET', 'FilesList')

    def get_files_list_async(self, request):
        """Get all files and folders within a folder


        :param request GetFilesListRequest object with parameters
        :return: FilesList
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'GET', 'FilesList')

    def move_file(self, request):
        """Move file


        :param request MoveFileRequest object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', None)

    def move_file_async(self, request):
        """Move file


        :param request MoveFileRequest object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', None)

    def move_folder(self, request):
        """Move folder


        :param request MoveFolderRequest object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', None)

    def move_folder_async(self, request):
        """Move folder


        :param request MoveFolderRequest object with parameters
        :return: None
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', None)

    def object_exists(self, request):
        """Check if file or folder exists


        :param request ObjectExistsRequest object with parameters
        :return: ObjectExist
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'GET', 'ObjectExist')

    def object_exists_async(self, request):
        """Check if file or folder exists


        :param request ObjectExistsRequest object with parameters
        :return: ObjectExist
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'GET', 'ObjectExist')

    def paper_to_cad(self, request):
        """Convert bitmap image to DXF, DWG, DGN, DWF, DWFX, IFC, STL, STP, STEP, CGM, GLB, GLTF, DWT, IGES, PLT, CF2, OBJ, HPGL, IGS, PCL, FBX, SVG format.


        :param request paper_to_CadRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def paper_to_cad_async(self, request):
        """Convert bitmap image to DXF, DWG, DGN, DWF, DWFX, IFC, STL, STP, STEP, CGM, GLB, GLTF, DWT, IGES, PLT, CF2, OBJ, HPGL, IGS, PCL, FBX, SVG format.


        :param request paper_to_CadRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_bmp(self, request):
        """Export an existing drawing to BMP format with export settings specified.


        :param request PostDrawingBmpRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_bmp_async(self, request):
        """Export an existing drawing to BMP format with export settings specified.


        :param request PostDrawingBmpRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_cgm(self, request):
        """Export an existing drawing to CGM format with export settings specified.


        :param request PostDrawingCgmRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_cgm_async(self, request):
        """Export an existing drawing to CGM format with export settings specified.


        :param request PostDrawingCgmRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_dwf(self, request):
        """Export an existing drawing to Dwf format with export settings specified.


        :param request PostDrawingDwfRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_dwf_async(self, request):
        """Export an existing drawing to Dwf format with export settings specified.


        :param request PostDrawingDwfRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_dxf(self, request):
        """Export an existing drawing to DXF format with export settings specified.


        :param request PostDrawingDxfRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_dxf_async(self, request):
        """Export an existing drawing to DXF format with export settings specified.


        :param request PostDrawingDxfRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_fbx(self, request):
        """Export an existing drawing to Fbx format with export settings specified.


        :param request PostDrawingFbxRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_fbx_async(self, request):
        """Export an existing drawing to Fbx format with export settings specified.


        :param request PostDrawingFbxRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_gif(self, request):
        """Export an existing drawing into GIF format with export settings specified.


        :param request PostDrawingGifRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_gif_async(self, request):
        """Export an existing drawing into GIF format with export settings specified.


        :param request PostDrawingGifRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_glb(self, request):
        """Export an existing drawing to GLB format with export settings specified.


        :param request PostDrawingGlbRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_glb_async(self, request):
        """Export an existing drawing to GLB format with export settings specified.


        :param request PostDrawingGlbRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_gltf(self, request):
        """Export an existing drawing to GLTF format with export settings specified.


        :param request PostDrawingGltfRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_gltf_async(self, request):
        """Export an existing drawing to GLTF format with export settings specified.


        :param request PostDrawingGltfRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_jpeg(self, request):
        """Export an existing drawing into JPEG format with export settings specified.


        :param request PostDrawingJpegRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_jpeg_async(self, request):
        """Export an existing drawing into JPEG format with export settings specified.


        :param request PostDrawingJpegRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_jpeg2000(self, request):
        """Export an existing drawing into JPEG2000 format with export settings specified.


        :param request PostDrawingJpeg2000Request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_jpeg2000_async(self, request):
        """Export an existing drawing into JPEG2000 format with export settings specified.


        :param request PostDrawingJpeg2000Request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_obj(self, request):
        """Export an existing drawing to Obj format with export settings specified.


        :param request PostDrawingObjRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_obj_async(self, request):
        """Export an existing drawing to Obj format with export settings specified.


        :param request PostDrawingObjRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_pdf(self, request):
        """Export an existing drawing to PDF format with export settings specified.


        :param request PostDrawingPdfRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_pdf_async(self, request):
        """Export an existing drawing to PDF format with export settings specified.


        :param request PostDrawingPdfRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_png(self, request):
        """Export an existing drawing into PNG format with export settings specified.


        :param request PostDrawingPngRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_png_async(self, request):
        """Export an existing drawing into PNG format with export settings specified.


        :param request PostDrawingPngRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_properties(self, request):
        """Retrieves info about drawing which is passed as a zero-indexed multipart/form-data content or as raw body stream.


        :param request PostDrawingPropertiesRequest object with parameters
        :return: CadResponse
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'CadResponse')

    def post_drawing_properties_async(self, request):
        """Retrieves info about drawing which is passed as a zero-indexed multipart/form-data content or as raw body stream.


        :param request PostDrawingPropertiesRequest object with parameters
        :return: CadResponse
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'CadResponse')

    def post_drawing_psd(self, request):
        """Export an existing drawing into PSD format with export settings specified.


        :param request PostDrawingPsdRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_psd_async(self, request):
        """Export an existing drawing into PSD format with export settings specified.


        :param request PostDrawingPsdRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_resize(self, request):
        """Resize a drawing. Drawing data is passed as a zero-indexed multipart/form-data content or as raw body stream.


        :param request PostDrawingResizeRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_resize_async(self, request):
        """Resize a drawing. Drawing data is passed as a zero-indexed multipart/form-data content or as raw body stream.


        :param request PostDrawingResizeRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_rotate_flip(self, request):
        """Rotate/flip a drawing. Drawing data is passed as a zero-indexed multipart/form-data content or as raw body stream.


        :param request PostDrawingRotateFlipRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_rotate_flip_async(self, request):
        """Rotate/flip a drawing. Drawing data is passed as a zero-indexed multipart/form-data content or as raw body stream.


        :param request PostDrawingRotateFlipRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_save_as(self, request):
        """Export existing drawing to another format. Drawing data is passed as zero-indexed multipart/form-data content or as raw body stream.             


        :param request PostDrawingSaveAsRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_save_as_async(self, request):
        """Export existing drawing to another format. Drawing data is passed as zero-indexed multipart/form-data content or as raw body stream.             


        :param request PostDrawingSaveAsRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_stp(self, request):
        """Export an existing drawing to STP format with export settings specified.


        :param request PostDrawingStpRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_stp_async(self, request):
        """Export an existing drawing to STP format with export settings specified.


        :param request PostDrawingStpRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_svg(self, request):
        """Export an existing drawing to SVG format with export settings specified.


        :param request PostDrawingSvgRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_svg_async(self, request):
        """Export an existing drawing to SVG format with export settings specified.


        :param request PostDrawingSvgRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_three_ds(self, request):
        """Export an existing drawing to 3DS format with export settings specified.


        :param request PostDrawingThreeDsRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_three_ds_async(self, request):
        """Export an existing drawing to 3DS format with export settings specified.


        :param request PostDrawingThreeDsRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_tiff(self, request):
        """Export an existing drawing into TIFF format with export settings specified.


        :param request PostDrawingTiffRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_tiff_async(self, request):
        """Export an existing drawing into TIFF format with export settings specified.


        :param request PostDrawingTiffRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_u3d(self, request):
        """Export an existing drawing to U3D format with export settings specified.


        :param request PostDrawingU3dRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_u3d_async(self, request):
        """Export an existing drawing to U3D format with export settings specified.


        :param request PostDrawingU3dRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def post_drawing_wmf(self, request):
        """Export an existing drawing to WMF format with export settings specified.


        :param request PostDrawingWmfRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def post_drawing_wmf_async(self, request):
        """Export an existing drawing to WMF format with export settings specified.


        :param request PostDrawingWmfRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def put_drawing_bmp(self, request):
        """Export drawing to BMP format. Drawing data is passed as zero-indexed multipart/form-data as well as export BMP options serialized as JSON. Order of drawing data and BMP options could vary.


        :param request PutDrawingBmpRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_bmp_async(self, request):
        """Export drawing to BMP format. Drawing data is passed as zero-indexed multipart/form-data as well as export BMP options serialized as JSON. Order of drawing data and BMP options could vary.


        :param request PutDrawingBmpRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_cgm(self, request):
        """Export drawing to CGM format. Drawing data is passed as zero-indexed multipart/form-data as well as export Cgm options serialized as JSON. Order of drawing data and Cgm options could vary.


        :param request PutDrawingCgmRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_cgm_async(self, request):
        """Export drawing to CGM format. Drawing data is passed as zero-indexed multipart/form-data as well as export Cgm options serialized as JSON. Order of drawing data and Cgm options could vary.


        :param request PutDrawingCgmRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_dwf(self, request):
        """Export drawing to Dwf format. Drawing data is passed as zero-indexed multipart/form-data as well as export Dwf options serialized as JSON. Order of drawing data and Dwf options could vary.


        :param request PutDrawingDwfRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_dwf_async(self, request):
        """Export drawing to Dwf format. Drawing data is passed as zero-indexed multipart/form-data as well as export Dwf options serialized as JSON. Order of drawing data and Dwf options could vary.


        :param request PutDrawingDwfRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_dxf(self, request):
        """Export drawing to DXF format. Drawing data is passed as zero-indexed multipart/form-data as well as export DXF options serialized as JSON. Order of drawing data and DXF options could vary.


        :param request PutDrawingDxfRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_dxf_async(self, request):
        """Export drawing to DXF format. Drawing data is passed as zero-indexed multipart/form-data as well as export DXF options serialized as JSON. Order of drawing data and DXF options could vary.


        :param request PutDrawingDxfRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_fbx(self, request):
        """Export drawing to Fbx format. Drawing data is passed as zero-indexed multipart/form-data as well as export Fbx options serialized as JSON. Order of drawing data and Fbx options could vary.


        :param request PutDrawingFbxRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_fbx_async(self, request):
        """Export drawing to Fbx format. Drawing data is passed as zero-indexed multipart/form-data as well as export Fbx options serialized as JSON. Order of drawing data and Fbx options could vary.


        :param request PutDrawingFbxRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_gif(self, request):
        """Export drawing to GIF format. Drawing data is passed as zero-indexed multipart/form-data as well as export GIF options serialized as JSON. Order of drawing data and GIF options could vary.


        :param request PutDrawingGifRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_gif_async(self, request):
        """Export drawing to GIF format. Drawing data is passed as zero-indexed multipart/form-data as well as export GIF options serialized as JSON. Order of drawing data and GIF options could vary.


        :param request PutDrawingGifRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_glb(self, request):
        """Export drawing to GLB format. Drawing data is passed as zero-indexed multipart/form-data as well as export GLB options serialized as JSON. Order of drawing data and GLB options could vary.


        :param request PutDrawingGlbRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_glb_async(self, request):
        """Export drawing to GLB format. Drawing data is passed as zero-indexed multipart/form-data as well as export GLB options serialized as JSON. Order of drawing data and GLB options could vary.


        :param request PutDrawingGlbRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_gltf(self, request):
        """Export drawing to GLTF format. Drawing data is passed as zero-indexed multipart/form-data as well as export GLTF options serialized as JSON. Order of drawing data and GLTF options could vary.


        :param request PutDrawingGltfRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_gltf_async(self, request):
        """Export drawing to GLTF format. Drawing data is passed as zero-indexed multipart/form-data as well as export GLTF options serialized as JSON. Order of drawing data and GLTF options could vary.


        :param request PutDrawingGltfRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_jpeg(self, request):
        """Export drawing to JPEG format. Drawing data is passed as zero-indexed multipart/form-data as well as export JPEG options serialized as JSON. Order of drawing data and JPEG options could vary.


        :param request PutDrawingJpegRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_jpeg_async(self, request):
        """Export drawing to JPEG format. Drawing data is passed as zero-indexed multipart/form-data as well as export JPEG options serialized as JSON. Order of drawing data and JPEG options could vary.


        :param request PutDrawingJpegRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_jpeg2000(self, request):
        """Export drawing to JPEG2000 format. Drawing data is passed as zero-indexed multipart/form-data as well as export JPEG2000 options serialized as JSON. Order of drawing data and JPEG2000 options could vary.


        :param request PutDrawingJpeg2000Request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_jpeg2000_async(self, request):
        """Export drawing to JPEG2000 format. Drawing data is passed as zero-indexed multipart/form-data as well as export JPEG2000 options serialized as JSON. Order of drawing data and JPEG2000 options could vary.


        :param request PutDrawingJpeg2000Request object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_obj(self, request):
        """Export drawing to Obj format. Drawing data is passed as zero-indexed multipart/form-data as well as export Obj options serialized as JSON. Order of drawing data and Obj options could vary.


        :param request PutDrawingObjRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_obj_async(self, request):
        """Export drawing to Obj format. Drawing data is passed as zero-indexed multipart/form-data as well as export Obj options serialized as JSON. Order of drawing data and Obj options could vary.


        :param request PutDrawingObjRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_pdf(self, request):
        """Export drawing to PDF format. Drawing data is passed as zero-indexed multipart/form-data as well as export PDF options serialized as JSON. Order of drawing data and PDF options could vary.


        :param request PutDrawingPdfRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_pdf_async(self, request):
        """Export drawing to PDF format. Drawing data is passed as zero-indexed multipart/form-data as well as export PDF options serialized as JSON. Order of drawing data and PDF options could vary.


        :param request PutDrawingPdfRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_png(self, request):
        """Export drawing to PNG format. Drawing data is passed as zero-indexed multipart/form-data as well as export PNG options serialized as JSON. Order of drawing data and PNG options could vary.


        :param request PutDrawingPngRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_png_async(self, request):
        """Export drawing to PNG format. Drawing data is passed as zero-indexed multipart/form-data as well as export PNG options serialized as JSON. Order of drawing data and PNG options could vary.


        :param request PutDrawingPngRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_psd(self, request):
        """Export drawing to PSD format. Drawing data is passed as zero-indexed multipart/form-data as well as export PSD options serialized as JSON. Order of drawing data and PSD options could vary.


        :param request PutDrawingPsdRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_psd_async(self, request):
        """Export drawing to PSD format. Drawing data is passed as zero-indexed multipart/form-data as well as export PSD options serialized as JSON. Order of drawing data and PSD options could vary.


        :param request PutDrawingPsdRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_stp(self, request):
        """Export drawing to Stp format. Drawing data is passed as zero-indexed multipart/form-data as well as export Stp options serialized as JSON. Order of drawing data and Stp options could vary.


        :param request PutDrawingStpRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_stp_async(self, request):
        """Export drawing to Stp format. Drawing data is passed as zero-indexed multipart/form-data as well as export Stp options serialized as JSON. Order of drawing data and Stp options could vary.


        :param request PutDrawingStpRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_svg(self, request):
        """Export drawing to SVG format. Drawing data is passed as zero-indexed multipart/form-data as well as export SVG options serialized as JSON. Order of drawing data and SVG options could vary.


        :param request PutDrawingSvgRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_svg_async(self, request):
        """Export drawing to SVG format. Drawing data is passed as zero-indexed multipart/form-data as well as export SVG options serialized as JSON. Order of drawing data and SVG options could vary.


        :param request PutDrawingSvgRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_three_ds(self, request):
        """Export drawing to 3DS format. Drawing data is passed as zero-indexed multipart/form-data as well as export 3DS options serialized as JSON. Order of drawing data and 3DS options could vary.


        :param request PutDrawingThreeDsRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_three_ds_async(self, request):
        """Export drawing to 3DS format. Drawing data is passed as zero-indexed multipart/form-data as well as export 3DS options serialized as JSON. Order of drawing data and 3DS options could vary.


        :param request PutDrawingThreeDsRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_tiff(self, request):
        """Export drawing to TIFF format. Drawing data is passed as zero-indexed multipart/form-data as well as export TIFF options serialized as JSON. Order of drawing data and TIFF options could vary.


        :param request PutDrawingTiffRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_tiff_async(self, request):
        """Export drawing to TIFF format. Drawing data is passed as zero-indexed multipart/form-data as well as export TIFF options serialized as JSON. Order of drawing data and TIFF options could vary.


        :param request PutDrawingTiffRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_u3d(self, request):
        """Export drawing to U3D format. Drawing data is passed as zero-indexed multipart/form-data as well as export U3D options serialized as JSON. Order of drawing data and U3D options could vary.


        :param request PutDrawingU3dRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_u3d_async(self, request):
        """Export drawing to U3D format. Drawing data is passed as zero-indexed multipart/form-data as well as export U3D options serialized as JSON. Order of drawing data and U3D options could vary.


        :param request PutDrawingU3dRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def put_drawing_wmf(self, request):
        """Export drawing to WMF format. Drawing data is passed as zero-indexed multipart/form-data as well as export WMF options serialized as JSON. Order of drawing data and WMF options could vary.


        :param request PutDrawingWmfRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'file')

    def put_drawing_wmf_async(self, request):
        """Export drawing to WMF format. Drawing data is passed as zero-indexed multipart/form-data as well as export WMF options serialized as JSON. Order of drawing data and WMF options could vary.


        :param request PutDrawingWmfRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'file')

    def storage_exists(self, request):
        """Check if storage exists


        :param request StorageExistsRequest object with parameters
        :return: StorageExist
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'GET', 'StorageExist')

    def storage_exists_async(self, request):
        """Check if storage exists


        :param request StorageExistsRequest object with parameters
        :return: StorageExist
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'GET', 'StorageExist')

    def upload_file(self, request):
        """Upload file


        :param request UploadFileRequest object with parameters
        :return: FilesUploadResult
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'PUT', 'FilesUploadResult')

    def upload_file_async(self, request):
        """Upload file


        :param request UploadFileRequest object with parameters
        :return: FilesUploadResult
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'PUT', 'FilesUploadResult')

    def viewer(self, request):
        """Return file for viewer.


        :param request ViewerRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def viewer_async(self, request):
        """Return file for viewer.


        :param request ViewerRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request_async(HttpRequest, 'POST', 'file')

    def watermark(self, request):
        """Convert CAD drawing to DXF, DWG, DGN, DWF, DWFX, IFC, STL, STP, STEP, CGM, GLB, GLTF, DWT, IGES, PLT, CF2, OBJ, HPGL, IGS, PCL, FBX, PDF, SVG format.


        :param request WatermarkRequest object with parameters
        :return: file
        """
        HttpRequest = request.to_http_info(self.api_client.configuration)
        return self.__make_request(HttpRequest, 'POST', 'file')

    def watermark_async(self, request):
        """Convert CAD drawing to DXF, DWG, DGN, DWF, DWFX, IFC, STL, STP, STEP, CGM, GLB, GLTF, DWT, IGES, PLT, CF2, OBJ, HPGL, IGS, PCL, FBX, PDF, SVG format.


        :param request WatermarkRequest object with parameters
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

