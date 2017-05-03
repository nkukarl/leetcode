class Solution(object):
    def valid_ip_address(self, ip):
        if '.' in ip and ':' in ip:
            return 'Neither'
        if '.' in ip:
            return self.validate_ipv4(ip)
        if ':' in ip:
            return self.validate_ipv6(ip)
        return 'Neither'

    def validate_ipv4(self, ip):
        nums = ip.split('.')
        if len(nums) != 4:
            return 'Neither'
        for num in nums:
            if '0' == num:
                continue
            if '' == num or num.startswith('0'):
                return 'Neither'
            for char in num:
                if char not in '0123456789':
                    return 'Neither'
            if int(num) > 255:
                return 'Neither'
        return 'IPv4'

    def validate_ipv6(self, ip):
        nums = ip.lower().split(':')
        if len(nums) != 8:
            return 'Neither'
        for num in nums:
            if '' == num or len(num) > 4:
                return 'Neither'
            for char in num:
                if char not in '0123456789abcdef':
                    return 'Neither'
        return 'IPv6'
