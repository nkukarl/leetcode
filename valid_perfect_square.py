class Solution(object):
    def is_perfect_square(self, num):
        sqrt_approximate = self.get_sqrt_approximate(num)
        for shift in [-1, 0, 1]:
            sqrt = sqrt_approximate + shift
            if sqrt * sqrt == num:
                return True
        return False

    def get_sqrt_approximate(self, num):
        guess = num / 2.0
        eps = 10 ** -9
        while True:
            guess_ = (guess + num / guess) / 2.0
            if abs(guess_ - guess) < eps:
                return int(guess_)
            guess = guess_
