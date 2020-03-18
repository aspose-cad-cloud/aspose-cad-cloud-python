#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="PenOptions.py">
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


class PenOptions(object):
    """Drawing pen options
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'start_cap': 'object',
        'end_cap': 'object'
    }

    attribute_map = {
        'start_cap': 'StartCap',
        'end_cap': 'EndCap'
    }

    def __init__(self, start_cap=None, end_cap=None):
        """PenOptions - a model defined in Swagger"""
        super(PenOptions, self).__init__()

        self._start_cap = None
        self._end_cap = None

        if start_cap is not None:
            self.start_cap = start_cap
        if end_cap is not None:
            self.end_cap = end_cap

    @property
    def start_cap(self):
        """Gets the start_cap of this PenOptions.

        Gets or sets the start cap.

        :return: The start_cap of this PenOptions.
        :rtype: object
        """
        return self._start_cap

    @start_cap.setter
    def start_cap(self, start_cap):
        """Sets the start_cap of this PenOptions.

        Gets or sets the start cap.

        :param start_cap: The start_cap of this PenOptions.
        :type: object
        """
        if start_cap is None:
            raise ValueError("Invalid value for `start_cap`, must not be `None`")
        self._start_cap = start_cap

    @property
    def end_cap(self):
        """Gets the end_cap of this PenOptions.

        Gets or sets the end cap.

        :return: The end_cap of this PenOptions.
        :rtype: object
        """
        return self._end_cap

    @end_cap.setter
    def end_cap(self, end_cap):
        """Sets the end_cap of this PenOptions.

        Gets or sets the end cap.

        :param end_cap: The end_cap of this PenOptions.
        :type: object
        """
        if end_cap is None:
            raise ValueError("Invalid value for `end_cap`, must not be `None`")
        self._end_cap = end_cap

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
        if not isinstance(other, PenOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
