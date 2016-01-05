# -*- coding: utf-8 -*-

"""
lightcache Tests

"""

import os
import sys
import unittest
import time
import random

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from lightcache import lightcache

class LightcacheTestCase(unittest.TestCase):

    def test_set_cache(self):

        @lightcache(timeout = 4)
        def cached_function(t = 2):
            time.sleep(t)
            return random.randint(1, 100)

        val_pre = cached_function()
        val = cached_function()
        self.assertEqual(val, val_pre)
        time.sleep(6)
        val = cached_function()
        self.assertNotEqual(val, val_pre)

    def test_cache_time(self):

        @lightcache(timeout=4)
        def cached_function(t=1):
            time.sleep(t)
            return random.randint(1, 100)

        cached_function()
        start = time.clock()
        cached_function()
        self.assertTrue((time.clock() - start) < 1)


if __name__ == "__main__":
    unittest.main()
