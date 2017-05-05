from unittest import TestCase

from nose_parameterized import parameterized

from container_with_most_water import Solution


class TestContainerWithMostWater(TestCase):
    @parameterized.expand([
        [
            {
                'heights': [1, 1]
            },
            1,
        ],
        [
            {
                'heights': [1, 3, 4]
            },
            3,
        ],
        [
            {
                'heights': [1, 3, 4, 2, 5, 1, 2, 4, 5, 6, 2, 4, 5, 6]
            },
            45,
        ],
    ])
    def test_get_max_area(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.get_max_area(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
