class Solution(object):
    def read_binary_watch(self, num):
        """

        Args:
            num (int): number of LED digits

        Returns:
            a list of valid_time_stamp

        hh_summary = {
            0: [0],
            1: [1, 2, 4, 8],
            2: [3, 5, 6, 9, 10],
            3: [7, 11],
        }
        mm_summary = {
            0: [0],
            1: [1, 2, 4, 8, 16, 32],
            2: [3, 5, 6, 9, 10, 12, 17, 18, 20, 24, 33, 34, 36, 40, 48],
            3: [7, 11, 13, 14, 19, 21, 22, 25, 26, 28, 35, 37, 38, 41, 42, 44,
                49, 50, 52, 56],
            4: [15, 23, 27, 29, 30, 39, 43, 45, 46, 51, 53, 54, 57, 58],
            5: [31, 47, 55, 59],
        }

        """
        hh_summary, mm_summary = self.get_summary()

        valid_time = []
        for hh in range(num + 1):
            mm = num - hh
            valid_hh = hh_summary.get(hh, [])
            valid_mm = mm_summary.get(mm, [])
            for h in valid_hh:
                for m in valid_mm:
                    valid_time.append('{0}:{1:02d}'.format(h, m))
        return valid_time

    def get_summary(self):
        hh_summary = self._get_summary(11)
        mm_summary = self._get_summary(59)
        return hh_summary, mm_summary

    def _get_summary(self, num):
        summary = {}
        for n in range(num + 1):
            bit = self.get_bit(n)
            summary[bit] = summary.get(bit, []) + [n]
        return summary

    def get_bit(self, n):
        bit = 0
        while n > 0:
            bit += n & 1
            n >>= 1
        return bit
