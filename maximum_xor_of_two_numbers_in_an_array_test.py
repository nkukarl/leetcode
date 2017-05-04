from unittest import TestCase

from nose_parameterized import parameterized

from maximum_xor_of_two_numbers_in_an_array import Solution


class TestMaximumXOROfTwoNumbersInAnArray(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [3, 10, 5, 25, 2, 8],
            },
        ],
        [
            {
                'nums': [0, 1, 2, 3, 4, 5, 6, 7],
            },
        ],
    ])
    def test_find_maximum_xor(self, kwargs):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.find_maximum_xor(**kwargs)

        # Verify
        expected_ans = self.find_maximum_xor(**kwargs)
        self.assertEqual(ans, expected_ans)

    def find_maximum_xor(self, nums):
        """

        O(N^2) solution

        Args:
            nums:

        Returns:

        """
        max_xor = 0
        N = len(nums)
        for i in range(N):
            for j in range(i + 1, N):
                n1, n2 = nums[i], nums[j]
                # print(n1, n2, n1 ^ n2)
                max_xor = max(max_xor, n1 ^ n2)
        return max_xor
