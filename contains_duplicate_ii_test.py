from unittest import TestCase

from nose_parameterized import parameterized

from contains_duplicate_ii import Solution


class TestContainsDuplicateII(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [1, 2, 3, 1, 2, 3],
                'k': 2,
            },
            False,
        ],
        [
            {
                'nums': [1, 2, 3, 1, 2, 3],
                'k': 3,
            },
            True,
        ],
    ])
    def test_contains_nearby_duplicate(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.contains_nearby_duplicate(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
