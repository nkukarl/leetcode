class Solution:
    def numTrees(self, n):
        if n == 0 or n == 1:
            return 1
        A = [1, 1]
        for i in range(2, n + 1):
            tmp = 0
            for j in range(i):
                tmp += A[j] * A[i - 1 - j]
            A.append(tmp)
        return A[-1]


inst = Solution()
print(inst.numTrees(4))
