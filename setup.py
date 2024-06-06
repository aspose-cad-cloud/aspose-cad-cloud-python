#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="setup.py">
#    Copyright (c) 2019 Aspose Pty Ltd. All rights reserved.
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

from setuptools import setup, find_packages

NAME = "aspose-cad-cloud"
VERSION = "24.5.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "urllib3>=1.22",
    "six>=1.11",
    "certifi>=2018.1",
    "python_dateutil>=2.8"
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=NAME,
    version=VERSION,
    description="Aspose.CAD Cloud Python SDK",
    author="Aspose",
    author_email="vitalii.kornyliuk@aspose.com",
    url="https://products.aspose.cloud/cad",
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Multimedia :: Graphics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12'
    ],
    keywords=[
        "Aspose",
        "CAD",
        "Cloud",
        "REST",
        "API",
        "SDK",
        "drawing",
        "watermark",
        "DWG",
        "DXF",
        "DWF",
        "DWFX",
        "DWT",
        "STL",
        "IGS",
        "DGN",
        "OBJ",
        "CF2",
        "GLB",
        "GLTF",
        "CGM",
        "U3D",
        "3DS"
        "image",
        "bmp",
        "gif",
        "jpg",
        "jpeg",
        "jpeg2000",
        "jp2",
        "j2k",
        "png",
        "psd",
        "tiff",
        "tif",
        "wmf",
        "svg",
        "export",
        "conversion"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "test*"]),
    include_package_data=True,
    data_files=[("", ["LICENSE"])],
    long_description=long_description,
    long_description_content_type="text/markdown"
)
