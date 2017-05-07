from unittest import TestCase

from nose_parameterized import parameterized

from find_the_duplicate_number import Solution


class TestFindTheDuplicateNumber(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [1, 1, 2, 1, 1],
            },
            1,
        ],
        [
            {
                'nums': [1, 2, 3, 4, 1],
            },
            1,
        ],
        [
            {
                'nums': [4, 2, 1, 3, 5, 1, 6],
            },
            1,
        ],
        [
            {
                'nums': [
                    8, 7, 1, 10, 17, 15, 18, 11, 16, 9, 19, 12, 5, 14, 3, 4, 2,
                    13, 18, 18
                ],
            },
            18,
        ]
    ])
    def test_find_duplicate(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.find_duplicate(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
