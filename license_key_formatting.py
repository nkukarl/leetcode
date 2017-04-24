class Solution(object):
    def license_key_formatting(self, s, k):
        s_ = s.replace('-', '').upper()[::-1]
        return self.split(s_, k)[::-1]

    def split(self, s, k):
        if len(s) <= k:
            return s
        return s[:k] + '-' + self.split(s[4:], k)
