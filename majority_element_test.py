from unittest import TestCase

from nose_parameterized import parameterized

from majority_element import Solution


class TestMajorityElement(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [1, 2, 3, 1, 2, 3, 1],
            },
            1,
        ],
        [
            {
                'nums': [1, 2, 2, 1, 2, 2],
            },
            2,
        ],
        [
            {
                'nums': [2],
            },
            2,
        ],
    ])
    def test_majority_element(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.majority_element(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
