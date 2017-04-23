class Solution(object):
    def check_record(self, s):
        return 'LLL' not in s and s.count('A') <= 1
