class Solution(object):
    def count_and_say(self, n):
        if n <= 1:
            return '1'
        say = self.count_and_say(n - 1)

        count = 1
        cur_char = say[0]
        ans = ''
        for char in say[1:]:
            if char == cur_char:
                count += 1
            else:
                ans += str(count) + cur_char
                cur_char = char
                count = 1
        ans += str(count) + cur_char

        return ans
