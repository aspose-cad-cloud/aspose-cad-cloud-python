#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="PdfDocumentInfo.py">
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


class PdfDocumentInfo(object):
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
        'keywords': 'str',
        'title': 'str',
        'author': 'str',
        'subject': 'str'
    }

    attribute_map = {
        'keywords': 'Keywords',
        'title': 'Title',
        'author': 'Author',
        'subject': 'Subject'
    }

    def __init__(self, keywords=None, title=None, author=None, subject=None):
        """PdfDocumentInfo - a model defined in Swagger"""
        super(PdfDocumentInfo, self).__init__()

        self._keywords = None
        self._title = None
        self._author = None
        self._subject = None

        if keywords is not None:
            self.keywords = keywords
        if title is not None:
            self.title = title
        if author is not None:
            self.author = author
        if subject is not None:
            self.subject = subject

    @property
    def keywords(self):
        """Gets the keywords of this PdfDocumentInfo.


        :return: The keywords of this PdfDocumentInfo.
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this PdfDocumentInfo.


        :param keywords: The keywords of this PdfDocumentInfo.
        :type: str
        """
        self._keywords = keywords

    @property
    def title(self):
        """Gets the title of this PdfDocumentInfo.


        :return: The title of this PdfDocumentInfo.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PdfDocumentInfo.


        :param title: The title of this PdfDocumentInfo.
        :type: str
        """
        self._title = title

    @property
    def author(self):
        """Gets the author of this PdfDocumentInfo.


        :return: The author of this PdfDocumentInfo.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this PdfDocumentInfo.


        :param author: The author of this PdfDocumentInfo.
        :type: str
        """
        self._author = author

    @property
    def subject(self):
        """Gets the subject of this PdfDocumentInfo.


        :return: The subject of this PdfDocumentInfo.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this PdfDocumentInfo.


        :param subject: The subject of this PdfDocumentInfo.
        :type: str
        """
        self._subject = subject

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
        if not isinstance(other, PdfDocumentInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
