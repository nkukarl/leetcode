from unittest import TestCase

from all_one_data_structure import AllOne


class TestAllOneDateStructure(TestCase):
    def test_all_one_ab(self):
        # Setup
        all_one = AllOne()
        key1 = 'a'
        key2 = 'b'

        # Exercise and Verify
        all_one.inc(key1)
        self.assertEqual(all_one.get_max_key(), key1)
        self.assertEqual(all_one.get_min_key(), key1)
        all_one.inc(key1)
        all_one.inc(key1)
        all_one.inc(key2)
        self.assertEqual(all_one.get_max_key(), key1)
        self.assertEqual(all_one.get_min_key(), key2)
        all_one.inc(key2)
        all_one.inc(key2)
        all_one.inc(key2)
        self.assertEqual(all_one.get_max_key(), key2)
        self.assertEqual(all_one.get_min_key(), key1)
        all_one.dec(key2)
        all_one.dec(key2)
        self.assertEqual(all_one.get_max_key(), key1)
        self.assertEqual(all_one.get_min_key(), key2)

    def test_all_one_abc(self):
        # Setup
        all_one = AllOne()
        key1 = 'a'
        key2 = 'b'
        key3 = 'c'

        # Exercise and Verify
        all_one.inc(key1)
        all_one.inc(key2)
        all_one.inc(key2)
        all_one.inc(key3)
        all_one.inc(key3)
        all_one.inc(key3)
        all_one.dec(key2)
        all_one.dec(key2)
        self.assertEqual(all_one.get_min_key(), key1)
        all_one.dec(key1)
        self.assertEqual(all_one.get_max_key(), key3)
        self.assertEqual(all_one.get_min_key(), key3)
