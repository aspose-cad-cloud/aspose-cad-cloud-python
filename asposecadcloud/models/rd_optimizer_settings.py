#  coding: utf-8
#  ----------------------------------------------------------------------------
#  <copyright company="Aspose" file="RdOptimizerSettings.py">
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


class RdOptimizerSettings(object):
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
        'bpp_scale': 'int',
        'bpp_max': 'float',
        'max_q': 'int',
        'min_q': 'int',
        'max_pixel_value': 'int',
        'psnr_max': 'int',
        'discretized_bpp_max': 'int'
    }

    attribute_map = {
        'bpp_scale': 'BppScale',
        'bpp_max': 'BppMax',
        'max_q': 'MaxQ',
        'min_q': 'MinQ',
        'max_pixel_value': 'MaxPixelValue',
        'psnr_max': 'PsnrMax',
        'discretized_bpp_max': 'DiscretizedBppMax'
    }

    def __init__(self, bpp_scale=None, bpp_max=None, max_q=None, min_q=None, max_pixel_value=None, psnr_max=None, discretized_bpp_max=None):
        """RdOptimizerSettings - a model defined in Swagger"""
        super(RdOptimizerSettings, self).__init__()

        self._bpp_scale = None
        self._bpp_max = None
        self._max_q = None
        self._min_q = None
        self._max_pixel_value = None
        self._psnr_max = None
        self._discretized_bpp_max = None

        if bpp_scale is not None:
            self.bpp_scale = bpp_scale
        if bpp_max is not None:
            self.bpp_max = bpp_max
        if max_q is not None:
            self.max_q = max_q
        if min_q is not None:
            self.min_q = min_q
        if max_pixel_value is not None:
            self.max_pixel_value = max_pixel_value
        if psnr_max is not None:
            self.psnr_max = psnr_max
        if discretized_bpp_max is not None:
            self.discretized_bpp_max = discretized_bpp_max

    @property
    def bpp_scale(self):
        """Gets the bpp_scale of this RdOptimizerSettings.


        :return: The bpp_scale of this RdOptimizerSettings.
        :rtype: int
        """
        return self._bpp_scale

    @bpp_scale.setter
    def bpp_scale(self, bpp_scale):
        """Sets the bpp_scale of this RdOptimizerSettings.


        :param bpp_scale: The bpp_scale of this RdOptimizerSettings.
        :type: int
        """
        if bpp_scale is None:
            raise ValueError("Invalid value for `bpp_scale`, must not be `None`")
        self._bpp_scale = bpp_scale

    @property
    def bpp_max(self):
        """Gets the bpp_max of this RdOptimizerSettings.


        :return: The bpp_max of this RdOptimizerSettings.
        :rtype: float
        """
        return self._bpp_max

    @bpp_max.setter
    def bpp_max(self, bpp_max):
        """Sets the bpp_max of this RdOptimizerSettings.


        :param bpp_max: The bpp_max of this RdOptimizerSettings.
        :type: float
        """
        if bpp_max is None:
            raise ValueError("Invalid value for `bpp_max`, must not be `None`")
        self._bpp_max = bpp_max

    @property
    def max_q(self):
        """Gets the max_q of this RdOptimizerSettings.


        :return: The max_q of this RdOptimizerSettings.
        :rtype: int
        """
        return self._max_q

    @max_q.setter
    def max_q(self, max_q):
        """Sets the max_q of this RdOptimizerSettings.


        :param max_q: The max_q of this RdOptimizerSettings.
        :type: int
        """
        if max_q is None:
            raise ValueError("Invalid value for `max_q`, must not be `None`")
        self._max_q = max_q

    @property
    def min_q(self):
        """Gets the min_q of this RdOptimizerSettings.


        :return: The min_q of this RdOptimizerSettings.
        :rtype: int
        """
        return self._min_q

    @min_q.setter
    def min_q(self, min_q):
        """Sets the min_q of this RdOptimizerSettings.


        :param min_q: The min_q of this RdOptimizerSettings.
        :type: int
        """
        if min_q is None:
            raise ValueError("Invalid value for `min_q`, must not be `None`")
        self._min_q = min_q

    @property
    def max_pixel_value(self):
        """Gets the max_pixel_value of this RdOptimizerSettings.


        :return: The max_pixel_value of this RdOptimizerSettings.
        :rtype: int
        """
        return self._max_pixel_value

    @max_pixel_value.setter
    def max_pixel_value(self, max_pixel_value):
        """Sets the max_pixel_value of this RdOptimizerSettings.


        :param max_pixel_value: The max_pixel_value of this RdOptimizerSettings.
        :type: int
        """
        if max_pixel_value is None:
            raise ValueError("Invalid value for `max_pixel_value`, must not be `None`")
        self._max_pixel_value = max_pixel_value

    @property
    def psnr_max(self):
        """Gets the psnr_max of this RdOptimizerSettings.


        :return: The psnr_max of this RdOptimizerSettings.
        :rtype: int
        """
        return self._psnr_max

    @psnr_max.setter
    def psnr_max(self, psnr_max):
        """Sets the psnr_max of this RdOptimizerSettings.


        :param psnr_max: The psnr_max of this RdOptimizerSettings.
        :type: int
        """
        if psnr_max is None:
            raise ValueError("Invalid value for `psnr_max`, must not be `None`")
        self._psnr_max = psnr_max

    @property
    def discretized_bpp_max(self):
        """Gets the discretized_bpp_max of this RdOptimizerSettings.


        :return: The discretized_bpp_max of this RdOptimizerSettings.
        :rtype: int
        """
        return self._discretized_bpp_max

    @discretized_bpp_max.setter
    def discretized_bpp_max(self, discretized_bpp_max):
        """Sets the discretized_bpp_max of this RdOptimizerSettings.


        :param discretized_bpp_max: The discretized_bpp_max of this RdOptimizerSettings.
        :type: int
        """
        if discretized_bpp_max is None:
            raise ValueError("Invalid value for `discretized_bpp_max`, must not be `None`")
        self._discretized_bpp_max = discretized_bpp_max

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
        if not isinstance(other, RdOptimizerSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
