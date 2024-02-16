#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="AsnEncodedData.py">
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

from asposecadcloud.models.oid import Oid


class AsnEncodedData(object):
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
        'oid': 'Oid',
        'raw_data': 'str'
    }

    attribute_map = {
        'oid': 'Oid',
        'raw_data': 'RawData'
    }

    discriminator_value_class_map = {
        'X500DistinguishedName': 'X500DistinguishedName'
    }

    def __init__(self, oid=None, raw_data=None):
        """AsnEncodedData - a model defined in Swagger"""
        super(AsnEncodedData, self).__init__()

        self._oid = None
        self._raw_data = None

        if oid is not None:
            self.oid = oid
        if raw_data is not None:
            self.raw_data = raw_data

    @property
    def oid(self):
        """Gets the oid of this AsnEncodedData.


        :return: The oid of this AsnEncodedData.
        :rtype: Oid
        """
        return self._oid

    @oid.setter
    def oid(self, oid):
        """Sets the oid of this AsnEncodedData.


        :param oid: The oid of this AsnEncodedData.
        :type: Oid
        """
        self._oid = oid

    @property
    def raw_data(self):
        """Gets the raw_data of this AsnEncodedData.


        :return: The raw_data of this AsnEncodedData.
        :rtype: str
        """
        return self._raw_data

    @raw_data.setter
    def raw_data(self, raw_data):
        """Sets the raw_data of this AsnEncodedData.


        :param raw_data: The raw_data of this AsnEncodedData.
        :type: str
        """
        if raw_data is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', raw_data):
            raise ValueError("Invalid value for `raw_data`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")
        self._raw_data = raw_data

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data.get(self.discriminator)
        return self.discriminator_value_class_map.get(discriminator_value.lower()) if discriminator_value else None

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
        if not isinstance(other, AsnEncodedData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
