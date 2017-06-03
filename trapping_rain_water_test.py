from unittest import TestCase

from nose_parameterized import parameterized

from trapping_rain_water import Solution


class TestTrappingRainWater(TestCase):
    @parameterized.expand([
        [
            {
                'heights': [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
            },
            6,
        ],
    ])
    def test_trap(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.trap(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
