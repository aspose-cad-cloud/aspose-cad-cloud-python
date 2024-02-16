#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="ResolutionSetting.py">
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


class ResolutionSetting(object):
    """
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'horizontal_resolution': 'float',
        'vertical_resolution': 'float'
    }

    attribute_map = {
        'horizontal_resolution': 'HorizontalResolution',
        'vertical_resolution': 'VerticalResolution'
    }

    def __init__(self, horizontal_resolution=None, vertical_resolution=None):
        """ResolutionSetting - a model defined in Swagger"""
        super(ResolutionSetting, self).__init__()

        self._horizontal_resolution = None
        self._vertical_resolution = None

        if horizontal_resolution is not None:
            self.horizontal_resolution = horizontal_resolution
        if vertical_resolution is not None:
            self.vertical_resolution = vertical_resolution

    @property
    def horizontal_resolution(self):
        """Gets the horizontal_resolution of this ResolutionSetting.


        :return: The horizontal_resolution of this ResolutionSetting.
        :rtype: float
        """
        return self._horizontal_resolution

    @horizontal_resolution.setter
    def horizontal_resolution(self, horizontal_resolution):
        """Sets the horizontal_resolution of this ResolutionSetting.


        :param horizontal_resolution: The horizontal_resolution of this ResolutionSetting.
        :type: float
        """
        if horizontal_resolution is None:
            raise ValueError("Invalid value for `horizontal_resolution`, must not be `None`")
        self._horizontal_resolution = horizontal_resolution

    @property
    def vertical_resolution(self):
        """Gets the vertical_resolution of this ResolutionSetting.


        :return: The vertical_resolution of this ResolutionSetting.
        :rtype: float
        """
        return self._vertical_resolution

    @vertical_resolution.setter
    def vertical_resolution(self, vertical_resolution):
        """Sets the vertical_resolution of this ResolutionSetting.


        :param vertical_resolution: The vertical_resolution of this ResolutionSetting.
        :type: float
        """
        if vertical_resolution is None:
            raise ValueError("Invalid value for `vertical_resolution`, must not be `None`")
        self._vertical_resolution = vertical_resolution

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
        if not isinstance(other, ResolutionSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
