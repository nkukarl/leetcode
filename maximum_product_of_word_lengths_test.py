from unittest import TestCase

from nose_parameterized import parameterized

from maximum_product_of_word_lengths import Solution


class TestMaximumProductOfWordLengths(TestCase):
    @parameterized.expand([
        [
            {
                'words': ['abcw', 'baz', 'foo', 'bar', 'xtfn', 'abcdef'],
            },
            16,
        ],
        [
            {
                'words': ['a', 'ab', 'abc', 'd', 'cd', 'bcd', 'abcd'],
            },
            4,
        ],
        [
            {
                'words': ['a', 'aa', 'aaa', 'aaaa'],
            },
            0
        ],
    ])
    def test_max_product(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.max_product(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
