class Solution(object):
    def integer_replacement(self, n):
        """
        
        If n is an even number, let n = 2k, we have
            f(2k) = f(k) + 1
        If n is an odd number, let n = 2k + 1, we have
            f(2k+1) = min[f(2k), f(2k+2)] + 1
        We then need to deal with two scenarios:
        <1> n % 4 = 3
        <2> n % 4 = 1
            If n % 4 == 3,
                It is easy to prove that when n = 3,
                3 -> 2 -> 1 is quicker than 3 -> 4 -> 2 -> 1.
                Hence, the operation shall be n -= 1
                
                TODO: Proof to be added

        """
        count = 0
        while n > 1:
            count += 1
            if 0 == n % 2:
                n //= 2
            else:
                if 3 == n % 4 and n != 3:
                    n += 1
                else:
                    n -= 1
        return count
