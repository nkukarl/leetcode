class Solution(object):
    def valid_square(self, p1, p2, p3, p4):
        points = [p1, p2, p3, p4]
        N = 4
        dists = {}
        for i in range(N):
            for j in range(i + 1, N):
                dist = self.calc_dist(points[i], points[j])
                dists[dist] = dists.get(dist, 0) + 1

        if len(dists) != 2:
            return False

        edge_sq, diag_sq = min(dists.keys()), max(dists.keys())

        return dists[edge_sq] == 4 and dists[diag_sq] == 2 and \
               edge_sq * 2 == diag_sq

    def calc_dist(self, p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
