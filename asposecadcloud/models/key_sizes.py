#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="KeySizes.py">
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


class KeySizes(object):
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
        'min_size': 'int',
        'max_size': 'int',
        'skip_size': 'int'
    }

    attribute_map = {
        'min_size': 'MinSize',
        'max_size': 'MaxSize',
        'skip_size': 'SkipSize'
    }

    def __init__(self, min_size=None, max_size=None, skip_size=None):
        """KeySizes - a model defined in Swagger"""
        super(KeySizes, self).__init__()

        self._min_size = None
        self._max_size = None
        self._skip_size = None

        if min_size is not None:
            self.min_size = min_size
        if max_size is not None:
            self.max_size = max_size
        if skip_size is not None:
            self.skip_size = skip_size

    @property
    def min_size(self):
        """Gets the min_size of this KeySizes.


        :return: The min_size of this KeySizes.
        :rtype: int
        """
        return self._min_size

    @min_size.setter
    def min_size(self, min_size):
        """Sets the min_size of this KeySizes.


        :param min_size: The min_size of this KeySizes.
        :type: int
        """
        if min_size is None:
            raise ValueError("Invalid value for `min_size`, must not be `None`")
        self._min_size = min_size

    @property
    def max_size(self):
        """Gets the max_size of this KeySizes.


        :return: The max_size of this KeySizes.
        :rtype: int
        """
        return self._max_size

    @max_size.setter
    def max_size(self, max_size):
        """Sets the max_size of this KeySizes.


        :param max_size: The max_size of this KeySizes.
        :type: int
        """
        if max_size is None:
            raise ValueError("Invalid value for `max_size`, must not be `None`")
        self._max_size = max_size

    @property
    def skip_size(self):
        """Gets the skip_size of this KeySizes.


        :return: The skip_size of this KeySizes.
        :rtype: int
        """
        return self._skip_size

    @skip_size.setter
    def skip_size(self, skip_size):
        """Sets the skip_size of this KeySizes.


        :param skip_size: The skip_size of this KeySizes.
        :type: int
        """
        if skip_size is None:
            raise ValueError("Invalid value for `skip_size`, must not be `None`")
        self._skip_size = skip_size

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
        if not isinstance(other, KeySizes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
