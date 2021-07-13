# coding: utf-8

"""
  Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.

  Licensed under the Apache License, Version 2.0 (the "License").
  You may not use this file except in compliance with the License.
  A copy of the License is located at

      http://www.apache.org/licenses/LICENSE-2.0

  or in the "license" file accompanying this file. This file is distributed
  on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
  express or implied. See the License for the specific language governing
  permissions and limitations under the License.
"""


"""
    ProductAdvertisingAPI

    https://webservices.amazon.com/paapi5/documentation/index.html  # noqa: E501
"""


import pprint
import re  # noqa: F401

import six

from .item import Item  # noqa: F401,E501
from .variation_summary import VariationSummary  # noqa: F401,E501


class VariationsResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'items': 'list[Item]',
        'variation_summary': 'VariationSummary'
    }

    attribute_map = {
        'items': 'Items',
        'variation_summary': 'VariationSummary'
    }

    def __init__(self, items=None, variation_summary=None):  # noqa: E501
        """VariationsResult - a model defined in Swagger"""  # noqa: E501

        self._items = None
        self._variation_summary = None
        self.discriminator = None

        if items is not None:
            self.items = items
        if variation_summary is not None:
            self.variation_summary = variation_summary

    @property
    def items(self):
        """Gets the items of this VariationsResult.  # noqa: E501


        :return: The items of this VariationsResult.  # noqa: E501
        :rtype: list[Item]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this VariationsResult.


        :param items: The items of this VariationsResult.  # noqa: E501
        :type: list[Item]
        """

        self._items = items

    @property
    def variation_summary(self):
        """Gets the variation_summary of this VariationsResult.  # noqa: E501


        :return: The variation_summary of this VariationsResult.  # noqa: E501
        :rtype: VariationSummary
        """
        return self._variation_summary

    @variation_summary.setter
    def variation_summary(self, variation_summary):
        """Sets the variation_summary of this VariationsResult.


        :param variation_summary: The variation_summary of this VariationsResult.  # noqa: E501
        :type: VariationSummary
        """

        self._variation_summary = variation_summary

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
        if issubclass(VariationsResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VariationsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
