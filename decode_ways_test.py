from unittest import TestCase

from nose_parameterized import parameterized

from decode_ways import Solution


class TestDecodeWays(TestCase):
    @parameterized.expand([
        [
            {
                's': '123'
            },
            3,
        ],
        [
            {
                's': '12121212',
            },
            34,
        ],
        [
            {
                's': '10',
            },
            1,
        ]
    ])
    def test_num_decodings(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.num_decodings(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
