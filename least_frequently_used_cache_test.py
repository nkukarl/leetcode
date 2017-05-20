from unittest import TestCase

from least_frequently_used_cache import LFUCache


class TestLeastFrequentlyUsedCache(TestCase):
    def test_lfu_cache(self):
        # Setup
        lfu_cache = LFUCache(2)

        # Exercise and Verify
        lfu_cache.put(1, 100)
        lfu_cache.put(2, 200)
        self.assertEqual(lfu_cache.get(1), 100)
        lfu_cache.put(3, 300)
        self.assertEqual(lfu_cache.get(2), -1)
        self.assertEqual(lfu_cache.get(3), 300)
        lfu_cache.put(4, 400)
        self.assertEqual(lfu_cache.get(1), -1)
        self.assertEqual(lfu_cache.get(3), 300)
        self.assertEqual(lfu_cache.get(4), 400)
