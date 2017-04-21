from unittest import TestCase

from detect_capital import Solution


class TestProblemToSolve(TestCase):
    def test_detect_capital_use(self):
        # Setup
        sol = Solution()
        words = [
            'Python',
            'PYTHON',
            'python',
            'PYthon',
            'PyThOn',
            'pythON',
        ]

        # Exercise and Verify
        for word in words:
            ans = sol.detect_capital_use(word)
            expected_ans = self.detect_capital_use(word)
            self.assertEqual(ans, expected_ans)

    def detect_capital_use(self, word):
        return word.isupper() or word.islower() or word.istitle()
