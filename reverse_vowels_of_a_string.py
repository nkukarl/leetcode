class Solution(object):
    def reverse_vowels(self, s):
        vowels = {
            'a', 'e', 'i', 'o', 'u',
            'A', 'E', 'I', 'O', 'U',
        }
        rs = list(s)
        left, right = 0, len(rs) - 1

        while left < right:
            while left < len(rs) and rs[left] not in vowels:
                left += 1
            while right >= 0 and rs[right] not in vowels:
                right -= 1
            if left < right:
                rs[left], rs[right] = rs[right], rs[left]
                left += 1
                right -= 1
        return ''.join(rs)
