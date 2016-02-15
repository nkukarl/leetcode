class Solution:
	def plusOne(self, digits):
		carry = 1
		n = len(digits)
		i = n - 1
		while carry and i >= 0:
			tmp = (digits[i] + carry) // 10
			digits[i] = (digits[i] + carry) % 10
			carry = tmp
			i -= 1
		if carry:
			digits.insert(0, 1)

		return digits

digits = [9, 9, 9]

inst = Solution()
print(inst.plusOne(digits))
