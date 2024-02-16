#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="VectorRasterizationOptionsDTO.py">
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


class VectorRasterizationOptionsDTO(object):
    """Base raster export options class
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'border_x': 'float',
        'border_y': 'float',
        'page_height': 'float',
        'page_width': 'float',
        'background_color': 'Color',
        'draw_color': 'Color',
        'unit_type': 'str',
        'content_as_bitmap': 'bool',
        'graphics_options': 'GraphicsOptions'
    }

    attribute_map = {
        'border_x': 'BorderX',
        'border_y': 'BorderY',
        'page_height': 'PageHeight',
        'page_width': 'PageWidth',
        'background_color': 'BackgroundColor',
        'draw_color': 'DrawColor',
        'unit_type': 'UnitType',
        'content_as_bitmap': 'ContentAsBitmap',
        'graphics_options': 'GraphicsOptions'
    }

    discriminator_value_class_map = {
        'CadRasterizationOptionsDTO': 'CadRasterizationOptionsDTO'
    }

    def __init__(self, border_x=None, border_y=None, page_height=None, page_width=None, background_color=None, draw_color=None, unit_type=None, content_as_bitmap=None, graphics_options=None):
        """VectorRasterizationOptionsDTO - a model defined in Swagger"""
        super(VectorRasterizationOptionsDTO, self).__init__()

        self._border_x = None
        self._border_y = None
        self._page_height = None
        self._page_width = None
        self._background_color = None
        self._draw_color = None
        self._unit_type = None
        self._content_as_bitmap = None
        self._graphics_options = None

        if border_x is not None:
            self.border_x = border_x
        if border_y is not None:
            self.border_y = border_y
        if page_height is not None:
            self.page_height = page_height
        if page_width is not None:
            self.page_width = page_width
        if background_color is not None:
            self.background_color = background_color
        if draw_color is not None:
            self.draw_color = draw_color
        if unit_type is not None:
            self.unit_type = unit_type
        if content_as_bitmap is not None:
            self.content_as_bitmap = content_as_bitmap
        if graphics_options is not None:
            self.graphics_options = graphics_options

    @property
    def border_x(self):
        """Gets the border_x of this VectorRasterizationOptionsDTO.

        Gets or sets the border X.

        :return: The border_x of this VectorRasterizationOptionsDTO.
        :rtype: float
        """
        return self._border_x

    @border_x.setter
    def border_x(self, border_x):
        """Sets the border_x of this VectorRasterizationOptionsDTO.

        Gets or sets the border X.

        :param border_x: The border_x of this VectorRasterizationOptionsDTO.
        :type: float
        """
        if border_x is None:
            raise ValueError("Invalid value for `border_x`, must not be `None`")
        self._border_x = border_x

    @property
    def border_y(self):
        """Gets the border_y of this VectorRasterizationOptionsDTO.

        Gets or sets the border Y.

        :return: The border_y of this VectorRasterizationOptionsDTO.
        :rtype: float
        """
        return self._border_y

    @border_y.setter
    def border_y(self, border_y):
        """Sets the border_y of this VectorRasterizationOptionsDTO.

        Gets or sets the border Y.

        :param border_y: The border_y of this VectorRasterizationOptionsDTO.
        :type: float
        """
        if border_y is None:
            raise ValueError("Invalid value for `border_y`, must not be `None`")
        self._border_y = border_y

    @property
    def page_height(self):
        """Gets the page_height of this VectorRasterizationOptionsDTO.

        Gets or sets the page height.

        :return: The page_height of this VectorRasterizationOptionsDTO.
        :rtype: float
        """
        return self._page_height

    @page_height.setter
    def page_height(self, page_height):
        """Sets the page_height of this VectorRasterizationOptionsDTO.

        Gets or sets the page height.

        :param page_height: The page_height of this VectorRasterizationOptionsDTO.
        :type: float
        """
        if page_height is None:
            raise ValueError("Invalid value for `page_height`, must not be `None`")
        self._page_height = page_height

    @property
    def page_width(self):
        """Gets the page_width of this VectorRasterizationOptionsDTO.

        Gets or sets the page width.

        :return: The page_width of this VectorRasterizationOptionsDTO.
        :rtype: float
        """
        return self._page_width

    @page_width.setter
    def page_width(self, page_width):
        """Sets the page_width of this VectorRasterizationOptionsDTO.

        Gets or sets the page width.

        :param page_width: The page_width of this VectorRasterizationOptionsDTO.
        :type: float
        """
        if page_width is None:
            raise ValueError("Invalid value for `page_width`, must not be `None`")
        self._page_width = page_width

    @property
    def background_color(self):
        """Gets the background_color of this VectorRasterizationOptionsDTO.

        Gets or sets a background color.

        :return: The background_color of this VectorRasterizationOptionsDTO.
        :rtype: Color
        """
        return self._background_color

    @background_color.setter
    def background_color(self, background_color):
        """Sets the background_color of this VectorRasterizationOptionsDTO.

        Gets or sets a background color.

        :param background_color: The background_color of this VectorRasterizationOptionsDTO.
        :type: Color
        """
        if background_color is None:
            raise ValueError("Invalid value for `background_color`, must not be `None`")
        self._background_color = background_color

    @property
    def draw_color(self):
        """Gets the draw_color of this VectorRasterizationOptionsDTO.

        Gets or sets a foreground color.

        :return: The draw_color of this VectorRasterizationOptionsDTO.
        :rtype: Color
        """
        return self._draw_color

    @draw_color.setter
    def draw_color(self, draw_color):
        """Sets the draw_color of this VectorRasterizationOptionsDTO.

        Gets or sets a foreground color.

        :param draw_color: The draw_color of this VectorRasterizationOptionsDTO.
        :type: Color
        """
        if draw_color is None:
            raise ValueError("Invalid value for `draw_color`, must not be `None`")
        self._draw_color = draw_color

    @property
    def unit_type(self):
        """Gets the unit_type of this VectorRasterizationOptionsDTO.


        :return: The unit_type of this VectorRasterizationOptionsDTO.
        :rtype: str
        """
        return self._unit_type

    @unit_type.setter
    def unit_type(self, unit_type):
        """Sets the unit_type of this VectorRasterizationOptionsDTO.


        :param unit_type: The unit_type of this VectorRasterizationOptionsDTO.
        :type: str
        """
        if unit_type is None:
            raise ValueError("Invalid value for `unit_type`, must not be `None`")
        allowed_values = ["Kilometer", "Meter", "Centimenter", "Millimeter", "Micrometer", "Nanometer", "Angstrom", "Decimeter", "Decameter", "Hectometer", "Gigameter", "AstronomicalUnit", "LightYear", "Parsec", "Mile", "Yard", "Foot", "Inch", "Mil", "MicroInch", "Custom", "Unitless"]
        if not unit_type.isdigit():
            if unit_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `unit_type` ({0}), must be one of {1}"
                    .format(unit_type, allowed_values))
            self._unit_type = unit_type
        else:
            self._unit_type = allowed_values[int(unit_type) if six.PY3 else long(unit_type)]

    @property
    def content_as_bitmap(self):
        """Gets the content_as_bitmap of this VectorRasterizationOptionsDTO.

        Gets or sets a value indicating whether content of a drawing is represented as image inside Pdf. Applicable only for CAD to Pdf export. Default is false.

        :return: The content_as_bitmap of this VectorRasterizationOptionsDTO.
        :rtype: bool
        """
        return self._content_as_bitmap

    @content_as_bitmap.setter
    def content_as_bitmap(self, content_as_bitmap):
        """Sets the content_as_bitmap of this VectorRasterizationOptionsDTO.

        Gets or sets a value indicating whether content of a drawing is represented as image inside Pdf. Applicable only for CAD to Pdf export. Default is false.

        :param content_as_bitmap: The content_as_bitmap of this VectorRasterizationOptionsDTO.
        :type: bool
        """
        if content_as_bitmap is None:
            raise ValueError("Invalid value for `content_as_bitmap`, must not be `None`")
        self._content_as_bitmap = content_as_bitmap

    @property
    def graphics_options(self):
        """Gets the graphics_options of this VectorRasterizationOptionsDTO.

        Gets or sets options to render bitmap inside pdf (if ContentAsBitmap is set to true).

        :return: The graphics_options of this VectorRasterizationOptionsDTO.
        :rtype: GraphicsOptions
        """
        return self._graphics_options

    @graphics_options.setter
    def graphics_options(self, graphics_options):
        """Sets the graphics_options of this VectorRasterizationOptionsDTO.

        Gets or sets options to render bitmap inside pdf (if ContentAsBitmap is set to true).

        :param graphics_options: The graphics_options of this VectorRasterizationOptionsDTO.
        :type: GraphicsOptions
        """
        self._graphics_options = graphics_options

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
        if not isinstance(other, VectorRasterizationOptionsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
