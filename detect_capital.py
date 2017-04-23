import re


class Solution(object):
    def detect_capital_use(self, word):
        return re.match(r'\b([A-Z]+|[A-Z][a-z]*|[a-z]+)\b', word) is not None
