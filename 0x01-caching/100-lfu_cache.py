#!/usr/bin/env python3
""" BaseCaching module documentation for LFUCache class
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    FIFOCache defines a FIFO caching system
    """

    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        self.order_of_access = []
        self.frequency = {}

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
                lfu = min(self.frequency.values())
                lfu_keys = []
                for k, v in self.frequency.items():
                    if v == lfu:
                        lfu_keys.append(k)
                if len(lfu_keys) > 1:
                    lru_lfu = {}
                    for k in lfu_keys:
                        lru_lfu[k] = self.order_of_access.index(k)
                    discard = min(lru_lfu.values())
                    discard = self.order_of_access[discard]
                else:
                    discard = lfu_keys[0]

                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]
                del self.order_of_access[self.order_of_access.index(discard)]
                del self.frequency[discard]
            # update usage frequency
            if key in self.frequency:
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1
            if key in self.order_of_access:
                del self.order_of_access[self.order_of_access.index(key)]
            self.order_of_access.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to a given key,
        If key is None or if the key doesn’t exist returns None.
        """
        if key is not None and key in self.cache_data.keys():
            del self.order_of_access[self.order_of_access.index(key)]
            self.order_of_access.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
