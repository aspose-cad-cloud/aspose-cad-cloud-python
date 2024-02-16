#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="CadRasterizationOptionsDTO.py">
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

from asposecadcloud.models.color import Color
from asposecadcloud.models.graphics_options import GraphicsOptions
from asposecadcloud.models.pen_options import PenOptions
from asposecadcloud.models.vector_rasterization_options_dto import VectorRasterizationOptionsDTO


class CadRasterizationOptionsDTO(VectorRasterizationOptionsDTO):
    """Raster export options
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'zoom': 'float',
        'pen_options': 'PenOptions',
        'automatic_layouts_scaling': 'bool',
        'layers': 'list[str]',
        'layouts': 'list[str]',
        'draw_type': 'str',
        'no_scaling': 'bool'
    }

    attribute_map = {
        'zoom': 'Zoom',
        'pen_options': 'PenOptions',
        'automatic_layouts_scaling': 'AutomaticLayoutsScaling',
        'layers': 'Layers',
        'layouts': 'Layouts',
        'draw_type': 'DrawType',
        'no_scaling': 'NoScaling'
    }

    def __init__(self, zoom=None, pen_options=None, automatic_layouts_scaling=None, layers=None, layouts=None, draw_type=None, no_scaling=None):
        """CadRasterizationOptionsDTO - a model defined in Swagger"""
        super(CadRasterizationOptionsDTO, self).__init__()

        self._zoom = None
        self._pen_options = None
        self._automatic_layouts_scaling = None
        self._layers = None
        self._layouts = None
        self._draw_type = None
        self._no_scaling = None

        if zoom is not None:
            self.zoom = zoom
        if pen_options is not None:
            self.pen_options = pen_options
        if automatic_layouts_scaling is not None:
            self.automatic_layouts_scaling = automatic_layouts_scaling
        if layers is not None:
            self.layers = layers
        if layouts is not None:
            self.layouts = layouts
        if draw_type is not None:
            self.draw_type = draw_type
        if no_scaling is not None:
            self.no_scaling = no_scaling

    @property
    def zoom(self):
        """Gets the zoom of this CadRasterizationOptionsDTO.

        Zoom factor

        :return: The zoom of this CadRasterizationOptionsDTO.
        :rtype: float
        """
        return self._zoom

    @zoom.setter
    def zoom(self, zoom):
        """Sets the zoom of this CadRasterizationOptionsDTO.

        Zoom factor

        :param zoom: The zoom of this CadRasterizationOptionsDTO.
        :type: float
        """
        if zoom is None:
            raise ValueError("Invalid value for `zoom`, must not be `None`")
        self._zoom = zoom

    @property
    def pen_options(self):
        """Gets the pen_options of this CadRasterizationOptionsDTO.

        Pen options

        :return: The pen_options of this CadRasterizationOptionsDTO.
        :rtype: PenOptions
        """
        return self._pen_options

    @pen_options.setter
    def pen_options(self, pen_options):
        """Sets the pen_options of this CadRasterizationOptionsDTO.

        Pen options

        :param pen_options: The pen_options of this CadRasterizationOptionsDTO.
        :type: PenOptions
        """
        self._pen_options = pen_options

    @property
    def automatic_layouts_scaling(self):
        """Gets the automatic_layouts_scaling of this CadRasterizationOptionsDTO.

        Determines whether layout has to be scaled automatically

        :return: The automatic_layouts_scaling of this CadRasterizationOptionsDTO.
        :rtype: bool
        """
        return self._automatic_layouts_scaling

    @automatic_layouts_scaling.setter
    def automatic_layouts_scaling(self, automatic_layouts_scaling):
        """Sets the automatic_layouts_scaling of this CadRasterizationOptionsDTO.

        Determines whether layout has to be scaled automatically

        :param automatic_layouts_scaling: The automatic_layouts_scaling of this CadRasterizationOptionsDTO.
        :type: bool
        """
        if automatic_layouts_scaling is None:
            raise ValueError("Invalid value for `automatic_layouts_scaling`, must not be `None`")
        self._automatic_layouts_scaling = automatic_layouts_scaling

    @property
    def layers(self):
        """Gets the layers of this CadRasterizationOptionsDTO.

        Layers to export

        :return: The layers of this CadRasterizationOptionsDTO.
        :rtype: list[str]
        """
        return self._layers

    @layers.setter
    def layers(self, layers):
        """Sets the layers of this CadRasterizationOptionsDTO.

        Layers to export

        :param layers: The layers of this CadRasterizationOptionsDTO.
        :type: list[str]
        """
        self._layers = layers

    @property
    def layouts(self):
        """Gets the layouts of this CadRasterizationOptionsDTO.

        Layouts to export

        :return: The layouts of this CadRasterizationOptionsDTO.
        :rtype: list[str]
        """
        return self._layouts

    @layouts.setter
    def layouts(self, layouts):
        """Sets the layouts of this CadRasterizationOptionsDTO.

        Layouts to export

        :param layouts: The layouts of this CadRasterizationOptionsDTO.
        :type: list[str]
        """
        self._layouts = layouts

    @property
    def draw_type(self):
        """Gets the draw_type of this CadRasterizationOptionsDTO.

        Drawing mode

        :return: The draw_type of this CadRasterizationOptionsDTO.
        :rtype: str
        """
        return self._draw_type

    @draw_type.setter
    def draw_type(self, draw_type):
        """Sets the draw_type of this CadRasterizationOptionsDTO.

        Drawing mode

        :param draw_type: The draw_type of this CadRasterizationOptionsDTO.
        :type: str
        """
        if draw_type is None:
            raise ValueError("Invalid value for `draw_type`, must not be `None`")
        allowed_values = ["UseDrawColor", "UseObjectColor"]
        if not draw_type.isdigit():
            if draw_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `draw_type` ({0}), must be one of {1}"
                    .format(draw_type, allowed_values))
            self._draw_type = draw_type
        else:
            self._draw_type = allowed_values[int(draw_type) if six.PY3 else long(draw_type)]

    @property
    def no_scaling(self):
        """Gets the no_scaling of this CadRasterizationOptionsDTO.

        Determines whether scaling has to be turned off

        :return: The no_scaling of this CadRasterizationOptionsDTO.
        :rtype: bool
        """
        return self._no_scaling

    @no_scaling.setter
    def no_scaling(self, no_scaling):
        """Sets the no_scaling of this CadRasterizationOptionsDTO.

        Determines whether scaling has to be turned off

        :param no_scaling: The no_scaling of this CadRasterizationOptionsDTO.
        :type: bool
        """
        if no_scaling is None:
            raise ValueError("Invalid value for `no_scaling`, must not be `None`")
        self._no_scaling = no_scaling

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
        if not isinstance(other, CadRasterizationOptionsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
