# Aspose.CAD Cloud Python SDK
[Aspose.CAD Cloud](https://products.aspose.cloud/cad) is a true [REST API](https://apireference.aspose.cloud/cad/) that enables you to perform a wide range of CAD and BIM drawings processing operations including manipulation, editing, export and conversion in a cloud, with zero initial costs.

This repository contains [Aspose.CAD Cloud Python SDK](https://products.aspose.cloud/cad/python) source code which is written in Python. This SDK allows you to work with Aspose.CAD Cloud REST APIs in your Node.js applications quickly and easily, with zero initial cost and gain all benefits of strong types and IDE highlights.

# Key Features

* Supports the latest versions of AutoCAD DWG, DXF, DWF, DWFX, DWT, STL, IGS, DGN, OBJ and CF2 files
* Convert CAD drawings to high quality PDF
* Convert CAD drawing to high quality raster images
* Convert CAD drawing to high quality vector files like SVG and WMF
* Modify and convert CAD drawing to DXF
* Modify and convert CAD drawing to DWF
* Select and modify specific entities
* Retrieve & update drawing properties and metadata
* Select and convert specific layouts
* Select and convert specific layers
* Track the file conversion process

#### Drawing Formats Support
Export the following drawing to various formats (generally supported ones are BMP, PSD, JPEG, TIFF, GIF, PNG, JPEG2000, SVG, WMF and PDF):
* DWG
* DXF
* DWF
* DWFX
* DWT
* STL
* IGS
* DGN
* OBJ
* CF2

Process options, change and return drawings in the same format:
* DXF
* DWF

Output formats to export:
* BMP
* PSD
* JPEG
* TIFF
* GIF
* PNG
* JPEG2000 (JP2, J2K)
* SVG
* WMF
* PDF

#### Supported CAD Operations
* Export 
* Resize
* Crop
* Rotate and Flip

Look at [API Reference](https://apireference.aspose.cloud/cad/) for full API specification.

For the complete list of use-cases, please refer to the [format support document](https://docs.aspose.cloud/cad/supported-file-formats/) to see what you can achieve!

Detalied official documentation can be found at the [following link](https://docs.aspose.cloud/cad/).

## Getting Started
1. **Sign Up**. Before you begin, you need to sign up for an account on our [Dashboard](https://dashboard.aspose.cloud/) and retrieve your [credentials](https://dashboard.aspose.cloud/#/apps).
2. **Minimum requirements**. This SDK requires [Python 2.7 or later](https://www.python.org/downloads/).
3. **Install Aspose.CAD Cloud Python SDK**.

Please, add the following [PyPi package](https://pypi.org/project/aspose-cad-cloud/) to your requirements.txt.
```
aspose-cad-cloud>=20.11
```
Or install it using command line.
```
pip install aspose-cad-cloud
```
Import the dependencies to your code as follows.
```python
import aspose-cad-cloud
```
4. **Using the SDK**. The best way to become familiar with how to use the SDK is to read the [Developer Guide](https://docs.aspose.cloud/cad/developer-guide/). The [Getting Started Guide](https://docs.aspose.cloud/cad/getting-started/) will help you to become familiar with the common concepts.

## Examples
```python
// optional parameters are base URL, API version and debug mode
// default base URL is https://api.aspose.cloud/
// default API version is v3.0
// default debug mode is false
// authentication type is OAuth2.0 (bearer JWT token)

from asposecadcloud import CadApi
import asposecadcloud.models.requests as requests
...

self.cad_api = CadApi(app_key, app_sid)
return self.cad_api.get_drawing_save_as(
                                requests.GetDrawingSaveAsRequest(name, format_extension, self.original_data_folder, output_path, storage))
```
Please, look at [Examples](EXAMPLES.md) document for basic usage or use the [Examples](Examples) folder for more sophisticated scenarios.

## Content
You may check our full [API endpoints list](docs/API_README.md#documentation-for-api-endpoints) or [models available](docs/API_README.md#documentation-for-models) in the SDK.

## Dependencies
* [Python 2.7 or later](https://www.python.org/downloads/)

## Licensing
All Aspose.CAD Cloud SDKs, helper scripts and templates are licensed under [MIT License](LICENSE).

## Contact Us
Your feedback is very important to us. Please feel free to contact via
+ [**Free Support Forum**](https://forum.aspose.cloud/c/cad)
+ [**Paid Support Helpdesk**](https://helpdesk.aspose.cloud/)

## Resources
+ [**Web API reference**](https://apireference.aspose.cloud/cad/)
+ [**Website**](https://www.aspose.cloud)
+ [**Product Home**](https://products.aspose.cloud/cad)
+ [**Documentation**](https://docs.aspose.cloud/cad/)
+ [**Blog**](https://blog.aspose.cloud/category/aspose-products/aspose.cad-cloud/)

## Other languages
We generate our SDKs in different languages so you may check if yours is available in our [repository](https://github.com/aspose-cad-cloud). If you don't find your language in the list, feel free to request it from us, or use raw REST API requests as you can find it [here](https://products.aspose.cloud/cad/curl).

## Code generator
The solution is updated using [code generator](https://github.com/aspose-cad-cloud/aspose-cad-cloud-codegen).
