class Solution(object):
    def get_permutation(self, n, k):
        factorial = self.get_factorial()
        k -= 1
        ans = ''
        nums = [i for i in range(1, n + 1)]
        for m in range(n - 1, -1, -1):
            index = k // factorial[m]
            k %= factorial[m]
            ans += str(nums[index])
            nums = nums[:index] + nums[index + 1:]
        return ans

    def get_factorial(self):
        factorial = [1]
        for n in range(1, 10):
            factorial.append(factorial[-1] * n)
        return factorial
