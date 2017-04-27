class Solution(object):
    def letter_combinations(self, digits):
        if '' == digits:
            return []
        digit_to_letters = {
            '0': [' '],
            '1': ['*'],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        ans = [letter for letter in digit_to_letters[digits[0]]]
        for digit in digits[1:]:
            ans_next = []
            letters = digit_to_letters[digit]
            for letter in letters:
                for ar in ans:
                    ans_next.append(ar + letter)
            ans = ans_next
        return ans
