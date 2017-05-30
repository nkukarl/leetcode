from unittest import TestCase

from nose_parameterized import parameterized

from excel_sheet_column_title import Solution


class TestExcelSheetColumnTitle(TestCase):
    @parameterized.expand([
        [
            {
                'n': 1,
            },
            'A',
        ],
        [
            {
                'n': 3345,
            },
            'DXQ',
        ],
        [
            {
                'n': 17576,
            },
            'YYZ',
        ],
        [
            {
                'n': 17577,
            },
            'YZA',
        ],
        [
            {
                'n': 18278,
            },
            'ZZZ',
        ],
        [
            {
                'n': 18279,
            },
            'AAAA',
        ],
    ])
    def test_convert_to_title(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.convert_to_title(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
