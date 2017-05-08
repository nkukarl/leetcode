from unittest import TestCase

from nose_parameterized import parameterized

from remove_duplicates_from_sorted_array import Solution


class TestRemoveDuplicatesFromSortedArray(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5, 6, 6, 6, 7]
            },
            7,
        ],
        [
            {
                'nums': [1, 2, 3, 4, 5, 6, 7]
            },
            7,
        ],
    ])
    def test_remove_duplicates(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.remove_duplicates(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
