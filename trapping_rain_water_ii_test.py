from unittest import TestCase

from nose_parameterized import parameterized

from trapping_rain_water_ii import Solution


class TestTrappingRainWaterII(TestCase):
    @parameterized.expand([
        [
            {
                'map_height': [
                    [1, 4, 3, 1, 3, 2],
                    [3, 2, 1, 3, 2, 4],
                    [2, 3, 3, 2, 3, 1],
                ],
            },
            4,
        ],
        [
            {
                'map_height': [
                    [12, 13, 1, 12],
                    [13, 4, 13, 12],
                    [13, 8, 10, 12],
                    [12, 13, 12, 12],
                    [13, 13, 13, 13],
                ],
            },
            14,
        ],
        [
            {
                'map_height': [
                    [78, 16, 94, 36],
                    [87, 93, 50, 22],
                    [63, 28, 91, 60],
                    [64, 27, 41, 27],
                    [73, 37, 12, 69],
                    [68, 30, 83, 31],
                    [63, 24, 68, 36],
                ],
            },
            44,
        ]
    ])
    def test_trap_rain_water(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.trap_rain_water(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
