class Solution(object):
    def repeated_substring_pattern(self, s):
        for i in range(1, len(s) // 2 + 1):
            # This implicitly confirms len(s) > 0
            if s[i] == s[0]:
                pattern = s[:i]
                if len(s) % i != 0:
                    continue
                if s.split(pattern) == [''] * (len(s) // i + 1):
                    return True

        return False
