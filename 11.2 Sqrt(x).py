class Solution:
    def mySqrt(self, x):
        if x <= 0:
            return 0
        low, high = 0, x
        ans = 0
        while low < high:
            mid = (low + high) // 2
            if x / mid >= mid:
                ans = mid
                low = mid + 1
            else:
                high = mid
        return ans


n = 17

inst = Solution()
print(inst.mySqrt(n))
