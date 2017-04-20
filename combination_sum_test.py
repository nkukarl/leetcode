from unittest import TestCase

from combination_sum import Solution


class TestCombinationSum(TestCase):
    def test_combination_sum(self):
        # Setup
        sol = Solution()
        numbers = [2, 3, 6, 7]
        target = 20

        # Exercise
        ans = sol.combination_sum(numbers, target)

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
