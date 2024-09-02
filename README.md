![](https://img.shields.io/badge/api-v3.0-lightgrey) ![PyPI](https://img.shields.io/pypi/v/aspose-cad-cloud) ![PyPI - Format](https://img.shields.io/pypi/format/aspose-cad-cloud) ![PyPI - Downloads](https://img.shields.io/pypi/dm/aspose-cad-cloud) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aspose-cad-cloud) [![GitHub license](https://img.shields.io/github/license/aspose-cad-cloud/aspose-cad-cloud-python)](https://github.com/aspose-cad-cloud/aspose-cad-cloud-python/blob/master/LICENSE) ![GitHub last commit](https://img.shields.io/github/last-commit/Aspose-cad-Cloud/aspose-cad-cloud-python)
# Aspose.CAD Cloud Python SDK
[Aspose.CAD Cloud](https://products.aspose.cloud/cad) is a true [REST API](https://apireference.aspose.cloud/cad/) that enables you to perform a wide range of CAD and BIM drawings processing operations including manipulation, editing, export and conversion in a cloud, with zero initial costs.

This repository contains [Aspose.CAD Cloud Python SDK](https://products.aspose.cloud/cad/python) source code which is written in Python. This SDK allows you to work with Aspose.CAD Cloud REST APIs in your Node.js applications quickly and easily, with zero initial cost and gain all benefits of strong types and IDE highlights.

## CAD Processing Features
- Export CAD drawings to other file formats.
- Get image properties of a CAD drawing.
- Change the scale of an AutoCAD sketch.
- Flip and rotate a CAD image.
- Upload or download CAD drawings to the cloud storage.
- Copy, move, delete CAD files from the cloud storage.

## Read & Write CAD Formats
DXF (R12/2007/2010)

## Save CAD As
*Fixed Layout*: PDF (as a vector and as a raster)
*Images*: BMP, PNG, JPG, JPEG, JPEG2000, TIF, TIFF, PSD, GIF, WMF

## Read CAD Formats
DWG (13, 14, 2000, 2004), DWG (2010, 2013, 2014), DWG (2015, 2017, 2018), DWT (13, 14, 2000, 2004), DWT (2010, 2013, 2014), DWT (2015, 2017, 2018), DWF, DGN v7, IGES (IGS), PLT, Industry Foundation Classes (IFC), STereoLithography (STL)
Look at [API Reference](https://apireference.aspose.cloud/cad/) for full API specification.

For the complete list of use-cases, please refer to the [format support document](https://docs.aspose.cloud/cad/supported-file-formats/) to see what you can achieve!

Detalied official documentation can be found at the [following link](https://docs.aspose.cloud/cad/).

## Getting Started
1. **Sign Up**. Before you begin, you need to sign up for an account on our [Dashboard](https://dashboard.aspose.cloud/) and retrieve your [credentials](https://dashboard.aspose.cloud/#/apps).
2. **Minimum requirements**. This SDK requires [Python 2.7 or later](https://www.python.org/downloads/).
3. **Install Aspose.CAD Cloud Python SDK**.

Please, add the following [PyPi package](https://pypi.org/project/aspose-cad-cloud/) to your requirements.txt.
```
aspose-cad-cloud>=24.5.2
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

## Convert Drawing to Image(PNG) in Python

```python
	# Get your ClientId and ClientSecret from https://dashboard.aspose.cloud (free registration required).

	cad_api = CadApi('MY_CLIENT_SECRET', 'MY_CLIENT_ID')

	request = requests.GetDrawingSaveAsRequest("sample.dwg", "png", "original_data_folder", "my_output_path", "my_storage_name")
	return cad_api.get_drawing_save_as(request)
```

## Content
You may check our full [API endpoints list](https://github.com/aspose-cad-cloud/aspose-cad-cloud-python/blob/master/asposecadcloud/api/cad_api.py) or [models available](https://github.com/aspose-cad-cloud/aspose-cad-cloud-python/tree/master/asposecadcloud/models) in the SDK.

## Dependencies
* [Python 2.7 or later](https://www.python.org/downloads/)

## Licensing
All Aspose.CAD Cloud SDKs, helper scripts and templates are licensed under [MIT License](LICENSE).

## Aspose.CAD Cloud SDKs in Popular Languages

| .NET | Java | PHP | Python | Ruby | Node.js |
|---|---|---|---|---|---|
| [GitHub](https://github.com/aspose-cad-cloud/aspose-cad-cloud-dotnet) | [GitHub](https://github.com/aspose-cad-cloud/aspose-cad-cloud-java) | [GitHub](https://github.com/aspose-cad-cloud/aspose-cad-cloud-php) | [GitHub](https://github.com/aspose-cad-cloud/aspose-cad-cloud-python) | [GitHub](https://github.com/aspose-cad-cloud/aspose-cad-cloud-ruby)  | [GitHub](https://github.com/aspose-cad-cloud/aspose-cad-cloud-nodejs) |
| [NuGet](https://www.nuget.org/packages/Aspose.cad-Cloud/) | [Maven](https://repository.aspose.cloud/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cad-cloud) | [Composer](https://packagist.org/packages/aspose/aspose-cad-cloud) | [PIP](https://pypi.org/project/aspose.cad-cloud/) | [GEM](https://rubygems.org/gems/aspose_cad_cloud)  | [NPM](https://www.npmjs.com/package/@asposecloud/aspose-cad-cloud) |

[Product Page](https://products.aspose.cloud/cad/python) | [Documentation](https://docs.aspose.cloud/display/cadcloud/Home) | [API Reference](https://apireference.aspose.cloud/cad/) | [Code Samples](https://github.com/aspose-cad-cloud/aspose-cad-cloud-python) | [Blog](https://blog.aspose.cloud/category/cad/) | [Free Support](https://forum.aspose.cloud/c/cad) | [Free Trial](https://dashboard.aspose.cloud/#/apps)|
