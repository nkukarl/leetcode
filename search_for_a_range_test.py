from unittest import TestCase

from nose_parameterized import parameterized

from search_for_a_range import Solution


class TestSearchForARange(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [],
                'target': 0,
            },
            [-1, -1],
        ],
        [
            {
                'nums': [5, 7, 7, 8, 8, 10, 10],
                'target': 6,
            },
            [-1, -1],
        ],
        [
            {
                'nums': [5, 7, 7, 8, 9, 10, 10],
                'target': 9,
            },
            [4, 4],
        ],
        [
            {
                'nums': [5, 7, 7, 8, 8, 10, 10],
                'target': 8,
            },
            [3, 4],
        ],
        [
            {
                'nums': [5, 7, 7, 8, 8, 10, 10],
                'target': 10,
            },
            [5, 6],
        ],
    ])
    def test_search_range(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.search_range(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
