#!/usr/bin/env python3
"""Extend the base class"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Basic Caching class"""
    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            items = list(self.cache_data.items())
            key, value = items.pop(0)
            self.cache_data = dict(items)
            print(f"DISCARD: {key}")

    def get(self, key):
        """ Get an item by key """
        if key:
            return self.cache_data[key] if key in self.cache_data else None
