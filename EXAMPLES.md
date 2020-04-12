### Cad - Save as: convert DXF drawing from storage to PNG raster format
```python
# to operate your storage you want to use Aspose.Storage API (asposestoragecloud)
from asposestoragecloud.api_client import ApiClient as StorageApiClient
from asposestoragecloud import StorageApi
...
storage_api_client = StorageApiClient('yourAppKey', 'yourAppSid')
storage_api = StorageApi(storage_api_client)

# optional parameters are base URL, API version, debug mode and proxy url
cad_api = CadApi('yourAppKey', 'yourAppSid')

try:
    # upload local drawing to storage
	f = open('local_filename.dxf', "rb").read()
	storage_api.put_create('remote_file_name.dxf', f, storage='storage')
    
    # convert drawing from storage to PNG
	cad_api.get_drawing_save_as(
		GetDrawingSaveAsRequest('remote_file_name.dxf', 'png', '', 'remote_file_name.png', 'storage'))
	
	#if output path is omitted - resulted image will be returned on response

finally:
    # remove file from storage
    storage_api.delete_file(path='remote_file_name.png', storage='storage')
```

### Cad - Export : convert AutoCAD DWG drawing from request stream to PDF
```python
# to operate your storage you want to use Aspose.Storage API (asposestoragecloud)
from asposestoragecloud.api_client import ApiClient as StorageApiClient
from asposestoragecloud import StorageApi
...
storage_api_client = StorageApiClient('yourAppKey', 'yourAppSid')
storage_api = StorageApi(storage_api_client)

# optional parameters are base URL, API version, debug mode and proxy url
cad_api = CadApi('yourAppKey', 'yourAppSid')

try:
    # convert drawing from provided stream to PDF
	f = open('local_filename.dwg', "rb").read()
	cad_api.post_drawing_save_as(
		PostDrawingSaveAsRequest(f, 'pdf', 'remote_file_name.pdf', 'storage'))
	
	#if output path is omitted - resulted image will be returned on response

finally:
    # remove file from storage
    storage_api.delete_file(path='remote_file_name.pdf', storage='storage')

# other Cad requests typically follow the same principles
```