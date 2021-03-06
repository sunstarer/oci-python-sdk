# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SearchResultCollection(object):
    """
    The list of search result items matching the criteria returned from the search operation. Search errors and
    messages, if any , will be part of the standard error response.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SearchResultCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param count:
            The value to assign to the count property of this SearchResultCollection.
        :type count: int

        :param items:
            The value to assign to the items property of this SearchResultCollection.
        :type items: list[SearchResult]

        """
        self.swagger_types = {
            'count': 'int',
            'items': 'list[SearchResult]'
        }

        self.attribute_map = {
            'count': 'count',
            'items': 'items'
        }

        self._count = None
        self._items = None

    @property
    def count(self):
        """
        Gets the count of this SearchResultCollection.
        Total number of items returned.


        :return: The count of this SearchResultCollection.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this SearchResultCollection.
        Total number of items returned.


        :param count: The count of this SearchResultCollection.
        :type: int
        """
        self._count = count

    @property
    def items(self):
        """
        Gets the items of this SearchResultCollection.
        Search result set.


        :return: The items of this SearchResultCollection.
        :rtype: list[SearchResult]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this SearchResultCollection.
        Search result set.


        :param items: The items of this SearchResultCollection.
        :type: list[SearchResult]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
