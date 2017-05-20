from unittest import TestCase

from least_recently_used_cache import LRUCache


class TestLeastRecentlyUsedCache(TestCase):
    def test_lru_cache_1(self):
        # Setup
        lru_cache = LRUCache(2)

        # Exercise and Verify
        lru_cache.put(1, 100)
        lru_cache.put(2, 200)
        self.assertEqual(lru_cache.get(1), 100)
        lru_cache.put(3, 300)
        self.assertEqual(lru_cache.get(2), -1)
        lru_cache.put(4, 400)
        self.assertEqual(lru_cache.get(1), -1)
        self.assertEqual(lru_cache.get(3), 300)
        self.assertEqual(lru_cache.get(4), 400)

    def test_lru_cache_2(self):
        # Setup
        lru_cache = LRUCache(1)

        # Exercise and Verify
        lru_cache.put(2, 100)
        self.assertEqual(lru_cache.get(2), 100)
        lru_cache.put(3, 200)
        self.assertEqual(lru_cache.get(2), -1)
        self.assertEqual(lru_cache.get(3), 200)
