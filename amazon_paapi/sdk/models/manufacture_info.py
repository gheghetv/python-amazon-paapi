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

from .single_string_valued_attribute import SingleStringValuedAttribute  # noqa: F401,E501


class ManufactureInfo(object):
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
        'item_part_number': 'SingleStringValuedAttribute',
        'model': 'SingleStringValuedAttribute',
        'warranty': 'SingleStringValuedAttribute'
    }

    attribute_map = {
        'item_part_number': 'ItemPartNumber',
        'model': 'Model',
        'warranty': 'Warranty'
    }

    def __init__(self, item_part_number=None, model=None, warranty=None):  # noqa: E501
        """ManufactureInfo - a model defined in Swagger"""  # noqa: E501

        self._item_part_number = None
        self._model = None
        self._warranty = None
        self.discriminator = None

        if item_part_number is not None:
            self.item_part_number = item_part_number
        if model is not None:
            self.model = model
        if warranty is not None:
            self.warranty = warranty

    @property
    def item_part_number(self):
        """Gets the item_part_number of this ManufactureInfo.  # noqa: E501


        :return: The item_part_number of this ManufactureInfo.  # noqa: E501
        :rtype: SingleStringValuedAttribute
        """
        return self._item_part_number

    @item_part_number.setter
    def item_part_number(self, item_part_number):
        """Sets the item_part_number of this ManufactureInfo.


        :param item_part_number: The item_part_number of this ManufactureInfo.  # noqa: E501
        :type: SingleStringValuedAttribute
        """

        self._item_part_number = item_part_number

    @property
    def model(self):
        """Gets the model of this ManufactureInfo.  # noqa: E501


        :return: The model of this ManufactureInfo.  # noqa: E501
        :rtype: SingleStringValuedAttribute
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this ManufactureInfo.


        :param model: The model of this ManufactureInfo.  # noqa: E501
        :type: SingleStringValuedAttribute
        """

        self._model = model

    @property
    def warranty(self):
        """Gets the warranty of this ManufactureInfo.  # noqa: E501


        :return: The warranty of this ManufactureInfo.  # noqa: E501
        :rtype: SingleStringValuedAttribute
        """
        return self._warranty

    @warranty.setter
    def warranty(self, warranty):
        """Sets the warranty of this ManufactureInfo.


        :param warranty: The warranty of this ManufactureInfo.  # noqa: E501
        :type: SingleStringValuedAttribute
        """

        self._warranty = warranty

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
        if issubclass(ManufactureInfo, dict):
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
        if not isinstance(other, ManufactureInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
