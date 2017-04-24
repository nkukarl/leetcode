from unittest import TestCase

from license_key_formatting import Solution


class TestLicenseKeyFormatting(TestCase):
    def test_license_key_formatting(self):
        # Setup
        sol = Solution()
        s = '2-4A0r7-4k'
        k = 4

        # Exercise
        ans = sol.license_key_formatting(s, k)

        # Verify
        expected_ans = '24A0-R74K'
        self.assertEqual(ans, expected_ans)
