import string


class Solution(object):
    def max_product(self, words):
        words = list(set(words))
        summary = {}
        for word in words:
            summary[word] = self.summarise(word)
        N = len(words)
        max_product = 0
        for i in range(N):
            for j in range(i + 1, N):
                word1, word2 = words[i], words[j]
                num1, num2 = summary[word1], summary[word2]
                if num1 ^ num2 == num1 + num2:
                    max_product = max(max_product, len(word1) * len(word2))
        return max_product

    def summarise(self, word):
        """
        Summarise word and return an integer, representing
        the existence of each character in word.

        For example, word = 'apple'

        num = 0

        ord('a') - ord('a') = 0, num += 2 ** 0
        ord('p') - ord('a') = 15, num += 2 ** 15
        ord('l') - ord('a') = 11, num += 2 ** 11
        ord('e') - ord('a') = 4, num += 2 ** 4

        num = 34833

        Args:
            word:

        Returns:

        """
        word = set(word)
        num = 0
        for w in word:
            num += 1 << (ord(w) - ord('a'))
        return num

        # One-liner
        # return sum([1 << (ord(w) - ord('a')) for w in set(word)])

    def summarise_(self, word):
        """
        This method would be more efficient when word is long.
        """
        word = set(list(word))
        num = 0
        weight = 1
        for char in string.ascii_lowercase:
            if char in word:
                num += weight
            weight <<= 1
        return num
