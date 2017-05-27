from unittest import TestCase

from nose_parameterized import parameterized

from minimum_moves_to_equal_array_elements import Solution


class TestMinimumMovesToEqualArrayElements(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [],
            },
            0
        ],
        [
            {
                'nums': [2, 3, 5, 7],
            },
            9,
        ],
        [
            {
                'nums': [1, 3, 7],
            },
            8,
        ],
    ])
    def test_min_moves(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.min_moves(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
