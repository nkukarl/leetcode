from unittest import TestCase

from combination_sum_ii import Solution


class TestCombinationSumII(TestCase):
    def test_combination_sum_ii(self):
        # Setup
        sol = Solution()
        numbers = [10, 1, 2, 7, 6, 1, 5]
        target = 8

        # Exercise
        ans = sol.combination_sum_ii(numbers, target)

        # Verify
        # TODO: How to ensure all answers are obtained?
        summary = set()
        for each_ans in ans:
            # Ensure each_ans is sorted
            self.assertEqual(each_ans, sorted(each_ans))
            res = tuple(each_ans)
            # Ensure there are no duplicates in ans
            self.assertNotIn(res, summary)
            # Ensure the sum of each_ans is equal to target
            self.assertEqual(sum(res), target)
            summary.add(res)
