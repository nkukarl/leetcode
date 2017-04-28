from unittest import TestCase

from nose_parameterized import parameterized

from contiguous_array import Solution


class TestContiguousArray(TestCase):
    @parameterized.expand([
        [
            [1, 0, 1],
            2,
        ],
        [
            [1, 0, 1, 0, 1, 0, 1],
            6,
        ],
    ])
    def test_find_max_length(self, nums, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.find_max_length(nums)

        # Verify
        self.assertEqual(ans, expected_ans)

    @parameterized.expand([
        [
            [1, 1, 0, 1],
            [1, 2, 1, 2],
        ],
        [
            [1, 0, 1, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 2, 1, 2, 1, 0, 1],
        ],
    ])
    def test_summarise(self, nums, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.summarise(nums)

        # Verify
        self.assertEqual(ans, expected_ans)
