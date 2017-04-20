class Solution(object):
    def complex_number_multiply(self, num1, num2):
        real1, imag1 = self.parse_complex(num1)
        real2, imag2 = self.parse_complex(num2)

        real = real1 * real2 - imag1 * imag2
        imag = real1 * imag2 + real2 * imag1
        return '{0}+{1}i'.format(real, imag)

    def parse_complex(self, num):
        """

        Args:
            num (str): a+bi
                a and b are integers

        Returns:
            (a, b) as integers

        """
        return map(int, num[:-1].split('+'))
