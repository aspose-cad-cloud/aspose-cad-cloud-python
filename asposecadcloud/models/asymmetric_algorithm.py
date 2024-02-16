#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="AsymmetricAlgorithm.py">
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

from asposecadcloud.models.key_sizes import KeySizes


class AsymmetricAlgorithm(object):
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
        'key_size': 'int',
        'legal_key_sizes': 'list[KeySizes]',
        'signature_algorithm': 'str',
        'key_exchange_algorithm': 'str'
    }

    attribute_map = {
        'key_size': 'KeySize',
        'legal_key_sizes': 'LegalKeySizes',
        'signature_algorithm': 'SignatureAlgorithm',
        'key_exchange_algorithm': 'KeyExchangeAlgorithm'
    }

    def __init__(self, key_size=None, legal_key_sizes=None, signature_algorithm=None, key_exchange_algorithm=None):
        """AsymmetricAlgorithm - a model defined in Swagger"""
        super(AsymmetricAlgorithm, self).__init__()

        self._key_size = None
        self._legal_key_sizes = None
        self._signature_algorithm = None
        self._key_exchange_algorithm = None

        if key_size is not None:
            self.key_size = key_size
        if legal_key_sizes is not None:
            self.legal_key_sizes = legal_key_sizes
        if signature_algorithm is not None:
            self.signature_algorithm = signature_algorithm
        if key_exchange_algorithm is not None:
            self.key_exchange_algorithm = key_exchange_algorithm

    @property
    def key_size(self):
        """Gets the key_size of this AsymmetricAlgorithm.


        :return: The key_size of this AsymmetricAlgorithm.
        :rtype: int
        """
        return self._key_size

    @key_size.setter
    def key_size(self, key_size):
        """Sets the key_size of this AsymmetricAlgorithm.


        :param key_size: The key_size of this AsymmetricAlgorithm.
        :type: int
        """
        if key_size is None:
            raise ValueError("Invalid value for `key_size`, must not be `None`")
        self._key_size = key_size

    @property
    def legal_key_sizes(self):
        """Gets the legal_key_sizes of this AsymmetricAlgorithm.


        :return: The legal_key_sizes of this AsymmetricAlgorithm.
        :rtype: list[KeySizes]
        """
        return self._legal_key_sizes

    @legal_key_sizes.setter
    def legal_key_sizes(self, legal_key_sizes):
        """Sets the legal_key_sizes of this AsymmetricAlgorithm.


        :param legal_key_sizes: The legal_key_sizes of this AsymmetricAlgorithm.
        :type: list[KeySizes]
        """
        self._legal_key_sizes = legal_key_sizes

    @property
    def signature_algorithm(self):
        """Gets the signature_algorithm of this AsymmetricAlgorithm.


        :return: The signature_algorithm of this AsymmetricAlgorithm.
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        """Sets the signature_algorithm of this AsymmetricAlgorithm.


        :param signature_algorithm: The signature_algorithm of this AsymmetricAlgorithm.
        :type: str
        """
        self._signature_algorithm = signature_algorithm

    @property
    def key_exchange_algorithm(self):
        """Gets the key_exchange_algorithm of this AsymmetricAlgorithm.


        :return: The key_exchange_algorithm of this AsymmetricAlgorithm.
        :rtype: str
        """
        return self._key_exchange_algorithm

    @key_exchange_algorithm.setter
    def key_exchange_algorithm(self, key_exchange_algorithm):
        """Sets the key_exchange_algorithm of this AsymmetricAlgorithm.


        :param key_exchange_algorithm: The key_exchange_algorithm of this AsymmetricAlgorithm.
        :type: str
        """
        self._key_exchange_algorithm = key_exchange_algorithm

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
        if not isinstance(other, AsymmetricAlgorithm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
