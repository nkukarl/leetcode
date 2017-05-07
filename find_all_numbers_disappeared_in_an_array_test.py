from unittest import TestCase

from nose_parameterized import parameterized

from find_all_numbers_disappeared_in_an_array import Solution


class TestFindAllNumbersDisappearedInAnArray(TestCase):
    @parameterized.expand([
        [
            {
                'nums': [4, 3, 2, 7, 8, 2, 3, 1],
            },
            [5, 6],
        ],
    ])
    def test_find_disappeared_numbers(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.find_disappeared_numbers(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
