# asposecadcloud.CadApi

<a name="copy_file"></a>
# **copy_file**
> copy_file(self, copy_file_request)

Copy file

### Return type

void (empty response body)

<a name="copy_file_async"></a>
# **copy_file_async**
> copy_file_async(self, copy_file_request)

Copy file

Performs operation asynchronously.

### Return type

void (empty response body)

### CopyFileRequest Parameters
```python
__init__(self, 
    src_path, 
    dest_path, 
    src_storage_name=src_storage_name, 
    dest_storage_name=dest_storage_name, 
    version_id=version_id)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source file path e.g. &#39;/folder/file.ext&#39; | 
 **dest_path** | **str**| Destination file path | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 
 **version_id** | **str**| File version ID to copy | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="copy_folder"></a>
# **copy_folder**
> copy_folder(self, copy_folder_request)

Copy folder

### Return type

void (empty response body)

<a name="copy_folder_async"></a>
# **copy_folder_async**
> copy_folder_async(self, copy_folder_request)

Copy folder

Performs operation asynchronously.

### Return type

void (empty response body)

### CopyFolderRequest Parameters
```python
__init__(self, 
    src_path, 
    dest_path, 
    src_storage_name=src_storage_name, 
    dest_storage_name=dest_storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source folder path e.g. &#39;/src&#39; | 
 **dest_path** | **str**| Destination folder path e.g. &#39;/dst&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="create_folder"></a>
# **create_folder**
> create_folder(self, create_folder_request)

Create the folder

### Return type

void (empty response body)

<a name="create_folder_async"></a>
# **create_folder_async**
> create_folder_async(self, create_folder_request)

Create the folder

Performs operation asynchronously.

### Return type

void (empty response body)

### CreateFolderRequest Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path to create e.g. &#39;folder_1/folder_2/&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="delete_file"></a>
# **delete_file**
> delete_file(self, delete_file_request)

Delete file

### Return type

void (empty response body)

<a name="delete_file_async"></a>
# **delete_file_async**
> delete_file_async(self, delete_file_request)

Delete file

Performs operation asynchronously.

### Return type

void (empty response body)

### DeleteFileRequest Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name, 
    version_id=version_id)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/folder/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID to delete | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="delete_folder"></a>
# **delete_folder**
> delete_folder(self, delete_folder_request)

Delete folder

### Return type

void (empty response body)

<a name="delete_folder_async"></a>
# **delete_folder_async**
> delete_folder_async(self, delete_folder_request)

Delete folder

Performs operation asynchronously.

### Return type

void (empty response body)

### DeleteFolderRequest Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name, 
    recursive=recursive)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path e.g. &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **recursive** | **bool**| Enable to delete folders, subfolders and files | [optional] [default to false]

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="download_file"></a>
# **download_file**
> download_file(self, download_file_request)

Download file

### Return type

**file**

<a name="download_file_async"></a>
# **download_file_async**
> download_file_async(self, download_file_request)

Download file

Performs operation asynchronously.

### Return type

**file**

### DownloadFileRequest Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name, 
    version_id=version_id)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/folder/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID to download | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="get_disc_usage"></a>
# **get_disc_usage**
> get_disc_usage(self, get_disc_usage_request)

Get disc usage

### Return type

[**DiscUsage**](DiscUsage.md)

<a name="get_disc_usage_async"></a>
# **get_disc_usage_async**
> get_disc_usage_async(self, get_disc_usage_request)

Get disc usage

Performs operation asynchronously.

### Return type

[**DiscUsage**](DiscUsage.md)

### GetDiscUsageRequest Parameters
```python
__init__(self, 
    storage_name=storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_name** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

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
 **rotate_flip_type** | **str**| Rotate/flip operation to apply. Possible values: RotateNoneFlipNone, Rotate90FlipNone, Rotate180FlipNone, Rotate270FlipNone, RotateNoneFlipX, Rotate90FlipX, Rotate180FlipX, Rotate270FlipX, RotateNoneFlipY, Rotate90FlipY, Rotate180FlipY, Rotate270FlipY, RotateNoneFlipXY, Rotate90FlipXY, Rotate180FlipXY, Rotate270FlipXY | 
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

<a name="get_file_versions"></a>
# **get_file_versions**
> get_file_versions(self, get_file_versions_request)

Get file versions

### Return type

[**FileVersions**](FileVersions.md)

<a name="get_file_versions_async"></a>
# **get_file_versions_async**
> get_file_versions_async(self, get_file_versions_request)

Get file versions

Performs operation asynchronously.

### Return type

[**FileVersions**](FileVersions.md)

### GetFileVersionsRequest Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File path e.g. &#39;/file.ext&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="get_files_list"></a>
# **get_files_list**
> get_files_list(self, get_files_list_request)

Get all files and folders within a folder

### Return type

[**FilesList**](FilesList.md)

<a name="get_files_list_async"></a>
# **get_files_list_async**
> get_files_list_async(self, get_files_list_request)

Get all files and folders within a folder

Performs operation asynchronously.

### Return type

[**FilesList**](FilesList.md)

### GetFilesListRequest Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Folder path e.g. &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="move_file"></a>
# **move_file**
> move_file(self, move_file_request)

Move file

### Return type

void (empty response body)

<a name="move_file_async"></a>
# **move_file_async**
> move_file_async(self, move_file_request)

Move file

Performs operation asynchronously.

### Return type

void (empty response body)

### MoveFileRequest Parameters
```python
__init__(self, 
    src_path, 
    dest_path, 
    src_storage_name=src_storage_name, 
    dest_storage_name=dest_storage_name, 
    version_id=version_id)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Source file path e.g. &#39;/src.ext&#39; | 
 **dest_path** | **str**| Destination file path e.g. &#39;/dest.ext&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 
 **version_id** | **str**| File version ID to move | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="move_folder"></a>
# **move_folder**
> move_folder(self, move_folder_request)

Move folder

### Return type

void (empty response body)

<a name="move_folder_async"></a>
# **move_folder_async**
> move_folder_async(self, move_folder_request)

Move folder

Performs operation asynchronously.

### Return type

void (empty response body)

### MoveFolderRequest Parameters
```python
__init__(self, 
    src_path, 
    dest_path, 
    src_storage_name=src_storage_name, 
    dest_storage_name=dest_storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **src_path** | **str**| Folder path to move e.g. &#39;/folder&#39; | 
 **dest_path** | **str**| Destination folder path to move to e.g &#39;/dst&#39; | 
 **src_storage_name** | **str**| Source storage name | [optional] 
 **dest_storage_name** | **str**| Destination storage name | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="object_exists"></a>
# **object_exists**
> object_exists(self, object_exists_request)

Check if file or folder exists

### Return type

[**ObjectExist**](ObjectExist.md)

<a name="object_exists_async"></a>
# **object_exists_async**
> object_exists_async(self, object_exists_request)

Check if file or folder exists

Performs operation asynchronously.

### Return type

[**ObjectExist**](ObjectExist.md)

### ObjectExistsRequest Parameters
```python
__init__(self, 
    path, 
    storage_name=storage_name, 
    version_id=version_id)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| File or folder path e.g. &#39;/file.ext&#39; or &#39;/folder&#39; | 
 **storage_name** | **str**| Storage name | [optional] 
 **version_id** | **str**| File version ID | [optional] 

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

<a name="post_drawing_dwf"></a>
# **post_drawing_dwf**
> post_drawing_dwf(self, post_drawing_dwf_request)

Export an existing drawing to Dwf format with export settings specified.

### Return type

**file**

<a name="post_drawing_dwf_async"></a>
# **post_drawing_dwf_async**
> post_drawing_dwf_async(self, post_drawing_dwf_request)

Export an existing drawing to Dwf format with export settings specified.

Performs operation asynchronously.

### Return type

**file**

### PostDrawingDwfRequest Parameters
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
 **options** | [**DwfOptionsDTO**](DwfOptionsDTO.md)| Export Dwf options passed as a JSON on a request body. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="post_drawing_dxf"></a>
# **post_drawing_dxf**
> post_drawing_dxf(self, post_drawing_dxf_request)

Export an existing drawing to DXF format with export settings specified.

### Return type

**file**

<a name="post_drawing_dxf_async"></a>
# **post_drawing_dxf_async**
> post_drawing_dxf_async(self, post_drawing_dxf_request)

Export an existing drawing to DXF format with export settings specified.

Performs operation asynchronously.

### Return type

**file**

### PostDrawingDXFRequest Parameters
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
 **options** | [**DxfOptionsDTO**](DxfOptionsDTO.md)| Export DXF options passed as a JSON on a request body. | 
 **folder** | **str**| Folder with a drawing to process. | [optional] 
 **out_path** | **str**| Path to updated file (if this is empty, response contains streamed file). | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="post_drawing_fbx"></a>
# **post_drawing_fbx**
> post_drawing_fbx(self, post_drawing_fbx_request)

Export an existing drawing to Fbx format with export settings specified.

### Return type

**file**

<a name="post_drawing_fbx_async"></a>
# **post_drawing_fbx_async**
> post_drawing_fbx_async(self, post_drawing_fbx_request)

Export an existing drawing to Fbx format with export settings specified.

Performs operation asynchronously.

### Return type

**file**

### PostDrawingFbxRequest Parameters
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
 **options** | [**FbxOptionsDTO**](FbxOptionsDTO.md)| Export Fbx options passed as a JSON on a request body. | 
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

<a name="post_drawing_obj"></a>
# **post_drawing_obj**
> post_drawing_obj(self, post_drawing_obj_request)

Export an existing drawing to Obj format with export settings specified.

### Return type

**file**

<a name="post_drawing_obj_async"></a>
# **post_drawing_obj_async**
> post_drawing_obj_async(self, post_drawing_obj_request)

Export an existing drawing to Obj format with export settings specified.

Performs operation asynchronously.

### Return type

**file**

### PostDrawingObjRequest Parameters
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
 **options** | [**ObjOptionsDTO**](ObjOptionsDTO.md)| Export Obj options passed as a JSON on a request body. | 
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
 **rotate_flip_type** | **str**| Rotate/flip operation to apply. Possible values: RotateNoneFlipNone, Rotate90FlipNone, Rotate180FlipNone, Rotate270FlipNone, RotateNoneFlipX, Rotate90FlipX, Rotate180FlipX, Rotate270FlipX, RotateNoneFlipY, Rotate90FlipY, Rotate180FlipY, Rotate270FlipY, RotateNoneFlipXY, Rotate90FlipXY, Rotate180FlipXY, Rotate270FlipXY | 
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

<a name="put_drawing_dwf"></a>
# **put_drawing_dwf**
> put_drawing_dwf(self, put_drawing_dwf_request)

Export drawing to Dwf format. Drawing data is passed as zero-indexed multipart/form-data as well as export Dwf options serialized as JSON. Order of drawing data and Dwf options could vary.

### Return type

**file**

<a name="put_drawing_dwf_async"></a>
# **put_drawing_dwf_async**
> put_drawing_dwf_async(self, put_drawing_dwf_request)

Export drawing to Dwf format. Drawing data is passed as zero-indexed multipart/form-data as well as export Dwf options serialized as JSON. Order of drawing data and Dwf options could vary.

Performs operation asynchronously.

### Return type

**file**

### PutDrawingDwfRequest Parameters
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
 **export_options** | **str**| JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/DwfOptionsDTO model definition. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="put_drawing_dxf"></a>
# **put_drawing_dxf**
> put_drawing_dxf(self, put_drawing_dxf_request)

Export drawing to DXF format. Drawing data is passed as zero-indexed multipart/form-data as well as export DXF options serialized as JSON. Order of drawing data and DXF options could vary.

### Return type

**file**

<a name="put_drawing_dxf_async"></a>
# **put_drawing_dxf_async**
> put_drawing_dxf_async(self, put_drawing_dxf_request)

Export drawing to DXF format. Drawing data is passed as zero-indexed multipart/form-data as well as export DXF options serialized as JSON. Order of drawing data and DXF options could vary.

Performs operation asynchronously.

### Return type

**file**

### PutDrawingDXFRequest Parameters
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
 **export_options** | **str**| JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/DxfOptionsDTO model definition. | [optional] 
 **storage** | **str**| Your Aspose Cloud Storage name. | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="put_drawing_fbx"></a>
# **put_drawing_fbx**
> put_drawing_fbx(self, put_drawing_fbx_request)

Export drawing to Fbx format. Drawing data is passed as zero-indexed multipart/form-data as well as export Fbx options serialized as JSON. Order of drawing data and Fbx options could vary.

### Return type

**file**

<a name="put_drawing_fbx_async"></a>
# **put_drawing_fbx_async**
> put_drawing_fbx_async(self, put_drawing_fbx_request)

Export drawing to Fbx format. Drawing data is passed as zero-indexed multipart/form-data as well as export Fbx options serialized as JSON. Order of drawing data and Fbx options could vary.

Performs operation asynchronously.

### Return type

**file**

### PutDrawingFbxRequest Parameters
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
 **export_options** | **str**| JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/FbxOptionsDTO model definition. | [optional] 
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

<a name="put_drawing_obj"></a>
# **put_drawing_obj**
> put_drawing_obj(self, put_drawing_obj_request)

Export drawing to Obj format. Drawing data is passed as zero-indexed multipart/form-data as well as export Obj options serialized as JSON. Order of drawing data and Obj options could vary.

### Return type

**file**

<a name="put_drawing_obj_async"></a>
# **put_drawing_obj_async**
> put_drawing_obj_async(self, put_drawing_obj_request)

Export drawing to Obj format. Drawing data is passed as zero-indexed multipart/form-data as well as export Obj options serialized as JSON. Order of drawing data and Obj options could vary.

Performs operation asynchronously.

### Return type

**file**

### PutDrawingObjRequest Parameters
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
 **export_options** | **str**| JSON-serialized export options passed as zero-indexed multipart/form-data. Follow #/definitions/ObjOptionsDTO model definition. | [optional] 
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

<a name="storage_exists"></a>
# **storage_exists**
> storage_exists(self, storage_exists_request)

Check if storage exists

### Return type

[**StorageExist**](StorageExist.md)

<a name="storage_exists_async"></a>
# **storage_exists_async**
> storage_exists_async(self, storage_exists_request)

Check if storage exists

Performs operation asynchronously.

### Return type

[**StorageExist**](StorageExist.md)

### StorageExistsRequest Parameters
```python
__init__(self, 
    storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_name** | **str**| Storage name | 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

<a name="upload_file"></a>
# **upload_file**
> upload_file(self, upload_file_request)

Upload file

### Return type

[**FilesUploadResult**](FilesUploadResult.md)

<a name="upload_file_async"></a>
# **upload_file_async**
> upload_file_async(self, upload_file_request)

Upload file

Performs operation asynchronously.

### Return type

[**FilesUploadResult**](FilesUploadResult.md)

### UploadFileRequest Parameters
```python
__init__(self, 
    path, 
    file, 
    storage_name=storage_name)
```

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Path where to upload including filename and extension e.g. /file.ext or /Folder 1/file.ext             If the content is multipart and path does not contains the file name it tries to get them from filename parameter             from Content-Disposition header.              | 
 **file** | **file**| File to upload | 
 **storage_name** | **str**| Storage name | [optional] 

[[Back to top]](#) [[Back to API list]](API_README.md#documentation-for-api-endpoints) [[Back to Model list]](API_README.md#documentation-for-models) [[Back to API_README]](API_README.md)

