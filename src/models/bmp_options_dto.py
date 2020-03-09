# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="BmpOptionsDTO.py">
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
import pprint
import re  # noqa: F401

import six


class BmpOptionsDTO(object):
    """Export options for BMP format
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'bits_per_pixel': 'int',
        'compression': 'str'
    }

    attribute_map = {
        'bits_per_pixel': 'BitsPerPixel',
        'compression': 'Compression'
    }

    def __init__(self, bits_per_pixel=None, compression=None):  # noqa: E501
        """BmpOptionsDTO - a model defined in Swagger"""  # noqa: E501

        self._bits_per_pixel = None
        self._compression = None
        self.discriminator = None

        if bits_per_pixel is not None:
            self.bits_per_pixel = bits_per_pixel
        if compression is not None:
            self.compression = compression

    @property
    def bits_per_pixel(self):
        """Gets the bits_per_pixel of this BmpOptionsDTO.  # noqa: E501

        Bits per pixel  # noqa: E501

        :return: The bits_per_pixel of this BmpOptionsDTO.  # noqa: E501
        :rtype: int
        """
        return self._bits_per_pixel

    @bits_per_pixel.setter
    def bits_per_pixel(self, bits_per_pixel):
        """Sets the bits_per_pixel of this BmpOptionsDTO.

        Bits per pixel  # noqa: E501

        :param bits_per_pixel: The bits_per_pixel of this BmpOptionsDTO.  # noqa: E501
        :type: int
        """
        if bits_per_pixel is None:
            raise ValueError("Invalid value for `bits_per_pixel`, must not be `None`")  # noqa: E501
        self._bits_per_pixel = bits_per_pixel
    @property
    def compression(self):
        """Gets the compression of this BmpOptionsDTO.  # noqa: E501

        Compression type  # noqa: E501

        :return: The compression of this BmpOptionsDTO.  # noqa: E501
        :rtype: str
        """
        return self._compression

    @compression.setter
    def compression(self, compression):
        """Sets the compression of this BmpOptionsDTO.

        Compression type  # noqa: E501

        :param compression: The compression of this BmpOptionsDTO.  # noqa: E501
        :type: str
        """
        if compression is None:
            raise ValueError("Invalid value for `compression`, must not be `None`")  # noqa: E501
        allowed_values = ["Rgb", "Rle8", "Rle4", "Bitfields", "Jpeg", "Png", "AlphaBitfields"]  # noqa: E501
        if not compression.isdigit():	
            if compression not in allowed_values:
                raise ValueError(
                    "Invalid value for `compression` ({0}), must be one of {1}"  # noqa: E501
                    .format(compression, allowed_values))
            self._compression = compression
        else:
            self._compression = allowed_values[int(compression) if six.PY3 else long(compression)]
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
        if not isinstance(other, BmpOptionsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
