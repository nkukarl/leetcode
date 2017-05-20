from unittest import TestCase

from nose_parameterized import parameterized

from compare_version_numbers import Solution


class TestCompareVersionNumbers(TestCase):
    @parameterized.expand([
        [
            {
                'v1': '1.2',
                'v2': '1.2.1',
            },
            -1,
        ],
        [
            {
                'v1': '1.3',
                'v2': '1.13',
            },
            -1,
        ],
        [
            {
                'v1': '1.0.0',
                'v2': '1.0',
            },
            0,
        ],
    ])
    def test_compare_version(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.compare_version(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
