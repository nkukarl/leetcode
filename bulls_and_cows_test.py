from unittest import TestCase

from bulls_and_cows import Solution


class TestGetHint(TestCase):
    def test_get_hint(self):
        # Setup
        sol = Solution()
        secret, guess = '28070', '38001'

        # Exercise
        ans = sol.get_hint(secret, guess)

        # Verify
        expected_ans = '2A1B'
        self.assertEqual(ans, expected_ans)
