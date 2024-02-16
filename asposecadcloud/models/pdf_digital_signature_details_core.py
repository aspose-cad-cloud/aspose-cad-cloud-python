#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="PdfDigitalSignatureDetailsCore.py">
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

from asposecadcloud.models.x509_certificate2 import X509Certificate2


class PdfDigitalSignatureDetailsCore(object):
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
        'certificate': 'X509Certificate2',
        'reason': 'str',
        'location': 'str',
        'signature_date': 'datetime',
        'hash_algorithm': 'str'
    }

    attribute_map = {
        'certificate': 'Certificate',
        'reason': 'Reason',
        'location': 'Location',
        'signature_date': 'SignatureDate',
        'hash_algorithm': 'HashAlgorithm'
    }

    def __init__(self, certificate=None, reason=None, location=None, signature_date=None, hash_algorithm=None):
        """PdfDigitalSignatureDetailsCore - a model defined in Swagger"""
        super(PdfDigitalSignatureDetailsCore, self).__init__()

        self._certificate = None
        self._reason = None
        self._location = None
        self._signature_date = None
        self._hash_algorithm = None

        if certificate is not None:
            self.certificate = certificate
        if reason is not None:
            self.reason = reason
        if location is not None:
            self.location = location
        if signature_date is not None:
            self.signature_date = signature_date
        if hash_algorithm is not None:
            self.hash_algorithm = hash_algorithm

    @property
    def certificate(self):
        """Gets the certificate of this PdfDigitalSignatureDetailsCore.


        :return: The certificate of this PdfDigitalSignatureDetailsCore.
        :rtype: X509Certificate2
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this PdfDigitalSignatureDetailsCore.


        :param certificate: The certificate of this PdfDigitalSignatureDetailsCore.
        :type: X509Certificate2
        """
        self._certificate = certificate

    @property
    def reason(self):
        """Gets the reason of this PdfDigitalSignatureDetailsCore.


        :return: The reason of this PdfDigitalSignatureDetailsCore.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this PdfDigitalSignatureDetailsCore.


        :param reason: The reason of this PdfDigitalSignatureDetailsCore.
        :type: str
        """
        self._reason = reason

    @property
    def location(self):
        """Gets the location of this PdfDigitalSignatureDetailsCore.


        :return: The location of this PdfDigitalSignatureDetailsCore.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this PdfDigitalSignatureDetailsCore.


        :param location: The location of this PdfDigitalSignatureDetailsCore.
        :type: str
        """
        self._location = location

    @property
    def signature_date(self):
        """Gets the signature_date of this PdfDigitalSignatureDetailsCore.


        :return: The signature_date of this PdfDigitalSignatureDetailsCore.
        :rtype: datetime
        """
        return self._signature_date

    @signature_date.setter
    def signature_date(self, signature_date):
        """Sets the signature_date of this PdfDigitalSignatureDetailsCore.


        :param signature_date: The signature_date of this PdfDigitalSignatureDetailsCore.
        :type: datetime
        """
        if signature_date is None:
            raise ValueError("Invalid value for `signature_date`, must not be `None`")
        self._signature_date = signature_date

    @property
    def hash_algorithm(self):
        """Gets the hash_algorithm of this PdfDigitalSignatureDetailsCore.


        :return: The hash_algorithm of this PdfDigitalSignatureDetailsCore.
        :rtype: str
        """
        return self._hash_algorithm

    @hash_algorithm.setter
    def hash_algorithm(self, hash_algorithm):
        """Sets the hash_algorithm of this PdfDigitalSignatureDetailsCore.


        :param hash_algorithm: The hash_algorithm of this PdfDigitalSignatureDetailsCore.
        :type: str
        """
        if hash_algorithm is None:
            raise ValueError("Invalid value for `hash_algorithm`, must not be `None`")
        allowed_values = ["Sha1", "Sha256", "Sha384", "Sha512", "Md5"]
        if not hash_algorithm.isdigit():
            if hash_algorithm not in allowed_values:
                raise ValueError(
                    "Invalid value for `hash_algorithm` ({0}), must be one of {1}"
                    .format(hash_algorithm, allowed_values))
            self._hash_algorithm = hash_algorithm
        else:
            self._hash_algorithm = allowed_values[int(hash_algorithm) if six.PY3 else long(hash_algorithm)]

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
        if not isinstance(other, PdfDigitalSignatureDetailsCore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
