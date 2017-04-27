import copy
import random
from unittest import TestCase

from insert_delete_get_random_duplicates_allowed import RandomizedCollection


class TestInsertDeleteGetRandomDuplicatesAllowed(TestCase):
    def test_randomized_collection(self):
        # Setup
        randomized_collection = RandomizedCollection()

        # Exercise and Verify
        self.assertTrue(randomized_collection.insert(0))
        self.assertTrue(randomized_collection.insert(1))
        self.assertFalse(randomized_collection.insert(0))
        self.assertTrue(randomized_collection.remove(0))
        self.assertTrue(randomized_collection.insert(-1))
        self.assertTrue(randomized_collection.remove(0))
        self.assertFalse(randomized_collection.remove(0))
        self.assertIn(randomized_collection.get_random(), [1, -1])

    def test_pop_from_set(self):
        # Setup
        randomized_collection = RandomizedCollection()
        s = set(random.sample(list(range(100)), random.randint(1, 9)))
        s_ = copy.deepcopy(s)

        # Exercise
        e = randomized_collection.pop_from_set(s)

        # Verify
        self.assertNotIn(e, s)
        self.assertIn(e, s_)
