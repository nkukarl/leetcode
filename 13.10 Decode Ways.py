class Solution:
    def numDecodings(self, s):
        if not s or s[0] == '0':
            return 0
        n = len(s)
        dp = [1, 1]
        for i in range(1, n):
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    dp.append(dp[-2])
                else:
                    return 0
            else:
                if str(int(s[i - 1] + s[i])) == s[i - 1] + s[i] and int(
                                s[i - 1] + s[i]) <= 26:
                    dp.append(dp[-1] + dp[-2])
                else:
                    dp.append(dp[-1])
        return dp[-1]
