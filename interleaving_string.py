class Solution(object):
    def is_interleave(self, s1, s2, s3):
        len_1, len_2, len_3 = len(s1), len(s2), len(s3)
        if len_1 + len_2 != len_3:
            return False
        last = {(0, 0)}
        for char in s3:
            cur = set()
            for i, j in last:
                if i < len_1 and s1[i] == char:
                    cur.add((i + 1, j))
                if j < len_2 and s2[j] == char:
                    cur.add((i, j + 1))
            if not cur:
                return False
            last = cur
        return True
