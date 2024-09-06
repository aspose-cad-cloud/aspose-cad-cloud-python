#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="ColorDTO.py">
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


class ColorDTO(object):
    """RGB color values
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'r': 'int',
        'g': 'int',
        'b': 'int'
    }

    attribute_map = {
        'r': 'R',
        'g': 'G',
        'b': 'B'
    }

    def __init__(self, r=None, g=None, b=None):
        """ColorDTO - a model defined in Swagger"""
        super(ColorDTO, self).__init__()

        self._r = None
        self._g = None
        self._b = None

        if r is not None:
            self.r = r
        if g is not None:
            self.g = g
        if b is not None:
            self.b = b

    @property
    def r(self):
        """Gets the r of this ColorDTO.

        Red light(0-255).

        :return: The r of this ColorDTO.
        :rtype: int
        """
        return self._r

    @r.setter
    def r(self, r):
        """Sets the r of this ColorDTO.

        Red light(0-255).

        :param r: The r of this ColorDTO.
        :type: int
        """
        if r is None:
            raise ValueError("Invalid value for `r`, must not be `None`")
        self._r = r

    @property
    def g(self):
        """Gets the g of this ColorDTO.

        Green light(0-255).

        :return: The g of this ColorDTO.
        :rtype: int
        """
        return self._g

    @g.setter
    def g(self, g):
        """Sets the g of this ColorDTO.

        Green light(0-255).

        :param g: The g of this ColorDTO.
        :type: int
        """
        if g is None:
            raise ValueError("Invalid value for `g`, must not be `None`")
        self._g = g

    @property
    def b(self):
        """Gets the b of this ColorDTO.

        Blue light(0-255).

        :return: The b of this ColorDTO.
        :rtype: int
        """
        return self._b

    @b.setter
    def b(self, b):
        """Sets the b of this ColorDTO.

        Blue light(0-255).

        :param b: The b of this ColorDTO.
        :type: int
        """
        if b is None:
            raise ValueError("Invalid value for `b`, must not be `None`")
        self._b = b

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
        if not isinstance(other, ColorDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
