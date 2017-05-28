from unittest import TestCase

from nose_parameterized import parameterized

from first_unique_character_in_a_string import Solution


class TestFirstUniqueCharacterInAString(TestCase):
    @parameterized.expand([
        [
            {
                's': 'leetcode',
            },
            0,
        ],
        [
            {
                's': 'loveleetcode',
            },
            2,
        ],
    ])
    def test_first_unique_char(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.first_unique_char(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
