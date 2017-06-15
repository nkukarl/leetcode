class Solution(object):
    def num_decodings(self, s):
        """
        Some examples to approach this problem:
        
        s = '0XXX'
        
        s = 'XXX10'
        s = 'XXX20'
        s = 'XXX40'
        
        s = 'XXX1?'
        s = 'XXX2?'
        s = 'XXX3?'
        
        """
        if not s or s.startswith('0'):
            return 0
        count_1, count_2 = 1, 1
        for i in range(1, len(s)):
            if '0' == s[i]:
                if s[i - 1] not in '12':
                    return 0
                count_1, count_2 = count_2, count_1
            elif s[i - 1] == '1':
                count_1, count_2 = count_2, count_1 + count_2
            elif s[i - 1] == '2':
                if s[i] in '123456':
                    count_1, count_2 = count_2, count_1 + count_2
                else:
                    count_1 = count_2
            else:
                count_1 = count_2
        return count_2
