class Solution:
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    return False
            elif s[left].isalnum():
                right -= 1
            else:
                left += 1
        return True


s = 'A man, a plan, a canal: Panama'
s = 'race a car'
s = 'aba'
s = 'aac'
s = 'cbc'

inst = Solution()
print(inst.isPalindrome(s))
