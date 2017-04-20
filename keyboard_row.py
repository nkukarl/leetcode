class Solution(object):
    def find_words(self, words):

        rows = [
            set('qwertyuiop'),
            set('asdfghjkl'),
            set('zxcvbnm'),
        ]
        ans = []
        for word in words:
            for row in rows:
                if self.check_sufficiency(word, row):
                    ans.append(word)
                    break
        return ans

    def check_sufficiency(self, word, row):
        return row >= set(word.lower())
