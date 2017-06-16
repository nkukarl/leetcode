class Solution(object):
    def different_ways_to_compute(self, s):
        if not s:
            return []
        ops = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
        }
        ans = []
        for i, char in enumerate(s):
            if char in ops:
                left = self.different_ways_to_compute(s[:i])
                right = self.different_ways_to_compute(s[i + 1:])
                for a in left:
                    for b in right:
                        f = ops[char]
                        ans.append(f(a, b))
        return ans if ans else [int(s)]
