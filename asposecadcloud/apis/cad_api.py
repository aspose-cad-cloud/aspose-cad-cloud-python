# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="cad_api.py">
#   Copyright (c) 2018 Aspose.CAD Cloud
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six
from asposecadcloud.rest import ApiException
from asposecadcloud.api_client import ApiClient


class CadApi(object):
    """
    Aspose.CAD Cloud API

    :param api_client: an api client to perfom http requests
    """
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.__request_token()

    def get_drawing_properties(self, request, **kwargs):  # noqa: E501
        """Retrieves info about an existing drawing.               # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : Filename of an input drawing on a storage. (required)
        :param folder str : Folder with a drawing to get properties for.
        :param storage str : Your Aspose Cloud Storage name.
        :return: CadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_drawing_properties_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_drawing_properties_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_drawing_properties_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_drawing_properties_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_drawing_properties_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves info about an existing drawing.               # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDrawingPropertiesRequest object with parameters
        :return: CadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_drawing_properties" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_drawing_properties`")  # noqa: E501

        collection_formats = {}
        path = '/cad/{name}/properties'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CadResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_drawing_resize(self, request, **kwargs):  # noqa: E501
        """Resize an existing drawing.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : Filename of a drawing. (required)
        :param output_format str : Resulting file format. (required)
        :param new_width int : New width. (required)
        :param new_height int : New height. (required)
        :param folder str : Folder with a drawing to process.
        :param out_path str : Path to updated file (if this is empty, response contains streamed file).
        :param storage str : Your Aspose Cloud Storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_drawing_resize_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_drawing_resize_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_drawing_resize_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_drawing_resize_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_drawing_resize_with_http_info(self, request, **kwargs):  # noqa: E501
        """Resize an existing drawing.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDrawingResizeRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_drawing_resize" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_drawing_resize`")  # noqa: E501
        # verify the required parameter 'output_format' is set
        if request.output_format is None:
            raise ValueError("Missing the required parameter `output_format` when calling `get_drawing_resize`")  # noqa: E501
        # verify the required parameter 'new_width' is set
        if request.new_width is None:
            raise ValueError("Missing the required parameter `new_width` when calling `get_drawing_resize`")  # noqa: E501
        # verify the required parameter 'new_height' is set
        if request.new_height is None:
            raise ValueError("Missing the required parameter `new_height` when calling `get_drawing_resize`")  # noqa: E501

        collection_formats = {}
        path = '/cad/{name}/resize'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('outputFormat') in path:
            path = path.replace('{' + self.__downcase_first_letter('outputFormat' + '}'), request.output_format if request.output_format is not None else '')
        else:
            if request.output_format is not None:
                query_params.append((self.__downcase_first_letter('outputFormat'), request.output_format))  # noqa: E501
        if self.__downcase_first_letter('newWidth') in path:
            path = path.replace('{' + self.__downcase_first_letter('newWidth' + '}'), request.new_width if request.new_width is not None else '')
        else:
            if request.new_width is not None:
                query_params.append((self.__downcase_first_letter('newWidth'), request.new_width))  # noqa: E501
        if self.__downcase_first_letter('newHeight') in path:
            path = path.replace('{' + self.__downcase_first_letter('newHeight' + '}'), request.new_height if request.new_height is not None else '')
        else:
            if request.new_height is not None:
                query_params.append((self.__downcase_first_letter('newHeight'), request.new_height))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_drawing_rotate_flip(self, request, **kwargs):  # noqa: E501
        """Rotate/flip an existing drawing.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : Filename of a drawing. (required)
        :param output_format str : Resulting file format. (required)
        :param rotate_flip_type str : Rotate/flip operation to apply. (required)
        :param folder str : Folder with a drawing to process.
        :param out_path str : Path to updated file (if this is empty, response contains streamed file).
        :param storage str : Your Aspose Cloud Storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_drawing_rotate_flip_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_drawing_rotate_flip_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_drawing_rotate_flip_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_drawing_rotate_flip_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_drawing_rotate_flip_with_http_info(self, request, **kwargs):  # noqa: E501
        """Rotate/flip an existing drawing.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDrawingRotateFlipRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_drawing_rotate_flip" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_drawing_rotate_flip`")  # noqa: E501
        # verify the required parameter 'output_format' is set
        if request.output_format is None:
            raise ValueError("Missing the required parameter `output_format` when calling `get_drawing_rotate_flip`")  # noqa: E501
        # verify the required parameter 'rotate_flip_type' is set
        if request.rotate_flip_type is None:
            raise ValueError("Missing the required parameter `rotate_flip_type` when calling `get_drawing_rotate_flip`")  # noqa: E501

        collection_formats = {}
        path = '/cad/{name}/rotateflip'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('outputFormat') in path:
            path = path.replace('{' + self.__downcase_first_letter('outputFormat' + '}'), request.output_format if request.output_format is not None else '')
        else:
            if request.output_format is not None:
                query_params.append((self.__downcase_first_letter('outputFormat'), request.output_format))  # noqa: E501
        if self.__downcase_first_letter('rotateFlipType') in path:
            path = path.replace('{' + self.__downcase_first_letter('rotateFlipType' + '}'), request.rotate_flip_type if request.rotate_flip_type is not None else '')
        else:
            if request.rotate_flip_type is not None:
                query_params.append((self.__downcase_first_letter('rotateFlipType'), request.rotate_flip_type))  # noqa: E501
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_drawing_save_as(self, request, **kwargs):  # noqa: E501
        """Export an existing drawing to another format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : Filename of an input drawing on a storage. (required)
        :param output_format str : Resulting file format. (required)
        :param folder str : Folder with a drawing to process.
        :param out_path str : Path to updated file (if this is empty, response contains streamed file).
        :param storage str : Your Aspose Cloud Storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.get_drawing_save_as_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_drawing_save_as_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.get_drawing_save_as_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.get_drawing_save_as_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def get_drawing_save_as_with_http_info(self, request, **kwargs):  # noqa: E501
        """Export an existing drawing to another format.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request GetDrawingSaveAsRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_drawing_save_as" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `get_drawing_save_as`")  # noqa: E501
        # verify the required parameter 'output_format' is set
        if request.output_format is None:
            raise ValueError("Missing the required parameter `output_format` when calling `get_drawing_save_as`")  # noqa: E501

        collection_formats = {}
        path = '/cad/{name}/saveAs/{outputFormat}'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501
        if request.output_format is not None:
            path_params[self.__downcase_first_letter('outputFormat')] = request.output_format  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_drawing_bmp(self, request, **kwargs):  # noqa: E501
        """Export an existing drawing to BMP format with export settings specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : Filename of an input drawing on a storage. (required)
        :param options BmpOptionsDTO : Export BMP options passed as a JSON on a request body. (required)
        :param folder str : Folder with a drawing to process.
        :param out_path str : Path to updated file (if this is empty, response contains streamed file).
        :param storage str : Your Aspose Cloud Storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_drawing_bmp_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_bmp_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_drawing_bmp_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_bmp_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_drawing_bmp_with_http_info(self, request, **kwargs):  # noqa: E501
        """Export an existing drawing to BMP format with export settings specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostDrawingBmpRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_drawing_bmp" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_bmp`")  # noqa: E501
        # verify the required parameter 'options' is set
        if request.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_bmp`")  # noqa: E501

        collection_formats = {}
        path = '/cad/{name}/bmp'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.options is not None:
            body_params = request.options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_drawing_gif(self, request, **kwargs):  # noqa: E501
        """Export an existing drawing into GIF format with export settings specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : Filename of an input drawing on a storage. (required)
        :param options GifOptionsDTO : Export GIF options passed as a JSON on a request body. (required)
        :param folder str : Folder with a drawing to process.
        :param out_path str : Path to updated file (if this is empty, response contains streamed file).
        :param storage str : Your Aspose Cloud Storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_drawing_gif_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_gif_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_drawing_gif_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_gif_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_drawing_gif_with_http_info(self, request, **kwargs):  # noqa: E501
        """Export an existing drawing into GIF format with export settings specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostDrawingGifRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_drawing_gif" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_gif`")  # noqa: E501
        # verify the required parameter 'options' is set
        if request.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_gif`")  # noqa: E501

        collection_formats = {}
        path = '/cad/{name}/gif'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.options is not None:
            body_params = request.options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_drawing_jpeg(self, request, **kwargs):  # noqa: E501
        """Export an existing drawing into JPEG format with export settings specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : Filename of an input drawing on a storage. (required)
        :param options JpegOptionsDTO : Export JPEG options passed as a JSON on a request body. (required)
        :param folder str : Folder with a drawing to process.
        :param out_path str : Path to updated file (if this is empty, response contains streamed file).
        :param storage str : Your Aspose Cloud Storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_drawing_jpeg_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_jpeg_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_drawing_jpeg_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_jpeg_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_drawing_jpeg_with_http_info(self, request, **kwargs):  # noqa: E501
        """Export an existing drawing into JPEG format with export settings specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostDrawingJpegRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_drawing_jpeg" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_jpeg`")  # noqa: E501
        # verify the required parameter 'options' is set
        if request.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_jpeg`")  # noqa: E501

        collection_formats = {}
        path = '/cad/{name}/jpeg'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.options is not None:
            body_params = request.options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_drawing_jpeg2000(self, request, **kwargs):  # noqa: E501
        """Export an existing drawing into JPEG2000 format with export settings specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : Filename of an input drawing on a storage. (required)
        :param options Jpeg2000OptionsDTO : Export JPEG2000 options passed as a JSON on a request body. (required)
        :param folder str : Folder with a drawing to process.
        :param out_path str : Path to updated file (if this is empty, response contains streamed file).
        :param storage str : Your Aspose Cloud Storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_drawing_jpeg2000_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_jpeg2000_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_drawing_jpeg2000_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_jpeg2000_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_drawing_jpeg2000_with_http_info(self, request, **kwargs):  # noqa: E501
        """Export an existing drawing into JPEG2000 format with export settings specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostDrawingJpeg2000Request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_drawing_jpeg2000" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_jpeg2000`")  # noqa: E501
        # verify the required parameter 'options' is set
        if request.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_jpeg2000`")  # noqa: E501

        collection_formats = {}
        path = '/cad/{name}/jpeg2000'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.options is not None:
            body_params = request.options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_drawing_pdf(self, request, **kwargs):  # noqa: E501
        """Export an existing drawing to PDF format with export settings specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : Filename of an input drawing on a storage. (required)
        :param options PdfOptionsDTO : Export PDF options passed as a JSON on a request body. (required)
        :param folder str : Folder with a drawing to process.
        :param out_path str : Path to updated file (if this is empty, response contains streamed file).
        :param storage str : Your Aspose Cloud Storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_drawing_pdf_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_pdf_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_drawing_pdf_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_pdf_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_drawing_pdf_with_http_info(self, request, **kwargs):  # noqa: E501
        """Export an existing drawing to PDF format with export settings specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostDrawingPdfRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_drawing_pdf" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_pdf`")  # noqa: E501
        # verify the required parameter 'options' is set
        if request.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_pdf`")  # noqa: E501

        collection_formats = {}
        path = '/cad/{name}/pdf'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.options is not None:
            body_params = request.options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_drawing_png(self, request, **kwargs):  # noqa: E501
        """Export an existing drawing into PNG format with export settings specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : Filename of an input drawing on a storage. (required)
        :param options PngOptionsDTO : Export PNG options passed as a JSON on a request body. (required)
        :param folder str : Folder with a drawing to process.
        :param out_path str : Path to updated file (if this is empty, response contains streamed file).
        :param storage str : Your Aspose Cloud Storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_drawing_png_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_png_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_drawing_png_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_png_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_drawing_png_with_http_info(self, request, **kwargs):  # noqa: E501
        """Export an existing drawing into PNG format with export settings specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostDrawingPngRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_drawing_png" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_png`")  # noqa: E501
        # verify the required parameter 'options' is set
        if request.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_png`")  # noqa: E501

        collection_formats = {}
        path = '/cad/{name}/png'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.options is not None:
            body_params = request.options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_drawing_properties(self, request, **kwargs):  # noqa: E501
        """Retrieves info about drawing which is passed as a zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param drawing_data file : Input drawing (required)
        :return: CadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_drawing_properties_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_properties_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_drawing_properties_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_properties_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_drawing_properties_with_http_info(self, request, **kwargs):  # noqa: E501
        """Retrieves info about drawing which is passed as a zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostDrawingPropertiesRequest object with parameters
        :return: CadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_drawing_properties" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'drawing_data' is set
        if request.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `post_drawing_properties`")  # noqa: E501

        collection_formats = {}
        path = '/cad/properties'
        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = []
        if request.drawing_data is not None:
            local_var_files.append((self.__downcase_first_letter('drawingData'), request.drawing_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data', 'application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CadResponse',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_drawing_psd(self, request, **kwargs):  # noqa: E501
        """Export an existing drawing into PSD format with export settings specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : Filename of an input drawing on a storage. (required)
        :param options PsdOptionsDTO : Export PSD options passed as a JSON on a request body. (required)
        :param folder str : Folder with a drawing to process.
        :param out_path str : Path to updated file (if this is empty, response contains streamed file).
        :param storage str : Your Aspose Cloud Storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_drawing_psd_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_psd_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_drawing_psd_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_psd_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_drawing_psd_with_http_info(self, request, **kwargs):  # noqa: E501
        """Export an existing drawing into PSD format with export settings specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostDrawingPsdRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_drawing_psd" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_psd`")  # noqa: E501
        # verify the required parameter 'options' is set
        if request.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_psd`")  # noqa: E501

        collection_formats = {}
        path = '/cad/{name}/psd'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.options is not None:
            body_params = request.options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_drawing_resize(self, request, **kwargs):  # noqa: E501
        """Resize a drawing. Drawing data is passed as a zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param drawing_data file : Input drawing (required)
        :param output_format str : Resulting file format. (required)
        :param new_width int : New width. (required)
        :param new_height int : New height. (required)
        :param out_path str : Path to updated file (if this is empty, response contains streamed file).
        :param storage str : Your Aspose Cloud Storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_drawing_resize_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_resize_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_drawing_resize_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_resize_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_drawing_resize_with_http_info(self, request, **kwargs):  # noqa: E501
        """Resize a drawing. Drawing data is passed as a zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostDrawingResizeRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_drawing_resize" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'drawing_data' is set
        if request.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `post_drawing_resize`")  # noqa: E501
        # verify the required parameter 'output_format' is set
        if request.output_format is None:
            raise ValueError("Missing the required parameter `output_format` when calling `post_drawing_resize`")  # noqa: E501
        # verify the required parameter 'new_width' is set
        if request.new_width is None:
            raise ValueError("Missing the required parameter `new_width` when calling `post_drawing_resize`")  # noqa: E501
        # verify the required parameter 'new_height' is set
        if request.new_height is None:
            raise ValueError("Missing the required parameter `new_height` when calling `post_drawing_resize`")  # noqa: E501

        collection_formats = {}
        path = '/cad/resize'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('outputFormat') in path:
            path = path.replace('{' + self.__downcase_first_letter('outputFormat' + '}'), request.output_format if request.output_format is not None else '')
        else:
            if request.output_format is not None:
                query_params.append((self.__downcase_first_letter('outputFormat'), request.output_format))  # noqa: E501
        if self.__downcase_first_letter('newWidth') in path:
            path = path.replace('{' + self.__downcase_first_letter('newWidth' + '}'), request.new_width if request.new_width is not None else '')
        else:
            if request.new_width is not None:
                query_params.append((self.__downcase_first_letter('newWidth'), request.new_width))  # noqa: E501
        if self.__downcase_first_letter('newHeight') in path:
            path = path.replace('{' + self.__downcase_first_letter('newHeight' + '}'), request.new_height if request.new_height is not None else '')
        else:
            if request.new_height is not None:
                query_params.append((self.__downcase_first_letter('newHeight'), request.new_height))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.drawing_data is not None:
            local_var_files.append((self.__downcase_first_letter('drawingData'), request.drawing_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/octet-stream', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_drawing_rotate_flip(self, request, **kwargs):  # noqa: E501
        """Rotate/flip a drawing. Drawing data is passed as a zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param drawing_data file : Input drawing (required)
        :param output_format str : Resulting file format. (required)
        :param rotate_flip_type str : Rotate/flip operation to apply. (required)
        :param out_path str : Path to updated file (if this is empty, response contains streamed file).
        :param storage str : Your Aspose Cloud Storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_drawing_rotate_flip_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_rotate_flip_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_drawing_rotate_flip_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_rotate_flip_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_drawing_rotate_flip_with_http_info(self, request, **kwargs):  # noqa: E501
        """Rotate/flip a drawing. Drawing data is passed as a zero-indexed multipart/form-data content or as raw body stream.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostDrawingRotateFlipRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_drawing_rotate_flip" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'drawing_data' is set
        if request.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `post_drawing_rotate_flip`")  # noqa: E501
        # verify the required parameter 'output_format' is set
        if request.output_format is None:
            raise ValueError("Missing the required parameter `output_format` when calling `post_drawing_rotate_flip`")  # noqa: E501
        # verify the required parameter 'rotate_flip_type' is set
        if request.rotate_flip_type is None:
            raise ValueError("Missing the required parameter `rotate_flip_type` when calling `post_drawing_rotate_flip`")  # noqa: E501

        collection_formats = {}
        path = '/cad/rotateflip'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('outputFormat') in path:
            path = path.replace('{' + self.__downcase_first_letter('outputFormat' + '}'), request.output_format if request.output_format is not None else '')
        else:
            if request.output_format is not None:
                query_params.append((self.__downcase_first_letter('outputFormat'), request.output_format))  # noqa: E501
        if self.__downcase_first_letter('rotateFlipType') in path:
            path = path.replace('{' + self.__downcase_first_letter('rotateFlipType' + '}'), request.rotate_flip_type if request.rotate_flip_type is not None else '')
        else:
            if request.rotate_flip_type is not None:
                query_params.append((self.__downcase_first_letter('rotateFlipType'), request.rotate_flip_type))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.drawing_data is not None:
            local_var_files.append((self.__downcase_first_letter('drawingData'), request.drawing_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/octet-stream', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_drawing_save_as(self, request, **kwargs):  # noqa: E501
        """Export existing drawing to another format. Drawing data is passed as zero-indexed multipart/form-data content or as raw body stream.               # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param drawing_data file : Input drawing (required)
        :param output_format str : Resulting file format. (required)
        :param out_path str : Path to updated file (if this is empty, response contains streamed file).
        :param storage str : Your Aspose Cloud Storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_drawing_save_as_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_save_as_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_drawing_save_as_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_save_as_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_drawing_save_as_with_http_info(self, request, **kwargs):  # noqa: E501
        """Export existing drawing to another format. Drawing data is passed as zero-indexed multipart/form-data content or as raw body stream.               # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostDrawingSaveAsRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_drawing_save_as" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'drawing_data' is set
        if request.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `post_drawing_save_as`")  # noqa: E501
        # verify the required parameter 'output_format' is set
        if request.output_format is None:
            raise ValueError("Missing the required parameter `output_format` when calling `post_drawing_save_as`")  # noqa: E501

        collection_formats = {}
        path = '/cad/saveAs/{outputFormat}'
        path_params = {}
        if request.output_format is not None:
            path_params[self.__downcase_first_letter('outputFormat')] = request.output_format  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.drawing_data is not None:
            local_var_files.append((self.__downcase_first_letter('drawingData'), request.drawing_data))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/octet-stream', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_drawing_svg(self, request, **kwargs):  # noqa: E501
        """Export an existing drawing to SVG format with export settings specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : Filename of an input drawing on a storage. (required)
        :param options SvgOptionsDTO : Export SVG options passed as a JSON on a request body. (required)
        :param folder str : Folder with a drawing to process.
        :param out_path str : Path to updated file (if this is empty, response contains streamed file).
        :param storage str : Your Aspose Cloud Storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_drawing_svg_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_svg_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_drawing_svg_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_svg_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_drawing_svg_with_http_info(self, request, **kwargs):  # noqa: E501
        """Export an existing drawing to SVG format with export settings specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostDrawingSvgRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_drawing_svg" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_svg`")  # noqa: E501
        # verify the required parameter 'options' is set
        if request.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_svg`")  # noqa: E501

        collection_formats = {}
        path = '/cad/{name}/svg'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.options is not None:
            body_params = request.options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_drawing_tiff(self, request, **kwargs):  # noqa: E501
        """Export an existing drawing into TIFF format with export settings specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : Filename of an input drawing on a storage. (required)
        :param options TiffOptionsDTO : Export TIFF options passed as a JSON on a request body. (required)
        :param folder str : Folder with a drawing to process.
        :param out_path str : Path to updated file (if this is empty, response contains streamed file).
        :param storage str : Your Aspose Cloud Storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_drawing_tiff_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_tiff_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_drawing_tiff_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_tiff_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_drawing_tiff_with_http_info(self, request, **kwargs):  # noqa: E501
        """Export an existing drawing into TIFF format with export settings specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostDrawingTiffRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_drawing_tiff" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_tiff`")  # noqa: E501
        # verify the required parameter 'options' is set
        if request.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_tiff`")  # noqa: E501

        collection_formats = {}
        path = '/cad/{name}/tiff'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.options is not None:
            body_params = request.options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_drawing_wmf(self, request, **kwargs):  # noqa: E501
        """Export an existing drawing to WMF format with export settings specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param name str : Filename of an input drawing on a storage. (required)
        :param options WmfOptionsDTO : Export WMF options passed as a JSON on a request body. (required)
        :param folder str : Folder with a drawing to process.
        :param out_path str : Path to updated file (if this is empty, response contains streamed file).
        :param storage str : Your Aspose Cloud Storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.post_drawing_wmf_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_wmf_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.post_drawing_wmf_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.post_drawing_wmf_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def post_drawing_wmf_with_http_info(self, request, **kwargs):  # noqa: E501
        """Export an existing drawing to WMF format with export settings specified.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PostDrawingWmfRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_drawing_wmf" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if request.name is None:
            raise ValueError("Missing the required parameter `name` when calling `post_drawing_wmf`")  # noqa: E501
        # verify the required parameter 'options' is set
        if request.options is None:
            raise ValueError("Missing the required parameter `options` when calling `post_drawing_wmf`")  # noqa: E501

        collection_formats = {}
        path = '/cad/{name}/wmf'
        path_params = {}
        if request.name is not None:
            path_params[self.__downcase_first_letter('name')] = request.name  # noqa: E501

        query_params = []
        if self.__downcase_first_letter('folder') in path:
            path = path.replace('{' + self.__downcase_first_letter('folder' + '}'), request.folder if request.folder is not None else '')
        else:
            if request.folder is not None:
                query_params.append((self.__downcase_first_letter('folder'), request.folder))  # noqa: E501
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []

        body_params = None
        if request.options is not None:
            body_params = request.options
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_drawing_bmp(self, request, **kwargs):  # noqa: E501
        """Export drawing to BMP format. Drawing data is passed as zero-indexed multipart/form-data as well as export BMP options serialized as JSON. Order of drawing data and BMP options could vary.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param drawing_data file : Input drawing (required)
        :param out_path str : Path to updated file (if this is empty, response contains streamed file).
        :param export_options str : JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/BmpOptionsDTO model definition.
        :param storage str : Your Aspose Cloud Storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_drawing_bmp_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_drawing_bmp_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_drawing_bmp_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_drawing_bmp_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_drawing_bmp_with_http_info(self, request, **kwargs):  # noqa: E501
        """Export drawing to BMP format. Drawing data is passed as zero-indexed multipart/form-data as well as export BMP options serialized as JSON. Order of drawing data and BMP options could vary.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PutDrawingBmpRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_drawing_bmp" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'drawing_data' is set
        if request.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_bmp`")  # noqa: E501

        collection_formats = {}
        path = '/cad/bmp'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.drawing_data is not None:
            local_var_files.append((self.__downcase_first_letter('drawingData'), request.drawing_data))  # noqa: E501
        if request.export_options is not None:
            form_params.append((self.__downcase_first_letter('exportOptions'), request.export_options))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/octet-stream', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_drawing_gif(self, request, **kwargs):  # noqa: E501
        """Export drawing to GIF format. Drawing data is passed as zero-indexed multipart/form-data as well as export GIF options serialized as JSON. Order of drawing data and GIF options could vary.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param drawing_data file : Input drawing (required)
        :param export_options str : JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/GifOptionsDTO model definition.
        :param out_path str : Path to updated file (if this is empty, response contains streamed file).
        :param storage str : Your Aspose Cloud Storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_drawing_gif_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_drawing_gif_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_drawing_gif_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_drawing_gif_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_drawing_gif_with_http_info(self, request, **kwargs):  # noqa: E501
        """Export drawing to GIF format. Drawing data is passed as zero-indexed multipart/form-data as well as export GIF options serialized as JSON. Order of drawing data and GIF options could vary.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PutDrawingGifRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_drawing_gif" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'drawing_data' is set
        if request.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_gif`")  # noqa: E501

        collection_formats = {}
        path = '/cad/gif'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.drawing_data is not None:
            local_var_files.append((self.__downcase_first_letter('drawingData'), request.drawing_data))  # noqa: E501
        if request.export_options is not None:
            form_params.append((self.__downcase_first_letter('exportOptions'), request.export_options))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data', 'application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_drawing_jpeg(self, request, **kwargs):  # noqa: E501
        """Export drawing to JPEG format. Drawing data is passed as zero-indexed multipart/form-data as well as export JPEG options serialized as JSON. Order of drawing data and JPEG options could vary.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param drawing_data file : Input drawing (required)
        :param out_path str : Path to updated file (if this is empty, response contains streamed file).
        :param export_options str : JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/JpegOptionsDTO model definition.
        :param storage str : Your Aspose Cloud Storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_drawing_jpeg_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_drawing_jpeg_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_drawing_jpeg_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_drawing_jpeg_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_drawing_jpeg_with_http_info(self, request, **kwargs):  # noqa: E501
        """Export drawing to JPEG format. Drawing data is passed as zero-indexed multipart/form-data as well as export JPEG options serialized as JSON. Order of drawing data and JPEG options could vary.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PutDrawingJpegRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_drawing_jpeg" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'drawing_data' is set
        if request.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_jpeg`")  # noqa: E501

        collection_formats = {}
        path = '/cad/jpeg'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.drawing_data is not None:
            local_var_files.append((self.__downcase_first_letter('drawingData'), request.drawing_data))  # noqa: E501
        if request.export_options is not None:
            form_params.append((self.__downcase_first_letter('exportOptions'), request.export_options))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data', 'application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_drawing_jpeg2000(self, request, **kwargs):  # noqa: E501
        """Export drawing to JPEG2000 format. Drawing data is passed as zero-indexed multipart/form-data as well as export JPEG2000 options serialized as JSON. Order of drawing data and JPEG2000 options could vary.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param drawing_data file : Input drawing (required)
        :param out_path str : Path to updated file (if this is empty, response contains streamed file).
        :param export_options str : JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/Jpeg2000OptionsDTO model definition.
        :param storage str : Your Aspose Cloud Storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_drawing_jpeg2000_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_drawing_jpeg2000_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_drawing_jpeg2000_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_drawing_jpeg2000_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_drawing_jpeg2000_with_http_info(self, request, **kwargs):  # noqa: E501
        """Export drawing to JPEG2000 format. Drawing data is passed as zero-indexed multipart/form-data as well as export JPEG2000 options serialized as JSON. Order of drawing data and JPEG2000 options could vary.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PutDrawingJpeg2000Request object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_drawing_jpeg2000" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'drawing_data' is set
        if request.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_jpeg2000`")  # noqa: E501

        collection_formats = {}
        path = '/cad/jpeg2000'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.drawing_data is not None:
            local_var_files.append((self.__downcase_first_letter('drawingData'), request.drawing_data))  # noqa: E501
        if request.export_options is not None:
            form_params.append((self.__downcase_first_letter('exportOptions'), request.export_options))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data', 'application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_drawing_pdf(self, request, **kwargs):  # noqa: E501
        """Export drawing to PDF format. Drawing data is passed as zero-indexed multipart/form-data as well as export PDF options serialized as JSON. Order of drawing data and PDF options could vary.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param drawing_data file : Input drawing (required)
        :param out_path str : Path to updated file (if this is empty, response contains streamed file).
        :param export_options str : JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/PdfOptionsDTO model definition.
        :param storage str : Your Aspose Cloud Storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_drawing_pdf_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_drawing_pdf_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_drawing_pdf_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_drawing_pdf_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_drawing_pdf_with_http_info(self, request, **kwargs):  # noqa: E501
        """Export drawing to PDF format. Drawing data is passed as zero-indexed multipart/form-data as well as export PDF options serialized as JSON. Order of drawing data and PDF options could vary.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PutDrawingPdfRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_drawing_pdf" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'drawing_data' is set
        if request.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_pdf`")  # noqa: E501

        collection_formats = {}
        path = '/cad/pdf'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.drawing_data is not None:
            local_var_files.append((self.__downcase_first_letter('drawingData'), request.drawing_data))  # noqa: E501
        if request.export_options is not None:
            form_params.append((self.__downcase_first_letter('exportOptions'), request.export_options))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data', 'application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_drawing_png(self, request, **kwargs):  # noqa: E501
        """Export drawing to PNG format. Drawing data is passed as zero-indexed multipart/form-data as well as export PNG options serialized as JSON. Order of drawing data and PNG options could vary.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param drawing_data file : Input drawing (required)
        :param out_path str : Path to updated file (if this is empty, response contains streamed file).
        :param export_options str : JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/PngOptionsDTO model definition.
        :param storage str : Your Aspose Cloud Storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_drawing_png_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_drawing_png_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_drawing_png_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_drawing_png_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_drawing_png_with_http_info(self, request, **kwargs):  # noqa: E501
        """Export drawing to PNG format. Drawing data is passed as zero-indexed multipart/form-data as well as export PNG options serialized as JSON. Order of drawing data and PNG options could vary.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PutDrawingPngRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_drawing_png" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'drawing_data' is set
        if request.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_png`")  # noqa: E501

        collection_formats = {}
        path = '/cad/png'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.drawing_data is not None:
            local_var_files.append((self.__downcase_first_letter('drawingData'), request.drawing_data))  # noqa: E501
        if request.export_options is not None:
            form_params.append((self.__downcase_first_letter('exportOptions'), request.export_options))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data', 'application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_drawing_psd(self, request, **kwargs):  # noqa: E501
        """Export drawing to PSD format. Drawing data is passed as zero-indexed multipart/form-data as well as export PSD options serialized as JSON. Order of drawing data and PSD options could vary.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param drawing_data file : Input drawing (required)
        :param out_path str : Path to updated file (if this is empty, response contains streamed file).
        :param export_options str : JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/PsdOptionsDTO model definition.
        :param storage str : Your Aspose Cloud Storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_drawing_psd_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_drawing_psd_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_drawing_psd_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_drawing_psd_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_drawing_psd_with_http_info(self, request, **kwargs):  # noqa: E501
        """Export drawing to PSD format. Drawing data is passed as zero-indexed multipart/form-data as well as export PSD options serialized as JSON. Order of drawing data and PSD options could vary.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PutDrawingPsdRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_drawing_psd" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'drawing_data' is set
        if request.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_psd`")  # noqa: E501

        collection_formats = {}
        path = '/cad/psd'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.drawing_data is not None:
            local_var_files.append((self.__downcase_first_letter('drawingData'), request.drawing_data))  # noqa: E501
        if request.export_options is not None:
            form_params.append((self.__downcase_first_letter('exportOptions'), request.export_options))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data', 'application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_drawing_svg(self, request, **kwargs):  # noqa: E501
        """Export drawing to SVG format. Drawing data is passed as zero-indexed multipart/form-data as well as export SVG options serialized as JSON. Order of drawing data and SVG options could vary.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param drawing_data file : Input drawing (required)
        :param out_path str : Path to updated file (if this is empty, response contains streamed file).
        :param export_options str : JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/SvgOptionsDTO model definition.
        :param storage str : Your Aspose Cloud Storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_drawing_svg_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_drawing_svg_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_drawing_svg_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_drawing_svg_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_drawing_svg_with_http_info(self, request, **kwargs):  # noqa: E501
        """Export drawing to SVG format. Drawing data is passed as zero-indexed multipart/form-data as well as export SVG options serialized as JSON. Order of drawing data and SVG options could vary.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PutDrawingSvgRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_drawing_svg" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'drawing_data' is set
        if request.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_svg`")  # noqa: E501

        collection_formats = {}
        path = '/cad/svg'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.drawing_data is not None:
            local_var_files.append((self.__downcase_first_letter('drawingData'), request.drawing_data))  # noqa: E501
        if request.export_options is not None:
            form_params.append((self.__downcase_first_letter('exportOptions'), request.export_options))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data', 'application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_drawing_tiff(self, request, **kwargs):  # noqa: E501
        """Export drawing to TIFF format. Drawing data is passed as zero-indexed multipart/form-data as well as export TIFF options serialized as JSON. Order of drawing data and TIFF options could vary.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param drawing_data file : Input drawing (required)
        :param out_path str : Path to updated file (if this is empty, response contains streamed file).
        :param export_options str : JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/TiffOptionsDTO model definition.
        :param storage str : Your Aspose Cloud Storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_drawing_tiff_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_drawing_tiff_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_drawing_tiff_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_drawing_tiff_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_drawing_tiff_with_http_info(self, request, **kwargs):  # noqa: E501
        """Export drawing to TIFF format. Drawing data is passed as zero-indexed multipart/form-data as well as export TIFF options serialized as JSON. Order of drawing data and TIFF options could vary.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PutDrawingTiffRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_drawing_tiff" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'drawing_data' is set
        if request.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_tiff`")  # noqa: E501

        collection_formats = {}
        path = '/cad/tiff'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.drawing_data is not None:
            local_var_files.append((self.__downcase_first_letter('drawingData'), request.drawing_data))  # noqa: E501
        if request.export_options is not None:
            form_params.append((self.__downcase_first_letter('exportOptions'), request.export_options))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data', 'application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_drawing_wmf(self, request, **kwargs):  # noqa: E501
        """Export drawing to WMF format. Drawing data is passed as zero-indexed multipart/form-data as well as export WMF options serialized as JSON. Order of drawing data and WMF options could vary.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param drawing_data file : Input drawing (required)
        :param out_path str : Path to updated file (if this is empty, response contains streamed file).
        :param export_options str : JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/WmfOptionsDTO model definition.
        :param storage str : Your Aspose Cloud Storage name.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        try:
            if kwargs.get('is_async'):
                return self.put_drawing_wmf_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_drawing_wmf_with_http_info(request, **kwargs)  # noqa: E501
            return data
        except ApiException as e:
            if e.status == 401:
                self.__request_token()
                if kwargs.get('is_async'):
                    return self.put_drawing_wmf_with_http_info(request, **kwargs)  # noqa: E501
            (data) = self.put_drawing_wmf_with_http_info(request, **kwargs)  # noqa: E501
            return data
        
    def put_drawing_wmf_with_http_info(self, request, **kwargs):  # noqa: E501
        """Export drawing to WMF format. Drawing data is passed as zero-indexed multipart/form-data as well as export WMF options serialized as JSON. Order of drawing data and WMF options could vary.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True

        :param is_async bool
        :param request PutDrawingWmfRequest object with parameters
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        params = locals()
        params['is_async'] = ''
        params['_return_http_data_only'] = False
        params['_preload_content'] = True
        params['_request_timeout'] = ''
        for key, val in six.iteritems(params['kwargs']):
            if key not in params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_drawing_wmf" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'drawing_data' is set
        if request.drawing_data is None:
            raise ValueError("Missing the required parameter `drawing_data` when calling `put_drawing_wmf`")  # noqa: E501

        collection_formats = {}
        path = '/cad/wmf'
        path_params = {}

        query_params = []
        if self.__downcase_first_letter('outPath') in path:
            path = path.replace('{' + self.__downcase_first_letter('outPath' + '}'), request.out_path if request.out_path is not None else '')
        else:
            if request.out_path is not None:
                query_params.append((self.__downcase_first_letter('outPath'), request.out_path))  # noqa: E501
        if self.__downcase_first_letter('storage') in path:
            path = path.replace('{' + self.__downcase_first_letter('storage' + '}'), request.storage if request.storage is not None else '')
        else:
            if request.storage is not None:
                query_params.append((self.__downcase_first_letter('storage'), request.storage))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = []
        if request.drawing_data is not None:
            local_var_files.append((self.__downcase_first_letter('drawingData'), request.drawing_data))  # noqa: E501
        if request.export_options is not None:
            form_params.append((self.__downcase_first_letter('exportOptions'), request.export_options))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data', 'application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            path, 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    # Helper method to convert first letter to downcase
    def __downcase_first_letter(self, s):
        if len(s) == 0:
            return s
        else:
            return s[0].lower() + s[1:]

    def __request_token(self):
        config = self.api_client.configuration
        api_version = config.api_version
        config.api_version = ''
        request_url = "connect/token"
        form_params = [('grant_type', 'client_credentials'), ('client_id', config.api_key['app_sid']),
                       ('client_secret', config.api_key['api_key'])]

        header_params = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}

        data = self.api_client.call_api(request_url, 'POST',
                                        {},
                                        [],
                                        header_params,
                                        post_params=form_params,
                                        response_type='object',
                                        files={}, _return_http_data_only=True)
        access_token = data['access_token'] if six.PY3 else data['access_token'].encode('utf8')
        refresh_token = data['refresh_token'] if six.PY3 else data['refresh_token'].encode('utf8')
        self.api_client.configuration.access_token = access_token
        self.api_client.configuration.api_version = api_version
        self.api_client.configuration.refresh_token = refresh_token

    
    # Refresh token method is going to be removed soon. Obsolete, do not use
    def __refresh_token(self):
        config = self.api_client.configuration
        api_version = config.api_version
        config.api_version = ''
        request_url = "connect/token"
        form_params = [('grant_type', 'refresh_token'), ('refresh_token', config.refresh_token)]

        header_params = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}

        data = self.api_client.call_api(request_url, 'POST',
                                        {},
                                        [],
                                        header_params,
                                        post_params=form_params,
                                        response_type='object',
                                        files={}, _return_http_data_only=True)
        access_token = data['access_token'] if six.PY3 else data['access_token'].encode('utf8')
        refresh_token = data['refresh_token'] if six.PY3 else data['refresh_token'].encode('utf8')
        self.api_client.configuration.access_token = access_token
        self.api_client.configuration.api_version = api_version
        self.api_client.configuration.refresh_token = refresh_token
