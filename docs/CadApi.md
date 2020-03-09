# asposecadcloud.CadApi

All URIs are relative to *https://api-qa.aspose.cloud/v3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_drawing_properties**](CadApi.md#get_drawing_properties) | **GET** /cad/{name}/properties | Retrieves info about an existing drawing.             
[**get_drawing_resize**](CadApi.md#get_drawing_resize) | **GET** /cad/{name}/resize | Resize an existing drawing.
[**get_drawing_rotate_flip**](CadApi.md#get_drawing_rotate_flip) | **GET** /cad/{name}/rotateflip | Rotate/flip an existing drawing.
[**get_drawing_save_as**](CadApi.md#get_drawing_save_as) | **GET** /cad/{name}/saveAs/{outputFormat} | Export an existing drawing to another format.
[**post_drawing_bmp**](CadApi.md#post_drawing_bmp) | **POST** /cad/{name}/bmp | Export an existing drawing to BMP format with export settings specified.
[**post_drawing_gif**](CadApi.md#post_drawing_gif) | **POST** /cad/{name}/gif | Export an existing drawing into GIF format with export settings specified.
[**post_drawing_jpeg**](CadApi.md#post_drawing_jpeg) | **POST** /cad/{name}/jpeg | Export an existing drawing into JPEG format with export settings specified.
[**post_drawing_jpeg2000**](CadApi.md#post_drawing_jpeg2000) | **POST** /cad/{name}/jpeg2000 | Export an existing drawing into JPEG2000 format with export settings specified.
[**post_drawing_pdf**](CadApi.md#post_drawing_pdf) | **POST** /cad/{name}/pdf | Export an existing drawing to PDF format with export settings specified.
[**post_drawing_png**](CadApi.md#post_drawing_png) | **POST** /cad/{name}/png | Export an existing drawing into PNG format with export settings specified.
[**post_drawing_properties**](CadApi.md#post_drawing_properties) | **POST** /cad/properties | Retrieves info about drawing which is passed as a zero-indexed multipart/form-data content or as raw body stream.
[**post_drawing_psd**](CadApi.md#post_drawing_psd) | **POST** /cad/{name}/psd | Export an existing drawing into PSD format with export settings specified.
[**post_drawing_resize**](CadApi.md#post_drawing_resize) | **POST** /cad/resize | Resize a drawing. Drawing data is passed as a zero-indexed multipart/form-data content or as raw body stream.
[**post_drawing_rotate_flip**](CadApi.md#post_drawing_rotate_flip) | **POST** /cad/rotateflip | Rotate/flip a drawing. Drawing data is passed as a zero-indexed multipart/form-data content or as raw body stream.
[**post_drawing_save_as**](CadApi.md#post_drawing_save_as) | **POST** /cad/saveAs/{outputFormat} | Export existing drawing to another format. Drawing data is passed as zero-indexed multipart/form-data content or as raw body stream.             
[**post_drawing_svg**](CadApi.md#post_drawing_svg) | **POST** /cad/{name}/svg | Export an existing drawing to SVG format with export settings specified.
[**post_drawing_tiff**](CadApi.md#post_drawing_tiff) | **POST** /cad/{name}/tiff | Export an existing drawing into TIFF format with export settings specified.
[**post_drawing_wmf**](CadApi.md#post_drawing_wmf) | **POST** /cad/{name}/wmf | Export an existing drawing to WMF format with export settings specified.
[**put_drawing_bmp**](CadApi.md#put_drawing_bmp) | **PUT** /cad/bmp | Export drawing to BMP format. Drawing data is passed as zero-indexed multipart/form-data as well as export BMP options serialized as JSON. Order of drawing data and BMP options could vary.
[**put_drawing_gif**](CadApi.md#put_drawing_gif) | **PUT** /cad/gif | Export drawing to GIF format. Drawing data is passed as zero-indexed multipart/form-data as well as export GIF options serialized as JSON. Order of drawing data and GIF options could vary.
[**put_drawing_jpeg**](CadApi.md#put_drawing_jpeg) | **PUT** /cad/jpeg | Export drawing to JPEG format. Drawing data is passed as zero-indexed multipart/form-data as well as export JPEG options serialized as JSON. Order of drawing data and JPEG options could vary.
[**put_drawing_jpeg2000**](CadApi.md#put_drawing_jpeg2000) | **PUT** /cad/jpeg2000 | Export drawing to JPEG2000 format. Drawing data is passed as zero-indexed multipart/form-data as well as export JPEG2000 options serialized as JSON. Order of drawing data and JPEG2000 options could vary.
[**put_drawing_pdf**](CadApi.md#put_drawing_pdf) | **PUT** /cad/pdf | Export drawing to PDF format. Drawing data is passed as zero-indexed multipart/form-data as well as export PDF options serialized as JSON. Order of drawing data and PDF options could vary.
[**put_drawing_png**](CadApi.md#put_drawing_png) | **PUT** /cad/png | Export drawing to PNG format. Drawing data is passed as zero-indexed multipart/form-data as well as export PNG options serialized as JSON. Order of drawing data and PNG options could vary.
[**put_drawing_psd**](CadApi.md#put_drawing_psd) | **PUT** /cad/psd | Export drawing to PSD format. Drawing data is passed as zero-indexed multipart/form-data as well as export PSD options serialized as JSON. Order of drawing data and PSD options could vary.
[**put_drawing_svg**](CadApi.md#put_drawing_svg) | **PUT** /cad/svg | Export drawing to SVG format. Drawing data is passed as zero-indexed multipart/form-data as well as export SVG options serialized as JSON. Order of drawing data and SVG options could vary.
[**put_drawing_tiff**](CadApi.md#put_drawing_tiff) | **PUT** /cad/tiff | Export drawing to TIFF format. Drawing data is passed as zero-indexed multipart/form-data as well as export TIFF options serialized as JSON. Order of drawing data and TIFF options could vary.
[**put_drawing_wmf**](CadApi.md#put_drawing_wmf) | **PUT** /cad/wmf | Export drawing to WMF format. Drawing data is passed as zero-indexed multipart/form-data as well as export WMF options serialized as JSON. Order of drawing data and WMF options could vary.


# **get_drawing_properties**
> CadResponse get_drawing_properties(name, folder=folder, storage=storage)

Retrieves info about an existing drawing.             

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
name = 'name_example' # str | Filename of an input drawing on a storage.
folder = 'folder_example' # str | Folder with a drawing to get properties for. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Retrieves info about an existing drawing.             
    api_response = api_instance.get_drawing_properties(name, folder=folder, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->get_drawing_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an input drawing on a storage. | 
 **folder** | **str**| Folder with a drawing to get properties for. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**CadResponse**](CadResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_drawing_resize**
> file get_drawing_resize(name, output_format, new_width, new_height, folder=folder, out_path=out_path, storage=storage)

Resize an existing drawing.

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
name = 'name_example' # str | Filename of a drawing.
output_format = 'output_format_example' # str | Resulting file format.
new_width = 56 # int | New width.
new_height = 56 # int | New height.
folder = 'folder_example' # str | Folder with a drawing to process. (optional)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed file). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Resize an existing drawing.
    api_response = api_instance.get_drawing_resize(name, output_format, new_width, new_height, folder=folder, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->get_drawing_resize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of a drawing. | 
 **output_format** | **str**| Resulting file format. | 
 **new_width** | **int**| New width. | 
 **new_height** | **int**| New height. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_drawing_rotate_flip**
> file get_drawing_rotate_flip(name, output_format, rotate_flip_type, folder=folder, out_path=out_path, storage=storage)

Rotate/flip an existing drawing.

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
name = 'name_example' # str | Filename of a drawing.
output_format = 'output_format_example' # str | Resulting file format.
rotate_flip_type = 'rotate_flip_type_example' # str | Rotate/flip operation to apply.
folder = 'folder_example' # str | Folder with a drawing to process. (optional)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed file). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Rotate/flip an existing drawing.
    api_response = api_instance.get_drawing_rotate_flip(name, output_format, rotate_flip_type, folder=folder, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->get_drawing_rotate_flip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of a drawing. | 
 **output_format** | **str**| Resulting file format. | 
 **rotate_flip_type** | **str**| Rotate/flip operation to apply. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_drawing_save_as**
> file get_drawing_save_as(name, output_format, folder=folder, out_path=out_path, storage=storage)

Export an existing drawing to another format.

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
name = 'name_example' # str | Filename of an input drawing on a storage.
output_format = 'output_format_example' # str | Resulting file format.
folder = 'folder_example' # str | Folder with a drawing to process. (optional)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed file). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Export an existing drawing to another format.
    api_response = api_instance.get_drawing_save_as(name, output_format, folder=folder, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->get_drawing_save_as: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an input drawing on a storage. | 
 **output_format** | **str**| Resulting file format. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_drawing_bmp**
> file post_drawing_bmp(name, options, folder=folder, out_path=out_path, storage=storage)

Export an existing drawing to BMP format with export settings specified.

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
name = 'name_example' # str | Filename of an input drawing on a storage.
options = asposecadcloud.BmpOptionsDTO() # BmpOptionsDTO | Export BMP options passed as a JSON on a request body.
folder = 'folder_example' # str | Folder with a drawing to process. (optional)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed file). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Export an existing drawing to BMP format with export settings specified.
    api_response = api_instance.post_drawing_bmp(name, options, folder=folder, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->post_drawing_bmp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an input drawing on a storage. | 
 **options** | [**BmpOptionsDTO**](BmpOptionsDTO.md)| Export BMP options passed as a JSON on a request body. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_drawing_gif**
> file post_drawing_gif(name, options, folder=folder, out_path=out_path, storage=storage)

Export an existing drawing into GIF format with export settings specified.

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
name = 'name_example' # str | Filename of an input drawing on a storage.
options = asposecadcloud.GifOptionsDTO() # GifOptionsDTO | Export GIF options passed as a JSON on a request body.
folder = 'folder_example' # str | Folder with a drawing to process. (optional)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed file). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Export an existing drawing into GIF format with export settings specified.
    api_response = api_instance.post_drawing_gif(name, options, folder=folder, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->post_drawing_gif: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an input drawing on a storage. | 
 **options** | [**GifOptionsDTO**](GifOptionsDTO.md)| Export GIF options passed as a JSON on a request body. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_drawing_jpeg**
> file post_drawing_jpeg(name, options, folder=folder, out_path=out_path, storage=storage)

Export an existing drawing into JPEG format with export settings specified.

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
name = 'name_example' # str | Filename of an input drawing on a storage.
options = asposecadcloud.JpegOptionsDTO() # JpegOptionsDTO | Export JPEG options passed as a JSON on a request body.
folder = 'folder_example' # str | Folder with a drawing to process. (optional)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed file). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Export an existing drawing into JPEG format with export settings specified.
    api_response = api_instance.post_drawing_jpeg(name, options, folder=folder, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->post_drawing_jpeg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an input drawing on a storage. | 
 **options** | [**JpegOptionsDTO**](JpegOptionsDTO.md)| Export JPEG options passed as a JSON on a request body. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_drawing_jpeg2000**
> file post_drawing_jpeg2000(name, options, folder=folder, out_path=out_path, storage=storage)

Export an existing drawing into JPEG2000 format with export settings specified.

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
name = 'name_example' # str | Filename of an input drawing on a storage.
options = asposecadcloud.Jpeg2000OptionsDTO() # Jpeg2000OptionsDTO | Export JPEG2000 options passed as a JSON on a request body.
folder = 'folder_example' # str | Folder with a drawing to process. (optional)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed file). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Export an existing drawing into JPEG2000 format with export settings specified.
    api_response = api_instance.post_drawing_jpeg2000(name, options, folder=folder, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->post_drawing_jpeg2000: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an input drawing on a storage. | 
 **options** | [**Jpeg2000OptionsDTO**](Jpeg2000OptionsDTO.md)| Export JPEG2000 options passed as a JSON on a request body. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_drawing_pdf**
> file post_drawing_pdf(name, options, folder=folder, out_path=out_path, storage=storage)

Export an existing drawing to PDF format with export settings specified.

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
name = 'name_example' # str | Filename of an input drawing on a storage.
options = asposecadcloud.PdfOptionsDTO() # PdfOptionsDTO | Export PDF options passed as a JSON on a request body.
folder = 'folder_example' # str | Folder with a drawing to process. (optional)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed file). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Export an existing drawing to PDF format with export settings specified.
    api_response = api_instance.post_drawing_pdf(name, options, folder=folder, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->post_drawing_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an input drawing on a storage. | 
 **options** | [**PdfOptionsDTO**](PdfOptionsDTO.md)| Export PDF options passed as a JSON on a request body. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_drawing_png**
> file post_drawing_png(name, options, folder=folder, out_path=out_path, storage=storage)

Export an existing drawing into PNG format with export settings specified.

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
name = 'name_example' # str | Filename of an input drawing on a storage.
options = asposecadcloud.PngOptionsDTO() # PngOptionsDTO | Export PNG options passed as a JSON on a request body.
folder = 'folder_example' # str | Folder with a drawing to process. (optional)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed file). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Export an existing drawing into PNG format with export settings specified.
    api_response = api_instance.post_drawing_png(name, options, folder=folder, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->post_drawing_png: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an input drawing on a storage. | 
 **options** | [**PngOptionsDTO**](PngOptionsDTO.md)| Export PNG options passed as a JSON on a request body. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_drawing_properties**
> CadResponse post_drawing_properties(drawing_data)

Retrieves info about drawing which is passed as a zero-indexed multipart/form-data content or as raw body stream.

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
drawing_data = '/path/to/file.txt' # file | Input drawing

try:
    # Retrieves info about drawing which is passed as a zero-indexed multipart/form-data content or as raw body stream.
    api_response = api_instance.post_drawing_properties(drawing_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->post_drawing_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 

### Return type

[**CadResponse**](CadResponse.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_drawing_psd**
> file post_drawing_psd(name, options, folder=folder, out_path=out_path, storage=storage)

Export an existing drawing into PSD format with export settings specified.

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
name = 'name_example' # str | Filename of an input drawing on a storage.
options = asposecadcloud.PsdOptionsDTO() # PsdOptionsDTO | Export PSD options passed as a JSON on a request body.
folder = 'folder_example' # str | Folder with a drawing to process. (optional)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed file). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Export an existing drawing into PSD format with export settings specified.
    api_response = api_instance.post_drawing_psd(name, options, folder=folder, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->post_drawing_psd: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an input drawing on a storage. | 
 **options** | [**PsdOptionsDTO**](PsdOptionsDTO.md)| Export PSD options passed as a JSON on a request body. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_drawing_resize**
> file post_drawing_resize(drawing_data, output_format, new_width, new_height, out_path=out_path, storage=storage)

Resize a drawing. Drawing data is passed as a zero-indexed multipart/form-data content or as raw body stream.

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
drawing_data = '/path/to/file.txt' # file | Input drawing
output_format = 'output_format_example' # str | Resulting file format.
new_width = 56 # int | New width.
new_height = 56 # int | New height.
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed file). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Resize a drawing. Drawing data is passed as a zero-indexed multipart/form-data content or as raw body stream.
    api_response = api_instance.post_drawing_resize(drawing_data, output_format, new_width, new_height, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->post_drawing_resize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 
 **output_format** | **str**| Resulting file format. | 
 **new_width** | **int**| New width. | 
 **new_height** | **int**| New height. | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/octet-stream, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_drawing_rotate_flip**
> file post_drawing_rotate_flip(drawing_data, output_format, rotate_flip_type, out_path=out_path, storage=storage)

Rotate/flip a drawing. Drawing data is passed as a zero-indexed multipart/form-data content or as raw body stream.

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
drawing_data = '/path/to/file.txt' # file | Input drawing
output_format = 'output_format_example' # str | Resulting file format.
rotate_flip_type = 'rotate_flip_type_example' # str | Rotate/flip operation to apply.
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed file). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Rotate/flip a drawing. Drawing data is passed as a zero-indexed multipart/form-data content or as raw body stream.
    api_response = api_instance.post_drawing_rotate_flip(drawing_data, output_format, rotate_flip_type, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->post_drawing_rotate_flip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 
 **output_format** | **str**| Resulting file format. | 
 **rotate_flip_type** | **str**| Rotate/flip operation to apply. | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/octet-stream, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_drawing_save_as**
> file post_drawing_save_as(drawing_data, output_format, out_path=out_path, storage=storage)

Export existing drawing to another format. Drawing data is passed as zero-indexed multipart/form-data content or as raw body stream.             

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
drawing_data = '/path/to/file.txt' # file | Input drawing
output_format = 'output_format_example' # str | Resulting file format.
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed file). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Export existing drawing to another format. Drawing data is passed as zero-indexed multipart/form-data content or as raw body stream.             
    api_response = api_instance.post_drawing_save_as(drawing_data, output_format, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->post_drawing_save_as: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 
 **output_format** | **str**| Resulting file format. | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/octet-stream, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_drawing_svg**
> file post_drawing_svg(name, options, folder=folder, out_path=out_path, storage=storage)

Export an existing drawing to SVG format with export settings specified.

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
name = 'name_example' # str | Filename of an input drawing on a storage.
options = asposecadcloud.SvgOptionsDTO() # SvgOptionsDTO | Export SVG options passed as a JSON on a request body.
folder = 'folder_example' # str | Folder with a drawing to process. (optional)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed file). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Export an existing drawing to SVG format with export settings specified.
    api_response = api_instance.post_drawing_svg(name, options, folder=folder, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->post_drawing_svg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an input drawing on a storage. | 
 **options** | [**SvgOptionsDTO**](SvgOptionsDTO.md)| Export SVG options passed as a JSON on a request body. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_drawing_tiff**
> file post_drawing_tiff(name, options, folder=folder, out_path=out_path, storage=storage)

Export an existing drawing into TIFF format with export settings specified.

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
name = 'name_example' # str | Filename of an input drawing on a storage.
options = asposecadcloud.TiffOptionsDTO() # TiffOptionsDTO | Export TIFF options passed as a JSON on a request body.
folder = 'folder_example' # str | Folder with a drawing to process. (optional)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed file). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Export an existing drawing into TIFF format with export settings specified.
    api_response = api_instance.post_drawing_tiff(name, options, folder=folder, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->post_drawing_tiff: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an input drawing on a storage. | 
 **options** | [**TiffOptionsDTO**](TiffOptionsDTO.md)| Export TIFF options passed as a JSON on a request body. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_drawing_wmf**
> file post_drawing_wmf(name, options, folder=folder, out_path=out_path, storage=storage)

Export an existing drawing to WMF format with export settings specified.

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
name = 'name_example' # str | Filename of an input drawing on a storage.
options = asposecadcloud.WmfOptionsDTO() # WmfOptionsDTO | Export WMF options passed as a JSON on a request body.
folder = 'folder_example' # str | Folder with a drawing to process. (optional)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed file). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Export an existing drawing to WMF format with export settings specified.
    api_response = api_instance.post_drawing_wmf(name, options, folder=folder, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->post_drawing_wmf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an input drawing on a storage. | 
 **options** | [**WmfOptionsDTO**](WmfOptionsDTO.md)| Export WMF options passed as a JSON on a request body. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_drawing_bmp**
> file put_drawing_bmp(drawing_data, out_path=out_path, export_options=export_options, storage=storage)

Export drawing to BMP format. Drawing data is passed as zero-indexed multipart/form-data as well as export BMP options serialized as JSON. Order of drawing data and BMP options could vary.

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
drawing_data = '/path/to/file.txt' # file | Input drawing
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed file). (optional)
export_options = 'export_options_example' # str | JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/BmpOptionsDTO model definition. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Export drawing to BMP format. Drawing data is passed as zero-indexed multipart/form-data as well as export BMP options serialized as JSON. Order of drawing data and BMP options could vary.
    api_response = api_instance.put_drawing_bmp(drawing_data, out_path=out_path, export_options=export_options, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->put_drawing_bmp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **export_options** | **str**| JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/BmpOptionsDTO model definition. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/octet-stream, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_drawing_gif**
> file put_drawing_gif(drawing_data, export_options=export_options, out_path=out_path, storage=storage)

Export drawing to GIF format. Drawing data is passed as zero-indexed multipart/form-data as well as export GIF options serialized as JSON. Order of drawing data and GIF options could vary.

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
drawing_data = '/path/to/file.txt' # file | Input drawing
export_options = 'export_options_example' # str | JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/GifOptionsDTO model definition. (optional)
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed file). (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Export drawing to GIF format. Drawing data is passed as zero-indexed multipart/form-data as well as export GIF options serialized as JSON. Order of drawing data and GIF options could vary.
    api_response = api_instance.put_drawing_gif(drawing_data, export_options=export_options, out_path=out_path, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->put_drawing_gif: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 
 **export_options** | **str**| JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/GifOptionsDTO model definition. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_drawing_jpeg**
> file put_drawing_jpeg(drawing_data, out_path=out_path, export_options=export_options, storage=storage)

Export drawing to JPEG format. Drawing data is passed as zero-indexed multipart/form-data as well as export JPEG options serialized as JSON. Order of drawing data and JPEG options could vary.

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
drawing_data = '/path/to/file.txt' # file | Input drawing
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed file). (optional)
export_options = 'export_options_example' # str | JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/JpegOptionsDTO model definition. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Export drawing to JPEG format. Drawing data is passed as zero-indexed multipart/form-data as well as export JPEG options serialized as JSON. Order of drawing data and JPEG options could vary.
    api_response = api_instance.put_drawing_jpeg(drawing_data, out_path=out_path, export_options=export_options, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->put_drawing_jpeg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **export_options** | **str**| JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/JpegOptionsDTO model definition. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_drawing_jpeg2000**
> file put_drawing_jpeg2000(drawing_data, out_path=out_path, export_options=export_options, storage=storage)

Export drawing to JPEG2000 format. Drawing data is passed as zero-indexed multipart/form-data as well as export JPEG2000 options serialized as JSON. Order of drawing data and JPEG2000 options could vary.

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
drawing_data = '/path/to/file.txt' # file | Input drawing
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed file). (optional)
export_options = 'export_options_example' # str | JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/Jpeg2000OptionsDTO model definition. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Export drawing to JPEG2000 format. Drawing data is passed as zero-indexed multipart/form-data as well as export JPEG2000 options serialized as JSON. Order of drawing data and JPEG2000 options could vary.
    api_response = api_instance.put_drawing_jpeg2000(drawing_data, out_path=out_path, export_options=export_options, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->put_drawing_jpeg2000: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **export_options** | **str**| JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/Jpeg2000OptionsDTO model definition. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_drawing_pdf**
> file put_drawing_pdf(drawing_data, out_path=out_path, export_options=export_options, storage=storage)

Export drawing to PDF format. Drawing data is passed as zero-indexed multipart/form-data as well as export PDF options serialized as JSON. Order of drawing data and PDF options could vary.

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
drawing_data = '/path/to/file.txt' # file | Input drawing
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed file). (optional)
export_options = 'export_options_example' # str | JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/PdfOptionsDTO model definition. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Export drawing to PDF format. Drawing data is passed as zero-indexed multipart/form-data as well as export PDF options serialized as JSON. Order of drawing data and PDF options could vary.
    api_response = api_instance.put_drawing_pdf(drawing_data, out_path=out_path, export_options=export_options, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->put_drawing_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **export_options** | **str**| JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/PdfOptionsDTO model definition. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_drawing_png**
> file put_drawing_png(drawing_data, out_path=out_path, export_options=export_options, storage=storage)

Export drawing to PNG format. Drawing data is passed as zero-indexed multipart/form-data as well as export PNG options serialized as JSON. Order of drawing data and PNG options could vary.

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
drawing_data = '/path/to/file.txt' # file | Input drawing
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed file). (optional)
export_options = 'export_options_example' # str | JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/PngOptionsDTO model definition. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Export drawing to PNG format. Drawing data is passed as zero-indexed multipart/form-data as well as export PNG options serialized as JSON. Order of drawing data and PNG options could vary.
    api_response = api_instance.put_drawing_png(drawing_data, out_path=out_path, export_options=export_options, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->put_drawing_png: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **export_options** | **str**| JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/PngOptionsDTO model definition. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_drawing_psd**
> file put_drawing_psd(drawing_data, out_path=out_path, export_options=export_options, storage=storage)

Export drawing to PSD format. Drawing data is passed as zero-indexed multipart/form-data as well as export PSD options serialized as JSON. Order of drawing data and PSD options could vary.

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
drawing_data = '/path/to/file.txt' # file | Input drawing
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed file). (optional)
export_options = 'export_options_example' # str | JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/PsdOptionsDTO model definition. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Export drawing to PSD format. Drawing data is passed as zero-indexed multipart/form-data as well as export PSD options serialized as JSON. Order of drawing data and PSD options could vary.
    api_response = api_instance.put_drawing_psd(drawing_data, out_path=out_path, export_options=export_options, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->put_drawing_psd: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **export_options** | **str**| JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/PsdOptionsDTO model definition. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_drawing_svg**
> file put_drawing_svg(drawing_data, out_path=out_path, export_options=export_options, storage=storage)

Export drawing to SVG format. Drawing data is passed as zero-indexed multipart/form-data as well as export SVG options serialized as JSON. Order of drawing data and SVG options could vary.

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
drawing_data = '/path/to/file.txt' # file | Input drawing
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed file). (optional)
export_options = 'export_options_example' # str | JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/SvgOptionsDTO model definition. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Export drawing to SVG format. Drawing data is passed as zero-indexed multipart/form-data as well as export SVG options serialized as JSON. Order of drawing data and SVG options could vary.
    api_response = api_instance.put_drawing_svg(drawing_data, out_path=out_path, export_options=export_options, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->put_drawing_svg: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **export_options** | **str**| JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/SvgOptionsDTO model definition. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_drawing_tiff**
> file put_drawing_tiff(drawing_data, out_path=out_path, export_options=export_options, storage=storage)

Export drawing to TIFF format. Drawing data is passed as zero-indexed multipart/form-data as well as export TIFF options serialized as JSON. Order of drawing data and TIFF options could vary.

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
drawing_data = '/path/to/file.txt' # file | Input drawing
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed file). (optional)
export_options = 'export_options_example' # str | JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/TiffOptionsDTO model definition. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Export drawing to TIFF format. Drawing data is passed as zero-indexed multipart/form-data as well as export TIFF options serialized as JSON. Order of drawing data and TIFF options could vary.
    api_response = api_instance.put_drawing_tiff(drawing_data, out_path=out_path, export_options=export_options, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->put_drawing_tiff: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **export_options** | **str**| JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/TiffOptionsDTO model definition. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_drawing_wmf**
> file put_drawing_wmf(drawing_data, out_path=out_path, export_options=export_options, storage=storage)

Export drawing to WMF format. Drawing data is passed as zero-indexed multipart/form-data as well as export WMF options serialized as JSON. Order of drawing data and WMF options could vary.

### Example
```python
from __future__ import print_function
import time
import asposecadcloud
from asposecadcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: JWT
configuration = asposecadcloud.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = asposecadcloud.CadApi(asposecadcloud.ApiClient(configuration))
drawing_data = '/path/to/file.txt' # file | Input drawing
out_path = 'out_path_example' # str | Path to updated file (if this is empty, response contains streamed file). (optional)
export_options = 'export_options_example' # str | JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/WmfOptionsDTO model definition. (optional)
storage = 'storage_example' # str | Your Aspose Cloud Storage name. (optional)

try:
    # Export drawing to WMF format. Drawing data is passed as zero-indexed multipart/form-data as well as export WMF options serialized as JSON. Order of drawing data and WMF options could vary.
    api_response = api_instance.put_drawing_wmf(drawing_data, out_path=out_path, export_options=export_options, storage=storage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CadApi->put_drawing_wmf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **export_options** | **str**| JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/WmfOptionsDTO model definition. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

