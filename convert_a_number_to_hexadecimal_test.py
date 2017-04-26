import random
from unittest import TestCase

from convert_a_number_to_hexadecimal import Solution


class TestConvertANumberToHexadecimal(TestCase):
    def test_to_hex(self):
        # Setup
        sol = Solution()
        num = random.randint(100, 400)

        # Exercise
        ans = sol.to_hex(num)
        expected_ans = self.to_hex(num)

        # Verify
        self.assertEqual(ans, expected_ans)

    def to_hex(self, num):
        if 0 == num:
            return '0'
        if num < 0:
            num = 2 ** 32 + num
        return self.dec_to_hex(num)

    def dec_to_hex(self, dec):
        hexadecimal = ''
        hex_seq = list('0123456789abcdef')
        base = 16 ** 7
        while base > 0:
            val = dec // base
            if val != 0 or hexadecimal != '':
                hexadecimal += hex_seq[val]

            dec = dec % base
            base //= 16
        return hexadecimal
