class Solution(object):
    def can_measure_water(self, x, y, z):
        """

        Args:
            x (int): Size of jug 1
            y (int): Size of jug 2
            z (int): Desired water size

        """
        if x < y:
            x, y = y, x
        if z in [0, x + y, x, y]:
            return True
        if z > x + y:
            return False
        gcd = self.get_gcd(x, y)
        return 0 == z % gcd

    def get_gcd(self, x, y):
        """

        Get greatest common divisor of x and y

        Args:
            x (int):
            y (int):

        Returns:
            int

        """
        return x if 0 == y else self.get_gcd(y, x % y)
