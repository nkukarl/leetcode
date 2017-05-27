from unittest import TestCase

from nose_parameterized import parameterized

from intersection_of_two_arrays_ii import Solution


class TestIntersectionOfTwoArraysII(TestCase):
    @parameterized.expand([
        [
            {
                'nums1': [1, 2, 2, 1],
                'nums2': [2, 4, 2],
            },
            [2, 2],
        ],
    ])
    def test_intersect(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.intersect(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
