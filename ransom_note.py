class Solution(object):
    def can_construct(self, ransom_note, magazine):
        summary = [0] * 26
        for char in magazine:
            summary[ord(char) - ord('a')] += 1
        for char in ransom_note:
            summary[ord(char) - ord('a')] -= 1
        for count in summary:
            if count < 0:
                return False
        return True
