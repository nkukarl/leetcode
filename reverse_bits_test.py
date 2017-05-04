from unittest import TestCase

from nose_parameterized import parameterized

from reverse_bits import Solution


class TestReverseBits(TestCase):
    @parameterized.expand([
        [
            {
                'n': 43261596,
            },
            964176192,
        ],
    ])
    def test_reverse_bits(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.reverse_bits(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
