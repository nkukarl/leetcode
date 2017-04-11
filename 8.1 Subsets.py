class Solution:
    def subsets(self, A):
        A.sort()
        self.res = [[]]
        self.helper(A, [])

        return self.res

    def helper(self, A, cur):
        if A:
            for i in range(len(A)):
                self.res.append(cur + [A[i]])
                self.helper(A[i + 1:], cur + [A[i]])


A = [1, 2, 3]

inst = Solution()
print(inst.subsets(A))
