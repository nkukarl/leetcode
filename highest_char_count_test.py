from unittest import TestCase

from nose_parameterized import parameterized

from highest_char_count import Solution


class TestHighestCharCount(TestCase):
    @parameterized.expand([
        [
            {
                's': 'coffee tuffee',
            },
            4,
        ],
    ])
    def test_get_highest_char_count(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.get_highest_char_count(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
