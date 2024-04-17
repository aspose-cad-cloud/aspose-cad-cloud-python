#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="PngOptionsDTO.py">
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


class PngOptionsDTO(DrawingOptionsBaseDTO):
    """Export options for PNG format
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'color_type': 'str',
        'progressive': 'bool',
        'filter_type': 'str',
        'compression_level': 'int',
        'bit_depth': 'int'
    }

    attribute_map = {
        'color_type': 'ColorType',
        'progressive': 'Progressive',
        'filter_type': 'FilterType',
        'compression_level': 'CompressionLevel',
        'bit_depth': 'BitDepth'
    }

    def __init__(self, color_type=None, progressive=None, filter_type=None, compression_level=None, bit_depth=None):
        """PngOptionsDTO - a model defined in Swagger"""
        super(PngOptionsDTO, self).__init__()

        self._color_type = None
        self._progressive = None
        self._filter_type = None
        self._compression_level = None
        self._bit_depth = None

        if color_type is not None:
            self.color_type = color_type
        if progressive is not None:
            self.progressive = progressive
        if filter_type is not None:
            self.filter_type = filter_type
        if compression_level is not None:
            self.compression_level = compression_level
        if bit_depth is not None:
            self.bit_depth = bit_depth

    @property
    def color_type(self):
        """Gets the color_type of this PngOptionsDTO.

        Color type

        :return: The color_type of this PngOptionsDTO.
        :rtype: str
        """
        return self._color_type

    @color_type.setter
    def color_type(self, color_type):
        """Sets the color_type of this PngOptionsDTO.

        Color type

        :param color_type: The color_type of this PngOptionsDTO.
        :type: str
        """
        if color_type is None:
            raise ValueError("Invalid value for `color_type`, must not be `None`")
        allowed_values = ["Grayscale", "Truecolor", "IndexedColor", "GrayscaleWithAlpha", "TruecolorWithAlpha"]
        if not color_type.isdigit():
            if color_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `color_type` ({0}), must be one of {1}"
                    .format(color_type, allowed_values))
            self._color_type = color_type
        else:
            self._color_type = allowed_values[int(color_type) if six.PY3 else long(color_type)]

    @property
    def progressive(self):
        """Gets the progressive of this PngOptionsDTO.

        Determines whether 'progressive' method is used

        :return: The progressive of this PngOptionsDTO.
        :rtype: bool
        """
        return self._progressive

    @progressive.setter
    def progressive(self, progressive):
        """Sets the progressive of this PngOptionsDTO.

        Determines whether 'progressive' method is used

        :param progressive: The progressive of this PngOptionsDTO.
        :type: bool
        """
        if progressive is None:
            raise ValueError("Invalid value for `progressive`, must not be `None`")
        self._progressive = progressive

    @property
    def filter_type(self):
        """Gets the filter_type of this PngOptionsDTO.

        Filter type

        :return: The filter_type of this PngOptionsDTO.
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """Sets the filter_type of this PngOptionsDTO.

        Filter type

        :param filter_type: The filter_type of this PngOptionsDTO.
        :type: str
        """
        if filter_type is None:
            raise ValueError("Invalid value for `filter_type`, must not be `None`")
        allowed_values = ["None", "Sub", "Up", "Avg", "Paeth", "Adaptive"]
        if not filter_type.isdigit():
            if filter_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `filter_type` ({0}), must be one of {1}"
                    .format(filter_type, allowed_values))
            self._filter_type = filter_type
        else:
            self._filter_type = allowed_values[int(filter_type) if six.PY3 else long(filter_type)]

    @property
    def compression_level(self):
        """Gets the compression_level of this PngOptionsDTO.

        Compression level

        :return: The compression_level of this PngOptionsDTO.
        :rtype: int
        """
        return self._compression_level

    @compression_level.setter
    def compression_level(self, compression_level):
        """Sets the compression_level of this PngOptionsDTO.

        Compression level

        :param compression_level: The compression_level of this PngOptionsDTO.
        :type: int
        """
        if compression_level is None:
            raise ValueError("Invalid value for `compression_level`, must not be `None`")
        self._compression_level = compression_level

    @property
    def bit_depth(self):
        """Gets the bit_depth of this PngOptionsDTO.

        Bits depth

        :return: The bit_depth of this PngOptionsDTO.
        :rtype: int
        """
        return self._bit_depth

    @bit_depth.setter
    def bit_depth(self, bit_depth):
        """Sets the bit_depth of this PngOptionsDTO.

        Bits depth

        :param bit_depth: The bit_depth of this PngOptionsDTO.
        :type: int
        """
        if bit_depth is None:
            raise ValueError("Invalid value for `bit_depth`, must not be `None`")
        self._bit_depth = bit_depth

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
        if not isinstance(other, PngOptionsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
