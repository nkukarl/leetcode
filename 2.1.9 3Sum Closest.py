class Solution:
    def threeSumClosest(self, A, target):
        if len(A) < 3:
            return False
        A.sort()
        res = sum(A[:3])
        diff = abs(target - res)

        for i in range(len(A) - 2):
            j, k = i + 1, len(A) - 1
            while j < k:
                cur = A[i] + A[j] + A[k]
                if cur == target:
                    return cur
                if cur < target:
                    if target - cur < diff:
                        res = cur
                        diff = target - cur
                    j += 1
                else:
                    if cur - target < diff:
                        res = cur
                        diff = cur - target
                    k -= 1
        return res


A = [-1, 2, 1, -4]
target = 1

inst = Solution()
print(inst.threeSumClosest(A, target))
