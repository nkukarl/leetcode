from unittest import TestCase

from nose_parameterized import parameterized

from third_maximum_number import Solution


class TestThirdMaximumNumber(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [1, 2, 3, 4, 5],
            },
            3,
        ],
        [
            {
                'nums': [1, 2, 2, 2, 3],
            },
            1,
        ],
        [
            {
                'nums': [1, 2, 2, 2, 2],
            },
            2,
        ],
    ])
    def test_third_max(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.third_max(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
