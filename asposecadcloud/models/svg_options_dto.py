#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="SvgOptionsDTO.py">
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


class SvgOptionsDTO(DrawingOptionsBaseDTO):
    """Export options for SVG format
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
        'text_as_shapes': 'bool'
    }

    attribute_map = {
        'color_type': 'ColorType',
        'text_as_shapes': 'TextAsShapes'
    }

    def __init__(self, color_type=None, text_as_shapes=None):
        """SvgOptionsDTO - a model defined in Swagger"""
        super(SvgOptionsDTO, self).__init__()

        self._color_type = None
        self._text_as_shapes = None

        if color_type is not None:
            self.color_type = color_type
        if text_as_shapes is not None:
            self.text_as_shapes = text_as_shapes

    @property
    def color_type(self):
        """Gets the color_type of this SvgOptionsDTO.

        Color type

        :return: The color_type of this SvgOptionsDTO.
        :rtype: str
        """
        return self._color_type

    @color_type.setter
    def color_type(self, color_type):
        """Sets the color_type of this SvgOptionsDTO.

        Color type

        :param color_type: The color_type of this SvgOptionsDTO.
        :type: str
        """
        if color_type is None:
            raise ValueError("Invalid value for `color_type`, must not be `None`")
        allowed_values = ["Grayscale", "YCbCr", "Cmyk", "Ycck", "Rgb"]
        if not color_type.isdigit():
            if color_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `color_type` ({0}), must be one of {1}"
                    .format(color_type, allowed_values))
            self._color_type = color_type
        else:
            self._color_type = allowed_values[int(color_type) if six.PY3 else long(color_type)]

    @property
    def text_as_shapes(self):
        """Gets the text_as_shapes of this SvgOptionsDTO.

        Render text as shapes

        :return: The text_as_shapes of this SvgOptionsDTO.
        :rtype: bool
        """
        return self._text_as_shapes

    @text_as_shapes.setter
    def text_as_shapes(self, text_as_shapes):
        """Sets the text_as_shapes of this SvgOptionsDTO.

        Render text as shapes

        :param text_as_shapes: The text_as_shapes of this SvgOptionsDTO.
        :type: bool
        """
        if text_as_shapes is None:
            raise ValueError("Invalid value for `text_as_shapes`, must not be `None`")
        self._text_as_shapes = text_as_shapes

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
        if not isinstance(other, SvgOptionsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
