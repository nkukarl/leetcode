from unittest import TestCase

from nose_parameterized import parameterized

from kth_smallest_element_in_a_sorted_matrix import Solution


class TestKthSmallestElementInASortedMatrix(TestCase):
    @parameterized.expand([
        [
            {
                'matrix': [
                    [1, 5, 9],
                    [10, 11, 13],
                    [12, 13, 15],
                ],
                'k': 8,
            },
            13,
        ],
    ])
    def test_kth_smallest(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.kth_smallest(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
