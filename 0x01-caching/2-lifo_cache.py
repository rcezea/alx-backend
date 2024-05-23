#!/usr/bin/env python3
"""Extend the base class"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    def put(self, key, item):
        """Basic Caching class"""
        if key and item:
            if key in self.cache_data.keys():
                self.cache_data.pop(key)
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            items = list(self.cache_data.items())
            key, value = items.pop(-2)
            self.cache_data = dict(items)
            print(f"DISCARD: {key}")

    def get(self, key):
        """ Get an item by key """
        if key:
            return self.cache_data[key] if key in self.cache_data else None
