from unittest import TestCase

from nose_parameterized import parameterized

from top_k_frequent_elements import Solution


class TestTopKFrequentElements(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [1, 1, 1, 1, 2, 2, 2, 3, 3, 4],
                'k': 2
            },
            [1, 2],
        ],
        [
            {
                'nums': [1, 1, 1, 1, 2, 2, 2, 3, 3, 4],
                'k': 3
            },
            [1, 2, 3],
        ],
    ])
    def test_top_k_frequent(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.top_k_frequent(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
