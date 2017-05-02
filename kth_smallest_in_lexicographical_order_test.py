from unittest import TestCase

from nose_parameterized import parameterized

from kth_smallest_in_lexicographical_order import Solution


class TestKthSmallestInLexicographicalOrder(TestCase):
    @parameterized.expand([
        [
            # 1, 10, 11, 12, 13, 14, 15, 2, 3, 4, 5, 6, 7, 8, 9
            {
                'n': 15,
                'k': 3,
            },
            11,
        ],
        [
            # 1, 10, 11, 12, 13, 14, 15, 2, 3, 4, 5, 6, 7, 8, 9
            {
                'n': 15,
                'k': 10,
            },
            4,
        ],
    ])
    def test_find_kth_number(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.find_kth_number(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
