class Solution:
    def canJump(self, A):
        canReach = 0
        for i in range(len(A)):
            if canReach >= i:
                canReach = max(canReach, i + A[i])
                if canReach >= len(A) - 1:
                    return True
        return False


A = [2, 3, 1, 1, 4]
A = [3, 2, 1, 0, 4]

inst = Solution()
print(inst.canJump(A))
