from unittest import TestCase

from nose_parameterized import parameterized

from ransom_note import Solution


class TestRansomNote(TestCase):
    @parameterized.expand([
        [
            {
                'ransom_note': 'a',
                'magazine': 'b',
            },
            False,
        ],
        [
            {
                'ransom_note': 'aa',
                'magazine': 'ab',
            },
            False,
        ],
        [
            {
                'ransom_note': 'aa',
                'magazine': 'aab',
            },
            True,
        ],
    ])
    def test_can_construct(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.can_construct(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
