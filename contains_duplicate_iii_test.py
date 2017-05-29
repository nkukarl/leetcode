from unittest import TestCase

from nose_parameterized import parameterized

from contains_duplicate_iii import Solution


class TestContainsDuplicateIII(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [1, 100, 20, 70],
                'k': 1,
                't': 40,
            },
        ],
        [
            {
                'nums': [1, 100, 20, 70],
                'k': 2,
                't': 40,
            },
        ],
    ])
    def test_contains_nearby_almost_duplicate(self, kwargs):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.contains_nearby_almost_duplicate(**kwargs)

        # Verify
        expected_ans = self.contains_nearby_almost_duplicate(**kwargs)
        self.assertEqual(ans, expected_ans)

    def contains_nearby_almost_duplicate(self, nums, k, t):
        N = len(nums)
        for i in range(N - 1):
            for n in nums[i + 1 : i + k + 1]:
                if abs(n - nums[i]) <= t:
                    return True
        return False
