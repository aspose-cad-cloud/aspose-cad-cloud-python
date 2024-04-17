#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="Color.py">
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


class Color(object):
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
        'r': 'int',
        'g': 'int',
        'b': 'int',
        'a': 'int',
        'is_known_color': 'bool',
        'is_empty': 'bool',
        'is_named_color': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'r': 'R',
        'g': 'G',
        'b': 'B',
        'a': 'A',
        'is_known_color': 'IsKnownColor',
        'is_empty': 'IsEmpty',
        'is_named_color': 'IsNamedColor',
        'name': 'Name'
    }

    def __init__(self, r=None, g=None, b=None, a=None, is_known_color=None, is_empty=None, is_named_color=None, name=None):
        """Color - a model defined in Swagger"""
        super(Color, self).__init__()

        self._r = None
        self._g = None
        self._b = None
        self._a = None
        self._is_known_color = None
        self._is_empty = None
        self._is_named_color = None
        self._name = None

        if r is not None:
            self.r = r
        if g is not None:
            self.g = g
        if b is not None:
            self.b = b
        if a is not None:
            self.a = a
        if is_known_color is not None:
            self.is_known_color = is_known_color
        if is_empty is not None:
            self.is_empty = is_empty
        if is_named_color is not None:
            self.is_named_color = is_named_color
        if name is not None:
            self.name = name

    @property
    def r(self):
        """Gets the r of this Color.


        :return: The r of this Color.
        :rtype: int
        """
        return self._r

    @r.setter
    def r(self, r):
        """Sets the r of this Color.


        :param r: The r of this Color.
        :type: int
        """
        if r is None:
            raise ValueError("Invalid value for `r`, must not be `None`")
        self._r = r

    @property
    def g(self):
        """Gets the g of this Color.


        :return: The g of this Color.
        :rtype: int
        """
        return self._g

    @g.setter
    def g(self, g):
        """Sets the g of this Color.


        :param g: The g of this Color.
        :type: int
        """
        if g is None:
            raise ValueError("Invalid value for `g`, must not be `None`")
        self._g = g

    @property
    def b(self):
        """Gets the b of this Color.


        :return: The b of this Color.
        :rtype: int
        """
        return self._b

    @b.setter
    def b(self, b):
        """Sets the b of this Color.


        :param b: The b of this Color.
        :type: int
        """
        if b is None:
            raise ValueError("Invalid value for `b`, must not be `None`")
        self._b = b

    @property
    def a(self):
        """Gets the a of this Color.


        :return: The a of this Color.
        :rtype: int
        """
        return self._a

    @a.setter
    def a(self, a):
        """Sets the a of this Color.


        :param a: The a of this Color.
        :type: int
        """
        if a is None:
            raise ValueError("Invalid value for `a`, must not be `None`")
        self._a = a

    @property
    def is_known_color(self):
        """Gets the is_known_color of this Color.


        :return: The is_known_color of this Color.
        :rtype: bool
        """
        return self._is_known_color

    @is_known_color.setter
    def is_known_color(self, is_known_color):
        """Sets the is_known_color of this Color.


        :param is_known_color: The is_known_color of this Color.
        :type: bool
        """
        if is_known_color is None:
            raise ValueError("Invalid value for `is_known_color`, must not be `None`")
        self._is_known_color = is_known_color

    @property
    def is_empty(self):
        """Gets the is_empty of this Color.


        :return: The is_empty of this Color.
        :rtype: bool
        """
        return self._is_empty

    @is_empty.setter
    def is_empty(self, is_empty):
        """Sets the is_empty of this Color.


        :param is_empty: The is_empty of this Color.
        :type: bool
        """
        if is_empty is None:
            raise ValueError("Invalid value for `is_empty`, must not be `None`")
        self._is_empty = is_empty

    @property
    def is_named_color(self):
        """Gets the is_named_color of this Color.


        :return: The is_named_color of this Color.
        :rtype: bool
        """
        return self._is_named_color

    @is_named_color.setter
    def is_named_color(self, is_named_color):
        """Sets the is_named_color of this Color.


        :param is_named_color: The is_named_color of this Color.
        :type: bool
        """
        if is_named_color is None:
            raise ValueError("Invalid value for `is_named_color`, must not be `None`")
        self._is_named_color = is_named_color

    @property
    def name(self):
        """Gets the name of this Color.


        :return: The name of this Color.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Color.


        :param name: The name of this Color.
        :type: str
        """
        self._name = name

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
        if not isinstance(other, Color):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
