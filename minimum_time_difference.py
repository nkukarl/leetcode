class Solution(object):
    def find_min_difference(self, time_points):
        minutes = []
        for tp in time_points:
            minutes.append(self.convert_to_minutes(tp))
        minutes.sort()
        min_diff = 720
        for m1, m2 in zip(minutes[:-1], minutes[1:]):
            diff = self.calc_diff(m1, m2)
            min_diff = min(min_diff, diff)
        diff = self.calc_diff(minutes[0], minutes[-1])
        return min(min_diff, diff)

    def convert_to_minutes(self, time_point):
        """

        Convert time point into minutes.

        Args:
            time_point:

        Returns:

        """
        hh, mm = map(int, time_point.split(':'))
        return hh * 60 + mm

    def calc_diff(self, m1, m2):
        """

        If minutes difference is greater than 720 (12 hours),
        should use 24 hours minus the minutes difference.

        Args:
            m1:
            m2:

        Returns:

        """
        diff = m2 - m1
        return diff if diff < 720 else 1440 - diff