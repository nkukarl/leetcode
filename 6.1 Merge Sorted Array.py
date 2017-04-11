class Solution:
    def merge(self, A, m, B, n):
        i = m + n - 1
        a = m - 1
        b = n - 1
        while a >= 0 and b >= 0:
            if A[a] > B[b]:
                A[i] = A[a]
                a -= 1
            else:
                A[i] = B[b]
                b -= 1
            i -= 1
        while b >= 0:
            A[i] = B[b]
            i -= 1
            b -= 1


A = [2, 4, 5, None, None]
B = [1, 3]
m = 3
n = 2

inst = Solution()
inst.merge(A, m, B, n)

print(A)
