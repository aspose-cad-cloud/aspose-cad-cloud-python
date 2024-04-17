#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="X509Certificate.py">
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

from asposecadcloud.models.int_ptr import IntPtr


class X509Certificate(object):
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
        'handle': 'IntPtr',
        'issuer': 'str',
        'subject': 'str'
    }

    attribute_map = {
        'handle': 'Handle',
        'issuer': 'Issuer',
        'subject': 'Subject'
    }

    discriminator_value_class_map = {
        'X509Certificate2': 'X509Certificate2'
    }

    def __init__(self, handle=None, issuer=None, subject=None):
        """X509Certificate - a model defined in Swagger"""
        super(X509Certificate, self).__init__()

        self._handle = None
        self._issuer = None
        self._subject = None

        if handle is not None:
            self.handle = handle
        if issuer is not None:
            self.issuer = issuer
        if subject is not None:
            self.subject = subject

    @property
    def handle(self):
        """Gets the handle of this X509Certificate.


        :return: The handle of this X509Certificate.
        :rtype: IntPtr
        """
        return self._handle

    @handle.setter
    def handle(self, handle):
        """Sets the handle of this X509Certificate.


        :param handle: The handle of this X509Certificate.
        :type: IntPtr
        """
        if handle is None:
            raise ValueError("Invalid value for `handle`, must not be `None`")
        self._handle = handle

    @property
    def issuer(self):
        """Gets the issuer of this X509Certificate.


        :return: The issuer of this X509Certificate.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this X509Certificate.


        :param issuer: The issuer of this X509Certificate.
        :type: str
        """
        self._issuer = issuer

    @property
    def subject(self):
        """Gets the subject of this X509Certificate.


        :return: The subject of this X509Certificate.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this X509Certificate.


        :param subject: The subject of this X509Certificate.
        :type: str
        """
        self._subject = subject

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
        if not isinstance(other, X509Certificate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
