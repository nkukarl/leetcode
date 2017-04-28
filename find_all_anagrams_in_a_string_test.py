from unittest import TestCase

from nose_parameterized import parameterized

from find_all_anagrams_in_a_string import Solution


class TestFindAllAnagramsInAString(TestCase):
    @parameterized.expand([
        [
            'cbaebabacd',
            'abc',
            [0, 6],
        ],
        [
            'abab',
            'ab',
            [0, 1, 2],
        ],
        [
            'a' * 1000000,
            'a' * 999999,
            [0, 1],
        ]
    ])
    def test_find_anagrams(self, s, word, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.find_anagrams(s, word)

        # Verify
        self.assertEqual(ans, expected_ans)
