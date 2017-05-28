class Solution(object):
    def generate(self, num_rows):
        if num_rows < 1:
            return []
        if 1 == num_rows:
            return [[1]]
        base = [[1]]
        for n in range(1, num_rows):
            last = base[-1]
            cur = [1]
            for i in range(len(last) - 1):
                cur.append(last[i] + last[i + 1])
            cur.append(1)
            base.append(cur)
        return base

    def get_row(self, row_index):
        if row_index < 1:
            return [1]
        ans = [1]
        for i in range(1, row_index + 1):
            cur = [1]
            for i in range(len(ans) - 1):
                cur.append(ans[i] + ans[i + 1])
            cur.append(1)
            ans = cur
        return ans
