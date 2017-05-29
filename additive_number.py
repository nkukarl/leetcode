class Solution(object):
    def is_additive_number(self, num):
        if len(num) < 3:
            return False

        for i in range(1, len(num)):
            for j in range(i + 1, len(num) + 1):
                a, b = num[:i], num[i : j]
                if self.check(a, b, num):
                    return True
        return False

    def check(self, a, b, num):
        if (a.startswith('0') and len(a) > 1) or \
                (b.startswith('0') and len(b) > 1):
            return False
        cur_num = a + b
        if len(cur_num) >= len(num):
            return False
        a, b = int(a), int(b)
        while len(cur_num) < len(num):
            a, b = b, a + b
            cur_num += str(b)
        return cur_num == num
