import random
from unittest import TestCase

from insert_delete_get_random import RandomizedSet


class TestInsertDeleteGetRandom(TestCase):
    def test_randomized_set(self):
        # Setup
        randomized_set = RandomizedSet()
        vals = random.sample(list(range(100)), 4)

        # Exercise and Verify
        self.assertTrue(randomized_set.insert(vals[0]))
        self.assertTrue(randomized_set.insert(vals[1]))
        self.assertTrue(randomized_set.insert(vals[2]))
        # Insert an existing element
        self.assertFalse(randomized_set.insert(vals[0]))
        self.assertTrue(randomized_set.remove(vals[1]))
        # Remove a non-existing element
        self.assertFalse(randomized_set.remove(vals[3]))
        self.assertIn(randomized_set.get_random(), [vals[0], vals[2], vals[3]])
        self.assertTrue(randomized_set.insert(vals[1]))
        self.assertIn(randomized_set.get_random(), vals)
