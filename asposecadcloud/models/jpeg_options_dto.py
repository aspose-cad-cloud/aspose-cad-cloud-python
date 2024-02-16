#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="JpegOptionsDTO.py">
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
from asposecadcloud.models.rd_optimizer_settings import RdOptimizerSettings
from asposecadcloud.models.resolution_setting import ResolutionSetting


class JpegOptionsDTO(DrawingOptionsBaseDTO):
    """Export options for JPEG format
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'comment': 'str',
        'compression_type': 'str',
        'color_type': 'str',
        'quality': 'int',
        'rd_opt_settings': 'RdOptimizerSettings'
    }

    attribute_map = {
        'comment': 'Comment',
        'compression_type': 'CompressionType',
        'color_type': 'ColorType',
        'quality': 'Quality',
        'rd_opt_settings': 'RdOptSettings'
    }

    def __init__(self, comment=None, compression_type=None, color_type=None, quality=None, rd_opt_settings=None):
        """JpegOptionsDTO - a model defined in Swagger"""
        super(JpegOptionsDTO, self).__init__()

        self._comment = None
        self._compression_type = None
        self._color_type = None
        self._quality = None
        self._rd_opt_settings = None

        if comment is not None:
            self.comment = comment
        if compression_type is not None:
            self.compression_type = compression_type
        if color_type is not None:
            self.color_type = color_type
        if quality is not None:
            self.quality = quality
        if rd_opt_settings is not None:
            self.rd_opt_settings = rd_opt_settings

    @property
    def comment(self):
        """Gets the comment of this JpegOptionsDTO.

        Comment to Resulting file

        :return: The comment of this JpegOptionsDTO.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this JpegOptionsDTO.

        Comment to Resulting file

        :param comment: The comment of this JpegOptionsDTO.
        :type: str
        """
        self._comment = comment

    @property
    def compression_type(self):
        """Gets the compression_type of this JpegOptionsDTO.

        Compression type

        :return: The compression_type of this JpegOptionsDTO.
        :rtype: str
        """
        return self._compression_type

    @compression_type.setter
    def compression_type(self, compression_type):
        """Sets the compression_type of this JpegOptionsDTO.

        Compression type

        :param compression_type: The compression_type of this JpegOptionsDTO.
        :type: str
        """
        if compression_type is None:
            raise ValueError("Invalid value for `compression_type`, must not be `None`")
        allowed_values = ["Baseline", "Progressive", "Lossless", "JpegLs"]
        if not compression_type.isdigit():
            if compression_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `compression_type` ({0}), must be one of {1}"
                    .format(compression_type, allowed_values))
            self._compression_type = compression_type
        else:
            self._compression_type = allowed_values[int(compression_type) if six.PY3 else long(compression_type)]

    @property
    def color_type(self):
        """Gets the color_type of this JpegOptionsDTO.

        Color type

        :return: The color_type of this JpegOptionsDTO.
        :rtype: str
        """
        return self._color_type

    @color_type.setter
    def color_type(self, color_type):
        """Sets the color_type of this JpegOptionsDTO.

        Color type

        :param color_type: The color_type of this JpegOptionsDTO.
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
    def quality(self):
        """Gets the quality of this JpegOptionsDTO.

        Quality level

        :return: The quality of this JpegOptionsDTO.
        :rtype: int
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """Sets the quality of this JpegOptionsDTO.

        Quality level

        :param quality: The quality of this JpegOptionsDTO.
        :type: int
        """
        if quality is None:
            raise ValueError("Invalid value for `quality`, must not be `None`")
        self._quality = quality

    @property
    def rd_opt_settings(self):
        """Gets the rd_opt_settings of this JpegOptionsDTO.

        Optimizer settings

        :return: The rd_opt_settings of this JpegOptionsDTO.
        :rtype: RdOptimizerSettings
        """
        return self._rd_opt_settings

    @rd_opt_settings.setter
    def rd_opt_settings(self, rd_opt_settings):
        """Sets the rd_opt_settings of this JpegOptionsDTO.

        Optimizer settings

        :param rd_opt_settings: The rd_opt_settings of this JpegOptionsDTO.
        :type: RdOptimizerSettings
        """
        self._rd_opt_settings = rd_opt_settings

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
        if not isinstance(other, JpegOptionsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
