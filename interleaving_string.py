# TODO: Anything more efficient?
class Solution(object):
    def is_interleave(self, s1, s2, s3):
        len_1, len_2, len_3 = len(s1), len(s2), len(s3)
        if len_1 + len_2 != len_3:
            return False
        self.s1, self.s2, self.s3 = s1[::-1], s2[::-1], s3[::-1]
        return self.explore(len_1 - 1, len_2 - 1, len_3 - 1)

    def explore(self, pos_1, pos_2, pos_3):
        if pos_1 < 0:
            return self.s2[:pos_2 + 1] == self.s3[:pos_3 + 1]
        if pos_2 < 0:
            return self.s1[:pos_1 + 1] == self.s3[:pos_3 + 1]

        flag_1 = flag_2 = False
        if self.s1[pos_1] == self.s3[pos_3]:
            flag_1 = self.explore(pos_1 - 1, pos_2, pos_3 - 1)
        if self.s2[pos_2] == self.s3[pos_3]:
            flag_2 = self.explore(pos_1, pos_2 - 1, pos_3 - 1)
        return flag_1 or flag_2
