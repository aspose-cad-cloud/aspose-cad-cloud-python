#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="X509Certificate2.py">
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

from asposecadcloud.models.asymmetric_algorithm import AsymmetricAlgorithm
from asposecadcloud.models.int_ptr import IntPtr
from asposecadcloud.models.oid import Oid
from asposecadcloud.models.public_key import PublicKey
from asposecadcloud.models.x500_distinguished_name import X500DistinguishedName
from asposecadcloud.models.x509_certificate import X509Certificate


class X509Certificate2(X509Certificate):
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
        'archived': 'bool',
        'extensions': 'list[object]',
        'friendly_name': 'str',
        'has_private_key': 'bool',
        'private_key': 'AsymmetricAlgorithm',
        'issuer_name': 'X500DistinguishedName',
        'not_after': 'datetime',
        'not_before': 'datetime',
        'public_key': 'PublicKey',
        'raw_data': 'str',
        'serial_number': 'str',
        'signature_algorithm': 'Oid',
        'subject_name': 'X500DistinguishedName',
        'thumbprint': 'str',
        'version': 'int'
    }

    attribute_map = {
        'archived': 'Archived',
        'extensions': 'Extensions',
        'friendly_name': 'FriendlyName',
        'has_private_key': 'HasPrivateKey',
        'private_key': 'PrivateKey',
        'issuer_name': 'IssuerName',
        'not_after': 'NotAfter',
        'not_before': 'NotBefore',
        'public_key': 'PublicKey',
        'raw_data': 'RawData',
        'serial_number': 'SerialNumber',
        'signature_algorithm': 'SignatureAlgorithm',
        'subject_name': 'SubjectName',
        'thumbprint': 'Thumbprint',
        'version': 'Version'
    }

    def __init__(self, archived=None, extensions=None, friendly_name=None, has_private_key=None, private_key=None, issuer_name=None, not_after=None, not_before=None, public_key=None, raw_data=None, serial_number=None, signature_algorithm=None, subject_name=None, thumbprint=None, version=None):
        """X509Certificate2 - a model defined in Swagger"""
        super(X509Certificate2, self).__init__()

        self._archived = None
        self._extensions = None
        self._friendly_name = None
        self._has_private_key = None
        self._private_key = None
        self._issuer_name = None
        self._not_after = None
        self._not_before = None
        self._public_key = None
        self._raw_data = None
        self._serial_number = None
        self._signature_algorithm = None
        self._subject_name = None
        self._thumbprint = None
        self._version = None

        if archived is not None:
            self.archived = archived
        if extensions is not None:
            self.extensions = extensions
        if friendly_name is not None:
            self.friendly_name = friendly_name
        if has_private_key is not None:
            self.has_private_key = has_private_key
        if private_key is not None:
            self.private_key = private_key
        if issuer_name is not None:
            self.issuer_name = issuer_name
        if not_after is not None:
            self.not_after = not_after
        if not_before is not None:
            self.not_before = not_before
        if public_key is not None:
            self.public_key = public_key
        if raw_data is not None:
            self.raw_data = raw_data
        if serial_number is not None:
            self.serial_number = serial_number
        if signature_algorithm is not None:
            self.signature_algorithm = signature_algorithm
        if subject_name is not None:
            self.subject_name = subject_name
        if thumbprint is not None:
            self.thumbprint = thumbprint
        if version is not None:
            self.version = version

    @property
    def archived(self):
        """Gets the archived of this X509Certificate2.


        :return: The archived of this X509Certificate2.
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this X509Certificate2.


        :param archived: The archived of this X509Certificate2.
        :type: bool
        """
        if archived is None:
            raise ValueError("Invalid value for `archived`, must not be `None`")
        self._archived = archived

    @property
    def extensions(self):
        """Gets the extensions of this X509Certificate2.


        :return: The extensions of this X509Certificate2.
        :rtype: list[object]
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """Sets the extensions of this X509Certificate2.


        :param extensions: The extensions of this X509Certificate2.
        :type: list[object]
        """
        self._extensions = extensions

    @property
    def friendly_name(self):
        """Gets the friendly_name of this X509Certificate2.


        :return: The friendly_name of this X509Certificate2.
        :rtype: str
        """
        return self._friendly_name

    @friendly_name.setter
    def friendly_name(self, friendly_name):
        """Sets the friendly_name of this X509Certificate2.


        :param friendly_name: The friendly_name of this X509Certificate2.
        :type: str
        """
        self._friendly_name = friendly_name

    @property
    def has_private_key(self):
        """Gets the has_private_key of this X509Certificate2.


        :return: The has_private_key of this X509Certificate2.
        :rtype: bool
        """
        return self._has_private_key

    @has_private_key.setter
    def has_private_key(self, has_private_key):
        """Sets the has_private_key of this X509Certificate2.


        :param has_private_key: The has_private_key of this X509Certificate2.
        :type: bool
        """
        if has_private_key is None:
            raise ValueError("Invalid value for `has_private_key`, must not be `None`")
        self._has_private_key = has_private_key

    @property
    def private_key(self):
        """Gets the private_key of this X509Certificate2.


        :return: The private_key of this X509Certificate2.
        :rtype: AsymmetricAlgorithm
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this X509Certificate2.


        :param private_key: The private_key of this X509Certificate2.
        :type: AsymmetricAlgorithm
        """
        self._private_key = private_key

    @property
    def issuer_name(self):
        """Gets the issuer_name of this X509Certificate2.


        :return: The issuer_name of this X509Certificate2.
        :rtype: X500DistinguishedName
        """
        return self._issuer_name

    @issuer_name.setter
    def issuer_name(self, issuer_name):
        """Sets the issuer_name of this X509Certificate2.


        :param issuer_name: The issuer_name of this X509Certificate2.
        :type: X500DistinguishedName
        """
        self._issuer_name = issuer_name

    @property
    def not_after(self):
        """Gets the not_after of this X509Certificate2.


        :return: The not_after of this X509Certificate2.
        :rtype: datetime
        """
        return self._not_after

    @not_after.setter
    def not_after(self, not_after):
        """Sets the not_after of this X509Certificate2.


        :param not_after: The not_after of this X509Certificate2.
        :type: datetime
        """
        if not_after is None:
            raise ValueError("Invalid value for `not_after`, must not be `None`")
        self._not_after = not_after

    @property
    def not_before(self):
        """Gets the not_before of this X509Certificate2.


        :return: The not_before of this X509Certificate2.
        :rtype: datetime
        """
        return self._not_before

    @not_before.setter
    def not_before(self, not_before):
        """Sets the not_before of this X509Certificate2.


        :param not_before: The not_before of this X509Certificate2.
        :type: datetime
        """
        if not_before is None:
            raise ValueError("Invalid value for `not_before`, must not be `None`")
        self._not_before = not_before

    @property
    def public_key(self):
        """Gets the public_key of this X509Certificate2.


        :return: The public_key of this X509Certificate2.
        :rtype: PublicKey
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this X509Certificate2.


        :param public_key: The public_key of this X509Certificate2.
        :type: PublicKey
        """
        self._public_key = public_key

    @property
    def raw_data(self):
        """Gets the raw_data of this X509Certificate2.


        :return: The raw_data of this X509Certificate2.
        :rtype: str
        """
        return self._raw_data

    @raw_data.setter
    def raw_data(self, raw_data):
        """Sets the raw_data of this X509Certificate2.


        :param raw_data: The raw_data of this X509Certificate2.
        :type: str
        """
        if raw_data is not None and not re.search('^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', raw_data):
            raise ValueError("Invalid value for `raw_data`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")
        self._raw_data = raw_data

    @property
    def serial_number(self):
        """Gets the serial_number of this X509Certificate2.


        :return: The serial_number of this X509Certificate2.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this X509Certificate2.


        :param serial_number: The serial_number of this X509Certificate2.
        :type: str
        """
        self._serial_number = serial_number

    @property
    def signature_algorithm(self):
        """Gets the signature_algorithm of this X509Certificate2.


        :return: The signature_algorithm of this X509Certificate2.
        :rtype: Oid
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        """Sets the signature_algorithm of this X509Certificate2.


        :param signature_algorithm: The signature_algorithm of this X509Certificate2.
        :type: Oid
        """
        self._signature_algorithm = signature_algorithm

    @property
    def subject_name(self):
        """Gets the subject_name of this X509Certificate2.


        :return: The subject_name of this X509Certificate2.
        :rtype: X500DistinguishedName
        """
        return self._subject_name

    @subject_name.setter
    def subject_name(self, subject_name):
        """Sets the subject_name of this X509Certificate2.


        :param subject_name: The subject_name of this X509Certificate2.
        :type: X500DistinguishedName
        """
        self._subject_name = subject_name

    @property
    def thumbprint(self):
        """Gets the thumbprint of this X509Certificate2.


        :return: The thumbprint of this X509Certificate2.
        :rtype: str
        """
        return self._thumbprint

    @thumbprint.setter
    def thumbprint(self, thumbprint):
        """Sets the thumbprint of this X509Certificate2.


        :param thumbprint: The thumbprint of this X509Certificate2.
        :type: str
        """
        self._thumbprint = thumbprint

    @property
    def version(self):
        """Gets the version of this X509Certificate2.


        :return: The version of this X509Certificate2.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this X509Certificate2.


        :param version: The version of this X509Certificate2.
        :type: int
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")
        self._version = version

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
        if not isinstance(other, X509Certificate2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
