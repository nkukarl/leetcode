from unittest import TestCase

from letter_combinations_of_a_phone_number import Solution


class TestLetterCombinationsOfAPhoneNumber(TestCase):
    def test_letter_combinations_23(self):
        # Setup
        sol = Solution()
        digits = '23'

        # Exercise
        ans = sol.letter_combinations(digits)
        expected_ans = [
            'ad', 'ae', 'af',
            'bd', 'be', 'bf',
            'cd', 'ce', 'cf',
        ]

        # Verify
        self.assertEqual(sorted(ans), sorted(expected_ans))

    def test_letter_combinations_495(self):
        # Setup
        sol = Solution()
        digits = '495'

        # Exercise
        ans = sol.letter_combinations(digits)
        expected_ans = [
            'gwj', 'gwk', 'gwl', 'gxj', 'gxk', 'gxl', 'gyj', 'gyk', 'gyl',
            'gzj', 'gzk', 'gzl', 'hwj', 'hwk', 'hwl', 'hxj', 'hxk', 'hxl',
            'hyj', 'hyk', 'hyl', 'hzj', 'hzk', 'hzl', 'iwj', 'iwk', 'iwl',
            'ixj', 'ixk', 'ixl', 'iyj', 'iyk', 'iyl', 'izj', 'izk', 'izl',
        ]

        # Verify
        self.assertEqual(sorted(ans), sorted(expected_ans))
