from unittest import TestCase

from nose_parameterized import parameterized

from print_diamond import Solution


class TestPrintDiamond(TestCase):
    @parameterized.expand([
        [
            {
                'n': 5,
            },
        ],
        [
            {
                'n': 21,
            },
        ],
    ])
    def test_print_diamond(self, kwargs):
        # Setup
        sol = Solution()

        # Exercise
        sol.print_diamond(**kwargs)
