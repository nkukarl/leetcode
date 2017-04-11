class Solution:
    def combinationSum(self, A, target):
        A = list(set(A))
        A.sort()
        self.target = target
        self.res = []
        self.helper(A, [])

        return self.res

    def helper(self, A, cur):
        if sum(cur) == self.target:
            self.res.append(cur)
        elif sum(cur) < self.target:
            for i in range(len(A)):
                self.helper(A[i:], cur + [A[i]])


A = [2, 3, 6, 7]
target = 50

inst = Solution()
print(inst.combinationSum(A, target))
