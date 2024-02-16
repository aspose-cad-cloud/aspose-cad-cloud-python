#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="GifOptionsDTO.py">
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
from asposecadcloud.models.resolution_setting import ResolutionSetting


class GifOptionsDTO(DrawingOptionsBaseDTO):
    """Export options for GIF format
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'do_palette_correction': 'bool',
        'color_resolution': 'int',
        'is_palette_sorted': 'bool',
        'pixel_aspect_ratio': 'int',
        'background_color_index': 'int',
        'has_trailer': 'bool',
        'interlaced': 'bool'
    }

    attribute_map = {
        'do_palette_correction': 'DoPaletteCorrection',
        'color_resolution': 'ColorResolution',
        'is_palette_sorted': 'IsPaletteSorted',
        'pixel_aspect_ratio': 'PixelAspectRatio',
        'background_color_index': 'BackgroundColorIndex',
        'has_trailer': 'HasTrailer',
        'interlaced': 'Interlaced'
    }

    def __init__(self, do_palette_correction=None, color_resolution=None, is_palette_sorted=None, pixel_aspect_ratio=None, background_color_index=None, has_trailer=None, interlaced=None):
        """GifOptionsDTO - a model defined in Swagger"""
        super(GifOptionsDTO, self).__init__()

        self._do_palette_correction = None
        self._color_resolution = None
        self._is_palette_sorted = None
        self._pixel_aspect_ratio = None
        self._background_color_index = None
        self._has_trailer = None
        self._interlaced = None

        if do_palette_correction is not None:
            self.do_palette_correction = do_palette_correction
        if color_resolution is not None:
            self.color_resolution = color_resolution
        if is_palette_sorted is not None:
            self.is_palette_sorted = is_palette_sorted
        if pixel_aspect_ratio is not None:
            self.pixel_aspect_ratio = pixel_aspect_ratio
        if background_color_index is not None:
            self.background_color_index = background_color_index
        if has_trailer is not None:
            self.has_trailer = has_trailer
        if interlaced is not None:
            self.interlaced = interlaced

    @property
    def do_palette_correction(self):
        """Gets the do_palette_correction of this GifOptionsDTO.

        Determines whether to do auto-correction of a palette

        :return: The do_palette_correction of this GifOptionsDTO.
        :rtype: bool
        """
        return self._do_palette_correction

    @do_palette_correction.setter
    def do_palette_correction(self, do_palette_correction):
        """Sets the do_palette_correction of this GifOptionsDTO.

        Determines whether to do auto-correction of a palette

        :param do_palette_correction: The do_palette_correction of this GifOptionsDTO.
        :type: bool
        """
        if do_palette_correction is None:
            raise ValueError("Invalid value for `do_palette_correction`, must not be `None`")
        self._do_palette_correction = do_palette_correction

    @property
    def color_resolution(self):
        """Gets the color_resolution of this GifOptionsDTO.

        Color resolution

        :return: The color_resolution of this GifOptionsDTO.
        :rtype: int
        """
        return self._color_resolution

    @color_resolution.setter
    def color_resolution(self, color_resolution):
        """Sets the color_resolution of this GifOptionsDTO.

        Color resolution

        :param color_resolution: The color_resolution of this GifOptionsDTO.
        :type: int
        """
        if color_resolution is None:
            raise ValueError("Invalid value for `color_resolution`, must not be `None`")
        self._color_resolution = color_resolution

    @property
    def is_palette_sorted(self):
        """Gets the is_palette_sorted of this GifOptionsDTO.

        Determines whether a palette is sorted

        :return: The is_palette_sorted of this GifOptionsDTO.
        :rtype: bool
        """
        return self._is_palette_sorted

    @is_palette_sorted.setter
    def is_palette_sorted(self, is_palette_sorted):
        """Sets the is_palette_sorted of this GifOptionsDTO.

        Determines whether a palette is sorted

        :param is_palette_sorted: The is_palette_sorted of this GifOptionsDTO.
        :type: bool
        """
        if is_palette_sorted is None:
            raise ValueError("Invalid value for `is_palette_sorted`, must not be `None`")
        self._is_palette_sorted = is_palette_sorted

    @property
    def pixel_aspect_ratio(self):
        """Gets the pixel_aspect_ratio of this GifOptionsDTO.

        Pixel aspect ration

        :return: The pixel_aspect_ratio of this GifOptionsDTO.
        :rtype: int
        """
        return self._pixel_aspect_ratio

    @pixel_aspect_ratio.setter
    def pixel_aspect_ratio(self, pixel_aspect_ratio):
        """Sets the pixel_aspect_ratio of this GifOptionsDTO.

        Pixel aspect ration

        :param pixel_aspect_ratio: The pixel_aspect_ratio of this GifOptionsDTO.
        :type: int
        """
        if pixel_aspect_ratio is None:
            raise ValueError("Invalid value for `pixel_aspect_ratio`, must not be `None`")
        self._pixel_aspect_ratio = pixel_aspect_ratio

    @property
    def background_color_index(self):
        """Gets the background_color_index of this GifOptionsDTO.

        Background color index

        :return: The background_color_index of this GifOptionsDTO.
        :rtype: int
        """
        return self._background_color_index

    @background_color_index.setter
    def background_color_index(self, background_color_index):
        """Sets the background_color_index of this GifOptionsDTO.

        Background color index

        :param background_color_index: The background_color_index of this GifOptionsDTO.
        :type: int
        """
        if background_color_index is None:
            raise ValueError("Invalid value for `background_color_index`, must not be `None`")
        self._background_color_index = background_color_index

    @property
    def has_trailer(self):
        """Gets the has_trailer of this GifOptionsDTO.

        Determines whether image has to have a trailer

        :return: The has_trailer of this GifOptionsDTO.
        :rtype: bool
        """
        return self._has_trailer

    @has_trailer.setter
    def has_trailer(self, has_trailer):
        """Sets the has_trailer of this GifOptionsDTO.

        Determines whether image has to have a trailer

        :param has_trailer: The has_trailer of this GifOptionsDTO.
        :type: bool
        """
        if has_trailer is None:
            raise ValueError("Invalid value for `has_trailer`, must not be `None`")
        self._has_trailer = has_trailer

    @property
    def interlaced(self):
        """Gets the interlaced of this GifOptionsDTO.

        Determines whether an image has to be interlaced

        :return: The interlaced of this GifOptionsDTO.
        :rtype: bool
        """
        return self._interlaced

    @interlaced.setter
    def interlaced(self, interlaced):
        """Sets the interlaced of this GifOptionsDTO.

        Determines whether an image has to be interlaced

        :param interlaced: The interlaced of this GifOptionsDTO.
        :type: bool
        """
        if interlaced is None:
            raise ValueError("Invalid value for `interlaced`, must not be `None`")
        self._interlaced = interlaced

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
        if not isinstance(other, GifOptionsDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
