from unittest import TestCase

from nose_parameterized import parameterized

from text_justification import Solution


class TestTextJustification(TestCase):
    @parameterized.expand([
        [
            {
                'words': 'This is an example of text justification.'.split(),
                'max_width': 16,
            },
            [
                'This    is    an',
                'example  of text',
                'justification.  ',
            ],
        ],
        [
            {
                'words': 'I think before I talk.'.split(),
                'max_width': 10,
            },
            [
                'I    think',
                'before   I',
                'talk.     ',
            ],
        ],
        [
            {
                'words': 'I know that is a red apple.'.split(),
                'max_width': 12,
            },
            [
                'I  know that',
                'is   a   red',
                'apple.      ',
            ],
        ],
        [
            {
                'words': [''],
                'max_width': 0,
            },
            [
                '',
            ],
        ],
    ])
    def test_full_justify(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.full_justify(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
