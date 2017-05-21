from unittest import TestCase

from nose_parameterized import parameterized

from integer_to_roman import Solution


class TestIntegerToRoman(TestCase):
    @parameterized.expand([
        [
            {
                'num': 1234,
            },
            'MCCXXXIV',
        ],
        [
            {
                'num': 3721,
            },
            'MMMDCCXXI',
        ],
    ])
    def test_int_to_roman(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.int_to_roman(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
