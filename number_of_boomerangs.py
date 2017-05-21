class Solution(object):
    def number_of_boomerangs(self, points):
        count = 0
        for p in points:
            summary = {}
            for q in points:
                dist = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
                summary[dist] = summary.get(dist, 0) + 1
            for v in summary.values():
                count += v * (v - 1)
        return count
