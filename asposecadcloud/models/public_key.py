#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="PublicKey.py">
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

from asposecadcloud.models.asn_encoded_data import AsnEncodedData
from asposecadcloud.models.asymmetric_algorithm import AsymmetricAlgorithm
from asposecadcloud.models.oid import Oid


class PublicKey(object):
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
        'encoded_key_value': 'AsnEncodedData',
        'encoded_parameters': 'AsnEncodedData',
        'key': 'AsymmetricAlgorithm',
        'oid': 'Oid'
    }

    attribute_map = {
        'encoded_key_value': 'EncodedKeyValue',
        'encoded_parameters': 'EncodedParameters',
        'key': 'Key',
        'oid': 'Oid'
    }

    def __init__(self, encoded_key_value=None, encoded_parameters=None, key=None, oid=None):
        """PublicKey - a model defined in Swagger"""
        super(PublicKey, self).__init__()

        self._encoded_key_value = None
        self._encoded_parameters = None
        self._key = None
        self._oid = None

        if encoded_key_value is not None:
            self.encoded_key_value = encoded_key_value
        if encoded_parameters is not None:
            self.encoded_parameters = encoded_parameters
        if key is not None:
            self.key = key
        if oid is not None:
            self.oid = oid

    @property
    def encoded_key_value(self):
        """Gets the encoded_key_value of this PublicKey.


        :return: The encoded_key_value of this PublicKey.
        :rtype: AsnEncodedData
        """
        return self._encoded_key_value

    @encoded_key_value.setter
    def encoded_key_value(self, encoded_key_value):
        """Sets the encoded_key_value of this PublicKey.


        :param encoded_key_value: The encoded_key_value of this PublicKey.
        :type: AsnEncodedData
        """
        self._encoded_key_value = encoded_key_value

    @property
    def encoded_parameters(self):
        """Gets the encoded_parameters of this PublicKey.


        :return: The encoded_parameters of this PublicKey.
        :rtype: AsnEncodedData
        """
        return self._encoded_parameters

    @encoded_parameters.setter
    def encoded_parameters(self, encoded_parameters):
        """Sets the encoded_parameters of this PublicKey.


        :param encoded_parameters: The encoded_parameters of this PublicKey.
        :type: AsnEncodedData
        """
        self._encoded_parameters = encoded_parameters

    @property
    def key(self):
        """Gets the key of this PublicKey.


        :return: The key of this PublicKey.
        :rtype: AsymmetricAlgorithm
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this PublicKey.


        :param key: The key of this PublicKey.
        :type: AsymmetricAlgorithm
        """
        self._key = key

    @property
    def oid(self):
        """Gets the oid of this PublicKey.


        :return: The oid of this PublicKey.
        :rtype: Oid
        """
        return self._oid

    @oid.setter
    def oid(self, oid):
        """Sets the oid of this PublicKey.


        :param oid: The oid of this PublicKey.
        :type: Oid
        """
        self._oid = oid

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
        if not isinstance(other, PublicKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
