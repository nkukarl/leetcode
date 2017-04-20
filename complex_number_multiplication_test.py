import random
from unittest import TestCase

from complex_number_multiplication import Solution


class TestComplexNumberMultiply(TestCase):
    def test_complex_number_multiply(self):
        # Setup
        sol = Solution()
        num1, real1, imag1 = self.get_complex_number()
        num2, real2, imag2 = self.get_complex_number()

        # Exercise
        ans = sol.complex_number_multiply(num1, num2)

        # Verify
        complex1 = complex(real1, imag1)
        complex2 = complex(real2, imag2)
        result = complex1 * complex2
        real, imag = int(result.real), int(result.imag)
        expected_ans = '{0}+{1}i'.format(real, imag)
        self.assertEqual(ans, expected_ans)

    def get_complex_number(self):
        real = random.randint(-100, 100)
        imag = random.randint(-100, 100)
        return '{0}+{1}i'.format(real, imag), real, imag
