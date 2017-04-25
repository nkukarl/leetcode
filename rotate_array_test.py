from unittest import TestCase

from rotate_array import Solution


class TestRotateArray(TestCase):
    def test_rotate(self):
        # Setup
        sol = Solution()
        nums = [1, 2, 3, 4, 5, 6, 7]

        # Exercise
        sol.rotate(nums, 2)

        # Verify
        self.assertEqual(nums, [6, 7, 1, 2, 3, 4, 5])
