class Solution:
    def maxSubArray(self, A):
        if max(A) <= 0:
            return max(A)
        if min(A) >= 0:
            return sum(A)

        cur = 0
        ans = 0
        for n in A:
            cur += n
            if cur <= 0:
                cur = 0
            else:
                ans = max(cur, ans)

        return ans


A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

inst = Solution()
print(inst.maxSubArray(A))
