from unittest import TestCase

from nose_parameterized import parameterized

from arithmetic_slices import Solution


class TestArithmeticSlices(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [1],
            },
            0
        ],
        [
            {
                'nums': [1, 2, 3, 4, 5],
            },
            6,
        ],
        [
            {
                'nums': [1, 2, 3, 5, 7],
            },
            2,
        ],
        [
            {
                'nums': [1, 2, 3, 4, 5, 7, 10, 13, 16],
            },
            9,
        ]
    ])
    def test_number_of_arithmetic_slices(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.number_of_arithmetic_slices(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
