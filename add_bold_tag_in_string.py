class Solution(object):
    def add_bold_tag(self, s, dict_):
        flags = [False] * len(s)
        for sub in dict_:
            pos = 0
            while True:
                index = s.find(sub, pos)
                if -1 == index:
                    break
                for i in range(index, index + len(sub)):
                    flags[i] = True
                pos += 1

        ans = ''
        is_open = False
        for i, flag in enumerate(flags):
            if (is_open, flag) == (False, True):
                ans += '<b>'
                is_open = True
            elif (is_open, flag) == (True, False):
                ans += '</b>'
                is_open = False
            ans += s[i]

        if is_open:
            ans += '</b>'

        return ans
