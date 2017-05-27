class Solution(object):
    def repeated_substring_pattern(self, s):
        # Handle simple scenario
        if len(s) < 2:
            return False
        if 2 == len(s):
            return s[0] == s[1]

        pattern = s[0]
        half_s = s[:len(s) // 2 + 1]
        for char in half_s[1:]:
            if char == s[0]:
                if self.check_pattern(s, pattern):
                    return True
            pattern += char
        return False

    def check_pattern(self, s, pattern):
        m, n = len(s), len(pattern)
        if m % n != 0:
            return False
        k = m // n
        for i in range(k):
            cur = s[i * len(pattern): (i + 1) * len(pattern)]
            if cur != pattern:
                return False
        return True
