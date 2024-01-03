#!/usr/bin/env python3
""" BaseCaching module documentation for MRUCache class
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    FIFOCache defines a FIFO caching system
    Implements a caching system using the MRU
    (Most Recently Used) algorithm.
    """

    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.order_of_access = []

    def put(self, key, item):
        """
        Cache a key-value pair
        If key or item is None, this method does nothing.
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order_of_access[-1]))
                del self.cache_data[self.order_of_access[-1]]
                del self.order_of_access[-1]
            if key in self.order_of_access:
                del self.order_of_access[self.order_of_access.index(key)]
            self.order_of_access.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to a given key,
        If key is None or if the key doesn’t exist in
        self.cache_data, returns None.
        """
        if key is not None and key in self.cache_data.keys():
            del self.order_of_access[self.order_of_access.index(key)]
            self.order_of_access.append(key)
            return self.cache_data[key]
        return None
