#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="Jpeg2000OptionsDTO.py">
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


class Jpeg2000OptionsDTO(DrawingOptionsBaseDTO):
    """Export options for JPEG2000 format
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'comments': 'list[str]',
        'codec': 'str'
    }

    attribute_map = {
        'comments': 'Comments',
        'codec': 'Codec'
    }

    def __init__(self, comments=None, codec=None):
        """Jpeg2000OptionsDTO - a model defined in Swagger"""
        super(Jpeg2000OptionsDTO, self).__init__()

        self._comments = None
        self._codec = None

        if comments is not None:
            self.comments = comments
        if codec is not None:
            self.codec = codec

    @property
    def comments(self):
        """Gets the comments of this Jpeg2000OptionsDTO.


        :return: The comments of this Jpeg2000OptionsDTO.
        :rtype: list[str]
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this Jpeg2000OptionsDTO.


        :param comments: The comments of this Jpeg2000OptionsDTO.
        :type: list[str]
        """
        self._comments = comments

    @property
    def codec(self):
        """Gets the codec of this Jpeg2000OptionsDTO.


        :return: The codec of this Jpeg2000OptionsDTO.
        :rtype: str
        """
        return self._codec

    @codec.setter
    def codec(self, codec):
        """Sets the codec of this Jpeg2000OptionsDTO.


        :param codec: The codec of this Jpeg2000OptionsDTO.
        :type: str
        """
        if codec is None:
            raise ValueError("Invalid value for `codec`, must not be `None`")
        allowed_values = ["J2K", "Jp2", "Jpt"]
        if not codec.isdigit():
            if codec not in allowed_values:
                raise ValueError(
                    "Invalid value for `codec` ({0}), must be one of {1}"
                    .format(codec, allowed_values))
            self._codec = codec
        else:
            self._codec = allowed_values[int(codec) if six.PY3 else long(codec)]

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
        if not isinstance(other, Jpeg2000OptionsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
