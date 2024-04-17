#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="PdfOptionsDTO.py">
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

from asposecadcloud.models.cad_rasterization_options_dto import CadRasterizationOptionsDTO
from asposecadcloud.models.drawing_options_base_dto import DrawingOptionsBaseDTO
from asposecadcloud.models.pdf_document_info import PdfDocumentInfo
from asposecadcloud.models.pdf_document_options import PdfDocumentOptions
from asposecadcloud.models.resolution_setting import ResolutionSetting


class PdfOptionsDTO(DrawingOptionsBaseDTO):
    """Export options for PDF format
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'pdf_document_info': 'PdfDocumentInfo',
        'core_pdf_options': 'PdfDocumentOptions'
    }

    attribute_map = {
        'pdf_document_info': 'PdfDocumentInfo',
        'core_pdf_options': 'CorePdfOptions'
    }

    def __init__(self, pdf_document_info=None, core_pdf_options=None):
        """PdfOptionsDTO - a model defined in Swagger"""
        super(PdfOptionsDTO, self).__init__()

        self._pdf_document_info = None
        self._core_pdf_options = None

        if pdf_document_info is not None:
            self.pdf_document_info = pdf_document_info
        if core_pdf_options is not None:
            self.core_pdf_options = core_pdf_options

    @property
    def pdf_document_info(self):
        """Gets the pdf_document_info of this PdfOptionsDTO.

        Document metadata

        :return: The pdf_document_info of this PdfOptionsDTO.
        :rtype: PdfDocumentInfo
        """
        return self._pdf_document_info

    @pdf_document_info.setter
    def pdf_document_info(self, pdf_document_info):
        """Sets the pdf_document_info of this PdfOptionsDTO.

        Document metadata

        :param pdf_document_info: The pdf_document_info of this PdfOptionsDTO.
        :type: PdfDocumentInfo
        """
        self._pdf_document_info = pdf_document_info

    @property
    def core_pdf_options(self):
        """Gets the core_pdf_options of this PdfOptionsDTO.

        Core PDF rendering options

        :return: The core_pdf_options of this PdfOptionsDTO.
        :rtype: PdfDocumentOptions
        """
        return self._core_pdf_options

    @core_pdf_options.setter
    def core_pdf_options(self, core_pdf_options):
        """Sets the core_pdf_options of this PdfOptionsDTO.

        Core PDF rendering options

        :param core_pdf_options: The core_pdf_options of this PdfOptionsDTO.
        :type: PdfDocumentOptions
        """
        self._core_pdf_options = core_pdf_options

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
        if not isinstance(other, PdfOptionsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
