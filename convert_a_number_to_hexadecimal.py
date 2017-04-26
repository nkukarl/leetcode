class Solution(object):
    def to_hex(self, num):
        if 0 == num:
            return '0'
        if num < 0:
            num = 2 ** 32 + num
        binary_ = bin(num)[2:][::-1]
        binary = self.split(binary_)
        return self.bin_to_hex(binary)

    def split(self, s):
        if len(s) <= 4:
            return ['{0:04d}'.format(int(s[::-1]))]
        return self.split(s[4:]) + [s[:4][::-1]]

    def bin_to_hex(self, binary):
        hexadecimal = ''
        lookup_tbl = {
            '0000': '0',
            '0001': '1',
            '0010': '2',
            '0011': '3',
            '0100': '4',
            '0101': '5',
            '0110': '6',
            '0111': '7',
            '1000': '8',
            '1001': '9',
            '1010': 'a',
            '1011': 'b',
            '1100': 'c',
            '1101': 'd',
            '1110': 'e',
            '1111': 'f',
        }
        for b in binary:
            hexadecimal += lookup_tbl[b]
        return hexadecimal
