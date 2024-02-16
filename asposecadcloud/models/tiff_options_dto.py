#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="TiffOptionsDTO.py">
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

import pprint
import re
import six

from asposecadcloud.models.cad_rasterization_options_dto import CadRasterizationOptionsDTO
from asposecadcloud.models.drawing_options_base_dto import DrawingOptionsBaseDTO
from asposecadcloud.models.resolution_setting import ResolutionSetting


class TiffOptionsDTO(DrawingOptionsBaseDTO):
    """Export options for TIFF format
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'byte_order': 'str',
        'compression': 'str',
        'expected_format': 'str',
        'bits_per_sample': 'list[int]',
        'photometric': 'str'
    }

    attribute_map = {
        'byte_order': 'ByteOrder',
        'compression': 'Compression',
        'expected_format': 'ExpectedFormat',
        'bits_per_sample': 'BitsPerSample',
        'photometric': 'Photometric'
    }

    def __init__(self, byte_order=None, compression=None, expected_format=None, bits_per_sample=None, photometric=None):
        """TiffOptionsDTO - a model defined in Swagger"""
        super(TiffOptionsDTO, self).__init__()

        self._byte_order = None
        self._compression = None
        self._expected_format = None
        self._bits_per_sample = None
        self._photometric = None

        if byte_order is not None:
            self.byte_order = byte_order
        if compression is not None:
            self.compression = compression
        if expected_format is not None:
            self.expected_format = expected_format
        if bits_per_sample is not None:
            self.bits_per_sample = bits_per_sample
        if photometric is not None:
            self.photometric = photometric

    @property
    def byte_order(self):
        """Gets the byte_order of this TiffOptionsDTO.

        Bytes order (little/big-endian notation)

        :return: The byte_order of this TiffOptionsDTO.
        :rtype: str
        """
        return self._byte_order

    @byte_order.setter
    def byte_order(self, byte_order):
        """Sets the byte_order of this TiffOptionsDTO.

        Bytes order (little/big-endian notation)

        :param byte_order: The byte_order of this TiffOptionsDTO.
        :type: str
        """
        if byte_order is None:
            raise ValueError("Invalid value for `byte_order`, must not be `None`")
        allowed_values = ["LittleEndian", "BigEndian"]
        if not byte_order.isdigit():
            if byte_order not in allowed_values:
                raise ValueError(
                    "Invalid value for `byte_order` ({0}), must be one of {1}"
                    .format(byte_order, allowed_values))
            self._byte_order = byte_order
        else:
            self._byte_order = allowed_values[int(byte_order) if six.PY3 else long(byte_order)]

    @property
    def compression(self):
        """Gets the compression of this TiffOptionsDTO.

        Compression level

        :return: The compression of this TiffOptionsDTO.
        :rtype: str
        """
        return self._compression

    @compression.setter
    def compression(self, compression):
        """Sets the compression of this TiffOptionsDTO.

        Compression level

        :param compression: The compression of this TiffOptionsDTO.
        :type: str
        """
        if compression is None:
            raise ValueError("Invalid value for `compression`, must not be `None`")
        allowed_values = ["None", "CcittRle", "CcittFax3", "CcittFax4", "Lzw", "Ojpeg", "Jpeg", "AdobeDeflate", "Next", "CcittRleW", "Packbits", "Thunderscan", "It8Ctpad", "It8Lw", "It8Mp", "It8Bl", "PixarFilm", "PixarLog", "Deflate", "Dcs", "Jbig", "Sgilog", "Sgilog24", "Jp2000"]
        if not compression.isdigit():
            if compression not in allowed_values:
                raise ValueError(
                    "Invalid value for `compression` ({0}), must be one of {1}"
                    .format(compression, allowed_values))
            self._compression = compression
        else:
            self._compression = allowed_values[int(compression) if six.PY3 else long(compression)]

    @property
    def expected_format(self):
        """Gets the expected_format of this TiffOptionsDTO.

        Expected TIFF sub-format

        :return: The expected_format of this TiffOptionsDTO.
        :rtype: str
        """
        return self._expected_format

    @expected_format.setter
    def expected_format(self, expected_format):
        """Sets the expected_format of this TiffOptionsDTO.

        Expected TIFF sub-format

        :param expected_format: The expected_format of this TiffOptionsDTO.
        :type: str
        """
        if expected_format is None:
            raise ValueError("Invalid value for `expected_format`, must not be `None`")
        allowed_values = ["Default", "TiffLzwBw", "TiffLzwRgb", "TiffLzwRgba", "TiffLzwCmyk", "TiffCcittFax3", "TiffCcittFax4", "TiffDeflateBw", "TiffDeflateRgb", "TiffDeflateRgba", "TiffCcitRle", "TiffJpegRgb", "TiffJpegYCbCr", "TiffNoCompressionBw", "TiffNoCompressionRgb", "TiffNoCompressionRgba"]
        if not expected_format.isdigit():
            if expected_format not in allowed_values:
                raise ValueError(
                    "Invalid value for `expected_format` ({0}), must be one of {1}"
                    .format(expected_format, allowed_values))
            self._expected_format = expected_format
        else:
            self._expected_format = allowed_values[int(expected_format) if six.PY3 else long(expected_format)]

    @property
    def bits_per_sample(self):
        """Gets the bits_per_sample of this TiffOptionsDTO.

        Bits per pixel

        :return: The bits_per_sample of this TiffOptionsDTO.
        :rtype: list[int]
        """
        return self._bits_per_sample

    @bits_per_sample.setter
    def bits_per_sample(self, bits_per_sample):
        """Sets the bits_per_sample of this TiffOptionsDTO.

        Bits per pixel

        :param bits_per_sample: The bits_per_sample of this TiffOptionsDTO.
        :type: list[int]
        """
        self._bits_per_sample = bits_per_sample

    @property
    def photometric(self):
        """Gets the photometric of this TiffOptionsDTO.

        Photometric options

        :return: The photometric of this TiffOptionsDTO.
        :rtype: str
        """
        return self._photometric

    @photometric.setter
    def photometric(self, photometric):
        """Sets the photometric of this TiffOptionsDTO.

        Photometric options

        :param photometric: The photometric of this TiffOptionsDTO.
        :type: str
        """
        if photometric is None:
            raise ValueError("Invalid value for `photometric`, must not be `None`")
        allowed_values = ["MinIsWhite", "MinIsBlack", "Rgb", "Palette", "Mask", "Separated", "Ycbcr", "Cielab", "Icclab", "Itulab", "Logl", "Logluv"]
        if not photometric.isdigit():
            if photometric not in allowed_values:
                raise ValueError(
                    "Invalid value for `photometric` ({0}), must be one of {1}"
                    .format(photometric, allowed_values))
            self._photometric = photometric
        else:
            self._photometric = allowed_values[int(photometric) if six.PY3 else long(photometric)]

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TiffOptionsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
