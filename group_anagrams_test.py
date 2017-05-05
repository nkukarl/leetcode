from unittest import TestCase

from nose_parameterized import parameterized

from group_anagrams import Solution


class TestGroupAnagrams(TestCase):
    @parameterized.expand([
        [
            {
                'strs': ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'],
            },
            [
                ['eat', 'tea', 'ate'],
                ['tan', 'nat'],
                ['bat'],
            ],
        ],
    ])
    def test_group_anagrams(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.group_anagrams(**kwargs)

        # Verify
        self.assertEqual(sorted(ans), sorted(expected_ans))
