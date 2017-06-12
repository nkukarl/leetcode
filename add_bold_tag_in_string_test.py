from unittest import TestCase

from nose_parameterized import parameterized

from add_bold_tag_in_string import Solution


class TestAddBoldTagInString(TestCase):
    @parameterized.expand([
        [
            {
                's': 'abcxyz123',
                'dict_': ['abc', '123'],
            },
            '<b>abc</b>xyz<b>123</b>',
        ],
        [
            {
                's': 'aaabbcc',
                'dict_': ['aaa', 'aab', 'bc'],
            },
            '<b>aaabbc</b>c',
        ],
    ])
    def test_add_bold_tag(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.add_bold_tag(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
