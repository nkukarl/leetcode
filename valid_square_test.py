from unittest import TestCase

from nose_parameterized import parameterized

from valid_square import Solution


class TestValidSquare(TestCase):
    @parameterized.expand([
        [
            {
                'p1': [0, 1],
                'p2': [1, 0],
                'p3': [1, 1],
                'p4': [0, 0],
            },
            True,
        ],
    ])
    def test_valid_square(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.valid_square(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
