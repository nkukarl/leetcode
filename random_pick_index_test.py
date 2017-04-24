from unittest import TestCase

from random_pick_index import \
    Solution, SolutionWithCache, SolutionSummariseWhenInitialised


class TestRandomPickIndex(TestCase):
    def setup(self):
        return [1, 2, 3, 3, 3]

    def exercise_and_verify(self, sol):
        for i in range(1000):
            index = sol.pick(3)
            self.assertIn(index, [2, 3, 4])

    def test_solution(self):
        # Setup
        nums = self.setup()
        sol = Solution(nums)

        # Exercise and Verify
        self.exercise_and_verify(sol)

    def test_solution_with_cache(self):
        # Setup
        nums = self.setup()
        sol = SolutionWithCache(nums)

        # Exercise and Verify
        self.exercise_and_verify(sol)

    def test_solution_summarise_when_initialised(self):
        # Setup
        nums = self.setup()
        sol = SolutionSummariseWhenInitialised(nums)

        # Exercise and Verify
        self.exercise_and_verify(sol)
