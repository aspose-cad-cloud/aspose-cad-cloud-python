#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="CadResponse.py">
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

from asposecadcloud.models.cf2_properties import Cf2Properties
from asposecadcloud.models.dgn_properties import DgnProperties
from asposecadcloud.models.dwf_properties import DwfProperties
from asposecadcloud.models.dwg_properties import DwgProperties
from asposecadcloud.models.dxf_properties import DxfProperties
from asposecadcloud.models.fbx_properties import FbxProperties
from asposecadcloud.models.ifc_properties import IfcProperties
from asposecadcloud.models.igs_properties import IgsProperties
from asposecadcloud.models.obj_properties import ObjProperties
from asposecadcloud.models.plt_properties import PltProperties
from asposecadcloud.models.stl_properties import StlProperties


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
        'cf2_properties': 'Cf2Properties',
        'fbx_properties': 'FbxProperties',
        'obj_properties': 'ObjProperties',
        'plt_properties': 'PltProperties'
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
        'cf2_properties': 'Cf2Properties',
        'fbx_properties': 'FbxProperties',
        'obj_properties': 'ObjProperties',
        'plt_properties': 'PltProperties'
    }

    def __init__(self, height=None, width=None, dwg_properties=None, dxf_properties=None, dwt_properties=None, dgn_properties=None, ifc_properties=None, igs_properties=None, stl_properties=None, dwf_properties=None, cf2_properties=None, fbx_properties=None, obj_properties=None, plt_properties=None):
        """CadResponse - a model defined in Swagger"""
        super(CadResponse, self).__init__()

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
        self._cf2_properties = None
        self._fbx_properties = None
        self._obj_properties = None
        self._plt_properties = None

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
        if cf2_properties is not None:
            self.cf2_properties = cf2_properties
        if fbx_properties is not None:
            self.fbx_properties = fbx_properties
        if obj_properties is not None:
            self.obj_properties = obj_properties
        if plt_properties is not None:
            self.plt_properties = plt_properties

    @property
    def height(self):
        """Gets the height of this CadResponse.

        Gets or sets the height of a drawing.

        :return: The height of this CadResponse.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this CadResponse.

        Gets or sets the height of a drawing.

        :param height: The height of this CadResponse.
        :type: int
        """
        if height is None:
            raise ValueError("Invalid value for `height`, must not be `None`")
        self._height = height

    @property
    def width(self):
        """Gets the width of this CadResponse.

        Gets or sets the width of a drawing.

        :return: The width of this CadResponse.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this CadResponse.

        Gets or sets the width of a drawing.

        :param width: The width of this CadResponse.
        :type: int
        """
        if width is None:
            raise ValueError("Invalid value for `width`, must not be `None`")
        self._width = width

    @property
    def dwg_properties(self):
        """Gets the dwg_properties of this CadResponse.

        Gets or sets the DWG properties.

        :return: The dwg_properties of this CadResponse.
        :rtype: DwgProperties
        """
        return self._dwg_properties

    @dwg_properties.setter
    def dwg_properties(self, dwg_properties):
        """Sets the dwg_properties of this CadResponse.

        Gets or sets the DWG properties.

        :param dwg_properties: The dwg_properties of this CadResponse.
        :type: DwgProperties
        """
        self._dwg_properties = dwg_properties

    @property
    def dxf_properties(self):
        """Gets the dxf_properties of this CadResponse.

        Gets or sets the DXF properties.

        :return: The dxf_properties of this CadResponse.
        :rtype: DxfProperties
        """
        return self._dxf_properties

    @dxf_properties.setter
    def dxf_properties(self, dxf_properties):
        """Sets the dxf_properties of this CadResponse.

        Gets or sets the DXF properties.

        :param dxf_properties: The dxf_properties of this CadResponse.
        :type: DxfProperties
        """
        self._dxf_properties = dxf_properties

    @property
    def dwt_properties(self):
        """Gets the dwt_properties of this CadResponse.

        Gets or sets the DWT properties.

        :return: The dwt_properties of this CadResponse.
        :rtype: DwgProperties
        """
        return self._dwt_properties

    @dwt_properties.setter
    def dwt_properties(self, dwt_properties):
        """Sets the dwt_properties of this CadResponse.

        Gets or sets the DWT properties.

        :param dwt_properties: The dwt_properties of this CadResponse.
        :type: DwgProperties
        """
        self._dwt_properties = dwt_properties

    @property
    def dgn_properties(self):
        """Gets the dgn_properties of this CadResponse.

        Gets or sets the DGN properties.

        :return: The dgn_properties of this CadResponse.
        :rtype: DgnProperties
        """
        return self._dgn_properties

    @dgn_properties.setter
    def dgn_properties(self, dgn_properties):
        """Sets the dgn_properties of this CadResponse.

        Gets or sets the DGN properties.

        :param dgn_properties: The dgn_properties of this CadResponse.
        :type: DgnProperties
        """
        self._dgn_properties = dgn_properties

    @property
    def ifc_properties(self):
        """Gets the ifc_properties of this CadResponse.

        Gets or sets the IFC properties.

        :return: The ifc_properties of this CadResponse.
        :rtype: IfcProperties
        """
        return self._ifc_properties

    @ifc_properties.setter
    def ifc_properties(self, ifc_properties):
        """Sets the ifc_properties of this CadResponse.

        Gets or sets the IFC properties.

        :param ifc_properties: The ifc_properties of this CadResponse.
        :type: IfcProperties
        """
        self._ifc_properties = ifc_properties

    @property
    def igs_properties(self):
        """Gets the igs_properties of this CadResponse.

        Gets or sets the IGS properties.

        :return: The igs_properties of this CadResponse.
        :rtype: IgsProperties
        """
        return self._igs_properties

    @igs_properties.setter
    def igs_properties(self, igs_properties):
        """Sets the igs_properties of this CadResponse.

        Gets or sets the IGS properties.

        :param igs_properties: The igs_properties of this CadResponse.
        :type: IgsProperties
        """
        self._igs_properties = igs_properties

    @property
    def stl_properties(self):
        """Gets the stl_properties of this CadResponse.

        Gets or sets the STL properties.

        :return: The stl_properties of this CadResponse.
        :rtype: StlProperties
        """
        return self._stl_properties

    @stl_properties.setter
    def stl_properties(self, stl_properties):
        """Sets the stl_properties of this CadResponse.

        Gets or sets the STL properties.

        :param stl_properties: The stl_properties of this CadResponse.
        :type: StlProperties
        """
        self._stl_properties = stl_properties

    @property
    def dwf_properties(self):
        """Gets the dwf_properties of this CadResponse.

        Gets or sets the DWF properties.

        :return: The dwf_properties of this CadResponse.
        :rtype: DwfProperties
        """
        return self._dwf_properties

    @dwf_properties.setter
    def dwf_properties(self, dwf_properties):
        """Sets the dwf_properties of this CadResponse.

        Gets or sets the DWF properties.

        :param dwf_properties: The dwf_properties of this CadResponse.
        :type: DwfProperties
        """
        self._dwf_properties = dwf_properties

    @property
    def cf2_properties(self):
        """Gets the cf2_properties of this CadResponse.

        Gets or sets the Cf2 properties.

        :return: The cf2_properties of this CadResponse.
        :rtype: Cf2Properties
        """
        return self._cf2_properties

    @cf2_properties.setter
    def cf2_properties(self, cf2_properties):
        """Sets the cf2_properties of this CadResponse.

        Gets or sets the Cf2 properties.

        :param cf2_properties: The cf2_properties of this CadResponse.
        :type: Cf2Properties
        """
        self._cf2_properties = cf2_properties

    @property
    def fbx_properties(self):
        """Gets the fbx_properties of this CadResponse.

        Gets or sets the Cf2 properties.

        :return: The fbx_properties of this CadResponse.
        :rtype: FbxProperties
        """
        return self._fbx_properties

    @fbx_properties.setter
    def fbx_properties(self, fbx_properties):
        """Sets the fbx_properties of this CadResponse.

        Gets or sets the Cf2 properties.

        :param fbx_properties: The fbx_properties of this CadResponse.
        :type: FbxProperties
        """
        self._fbx_properties = fbx_properties

    @property
    def obj_properties(self):
        """Gets the obj_properties of this CadResponse.

        Gets or sets the FBX properties.

        :return: The obj_properties of this CadResponse.
        :rtype: ObjProperties
        """
        return self._obj_properties

    @obj_properties.setter
    def obj_properties(self, obj_properties):
        """Sets the obj_properties of this CadResponse.

        Gets or sets the FBX properties.

        :param obj_properties: The obj_properties of this CadResponse.
        :type: ObjProperties
        """
        self._obj_properties = obj_properties

    @property
    def plt_properties(self):
        """Gets the plt_properties of this CadResponse.

        Gets or sets the Cf2 properties.

        :return: The plt_properties of this CadResponse.
        :rtype: PltProperties
        """
        return self._plt_properties

    @plt_properties.setter
    def plt_properties(self, plt_properties):
        """Sets the plt_properties of this CadResponse.

        Gets or sets the Cf2 properties.

        :param plt_properties: The plt_properties of this CadResponse.
        :type: PltProperties
        """
        self._plt_properties = plt_properties

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
