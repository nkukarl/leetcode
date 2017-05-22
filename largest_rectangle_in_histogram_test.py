from unittest import TestCase

from nose_parameterized import parameterized

from largest_rectangle_in_histogram import Solution


class TestLargestRectangleInHistogram(TestCase):
    @parameterized.expand([
        [
            {
                'heights': [2, 1, 5, 6, 2, 3],
            },
            10,
        ],
    ])
    def test_largest_rectangle_area(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.largest_rectangle_area(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
