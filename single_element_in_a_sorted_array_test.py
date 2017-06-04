from unittest import TestCase

from nose_parameterized import parameterized

from single_element_in_a_sorted_array import Solution


class TestSingleElementInASortedArray(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [1, 1, 2, 3, 3],
            },
            2,
        ],
        [
            {
                'nums': [1, 1, 2, 3, 3, 4, 4],
            },
            2,
        ],
        [
            {
                'nums': [1, 1, 2, 2, 3, 3, 4, 4, 5],
            },
            5,
        ],
        [
            {
                'nums': [1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6],
            },
            5,
        ],
        [
            {
                'nums': [1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 7],
            },
            5,
        ],
    ])
    def test_single_non_duplicate(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.single_non_duplicate(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
