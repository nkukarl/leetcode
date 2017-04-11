class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Solution:
    def maxPoints(self, points):
        if len(points) < 3:
            return len(points)
        ans = 1
        for p in points:
            summary = {'inf': 0}
            dupPoints = 1
            for q in points:
                if p == q:
                    continue
                if p.x == q.x and p.y == q.y:
                    dupPoints += 1
                elif p.x == q.x:
                    summary['inf'] += 1
                else:
                    slope = 1.0 * (p.y - q.y) / (p.x - q.x)
                    summary[slope] = summary.get(slope, 0) + 1
            ans = max(ans, max(summary.values()) + dupPoints)

        return ans
