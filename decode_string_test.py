from unittest import TestCase

from nose_parameterized import parameterized

from decode_string import Solution


class TestDecodeString(TestCase):
    @parameterized.expand([
        [
            {
                's': '3[a]2[bc]',
            },
            'aaabcbc',
        ],
        [
            {
                's': '3[a2[c]]',
            },
            'accaccacc',
        ],
        [
            {
                's': '2[abc]3[cd]ef',
            },
            'abcabccdcdcdef',
        ],
        [
            {
                's': '2[abc]10[cd]ef',
            },
            'abcabccdcdcdcdcdcdcdcdcdcdef',
        ],

    ])
    def test_decode_string(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.decode_string(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
