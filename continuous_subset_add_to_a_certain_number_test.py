from unittest import TestCase

from nose_parameterized import parameterized

from continuous_subset_add_to_a_certain_number import Solution


class TestContinuousSubsetAddToACertainNumber(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [1, 1, 1, 1, 1],
                'subtotal': 5,
            },
            [0, 4],
        ],
        [
            {
                'nums': [1, 2, 3, 4],
                'subtotal': 6,
            },
            [0, 2],
        ],
    ])
    def test_get_continuous_subset(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.get_continuous_subset(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
