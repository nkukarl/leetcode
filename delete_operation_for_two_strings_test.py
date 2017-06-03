from unittest import TestCase

from nose_parameterized import parameterized

from delete_operation_for_two_strings import Solution


class TestDeleteOperationForTwoStrings(TestCase):
    @parameterized.expand([
        [
            {
                'word1': 'abcd1234',
                'word2': 'a1b2c3d4',
            },
            6,
        ],
        [
            {
                'word1': 'eat',
                'word2': 'sea',
            },
            2,
        ],
    ])
    def test_min_distance(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.min_distance(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
