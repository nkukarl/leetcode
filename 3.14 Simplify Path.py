class Solution:
	def simplifyPath(self, path):
		path = path.split('/')
		stack = []
		for p in path:
			if p == '' or p == '.':
				continue
			if p == '..':
				if stack:
					stack.pop()
				continue
			stack.append(p)
		return '/'+ '/'.join(stack)

path = '/home/a//./b/c/../d/e/f'

inst = Solution()
print(inst.simplifyPath(path))