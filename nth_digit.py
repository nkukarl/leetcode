class Solution(object):
    def find_nth_digit(self, n):
        if n <= 9:
            return n
        boundary = self.get_boundary()
        base = 1
        digits = 1
        while n >= boundary[digits]:
            digits += 1
            base *= 10
        diff = n - boundary[digits - 1]
        num = diff // digits + base
        rem = diff % digits
        if rem == 0:
            return int(str(num - 1)[-1])
        return int(str(num)[rem - 1])

    def get_boundary(self):
        # boundary = {}
        # count = 0
        # for i in range(1, 10):
        #     count += i * 9 * 10 ** (i - 1)
        #     boundary[i] = count
        boundary = {
            1: 9,
            2: 189,
            3: 2889,
            4: 38889,
            5: 488889,
            6: 5888889,
            7: 68888889,
            8: 788888889,
            9: 8888888889,
        }
        return boundary
