class Solution(object):
    def minimum_total(self, triangle):
        prev = triangle[0]
        for row in triangle[1:]:
            cur = [row[0] + prev[0]]
            for i, n in enumerate(row[1:-1]):
                cur.append(n + min(prev[i], prev[i + 1]))
            cur.append(row[-1] + prev[-1])
            prev = cur
        return min(prev)
