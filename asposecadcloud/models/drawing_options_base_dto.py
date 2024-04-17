#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="DrawingOptionsBaseDTO.py">
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
from asposecadcloud.models.resolution_setting import ResolutionSetting


class DrawingOptionsBaseDTO(object):
    """Image options base class
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
        'vector_rasterization_options': 'CadRasterizationOptionsDTO'
    }

    attribute_map = {
        'rotation': 'Rotation',
        'layers': 'Layers',
        'resolution_settings': 'ResolutionSettings',
        'vector_rasterization_options': 'VectorRasterizationOptions'
    }

    discriminator_value_class_map = {
        'BmpOptionsDTO': 'BmpOptionsDTO',
        'StpOptionsDTO': 'StpOptionsDTO',
        'GlbOptionsDTO': 'GlbOptionsDTO',
        'PsdOptionsDTO': 'PsdOptionsDTO',
        'GifOptionsDTO': 'GifOptionsDTO',
        'ThreeDSOptionsDTO': 'ThreeDSOptionsDTO',
        'WmfOptionsDTO': 'WmfOptionsDTO',
        'DxfOptionsDTO': 'DxfOptionsDTO',
        'PngOptionsDTO': 'PngOptionsDTO',
        'CgmOptionsDTO': 'CgmOptionsDTO',
        'JpegOptionsDTO': 'JpegOptionsDTO',
        'FbxOptionsDTO': 'FbxOptionsDTO',
        'SvgOptionsDTO': 'SvgOptionsDTO',
        'GltfOptionsDTO': 'GltfOptionsDTO',
        'U3dOptionsDTO': 'U3dOptionsDTO',
        'Jpeg2000OptionsDTO': 'Jpeg2000OptionsDTO',
        'PdfOptionsDTO': 'PdfOptionsDTO',
        'DwfOptionsDTO': 'DwfOptionsDTO',
        'ObjOptionsDTO': 'ObjOptionsDTO',
        'TiffOptionsDTO': 'TiffOptionsDTO'
    }

    def __init__(self, rotation=None, layers=None, resolution_settings=None, vector_rasterization_options=None):
        """DrawingOptionsBaseDTO - a model defined in Swagger"""
        super(DrawingOptionsBaseDTO, self).__init__()

        self._rotation = None
        self._layers = None
        self._resolution_settings = None
        self._vector_rasterization_options = None

        if rotation is not None:
            self.rotation = rotation
        if layers is not None:
            self.layers = layers
        if resolution_settings is not None:
            self.resolution_settings = resolution_settings
        if vector_rasterization_options is not None:
            self.vector_rasterization_options = vector_rasterization_options

    @property
    def rotation(self):
        """Gets the rotation of this DrawingOptionsBaseDTO.

        Resulting rotation operation

        :return: The rotation of this DrawingOptionsBaseDTO.
        :rtype: str
        """
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        """Sets the rotation of this DrawingOptionsBaseDTO.

        Resulting rotation operation

        :param rotation: The rotation of this DrawingOptionsBaseDTO.
        :type: str
        """
        if rotation is None:
            raise ValueError("Invalid value for `rotation`, must not be `None`")
        allowed_values = ["RotateNoneFlipNone", "Rotate90FlipNone", "Rotate180FlipNone", "Rotate270FlipNone", "RotateNoneFlipX", "Rotate90FlipX", "Rotate180FlipX", "Rotate270FlipX", "RotateNoneFlipY", "Rotate90FlipY", "Rotate180FlipY", "Rotate270FlipY", "RotateNoneFlipXY", "Rotate90FlipXY", "Rotate180FlipXY", "Rotate270FlipXY"]
        if not rotation.isdigit():
            if rotation not in allowed_values:
                raise ValueError(
                    "Invalid value for `rotation` ({0}), must be one of {1}"
                    .format(rotation, allowed_values))
            self._rotation = rotation
        else:
            self._rotation = allowed_values[int(rotation) if six.PY3 else long(rotation)]

    @property
    def layers(self):
        """Gets the layers of this DrawingOptionsBaseDTO.

        Layers to export

        :return: The layers of this DrawingOptionsBaseDTO.
        :rtype: list[str]
        """
        return self._layers

    @layers.setter
    def layers(self, layers):
        """Sets the layers of this DrawingOptionsBaseDTO.

        Layers to export

        :param layers: The layers of this DrawingOptionsBaseDTO.
        :type: list[str]
        """
        self._layers = layers

    @property
    def resolution_settings(self):
        """Gets the resolution_settings of this DrawingOptionsBaseDTO.

        DPI resolution settings

        :return: The resolution_settings of this DrawingOptionsBaseDTO.
        :rtype: ResolutionSetting
        """
        return self._resolution_settings

    @resolution_settings.setter
    def resolution_settings(self, resolution_settings):
        """Sets the resolution_settings of this DrawingOptionsBaseDTO.

        DPI resolution settings

        :param resolution_settings: The resolution_settings of this DrawingOptionsBaseDTO.
        :type: ResolutionSetting
        """
        self._resolution_settings = resolution_settings

    @property
    def vector_rasterization_options(self):
        """Gets the vector_rasterization_options of this DrawingOptionsBaseDTO.

        Raster options

        :return: The vector_rasterization_options of this DrawingOptionsBaseDTO.
        :rtype: CadRasterizationOptionsDTO
        """
        return self._vector_rasterization_options

    @vector_rasterization_options.setter
    def vector_rasterization_options(self, vector_rasterization_options):
        """Sets the vector_rasterization_options of this DrawingOptionsBaseDTO.

        Raster options

        :param vector_rasterization_options: The vector_rasterization_options of this DrawingOptionsBaseDTO.
        :type: CadRasterizationOptionsDTO
        """
        self._vector_rasterization_options = vector_rasterization_options

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data.get(self.discriminator)
        return self.discriminator_value_class_map.get(discriminator_value.lower()) if discriminator_value else None

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
        if not isinstance(other, DrawingOptionsBaseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
