from unittest import TestCase

from nose_parameterized import parameterized

from reconstruct_original_digits_from_english import Solution


class TestReconstructOriginalDigitsFromEnglish(TestCase):
    @parameterized.expand([
        [
            {
                's': 'owoztneoer',
            },
            '012',
        ],
        [
            {
                's': 'fviefuro',
            },
            '45',
        ],
    ])
    def test_original_digits(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.original_digits(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
