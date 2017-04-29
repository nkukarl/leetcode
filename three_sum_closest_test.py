from unittest import TestCase

from nose_parameterized import parameterized

from three_sum_closest import Solution


class TestThreeSumClosest(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [0, 0, 0],
                'target': 1,
            },
            0,
        ],
        [
            {
                'nums': [1, 1, 1, 0],
                'target': 100,
            },
            3,
        ],
        [
            {
                'nums': [1, 2, -1, 4],
                'target': 1,
            },
            2,
        ],
        [
            {
                'nums': [1, 2, -1, -4],
                'target': 1,
            },
            2,
        ],
    ])
    def test_three_sum_closest(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.three_sum_closest(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
