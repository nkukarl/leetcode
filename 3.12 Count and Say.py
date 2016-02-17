class Solution:
	def countAndSay(self, n):
		if n == 1:
			return '1'
		s = self.countAndSay(n - 1)
		counter = 1
		cur = s[0]
		output = ''
		for char in s[1:]:
			if char == cur:
				counter += 1
			else:
				output += str(counter) + cur
				cur = char
				counter = 1
		output += str(counter) + cur
		return output

inst = Solution()
print(inst.countAndSay(8))