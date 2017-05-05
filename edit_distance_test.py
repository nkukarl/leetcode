from unittest import TestCase

from nose_parameterized import parameterized

from edit_distance import Solution


class TestEditDistance(TestCase):
    @parameterized.expand([
        [
            {
                'word1': '',
                'word2': '',
            },
            0,
        ],
        [
            {
                'word1': '',
                'word2': 'abc',
            },
            3,
        ],
        [
            {
                'word1': 'abc',
                'word2': 'abc',
            },
            0,
        ],
        [
            {
                'word1': 'zoologicoarchaeologist',
                'word2': 'zoogeologist',
            },
            10,
        ],
    ])
    def test_min_distance(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.min_distance(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
