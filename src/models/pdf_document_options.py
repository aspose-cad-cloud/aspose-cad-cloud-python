# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="PdfDocumentOptions.py">
#   Copyright (c) 2018 Aspose.CAD Cloud
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------
import pprint
import re  # noqa: F401

import six


class PdfDocumentOptions(object):
    """The PDF options.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'compliance': 'str'
    }

    attribute_map = {
        'compliance': 'Compliance'
    }

    def __init__(self, compliance=None):  # noqa: E501
        """PdfDocumentOptions - a model defined in Swagger"""  # noqa: E501

        self._compliance = None
        self.discriminator = None

        if compliance is not None:
            self.compliance = compliance

    @property
    def compliance(self):
        """Gets the compliance of this PdfDocumentOptions.  # noqa: E501

        Desired conformance level for generated PDF document. Important note: This option should not be changed after PdfDocument object is constructed. Default is Pdf15.  # noqa: E501

        :return: The compliance of this PdfDocumentOptions.  # noqa: E501
        :rtype: str
        """
        return self._compliance

    @compliance.setter
    def compliance(self, compliance):
        """Sets the compliance of this PdfDocumentOptions.

        Desired conformance level for generated PDF document. Important note: This option should not be changed after PdfDocument object is constructed. Default is Pdf15.  # noqa: E501

        :param compliance: The compliance of this PdfDocumentOptions.  # noqa: E501
        :type: str
        """
        if compliance is None:
            raise ValueError("Invalid value for `compliance`, must not be `None`")  # noqa: E501
        allowed_values = ["Pdf15", "PdfA1a", "PdfA1b"]  # noqa: E501
        if not compliance.isdigit():	
            if compliance not in allowed_values:
                raise ValueError(
                    "Invalid value for `compliance` ({0}), must be one of {1}"  # noqa: E501
                    .format(compliance, allowed_values))
            self._compliance = compliance
        else:
            self._compliance = allowed_values[int(compliance) if six.PY3 else long(compliance)]
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
