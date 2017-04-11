class Solution:
    def firstMissingPositive(self, A):
        if 0 not in A:
            A.append(0)
        for i in range(len(A)):
            while A[i] >= 0 and A[i] < len(A) and A[A[i]] != A[i]:
                A[A[i]], A[i] = A[i], A[A[i]]
        print(A)
        for i in range(len(A)):
            if A[i] != i:
                return i
        return len(A)


A = [3, 4, 5, 1, 2, 7]

inst = Solution()
print(inst.firstMissingPositive(A))
