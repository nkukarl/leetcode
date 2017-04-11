class Solution:
    def subsets(self, A):
        A.sort()
        self.res = set()
        self.helper(A, tuple())

        return [list(r) for r in self.res] + [[]]

    def helper(self, A, cur):
        if A:
            for i in range(len(A)):
                self.res.add(cur + (A[i],))
                self.helper(A[i + 1:], cur + (A[i],))


A = [1, 2, 2]

inst = Solution()
print(inst.subsets(A))
