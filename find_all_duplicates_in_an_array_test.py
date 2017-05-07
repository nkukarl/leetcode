import random
from unittest import TestCase

from nose_parameterized import parameterized

from find_all_duplicates_in_an_array import Solution


class TestFindAllDuplicatesInAnArray(TestCase):
    def test_find_duplicates(self):
        # Setup
        sol = Solution()
        nums = [i for i in range(10)]
        extras = [random.randint(1, 10) for _ in range(random.randint(0, 5))]
        nums += extras
        random.shuffle(nums)

        # Exercise
        duplicates = sol.find_duplicates(nums)

        # Verify
        expected_duplicates = list(set(extras))
        self.assertEqual(sorted(duplicates), sorted(expected_duplicates))
