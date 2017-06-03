class Solution(object):
    def trap_rain_water(self, map_height):
        m = len(map_height)
        if m < 3:
            return 0
        n = len(map_height[0])
        if n < 3:
            return 0
        map_l2r, map_r2l = self.traverse_horizontal(map_height)
        map_t2b, map_b2t = self.traverse_vertical(map_height)

        map_water = [[0] * n for _ in range(m)]
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                L, R, T, B = \
                    map_l2r[i][j], map_r2l[i][j], map_t2b[i][j], map_b2t[i][j]
                H = min(L, R, T, B)
                h = map_height[i][j]
                if H > h:
                    map_water[i][j] = H

        ans = self.spill_water(map_height, map_water)
        return ans

    def traverse_horizontal(self, map_height):
        map_l2r, map_r2l = [], []
        for i in range(len(map_height)):
            L = self.get_max_height_to_one_side(map_height[i])
            R = self.get_max_height_to_one_side(map_height[i][::-1])[::-1]
            map_l2r.append(L)
            map_r2l.append(R)
        return map_l2r, map_r2l

    def traverse_vertical(self, map_height):
        map_height = list(zip(*map_height))
        map_t2b_raw, map_b2t_raw = self.traverse_horizontal(map_height)
        map_t2b, map_b2t = list(zip(*map_t2b_raw)), list(zip(*map_b2t_raw))
        return map_t2b, map_b2t

    def get_max_height_to_one_side(self, heights):
        L = [0]
        max_height = 0
        for i in range(1, len(heights)):
            if heights[i - 1] > max_height:
                max_height = heights[i - 1]
            L.append(max_height)
        return L

    def spill_water(self, map_height, map_water):
        # TODO: There is a problem with this function, the third test case fails.
        m, n = len(map_water), len(map_water[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if map_water[i][j] != 0:
                    collection = set()
                    w = self._spill(map_water, i, j, collection,
                                    map_water[i][j])
                    for point in collection:
                        r, c = point
                        ans += max(w - map_height[r][c], 0)
        return ans

    def _spill(self, map_water, i, j, cur_col, min_height):
        if 0 == map_water[i][j]:
            return min_height
        cur_col.add((i, j))
        min_height = min(min_height, map_water[i][j])
        map_water[i][j] = 0
        return min([
            self._spill(map_water, i - 1, j, cur_col, min_height),
            self._spill(map_water, i + 1, j, cur_col, min_height),
            self._spill(map_water, i, j - 1, cur_col, min_height),
            self._spill(map_water, i, j + 1, cur_col, min_height),
        ])
