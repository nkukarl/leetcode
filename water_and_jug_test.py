from unittest import TestCase

from nose_parameterized import parameterized

from water_and_jug import Solution


class TestWaterAndJug(TestCase):
    @parameterized.expand([
        [
            {
                'x': 5,
                'y': 3,
                'z': 1,
            },
            True,
        ],
        [
            {
                'x': 9,
                'y': 3,
                'z': 4,
            },
            False,
        ],
    ])
    def test_can_measure_water(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.can_measure_water(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
