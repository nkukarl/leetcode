from unittest import TestCase

from nose_parameterized import parameterized

from roman_to_integer import Solution


class TestRomanToInteger(TestCase):
    @parameterized.expand([
        [
            {
                's': 'MMMCDXXI',
            },
            3421,
        ],
        [
            {
                's': 'CMLXXXVII',
            },
            987,
        ],
    ])
    def test_roman_to_int(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.roman_to_int(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
