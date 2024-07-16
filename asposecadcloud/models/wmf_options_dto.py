#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="WmfOptionsDTO.py">
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


class WmfOptionsDTO(DrawingOptionsBaseDTO):
    """Export options for WMF format
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'rotation': 'str',
        'layers': 'list[str]',
        'resolution_settings': 'ResolutionSetting',
        'vector_rasterization_options': 'CadRasterizationOptionsDTO',
        'bits_per_pixel': 'int'
    }

    attribute_map = {
        'rotation': 'Rotation',
        'layers': 'Layers',
        'resolution_settings': 'ResolutionSettings',
        'vector_rasterization_options': 'VectorRasterizationOptions',
        'bits_per_pixel': 'BitsPerPixel'
    }

    def __init__(self, bits_per_pixel=None):
        """WmfOptionsDTO - a model defined in Swagger"""
        super(WmfOptionsDTO, self).__init__()

        self._bits_per_pixel = None

        if bits_per_pixel is not None:
            self.bits_per_pixel = bits_per_pixel

    @property
    def bits_per_pixel(self):
        """Gets the bits_per_pixel of this WmfOptionsDTO.

        Bits per pixel for Resulting file

        :return: The bits_per_pixel of this WmfOptionsDTO.
        :rtype: int
        """
        return self._bits_per_pixel

    @bits_per_pixel.setter
    def bits_per_pixel(self, bits_per_pixel):
        """Sets the bits_per_pixel of this WmfOptionsDTO.

        Bits per pixel for Resulting file

        :param bits_per_pixel: The bits_per_pixel of this WmfOptionsDTO.
        :type: int
        """
        if bits_per_pixel is None:
            raise ValueError("Invalid value for `bits_per_pixel`, must not be `None`")
        self._bits_per_pixel = bits_per_pixel

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
        if not isinstance(other, WmfOptionsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
