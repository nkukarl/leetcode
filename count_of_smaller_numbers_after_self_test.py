from unittest import TestCase

from nose_parameterized import parameterized

from count_of_smaller_numbers_after_self import Solution


class TestCountOfSmallerNumbersAfterSelf(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [5, 2, 6, 1],
            },
            [2, 1, 1, 0],
        ],
        [
            {
                'nums': [3, 4, 2, 1, 5, 6, 2, 3, 4, 5, 4],
            },
            [3, 4, 1, 0, 4, 5, 0, 0, 0, 1, 0],
        ],
    ])
    def test_count_smaller(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.count_smaller(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
