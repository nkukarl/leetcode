class Solution:
    def removeDuplicates(self, A):
        if len(A) <= 2:
            return len(A)
        pos = 2
        n = len(A)
        for i in range(2, n):
            if A[i] != A[pos - 3]:
                A[pos] = A[i]
                pos += 1
        return pos


A = [1] * 5 + [2] * 6 + [3] * 4

inst = Solution()
length = inst.removeDuplicates(A)

print(A[:length])
