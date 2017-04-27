from unittest import TestCase

from nose_parameterized import parameterized

from problem_to_solve import Solution


class TestProblemToSolve(TestCase):
    @parameterized.expand([
        [
            kwargs,
            expected_ans,
        ],
        [
            kwargs,
            expected_ans,
        ],
    ])
    def test_problem_to_solve(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.problem_to_solve(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
