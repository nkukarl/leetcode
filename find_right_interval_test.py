from unittest import TestCase

from nose_parameterized import parameterized

from find_right_interval import Solution


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class TestFindRightInterval(TestCase):
    @parameterized.expand([
        [
            [
                [2, 5], [9, 13], [11, 15], [21, 23], [4, 7], [15, 37],
            ],
            [1, 5, 5, -1, 1, -1],
        ],
        [
            [
                [1, 4], [2, 3], [3, 4],
            ],
            [-1, 2, -1],
        ],
        [
            [
                [1, 2],
            ],
            [-1],
        ],
        [
            [
                [3, 4], [2, 3], [1, 2],
            ],
            [-1, 0, 1],
        ],
    ])
    def test_find_right_interval(self, intervals_raw, expected_ans):
        # Setup
        sol = Solution()
        intervals = [Interval(*ir) for ir in intervals_raw]

        # Exercise
        ans = sol.find_right_interval(intervals)

        # Verify
        self.assertEqual(ans, expected_ans)
