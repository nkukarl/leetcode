class Solution:
    def combine(self, n, k):
        self.k = k
        A = [i for i in range(1, n + 1)]
        self.res = []
        self.helper(A, [])

        return self.res

    def helper(self, A, cur):
        if len(cur) == self.k:
            self.res.append(cur)
        else:
            for i in range(len(A)):
                self.helper(A[i + 1:], cur + [A[i]])


n = 4
k = 4

inst = Solution()
print(inst.combine(n, k))
