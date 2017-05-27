class Solution(object):
    def reverse_str(self, s, k):
        if k <= 0:
            return ''
        s = list(s)[::-1]
        flag = True
        ans = []
        while len(s) >= k:
            cur = []
            for _ in range(k):
                cur.append(s.pop())
            if flag:
                ans.extend(cur[::-1])
            else:
                ans.extend(cur)
            flag = not flag
        if flag:
            ans.extend(s)
        else:
            ans.extend(s[::-1])
        return ''.join(ans)
