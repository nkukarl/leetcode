from unittest import TestCase
from restore_ip_addresses import Solution


class TestRestoreIPAddresses(TestCase):
    def test_restore_ip_addresses(self):
        # Setup
        s = '25525511135'

        sol = Solution()

        # Exercise
        ans = sol.restore_ip_addresses(s)

        # Verify
        self.assertEqual(
            sorted(ans),
            sorted(['255.255.11.135', '255.255.111.35'])
        )
