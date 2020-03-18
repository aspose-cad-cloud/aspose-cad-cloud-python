# asposecadcloud.CadApi

<a name="get_drawing_properties"></a>
# **get_drawing_properties**
> get_drawing_properties(self, get_drawing_properties_request)

Retrieves info about an existing drawing.             

### Return type

[**CadResponse**](CadResponse.md)

<a name="get_drawing_properties_async"></a>
# **get_drawing_properties_async**
> get_drawing_properties_async(self, get_drawing_properties_request)

Retrieves info about an existing drawing.             

Performs operation asynchronously.

### Return type

[**CadResponse**](CadResponse.md)

### GetDrawingPropertiesRequest Parameters
```python
__init__(self, 
    name, 
    folder=folder, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an input drawing on a storage. | 
 **folder** | **str**| Folder with a drawing to get properties for. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="get_drawing_resize"></a>
# **get_drawing_resize**
> get_drawing_resize(self, get_drawing_resize_request)

Resize an existing drawing.

### Return type

**file**

<a name="get_drawing_resize_async"></a>
# **get_drawing_resize_async**
> get_drawing_resize_async(self, get_drawing_resize_request)

Resize an existing drawing.

Performs operation asynchronously.

### Return type

**file**

### GetDrawingResizeRequest Parameters
```python
__init__(self, 
    name, 
    output_format, 
    new_width, 
    new_height, 
    folder=folder, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of a drawing. | 
 **output_format** | **str**| Resulting file format. | 
 **new_width** | **int**| New width. | 
 **new_height** | **int**| New height. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="get_drawing_rotate_flip"></a>
# **get_drawing_rotate_flip**
> get_drawing_rotate_flip(self, get_drawing_rotate_flip_request)

Rotate/flip an existing drawing.

### Return type

**file**

<a name="get_drawing_rotate_flip_async"></a>
# **get_drawing_rotate_flip_async**
> get_drawing_rotate_flip_async(self, get_drawing_rotate_flip_request)

Rotate/flip an existing drawing.

Performs operation asynchronously.

### Return type

**file**

### GetDrawingRotateFlipRequest Parameters
```python
__init__(self, 
    name, 
    output_format, 
    rotate_flip_type, 
    folder=folder, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of a drawing. | 
 **output_format** | **str**| Resulting file format. | 
 **rotate_flip_type** | **str**| Rotate/flip operation to apply. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="get_drawing_save_as"></a>
# **get_drawing_save_as**
> get_drawing_save_as(self, get_drawing_save_as_request)

Export an existing drawing to another format.

### Return type

**file**

<a name="get_drawing_save_as_async"></a>
# **get_drawing_save_as_async**
> get_drawing_save_as_async(self, get_drawing_save_as_request)

Export an existing drawing to another format.

Performs operation asynchronously.

### Return type

**file**

### GetDrawingSaveAsRequest Parameters
```python
__init__(self, 
    name, 
    output_format, 
    folder=folder, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an input drawing on a storage. | 
 **output_format** | **str**| Resulting file format. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="post_drawing_bmp"></a>
# **post_drawing_bmp**
> post_drawing_bmp(self, post_drawing_bmp_request)

Export an existing drawing to BMP format with export settings specified.

### Return type

**file**

<a name="post_drawing_bmp_async"></a>
# **post_drawing_bmp_async**
> post_drawing_bmp_async(self, post_drawing_bmp_request)

Export an existing drawing to BMP format with export settings specified.

Performs operation asynchronously.

### Return type

**file**

### PostDrawingBmpRequest Parameters
```python
__init__(self, 
    name, 
    options, 
    folder=folder, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an input drawing on a storage. | 
 **options** | [**BmpOptionsDTO**](BmpOptionsDTO.md)| Export BMP options passed as a JSON on a request body. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="post_drawing_gif"></a>
# **post_drawing_gif**
> post_drawing_gif(self, post_drawing_gif_request)

Export an existing drawing into GIF format with export settings specified.

### Return type

**file**

<a name="post_drawing_gif_async"></a>
# **post_drawing_gif_async**
> post_drawing_gif_async(self, post_drawing_gif_request)

Export an existing drawing into GIF format with export settings specified.

Performs operation asynchronously.

### Return type

**file**

### PostDrawingGifRequest Parameters
```python
__init__(self, 
    name, 
    options, 
    folder=folder, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an input drawing on a storage. | 
 **options** | [**GifOptionsDTO**](GifOptionsDTO.md)| Export GIF options passed as a JSON on a request body. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="post_drawing_jpeg"></a>
# **post_drawing_jpeg**
> post_drawing_jpeg(self, post_drawing_jpeg_request)

Export an existing drawing into JPEG format with export settings specified.

### Return type

**file**

<a name="post_drawing_jpeg_async"></a>
# **post_drawing_jpeg_async**
> post_drawing_jpeg_async(self, post_drawing_jpeg_request)

Export an existing drawing into JPEG format with export settings specified.

Performs operation asynchronously.

### Return type

**file**

### PostDrawingJpegRequest Parameters
```python
__init__(self, 
    name, 
    options, 
    folder=folder, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an input drawing on a storage. | 
 **options** | [**JpegOptionsDTO**](JpegOptionsDTO.md)| Export JPEG options passed as a JSON on a request body. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="post_drawing_jpeg2000"></a>
# **post_drawing_jpeg2000**
> post_drawing_jpeg2000(self, post_drawing_jpeg2000_request)

Export an existing drawing into JPEG2000 format with export settings specified.

### Return type

**file**

<a name="post_drawing_jpeg2000_async"></a>
# **post_drawing_jpeg2000_async**
> post_drawing_jpeg2000_async(self, post_drawing_jpeg2000_request)

Export an existing drawing into JPEG2000 format with export settings specified.

Performs operation asynchronously.

### Return type

**file**

### PostDrawingJpeg2000Request Parameters
```python
__init__(self, 
    name, 
    options, 
    folder=folder, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an input drawing on a storage. | 
 **options** | [**Jpeg2000OptionsDTO**](Jpeg2000OptionsDTO.md)| Export JPEG2000 options passed as a JSON on a request body. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="post_drawing_pdf"></a>
# **post_drawing_pdf**
> post_drawing_pdf(self, post_drawing_pdf_request)

Export an existing drawing to PDF format with export settings specified.

### Return type

**file**

<a name="post_drawing_pdf_async"></a>
# **post_drawing_pdf_async**
> post_drawing_pdf_async(self, post_drawing_pdf_request)

Export an existing drawing to PDF format with export settings specified.

Performs operation asynchronously.

### Return type

**file**

### PostDrawingPdfRequest Parameters
```python
__init__(self, 
    name, 
    options, 
    folder=folder, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an input drawing on a storage. | 
 **options** | [**PdfOptionsDTO**](PdfOptionsDTO.md)| Export PDF options passed as a JSON on a request body. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="post_drawing_png"></a>
# **post_drawing_png**
> post_drawing_png(self, post_drawing_png_request)

Export an existing drawing into PNG format with export settings specified.

### Return type

**file**

<a name="post_drawing_png_async"></a>
# **post_drawing_png_async**
> post_drawing_png_async(self, post_drawing_png_request)

Export an existing drawing into PNG format with export settings specified.

Performs operation asynchronously.

### Return type

**file**

### PostDrawingPngRequest Parameters
```python
__init__(self, 
    name, 
    options, 
    folder=folder, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an input drawing on a storage. | 
 **options** | [**PngOptionsDTO**](PngOptionsDTO.md)| Export PNG options passed as a JSON on a request body. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="post_drawing_properties"></a>
# **post_drawing_properties**
> post_drawing_properties(self, post_drawing_properties_request)

Retrieves info about drawing which is passed as a zero-indexed multipart/form-data content or as raw body stream.

### Return type

[**CadResponse**](CadResponse.md)

<a name="post_drawing_properties_async"></a>
# **post_drawing_properties_async**
> post_drawing_properties_async(self, post_drawing_properties_request)

Retrieves info about drawing which is passed as a zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

[**CadResponse**](CadResponse.md)

### PostDrawingPropertiesRequest Parameters
```python
__init__(self, 
    drawing_data)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="post_drawing_psd"></a>
# **post_drawing_psd**
> post_drawing_psd(self, post_drawing_psd_request)

Export an existing drawing into PSD format with export settings specified.

### Return type

**file**

<a name="post_drawing_psd_async"></a>
# **post_drawing_psd_async**
> post_drawing_psd_async(self, post_drawing_psd_request)

Export an existing drawing into PSD format with export settings specified.

Performs operation asynchronously.

### Return type

**file**

### PostDrawingPsdRequest Parameters
```python
__init__(self, 
    name, 
    options, 
    folder=folder, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an input drawing on a storage. | 
 **options** | [**PsdOptionsDTO**](PsdOptionsDTO.md)| Export PSD options passed as a JSON on a request body. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="post_drawing_resize"></a>
# **post_drawing_resize**
> post_drawing_resize(self, post_drawing_resize_request)

Resize a drawing. Drawing data is passed as a zero-indexed multipart/form-data content or as raw body stream.

### Return type

**file**

<a name="post_drawing_resize_async"></a>
# **post_drawing_resize_async**
> post_drawing_resize_async(self, post_drawing_resize_request)

Resize a drawing. Drawing data is passed as a zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

**file**

### PostDrawingResizeRequest Parameters
```python
__init__(self, 
    drawing_data, 
    output_format, 
    new_width, 
    new_height, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 
 **output_format** | **str**| Resulting file format. | 
 **new_width** | **int**| New width. | 
 **new_height** | **int**| New height. | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="post_drawing_rotate_flip"></a>
# **post_drawing_rotate_flip**
> post_drawing_rotate_flip(self, post_drawing_rotate_flip_request)

Rotate/flip a drawing. Drawing data is passed as a zero-indexed multipart/form-data content or as raw body stream.

### Return type

**file**

<a name="post_drawing_rotate_flip_async"></a>
# **post_drawing_rotate_flip_async**
> post_drawing_rotate_flip_async(self, post_drawing_rotate_flip_request)

Rotate/flip a drawing. Drawing data is passed as a zero-indexed multipart/form-data content or as raw body stream.

Performs operation asynchronously.

### Return type

**file**

### PostDrawingRotateFlipRequest Parameters
```python
__init__(self, 
    drawing_data, 
    output_format, 
    rotate_flip_type, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 
 **output_format** | **str**| Resulting file format. | 
 **rotate_flip_type** | **str**| Rotate/flip operation to apply. | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="post_drawing_save_as"></a>
# **post_drawing_save_as**
> post_drawing_save_as(self, post_drawing_save_as_request)

Export existing drawing to another format. Drawing data is passed as zero-indexed multipart/form-data content or as raw body stream.             

### Return type

**file**

<a name="post_drawing_save_as_async"></a>
# **post_drawing_save_as_async**
> post_drawing_save_as_async(self, post_drawing_save_as_request)

Export existing drawing to another format. Drawing data is passed as zero-indexed multipart/form-data content or as raw body stream.             

Performs operation asynchronously.

### Return type

**file**

### PostDrawingSaveAsRequest Parameters
```python
__init__(self, 
    drawing_data, 
    output_format, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 
 **output_format** | **str**| Resulting file format. | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="post_drawing_svg"></a>
# **post_drawing_svg**
> post_drawing_svg(self, post_drawing_svg_request)

Export an existing drawing to SVG format with export settings specified.

### Return type

**file**

<a name="post_drawing_svg_async"></a>
# **post_drawing_svg_async**
> post_drawing_svg_async(self, post_drawing_svg_request)

Export an existing drawing to SVG format with export settings specified.

Performs operation asynchronously.

### Return type

**file**

### PostDrawingSvgRequest Parameters
```python
__init__(self, 
    name, 
    options, 
    folder=folder, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an input drawing on a storage. | 
 **options** | [**SvgOptionsDTO**](SvgOptionsDTO.md)| Export SVG options passed as a JSON on a request body. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="post_drawing_tiff"></a>
# **post_drawing_tiff**
> post_drawing_tiff(self, post_drawing_tiff_request)

Export an existing drawing into TIFF format with export settings specified.

### Return type

**file**

<a name="post_drawing_tiff_async"></a>
# **post_drawing_tiff_async**
> post_drawing_tiff_async(self, post_drawing_tiff_request)

Export an existing drawing into TIFF format with export settings specified.

Performs operation asynchronously.

### Return type

**file**

### PostDrawingTiffRequest Parameters
```python
__init__(self, 
    name, 
    options, 
    folder=folder, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an input drawing on a storage. | 
 **options** | [**TiffOptionsDTO**](TiffOptionsDTO.md)| Export TIFF options passed as a JSON on a request body. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="post_drawing_wmf"></a>
# **post_drawing_wmf**
> post_drawing_wmf(self, post_drawing_wmf_request)

Export an existing drawing to WMF format with export settings specified.

### Return type

**file**

<a name="post_drawing_wmf_async"></a>
# **post_drawing_wmf_async**
> post_drawing_wmf_async(self, post_drawing_wmf_request)

Export an existing drawing to WMF format with export settings specified.

Performs operation asynchronously.

### Return type

**file**

### PostDrawingWmfRequest Parameters
```python
__init__(self, 
    name, 
    options, 
    folder=folder, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filename of an input drawing on a storage. | 
 **options** | [**WmfOptionsDTO**](WmfOptionsDTO.md)| Export WMF options passed as a JSON on a request body. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="put_drawing_bmp"></a>
# **put_drawing_bmp**
> put_drawing_bmp(self, put_drawing_bmp_request)

Export drawing to BMP format. Drawing data is passed as zero-indexed multipart/form-data as well as export BMP options serialized as JSON. Order of drawing data and BMP options could vary.

### Return type

**file**

<a name="put_drawing_bmp_async"></a>
# **put_drawing_bmp_async**
> put_drawing_bmp_async(self, put_drawing_bmp_request)

Export drawing to BMP format. Drawing data is passed as zero-indexed multipart/form-data as well as export BMP options serialized as JSON. Order of drawing data and BMP options could vary.

Performs operation asynchronously.

### Return type

**file**

### PutDrawingBmpRequest Parameters
```python
__init__(self, 
    drawing_data, 
    out_path=out_path, 
    export_options=export_options, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **export_options** | **str**| JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/BmpOptionsDTO model definition. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="put_drawing_gif"></a>
# **put_drawing_gif**
> put_drawing_gif(self, put_drawing_gif_request)

Export drawing to GIF format. Drawing data is passed as zero-indexed multipart/form-data as well as export GIF options serialized as JSON. Order of drawing data and GIF options could vary.

### Return type

**file**

<a name="put_drawing_gif_async"></a>
# **put_drawing_gif_async**
> put_drawing_gif_async(self, put_drawing_gif_request)

Export drawing to GIF format. Drawing data is passed as zero-indexed multipart/form-data as well as export GIF options serialized as JSON. Order of drawing data and GIF options could vary.

Performs operation asynchronously.

### Return type

**file**

### PutDrawingGifRequest Parameters
```python
__init__(self, 
    drawing_data, 
    export_options=export_options, 
    out_path=out_path, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 
 **export_options** | **str**| JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/GifOptionsDTO model definition. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="put_drawing_jpeg"></a>
# **put_drawing_jpeg**
> put_drawing_jpeg(self, put_drawing_jpeg_request)

Export drawing to JPEG format. Drawing data is passed as zero-indexed multipart/form-data as well as export JPEG options serialized as JSON. Order of drawing data and JPEG options could vary.

### Return type

**file**

<a name="put_drawing_jpeg_async"></a>
# **put_drawing_jpeg_async**
> put_drawing_jpeg_async(self, put_drawing_jpeg_request)

Export drawing to JPEG format. Drawing data is passed as zero-indexed multipart/form-data as well as export JPEG options serialized as JSON. Order of drawing data and JPEG options could vary.

Performs operation asynchronously.

### Return type

**file**

### PutDrawingJpegRequest Parameters
```python
__init__(self, 
    drawing_data, 
    out_path=out_path, 
    export_options=export_options, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **export_options** | **str**| JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/JpegOptionsDTO model definition. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="put_drawing_jpeg2000"></a>
# **put_drawing_jpeg2000**
> put_drawing_jpeg2000(self, put_drawing_jpeg2000_request)

Export drawing to JPEG2000 format. Drawing data is passed as zero-indexed multipart/form-data as well as export JPEG2000 options serialized as JSON. Order of drawing data and JPEG2000 options could vary.

### Return type

**file**

<a name="put_drawing_jpeg2000_async"></a>
# **put_drawing_jpeg2000_async**
> put_drawing_jpeg2000_async(self, put_drawing_jpeg2000_request)

Export drawing to JPEG2000 format. Drawing data is passed as zero-indexed multipart/form-data as well as export JPEG2000 options serialized as JSON. Order of drawing data and JPEG2000 options could vary.

Performs operation asynchronously.

### Return type

**file**

### PutDrawingJpeg2000Request Parameters
```python
__init__(self, 
    drawing_data, 
    out_path=out_path, 
    export_options=export_options, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **export_options** | **str**| JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/Jpeg2000OptionsDTO model definition. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="put_drawing_pdf"></a>
# **put_drawing_pdf**
> put_drawing_pdf(self, put_drawing_pdf_request)

Export drawing to PDF format. Drawing data is passed as zero-indexed multipart/form-data as well as export PDF options serialized as JSON. Order of drawing data and PDF options could vary.

### Return type

**file**

<a name="put_drawing_pdf_async"></a>
# **put_drawing_pdf_async**
> put_drawing_pdf_async(self, put_drawing_pdf_request)

Export drawing to PDF format. Drawing data is passed as zero-indexed multipart/form-data as well as export PDF options serialized as JSON. Order of drawing data and PDF options could vary.

Performs operation asynchronously.

### Return type

**file**

### PutDrawingPdfRequest Parameters
```python
__init__(self, 
    drawing_data, 
    out_path=out_path, 
    export_options=export_options, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **export_options** | **str**| JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/PdfOptionsDTO model definition. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="put_drawing_png"></a>
# **put_drawing_png**
> put_drawing_png(self, put_drawing_png_request)

Export drawing to PNG format. Drawing data is passed as zero-indexed multipart/form-data as well as export PNG options serialized as JSON. Order of drawing data and PNG options could vary.

### Return type

**file**

<a name="put_drawing_png_async"></a>
# **put_drawing_png_async**
> put_drawing_png_async(self, put_drawing_png_request)

Export drawing to PNG format. Drawing data is passed as zero-indexed multipart/form-data as well as export PNG options serialized as JSON. Order of drawing data and PNG options could vary.

Performs operation asynchronously.

### Return type

**file**

### PutDrawingPngRequest Parameters
```python
__init__(self, 
    drawing_data, 
    out_path=out_path, 
    export_options=export_options, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **export_options** | **str**| JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/PngOptionsDTO model definition. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="put_drawing_psd"></a>
# **put_drawing_psd**
> put_drawing_psd(self, put_drawing_psd_request)

Export drawing to PSD format. Drawing data is passed as zero-indexed multipart/form-data as well as export PSD options serialized as JSON. Order of drawing data and PSD options could vary.

### Return type

**file**

<a name="put_drawing_psd_async"></a>
# **put_drawing_psd_async**
> put_drawing_psd_async(self, put_drawing_psd_request)

Export drawing to PSD format. Drawing data is passed as zero-indexed multipart/form-data as well as export PSD options serialized as JSON. Order of drawing data and PSD options could vary.

Performs operation asynchronously.

### Return type

**file**

### PutDrawingPsdRequest Parameters
```python
__init__(self, 
    drawing_data, 
    out_path=out_path, 
    export_options=export_options, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **export_options** | **str**| JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/PsdOptionsDTO model definition. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="put_drawing_svg"></a>
# **put_drawing_svg**
> put_drawing_svg(self, put_drawing_svg_request)

Export drawing to SVG format. Drawing data is passed as zero-indexed multipart/form-data as well as export SVG options serialized as JSON. Order of drawing data and SVG options could vary.

### Return type

**file**

<a name="put_drawing_svg_async"></a>
# **put_drawing_svg_async**
> put_drawing_svg_async(self, put_drawing_svg_request)

Export drawing to SVG format. Drawing data is passed as zero-indexed multipart/form-data as well as export SVG options serialized as JSON. Order of drawing data and SVG options could vary.

Performs operation asynchronously.

### Return type

**file**

### PutDrawingSvgRequest Parameters
```python
__init__(self, 
    drawing_data, 
    out_path=out_path, 
    export_options=export_options, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **export_options** | **str**| JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/SvgOptionsDTO model definition. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="put_drawing_tiff"></a>
# **put_drawing_tiff**
> put_drawing_tiff(self, put_drawing_tiff_request)

Export drawing to TIFF format. Drawing data is passed as zero-indexed multipart/form-data as well as export TIFF options serialized as JSON. Order of drawing data and TIFF options could vary.

### Return type

**file**

<a name="put_drawing_tiff_async"></a>
# **put_drawing_tiff_async**
> put_drawing_tiff_async(self, put_drawing_tiff_request)

Export drawing to TIFF format. Drawing data is passed as zero-indexed multipart/form-data as well as export TIFF options serialized as JSON. Order of drawing data and TIFF options could vary.

Performs operation asynchronously.

### Return type

**file**

### PutDrawingTiffRequest Parameters
```python
__init__(self, 
    drawing_data, 
    out_path=out_path, 
    export_options=export_options, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **export_options** | **str**| JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/TiffOptionsDTO model definition. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="put_drawing_wmf"></a>
# **put_drawing_wmf**
> put_drawing_wmf(self, put_drawing_wmf_request)

Export drawing to WMF format. Drawing data is passed as zero-indexed multipart/form-data as well as export WMF options serialized as JSON. Order of drawing data and WMF options could vary.

### Return type

**file**

<a name="put_drawing_wmf_async"></a>
# **put_drawing_wmf_async**
> put_drawing_wmf_async(self, put_drawing_wmf_request)

Export drawing to WMF format. Drawing data is passed as zero-indexed multipart/form-data as well as export WMF options serialized as JSON. Order of drawing data and WMF options could vary.

Performs operation asynchronously.

### Return type

**file**

### PutDrawingWmfRequest Parameters
```python
__init__(self, 
    drawing_data, 
    out_path=out_path, 
    export_options=export_options, 
    storage=storage)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drawing_data** | **file**| Input drawing | 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **export_options** | **str**| JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/WmfOptionsDTO model definition. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

