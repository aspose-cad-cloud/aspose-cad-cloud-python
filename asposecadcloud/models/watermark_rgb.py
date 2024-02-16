#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="WatermarkRGB.py">
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


class WatermarkRGB(object):
    """Watermark text with RGB values
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'watermarktext': 'str',
        'watermarkr': 'str',
        'watermarkg': 'str',
        'watermarkb': 'str'
    }

    attribute_map = {
        'watermarktext': 'Watermarktext',
        'watermarkr': 'Watermarkr',
        'watermarkg': 'Watermarkg',
        'watermarkb': 'Watermarkb'
    }

    def __init__(self, watermarktext='Default', watermarkr='0', watermarkg='0', watermarkb='0'):
        """WatermarkRGB - a model defined in Swagger"""
        super(WatermarkRGB, self).__init__()

        self._watermarktext = None
        self._watermarkr = None
        self._watermarkg = None
        self._watermarkb = None

        if watermarktext is not None:
            self.watermarktext = watermarktext
        if watermarkr is not None:
            self.watermarkr = watermarkr
        if watermarkg is not None:
            self.watermarkg = watermarkg
        if watermarkb is not None:
            self.watermarkb = watermarkb

    @property
    def watermarktext(self):
        """Gets the watermarktext of this WatermarkRGB.

        Watermark text.

        :return: The watermarktext of this WatermarkRGB.
        :rtype: str
        """
        return self._watermarktext

    @watermarktext.setter
    def watermarktext(self, watermarktext):
        """Sets the watermarktext of this WatermarkRGB.

        Watermark text.

        :param watermarktext: The watermarktext of this WatermarkRGB.
        :type: str
        """
        self._watermarktext = watermarktext

    @property
    def watermarkr(self):
        """Gets the watermarkr of this WatermarkRGB.

        Red light(0-255).

        :return: The watermarkr of this WatermarkRGB.
        :rtype: str
        """
        return self._watermarkr

    @watermarkr.setter
    def watermarkr(self, watermarkr):
        """Sets the watermarkr of this WatermarkRGB.

        Red light(0-255).

        :param watermarkr: The watermarkr of this WatermarkRGB.
        :type: str
        """
        self._watermarkr = watermarkr

    @property
    def watermarkg(self):
        """Gets the watermarkg of this WatermarkRGB.

        Green light(0-255).

        :return: The watermarkg of this WatermarkRGB.
        :rtype: str
        """
        return self._watermarkg

    @watermarkg.setter
    def watermarkg(self, watermarkg):
        """Sets the watermarkg of this WatermarkRGB.

        Green light(0-255).

        :param watermarkg: The watermarkg of this WatermarkRGB.
        :type: str
        """
        self._watermarkg = watermarkg

    @property
    def watermarkb(self):
        """Gets the watermarkb of this WatermarkRGB.

        Blue light(0-255).

        :return: The watermarkb of this WatermarkRGB.
        :rtype: str
        """
        return self._watermarkb

    @watermarkb.setter
    def watermarkb(self, watermarkb):
        """Sets the watermarkb of this WatermarkRGB.

        Blue light(0-255).

        :param watermarkb: The watermarkb of this WatermarkRGB.
        :type: str
        """
        self._watermarkb = watermarkb

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
        if not isinstance(other, WatermarkRGB):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
