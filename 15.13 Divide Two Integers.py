class Solution:
	def divide(self, dividend, divisor):
		sign = 1
		if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
			sign = -1
		if divisor == 0:
			if sign == 1:
				return 2 ** 31 - 1
			return -2 ** 31
		dividend, divisor = abs(dividend), abs(divisor)
		mask = 1

		while divisor <= dividend:
			divisor <<= 1
			mask <<= 1

		divisor >>= 1
		mask >>= 1

		ans = 0

		while dividend > 0:
			if dividend >= divisor:
				ans += mask
				dividend -= divisor
			mask >>= 1
			divisor >>= 1

		return ans

dividend, divisor = 1024, 4

inst = Solution()
print(inst.divide(dividend, divisor))



