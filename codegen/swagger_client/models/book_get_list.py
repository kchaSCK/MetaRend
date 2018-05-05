# coding: utf-8

"""
    SAFRS Demo Application

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BookGetList(object):
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
        'args': 'str',
        'method': 'str'
    }

    attribute_map = {
        'args': 'args',
        'method': 'method'
    }

    def __init__(self, args=None, method=None):  # noqa: E501
        """BookGetList - a model defined in Swagger"""  # noqa: E501

        self._args = None
        self._method = None
        self.discriminator = None

        if args is not None:
            self.args = args
        if method is not None:
            self.method = method

    @property
    def args(self):
        """Gets the args of this BookGetList.  # noqa: E501


        :return: The args of this BookGetList.  # noqa: E501
        :rtype: str
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this BookGetList.


        :param args: The args of this BookGetList.  # noqa: E501
        :type: str
        """

        self._args = args

    @property
    def method(self):
        """Gets the method of this BookGetList.  # noqa: E501


        :return: The method of this BookGetList.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this BookGetList.


        :param method: The method of this BookGetList.  # noqa: E501
        :type: str
        """

        self._method = method

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
        if not isinstance(other, BookGetList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
