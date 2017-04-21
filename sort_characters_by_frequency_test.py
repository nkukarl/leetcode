from unittest import TestCase

from sort_characters_by_frequency import Solution


class TestSortCharactersByFrequency(TestCase):
    def test_frequency_sort(self):
        # Setup
        sol = Solution()
        s = 'abcbaccaaa'

        # Exercise
        ans = sol.frequency_sort(s)

        # Verify
        self.assertEqual(ans, 'aaaaacccbb')
