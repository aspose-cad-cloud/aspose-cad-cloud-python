#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="GraphicsOptions.py">
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


class GraphicsOptions(object):
    """Represents graphics options for embedded bitmap.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'text_rendering_hint': 'object',
        'smoothing_mode': 'object',
        'interpolation_mode': 'object'
    }

    attribute_map = {
        'text_rendering_hint': 'TextRenderingHint',
        'smoothing_mode': 'SmoothingMode',
        'interpolation_mode': 'InterpolationMode'
    }

    def __init__(self, text_rendering_hint=None, smoothing_mode=None, interpolation_mode=None):
        """GraphicsOptions - a model defined in Swagger"""
        super(GraphicsOptions, self).__init__()

        self._text_rendering_hint = None
        self._smoothing_mode = None
        self._interpolation_mode = None

        if text_rendering_hint is not None:
            self.text_rendering_hint = text_rendering_hint
        if smoothing_mode is not None:
            self.smoothing_mode = smoothing_mode
        if interpolation_mode is not None:
            self.interpolation_mode = interpolation_mode

    @property
    def text_rendering_hint(self):
        """Gets the text_rendering_hint of this GraphicsOptions.

        Gets or sets text rendering hint.

        :return: The text_rendering_hint of this GraphicsOptions.
        :rtype: object
        """
        return self._text_rendering_hint

    @text_rendering_hint.setter
    def text_rendering_hint(self, text_rendering_hint):
        """Sets the text_rendering_hint of this GraphicsOptions.

        Gets or sets text rendering hint.

        :param text_rendering_hint: The text_rendering_hint of this GraphicsOptions.
        :type: object
        """
        if text_rendering_hint is None:
            raise ValueError("Invalid value for `text_rendering_hint`, must not be `None`")
        self._text_rendering_hint = text_rendering_hint

    @property
    def smoothing_mode(self):
        """Gets the smoothing_mode of this GraphicsOptions.

        Gets or sets smoothing mode.

        :return: The smoothing_mode of this GraphicsOptions.
        :rtype: object
        """
        return self._smoothing_mode

    @smoothing_mode.setter
    def smoothing_mode(self, smoothing_mode):
        """Sets the smoothing_mode of this GraphicsOptions.

        Gets or sets smoothing mode.

        :param smoothing_mode: The smoothing_mode of this GraphicsOptions.
        :type: object
        """
        if smoothing_mode is None:
            raise ValueError("Invalid value for `smoothing_mode`, must not be `None`")
        self._smoothing_mode = smoothing_mode

    @property
    def interpolation_mode(self):
        """Gets the interpolation_mode of this GraphicsOptions.

        Gets or sets interpolation mode.

        :return: The interpolation_mode of this GraphicsOptions.
        :rtype: object
        """
        return self._interpolation_mode

    @interpolation_mode.setter
    def interpolation_mode(self, interpolation_mode):
        """Sets the interpolation_mode of this GraphicsOptions.

        Gets or sets interpolation mode.

        :param interpolation_mode: The interpolation_mode of this GraphicsOptions.
        :type: object
        """
        if interpolation_mode is None:
            raise ValueError("Invalid value for `interpolation_mode`, must not be `None`")
        self._interpolation_mode = interpolation_mode

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
        if not isinstance(other, GraphicsOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
