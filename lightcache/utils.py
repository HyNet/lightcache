# -*- coding: utf-8 -*-

"""
   lightcache.utils
   ~~~~~~~~~~~~~~~~

   This module implements various utilities for lightcache
"""

import threading

class SingletonMixin(object):
    """A thread safe singleton
    """
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(SingletonMixin, '_instance'):
            with SingletonMixin._instance_lock:
                if not hasattr(SingletonMixin, '_instance'):
                    SingletonMixin._instance = super(SingletonMixin, cls).__new__(cls, *args, **kwargs)
        return SingletonMixin._instance
