from unittest import TestCase

from nose_parameterized import parameterized

from letter_combinations_of_a_phone_number import Solution


class TestLetterCombinationsOfAPhoneNumber(TestCase):
    @parameterized.expand([
        [
            '23',
            [
                'ad', 'ae', 'af',
                'bd', 'be', 'bf',
                'cd', 'ce', 'cf',
            ]
        ],
        [
            '495',
            [
                'gwj', 'gwk', 'gwl', 'gxj', 'gxk', 'gxl',
                'gyj', 'gyk', 'gyl', 'gzj', 'gzk', 'gzl',
                'hwj', 'hwk', 'hwl', 'hxj', 'hxk', 'hxl',
                'hyj', 'hyk', 'hyl', 'hzj', 'hzk', 'hzl',
                'iwj', 'iwk', 'iwl', 'ixj', 'ixk', 'ixl',
                'iyj', 'iyk', 'iyl', 'izj', 'izk', 'izl',
            ],
        ]
    ])
    def test_letter_combinations(self, digits, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.letter_combinations(digits)

        # Verify
        self.assertEqual(sorted(ans), sorted(expected_ans))
