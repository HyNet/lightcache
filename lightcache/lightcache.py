# -*-: coding:utf-8 -*-

'''

'''

from __future__ import unicode_literals, with_statement, print_function, division
import time
import hashlib
import pickle
from functools import update_wrapper
from utils import SingletonMixin


class MemoryAdapter(SingletonMixin):
    """ A Memory Adapter
    """
    _db = None

    def __init__(self, timeout=None):
        self.timeout = timeout
        if not MemoryAdapter._db:
            MemoryAdapter._db = {}

    def get(self, key):
        """get value cached by key
        """
        cache = MemoryAdapter._db.get(key, {})
        if time.time() - cache.get('time', 0) > 0:
            self.remove(key)
            return None
        else:
            return cache.get('value', None)

    def remove(self, key):
        """Remove cached value
        """
        return MemoryAdapter._db.pop(key, {}).get('value', None)

    def set(self, key, value):
        """set value cached
        """
        cache = {'value': value, 'time': time.time() + self.timeout}
        MemoryAdapter._db[key] = cache
        return value


def lightcache(timeout=None, adapter=MemoryAdapter):
    """light wight cache decorator
    """
    def wrap(func):
        """decorator
        """

        def _warp(*args, **kwargs):
            hash_key = hashlib.md5(pickle.dumps((func.__name__, args, kwargs))).hexdigest()
            adapter_instance = adapter(timeout=timeout)
            value = adapter_instance.get(hash_key)
            if not value:
                value = func(*args, **kwargs)
                adapter_instance.set(hash_key, value)
                return value
            else:
                return value
        return update_wrapper(_warp, func)
    return wrap
