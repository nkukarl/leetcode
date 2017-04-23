class Solution(object):
    def hamming_distance(self, num1, num2):
        xor = num1 ^ num2
        distance = 0
        while xor:
            distance += xor & 1
            xor >>= 1
        return distance
