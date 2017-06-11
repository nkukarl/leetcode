class Solution(object):
    def can_construct(self, ransom_note, magazine):
        summary = {}
        for char in magazine:
            summary[char] = summary.get(char, 0) + 1

        for char in ransom_note:
            if 0 == summary.get(char, 0):
                return False
            summary[char] -= 1

        return True
