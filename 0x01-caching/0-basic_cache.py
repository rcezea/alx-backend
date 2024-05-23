#!/usr/bin/env python3
"""Extend the base class"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic Caching class"""
    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key:
            return self.cache_data[key] if key in self.cache_data else None
