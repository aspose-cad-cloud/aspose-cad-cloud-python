#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="PsdOptionsDTO.py">
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


class PsdOptionsDTO(DrawingOptionsBaseDTO):
    """Export options for PSD format
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'version': 'int',
        'compression_method': 'str',
        'color_mode': 'str',
        'channel_bits_count': 'int',
        'channels_count': 'int'
    }

    attribute_map = {
        'version': 'Version',
        'compression_method': 'CompressionMethod',
        'color_mode': 'ColorMode',
        'channel_bits_count': 'ChannelBitsCount',
        'channels_count': 'ChannelsCount'
    }

    def __init__(self, version=None, compression_method=None, color_mode=None, channel_bits_count=None, channels_count=None):
        """PsdOptionsDTO - a model defined in Swagger"""
        super(PsdOptionsDTO, self).__init__()

        self._version = None
        self._compression_method = None
        self._color_mode = None
        self._channel_bits_count = None
        self._channels_count = None

        if version is not None:
            self.version = version
        if compression_method is not None:
            self.compression_method = compression_method
        if color_mode is not None:
            self.color_mode = color_mode
        if channel_bits_count is not None:
            self.channel_bits_count = channel_bits_count
        if channels_count is not None:
            self.channels_count = channels_count

    @property
    def version(self):
        """Gets the version of this PsdOptionsDTO.

        PSD format version

        :return: The version of this PsdOptionsDTO.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PsdOptionsDTO.

        PSD format version

        :param version: The version of this PsdOptionsDTO.
        :type: int
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")
        self._version = version

    @property
    def compression_method(self):
        """Gets the compression_method of this PsdOptionsDTO.

        Compression method

        :return: The compression_method of this PsdOptionsDTO.
        :rtype: str
        """
        return self._compression_method

    @compression_method.setter
    def compression_method(self, compression_method):
        """Sets the compression_method of this PsdOptionsDTO.

        Compression method

        :param compression_method: The compression_method of this PsdOptionsDTO.
        :type: str
        """
        if compression_method is None:
            raise ValueError("Invalid value for `compression_method`, must not be `None`")
        allowed_values = ["Raw", "RLE", "ZipWithoutPrediction", "ZipWithPrediction"]
        if not compression_method.isdigit():
            if compression_method not in allowed_values:
                raise ValueError(
                    "Invalid value for `compression_method` ({0}), must be one of {1}"
                    .format(compression_method, allowed_values))
            self._compression_method = compression_method
        else:
            self._compression_method = allowed_values[int(compression_method) if six.PY3 else long(compression_method)]

    @property
    def color_mode(self):
        """Gets the color_mode of this PsdOptionsDTO.

        Color mode

        :return: The color_mode of this PsdOptionsDTO.
        :rtype: str
        """
        return self._color_mode

    @color_mode.setter
    def color_mode(self, color_mode):
        """Sets the color_mode of this PsdOptionsDTO.

        Color mode

        :param color_mode: The color_mode of this PsdOptionsDTO.
        :type: str
        """
        if color_mode is None:
            raise ValueError("Invalid value for `color_mode`, must not be `None`")
        allowed_values = ["Bitmap", "Grayscale", "Indexed", "Rgb", "Cmyk", "Multichannel", "Duotone", "Lab"]
        if not color_mode.isdigit():
            if color_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `color_mode` ({0}), must be one of {1}"
                    .format(color_mode, allowed_values))
            self._color_mode = color_mode
        else:
            self._color_mode = allowed_values[int(color_mode) if six.PY3 else long(color_mode)]

    @property
    def channel_bits_count(self):
        """Gets the channel_bits_count of this PsdOptionsDTO.

        Bits count per channel

        :return: The channel_bits_count of this PsdOptionsDTO.
        :rtype: int
        """
        return self._channel_bits_count

    @channel_bits_count.setter
    def channel_bits_count(self, channel_bits_count):
        """Sets the channel_bits_count of this PsdOptionsDTO.

        Bits count per channel

        :param channel_bits_count: The channel_bits_count of this PsdOptionsDTO.
        :type: int
        """
        if channel_bits_count is None:
            raise ValueError("Invalid value for `channel_bits_count`, must not be `None`")
        self._channel_bits_count = channel_bits_count

    @property
    def channels_count(self):
        """Gets the channels_count of this PsdOptionsDTO.

        Channels count

        :return: The channels_count of this PsdOptionsDTO.
        :rtype: int
        """
        return self._channels_count

    @channels_count.setter
    def channels_count(self, channels_count):
        """Sets the channels_count of this PsdOptionsDTO.

        Channels count

        :param channels_count: The channels_count of this PsdOptionsDTO.
        :type: int
        """
        if channels_count is None:
            raise ValueError("Invalid value for `channels_count`, must not be `None`")
        self._channels_count = channels_count

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
        if not isinstance(other, PsdOptionsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
