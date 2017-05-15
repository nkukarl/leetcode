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
        word = set(list(word))
        num = 0
        weight = 1
        for char in string.ascii_lowercase:
            if char in word:
                num += weight
            weight <<= 1
        return num
