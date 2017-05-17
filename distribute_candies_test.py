from unittest import TestCase

from nose_parameterized import parameterized

from distribute_candies import Solution


class TestDistributeCandies(TestCase):
    @parameterized.expand([
        [
            {
                'candies': ['a', 'a', 'b', 'b', 'c', 'c'],
            },
            3,
        ],
        [
            {
                'candies': ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'e'],
            },
            4,
        ],
        [
            {
                'candies': ['a', 'a', 'b', 'c'],
            },
            2,
        ],
    ])
    def test_distribute_candies(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.distribute_candies(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
