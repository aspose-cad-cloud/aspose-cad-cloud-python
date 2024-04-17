#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="PdfDocumentOptions.py">
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

from asposecadcloud.models.pdf_digital_signature_details_core import PdfDigitalSignatureDetailsCore


class PdfDocumentOptions(object):
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
        'compliance': 'str',
        'digital_signature_details': 'PdfDigitalSignatureDetailsCore'
    }

    attribute_map = {
        'compliance': 'Compliance',
        'digital_signature_details': 'DigitalSignatureDetails'
    }

    def __init__(self, compliance=None, digital_signature_details=None):
        """PdfDocumentOptions - a model defined in Swagger"""
        super(PdfDocumentOptions, self).__init__()

        self._compliance = None
        self._digital_signature_details = None

        if compliance is not None:
            self.compliance = compliance
        if digital_signature_details is not None:
            self.digital_signature_details = digital_signature_details

    @property
    def compliance(self):
        """Gets the compliance of this PdfDocumentOptions.


        :return: The compliance of this PdfDocumentOptions.
        :rtype: str
        """
        return self._compliance

    @compliance.setter
    def compliance(self, compliance):
        """Sets the compliance of this PdfDocumentOptions.


        :param compliance: The compliance of this PdfDocumentOptions.
        :type: str
        """
        if compliance is None:
            raise ValueError("Invalid value for `compliance`, must not be `None`")
        allowed_values = ["Pdf15", "PdfA1a", "PdfA1b"]
        if not compliance.isdigit():
            if compliance not in allowed_values:
                raise ValueError(
                    "Invalid value for `compliance` ({0}), must be one of {1}"
                    .format(compliance, allowed_values))
            self._compliance = compliance
        else:
            self._compliance = allowed_values[int(compliance) if six.PY3 else long(compliance)]

    @property
    def digital_signature_details(self):
        """Gets the digital_signature_details of this PdfDocumentOptions.


        :return: The digital_signature_details of this PdfDocumentOptions.
        :rtype: PdfDigitalSignatureDetailsCore
        """
        return self._digital_signature_details

    @digital_signature_details.setter
    def digital_signature_details(self, digital_signature_details):
        """Sets the digital_signature_details of this PdfDocumentOptions.


        :param digital_signature_details: The digital_signature_details of this PdfDocumentOptions.
        :type: PdfDigitalSignatureDetailsCore
        """
        self._digital_signature_details = digital_signature_details

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
        if not isinstance(other, PdfDocumentOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
