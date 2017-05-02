from unittest import TestCase

from nose_parameterized import parameterized

from find_k_pairs_with_smallest_sums import Solution


class TestFindKPairsWithSmallestSums(TestCase):
    @parameterized.expand([
        [
            {
                'nums1': [1, 2, 3, 4],
                'nums2': [1, 2, 3, 4],
                'k': 1,
            },
            [[1, 1]],
        ],
        [
            {
                'nums1': [1, 2, 3, 4],
                'nums2': [1, 2, 3, 4],
                'k': 3,
            },
            [[1, 1], [1, 2], [2, 1]],
        ],
        [
            {
                'nums1': [1, 2, 3, 4],
                'nums2': [2],
                'k': 4,
            },
            [[1, 2], [2, 2], [3, 2], [4, 2]],
        ],
        [
            {
                'nums1': [1, 1, 2],
                'nums2': [1, 2, 3],
                'k': 2,
            },
            [[1, 1], [1, 1]],
        ],
    ])
    def test_k_smallest_pairs(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.k_smallest_pairs(**kwargs)

        # Verify
        self.assertEqual(sorted(ans), sorted(expected_ans))
