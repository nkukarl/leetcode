class Solution:
	def isPalindrome(self, n):
		if n < 0:
			return False
		if n == 0:
			return True
		m = n
		counter = 0
		while m:
			counter += 1
			m //= 10
		m = n
		while m >= 10:
			left = m // 10 ** (counter - 1)
			right = m % 10
			print(left, right)
			if left != right:
				return False
			m %= 10 ** (counter - 1)
			m //= 10
			counter -= 2
		return True

n = 1234321

inst = Solution()
print(inst.isPalindrome(n))