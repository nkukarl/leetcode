from fractions import Fraction


class Solution(object):
    def max_points(self, points):
        # Handle simple scenario
        if len(points) <= 2:
            return len(points)

        max_count = 2
        for p in points:
            summary = {}
            dup_count = 1
            for q in points:
                if q == p:
                    continue
                if (q.x, q.y) == (p.x, p.y):
                    dup_count += 1
                elif q.x == p.x:
                    summary['inf'] = summary.get('inf', 0) + 1
                else:
                    # Have to use Fraction to handle python precision issue
                    # Otherwise, e.g.,
                    # 94911150 / 94911151 == 94911151 / 94911152
                    # which means a test case of
                    # points = [Point(0, 0), Point(94911151, 94911150),
                    # Point(94911152, 94911151)] would fail.
                    slope = Fraction(q.y - p.y, q.x - p.x)

                    # Alternatively, if we assume all the points have integer
                    # x and y coordinates,
                    # we can first get gcd of delta_x and delta_y
                    # delta_x, delta_y = q.x - p.x, q.y - p.y
                    # gcd = get_gcd(delta_x, delta_y)
                    # then divide delta_x and delta_y by gcd
                    # delta_x //= gcd, delta_y //= gcd
                    # and then use (ratio, remainder) tuple as slope
                    # slope = (delta_y // delta_x, delta_y % delta_x)

                    summary[slope] = summary.get(slope, 0) + 1
            if {} == summary:
                max_count_p = dup_count
            else:
                max_count_p = max(summary.values()) + dup_count
            max_count = max(max_count, max_count_p)
        return max_count
