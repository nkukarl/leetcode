from unittest import TestCase

from nose_parameterized import parameterized

from rotate_function import Solution


class TestRotateFunction(TestCase):
    @parameterized.expand([
        [
            [4, 3, 2, 6],
            26,
        ],
    ])
    def test_max_rotate_function(self, nums, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.max_rotate_function(nums)

        # Verify
        self.assertEqual(ans, expected_ans)
