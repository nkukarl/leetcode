from unittest import TestCase

from nose_parameterized import parameterized

from max_points_on_a_line import Solution


class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class TestMaxPointsOnALine(TestCase):
    @parameterized.expand([
        [
            {
                'points': [
                    Point(1, 1), Point(2, 2), Point(3, 3), Point(3, 2),
                ],
            },
            3,
        ],
        [
            {
                'points': [
                    Point(1, 2), Point(2, 1), Point(3, 4), Point(7, 8),
                    Point(4, 5), Point(5, 4), Point(2, 1), Point(3, 3),
                    Point(2, 0),
                ],
            },
            4,
        ],
        [
            {
                'points': [
                    Point(1, 1), Point(1, 1), Point(1, 1),
                ],
            },
            3,
        ],
        [
            {
                'points': [
                    Point(0, 0), Point(94911151, 94911150),
                    Point(94911152, 94911151),
                ],
            },
            2,
        ],
    ])
    def test_max_points(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.max_points(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
