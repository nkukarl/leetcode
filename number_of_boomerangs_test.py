from unittest import TestCase

from nose_parameterized import parameterized

from number_of_boomerangs import Solution


class TestNumberOfBoomerangs(TestCase):
    @parameterized.expand([
        # [
        #     {
        #         'points': [[0, 0], [1, 0], [2, 0]],
        #     },
        #     2,
        # ],
        [
            {
                'points': [
                    [0, 0], [1, 0], [-1, 0], [0, 1], [0, -1],
                ],
            },
            20
        ]
    ])
    def test_number_of_boomerangs(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.number_of_boomerangs(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
