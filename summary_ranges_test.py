from unittest import TestCase

from nose_parameterized import parameterized

from summary_ranges import Solution


class TestSummaryRanges(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [0, 1, 2, 4, 5, 7],
            },
            ['0->2', '4->5', '7'],
        ],
        [
            {
                'nums': [0, 1, 2, 3, 5, 7],
            },
            ['0->3', '5', '7'],
        ],
        [
            {
                'nums': [],
            },
            [],
        ],
        [
            {
                'nums': [1],
            },
            ['1'],
        ],
    ])
    def test_summary_ranges(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.summary_ranges(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
