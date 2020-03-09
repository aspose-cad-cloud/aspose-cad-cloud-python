# coding: utf-8
# -----------------------------------------------------------------------------------
# <copyright company="Aspose" file="CadResponse.py">
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


class CadResponse(object):
    """Represents information about a drawing.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'height': 'int',
        'width': 'int',
        'dwg_properties': 'DwgProperties',
        'dxf_properties': 'DxfProperties',
        'dwt_properties': 'DwgProperties',
        'dgn_properties': 'DgnProperties',
        'ifc_properties': 'IfcProperties',
        'igs_properties': 'IgsProperties',
        'stl_properties': 'StlProperties',
        'dwf_properties': 'DwfProperties',
        'cff2_properties': 'Cff2Properties'
    }

    attribute_map = {
        'height': 'Height',
        'width': 'Width',
        'dwg_properties': 'DwgProperties',
        'dxf_properties': 'DxfProperties',
        'dwt_properties': 'DwtProperties',
        'dgn_properties': 'DgnProperties',
        'ifc_properties': 'IfcProperties',
        'igs_properties': 'IgsProperties',
        'stl_properties': 'StlProperties',
        'dwf_properties': 'DwfProperties',
        'cff2_properties': 'Cff2Properties'
    }

    def __init__(self, height=None, width=None, dwg_properties=None, dxf_properties=None, dwt_properties=None, dgn_properties=None, ifc_properties=None, igs_properties=None, stl_properties=None, dwf_properties=None, cff2_properties=None):  # noqa: E501
        """CadResponse - a model defined in Swagger"""  # noqa: E501

        self._height = None
        self._width = None
        self._dwg_properties = None
        self._dxf_properties = None
        self._dwt_properties = None
        self._dgn_properties = None
        self._ifc_properties = None
        self._igs_properties = None
        self._stl_properties = None
        self._dwf_properties = None
        self._cff2_properties = None
        self.discriminator = None

        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if dwg_properties is not None:
            self.dwg_properties = dwg_properties
        if dxf_properties is not None:
            self.dxf_properties = dxf_properties
        if dwt_properties is not None:
            self.dwt_properties = dwt_properties
        if dgn_properties is not None:
            self.dgn_properties = dgn_properties
        if ifc_properties is not None:
            self.ifc_properties = ifc_properties
        if igs_properties is not None:
            self.igs_properties = igs_properties
        if stl_properties is not None:
            self.stl_properties = stl_properties
        if dwf_properties is not None:
            self.dwf_properties = dwf_properties
        if cff2_properties is not None:
            self.cff2_properties = cff2_properties

    @property
    def height(self):
        """Gets the height of this CadResponse.  # noqa: E501

        Gets or sets the height of a drawing.  # noqa: E501

        :return: The height of this CadResponse.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this CadResponse.

        Gets or sets the height of a drawing.  # noqa: E501

        :param height: The height of this CadResponse.  # noqa: E501
        :type: int
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501
        self._height = height
    @property
    def width(self):
        """Gets the width of this CadResponse.  # noqa: E501

        Gets or sets the width of a drawing.  # noqa: E501

        :return: The width of this CadResponse.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this CadResponse.

        Gets or sets the width of a drawing.  # noqa: E501

        :param width: The width of this CadResponse.  # noqa: E501
        :type: int
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")  # noqa: E501
        self._width = width
    @property
    def dwg_properties(self):
        """Gets the dwg_properties of this CadResponse.  # noqa: E501

        Gets or sets the DWG properties.  # noqa: E501

        :return: The dwg_properties of this CadResponse.  # noqa: E501
        :rtype: DwgProperties
        """
        return self._dwg_properties

    @dwg_properties.setter
    def dwg_properties(self, dwg_properties):
        """Sets the dwg_properties of this CadResponse.

        Gets or sets the DWG properties.  # noqa: E501

        :param dwg_properties: The dwg_properties of this CadResponse.  # noqa: E501
        :type: DwgProperties
        """
        self._dwg_properties = dwg_properties
    @property
    def dxf_properties(self):
        """Gets the dxf_properties of this CadResponse.  # noqa: E501

        Gets or sets the DXF properties.  # noqa: E501

        :return: The dxf_properties of this CadResponse.  # noqa: E501
        :rtype: DxfProperties
        """
        return self._dxf_properties

    @dxf_properties.setter
    def dxf_properties(self, dxf_properties):
        """Sets the dxf_properties of this CadResponse.

        Gets or sets the DXF properties.  # noqa: E501

        :param dxf_properties: The dxf_properties of this CadResponse.  # noqa: E501
        :type: DxfProperties
        """
        self._dxf_properties = dxf_properties
    @property
    def dwt_properties(self):
        """Gets the dwt_properties of this CadResponse.  # noqa: E501

        Gets or sets the DWT properties.  # noqa: E501

        :return: The dwt_properties of this CadResponse.  # noqa: E501
        :rtype: DwgProperties
        """
        return self._dwt_properties

    @dwt_properties.setter
    def dwt_properties(self, dwt_properties):
        """Sets the dwt_properties of this CadResponse.

        Gets or sets the DWT properties.  # noqa: E501

        :param dwt_properties: The dwt_properties of this CadResponse.  # noqa: E501
        :type: DwgProperties
        """
        self._dwt_properties = dwt_properties
    @property
    def dgn_properties(self):
        """Gets the dgn_properties of this CadResponse.  # noqa: E501

        Gets or sets the DGN properties.  # noqa: E501

        :return: The dgn_properties of this CadResponse.  # noqa: E501
        :rtype: DgnProperties
        """
        return self._dgn_properties

    @dgn_properties.setter
    def dgn_properties(self, dgn_properties):
        """Sets the dgn_properties of this CadResponse.

        Gets or sets the DGN properties.  # noqa: E501

        :param dgn_properties: The dgn_properties of this CadResponse.  # noqa: E501
        :type: DgnProperties
        """
        self._dgn_properties = dgn_properties
    @property
    def ifc_properties(self):
        """Gets the ifc_properties of this CadResponse.  # noqa: E501

        Gets or sets the IFC properties.  # noqa: E501

        :return: The ifc_properties of this CadResponse.  # noqa: E501
        :rtype: IfcProperties
        """
        return self._ifc_properties

    @ifc_properties.setter
    def ifc_properties(self, ifc_properties):
        """Sets the ifc_properties of this CadResponse.

        Gets or sets the IFC properties.  # noqa: E501

        :param ifc_properties: The ifc_properties of this CadResponse.  # noqa: E501
        :type: IfcProperties
        """
        self._ifc_properties = ifc_properties
    @property
    def igs_properties(self):
        """Gets the igs_properties of this CadResponse.  # noqa: E501

        Gets or sets the IGS properties.  # noqa: E501

        :return: The igs_properties of this CadResponse.  # noqa: E501
        :rtype: IgsProperties
        """
        return self._igs_properties

    @igs_properties.setter
    def igs_properties(self, igs_properties):
        """Sets the igs_properties of this CadResponse.

        Gets or sets the IGS properties.  # noqa: E501

        :param igs_properties: The igs_properties of this CadResponse.  # noqa: E501
        :type: IgsProperties
        """
        self._igs_properties = igs_properties
    @property
    def stl_properties(self):
        """Gets the stl_properties of this CadResponse.  # noqa: E501

        Gets or sets the STL properties.  # noqa: E501

        :return: The stl_properties of this CadResponse.  # noqa: E501
        :rtype: StlProperties
        """
        return self._stl_properties

    @stl_properties.setter
    def stl_properties(self, stl_properties):
        """Sets the stl_properties of this CadResponse.

        Gets or sets the STL properties.  # noqa: E501

        :param stl_properties: The stl_properties of this CadResponse.  # noqa: E501
        :type: StlProperties
        """
        self._stl_properties = stl_properties
    @property
    def dwf_properties(self):
        """Gets the dwf_properties of this CadResponse.  # noqa: E501

        Gets or sets the DWF properties.  # noqa: E501

        :return: The dwf_properties of this CadResponse.  # noqa: E501
        :rtype: DwfProperties
        """
        return self._dwf_properties

    @dwf_properties.setter
    def dwf_properties(self, dwf_properties):
        """Sets the dwf_properties of this CadResponse.

        Gets or sets the DWF properties.  # noqa: E501

        :param dwf_properties: The dwf_properties of this CadResponse.  # noqa: E501
        :type: DwfProperties
        """
        self._dwf_properties = dwf_properties
    @property
    def cff2_properties(self):
        """Gets the cff2_properties of this CadResponse.  # noqa: E501

        Gets or sets the CFF2 properties.  # noqa: E501

        :return: The cff2_properties of this CadResponse.  # noqa: E501
        :rtype: Cff2Properties
        """
        return self._cff2_properties

    @cff2_properties.setter
    def cff2_properties(self, cff2_properties):
        """Sets the cff2_properties of this CadResponse.

        Gets or sets the CFF2 properties.  # noqa: E501

        :param cff2_properties: The cff2_properties of this CadResponse.  # noqa: E501
        :type: Cff2Properties
        """
        self._cff2_properties = cff2_properties
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
        if not isinstance(other, CadResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
