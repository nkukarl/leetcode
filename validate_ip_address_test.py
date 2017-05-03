from unittest import TestCase

from nose_parameterized import parameterized

from validate_ip_address import Solution


class TestValidateIPAddress(TestCase):
    @parameterized.expand([
        [
            {
                'ip': '172.16.254.1',
            },
            'IPv4',
        ],
        [
            {
                'ip': '2001:0db8:85a3:0000:0000:8a2e:0370:7334',
            },
            'IPv6',
        ],
        [
            {
                'ip': '2001:db8:85a3:0:0:8A2E:0370:7334',
            },
            'IPv6',
        ],
        [
            {
                'ip': '172.16.254.12.12',
            },
            'Neither',
        ],
        [
            {
                'ip': '172.16.254.01',
            },
            'Neither',
        ],
        [
            {
                'ip': '172.1e6.254.01',
            },
            'Neither',
        ],
        [
            {
                'ip': '256.256.256.256',
            },
            'Neither',
        ],
        [
            {
                'ip': '2001:0db8:85a3::8A2E:0370:7334',
            },
            'Neither',
        ],
        [
            {
                'ip': '2001:0db8:85a3:0g00:8A2E:r370:7334',
            },
            'Neither',
        ],
        [
            {
                'ip': '02001:0db8:85a3:0000:0000:8a2e:0370:7334',
            },
            'Neither',
        ],
    ])
    def test_valid_ip_address(self, kwargs, expected_ans):
        # Setup
        sol = Solution()

        # Exercise
        ans = sol.valid_ip_address(**kwargs)

        # Verify
        self.assertEqual(ans, expected_ans)
