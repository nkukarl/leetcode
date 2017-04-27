from unittest import TestCase

from insert_delete_get_random import RandomizedSet


class TestInsertDeleteGetRandom(TestCase):
    def test_randomized_set(self):
        # Setup
        randomized_set = RandomizedSet()

        # Exercise and Verify
        self.assertTrue(randomized_set.insert(1))
        self.assertTrue(randomized_set.insert(2))
        self.assertTrue(randomized_set.insert(3))
        # Insert an existing element
        self.assertFalse(randomized_set.insert(1))
        self.assertTrue(randomized_set.remove(3))
        # Remove a non-existing element
        self.assertFalse(randomized_set.remove(4))
        self.assertIn(randomized_set.getRandom(), [1, 2, 3])
