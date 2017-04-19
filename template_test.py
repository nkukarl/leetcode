from unittest import TestCase

from problem_to_solve import Solution


class TestProblemToSolve(TestCase):
    def test_problem_to_solve(self):
        # Setup
        sol = Solution()
        arg1, arg2 = [], []

        # Exercise
        ans = sol.problem_to_solve(arg1, arg2)

        # Verify
        self.assertEqual(ans, 'expected_ans')
