from unittest import TestCase

from nose_parameterized import parameterized

from house_robber import Solution


class TestHouseRobber(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [],
            },
            0,
        ],
        [
            {
                'nums': [1],
            },
            1,
        ],
        [
            {
                'nums': [1, 2],
            },
            2,
        ],
        [
            {
                'nums': [1, 3, 2, 4, 1, 5, 2, 6],
            },
            18,
        ],
        [
            {
                'nums': [4, 3, 1, 3, 6, 2, 1, 4, 5, 6],
            },
            21,
        ]
    ])
    def test_rob(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.rob(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
