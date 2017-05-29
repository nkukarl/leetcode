from unittest import TestCase

from nose_parameterized import parameterized

from next_greater_element_i import Solution


class TestNextGreaterElementI(TestCase):
    @parameterized.expand([
        [
            {
                'find_nums': [4, 1, 2],
                'nums': [1, 3, 4, 2],
            },
            [-1, 3, -1],
        ],
        [
            {
                'find_nums': [2, 4],
                'nums': [1, 2, 3, 4],
            },
            [3, -1],
        ],
    ])
    def test_next_greater_element(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.next_greater_element(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
