class Solution:
    def fullJustify(self, words, L):
        cur = []
        curLen = 0
        lines = []
        for word in words:
            if cur == []:
                cur.append(word)
                curLen += len(word)
            else:
                if curLen + len(word) + 1 <= L:
                    cur.append(word)
                    curLen += len(word) + 1
                else:
                    lines.append(cur)
                    cur = [word]
                    curLen = len(word)
        lines.append(cur)

        print(lines)

        res = []

        for line in lines[:-1]:
            wordLen = 0
            for word in line:
                wordLen += len(word)
            emptySpaces = L - wordLen
            gaps = len(line) - 1
            eachWidth = []
            while gaps:
                tmp = emptySpaces // gaps
                eachWidth.append(tmp)
                emptySpaces -= tmp
                gaps -= 1
            eachWidth.reverse()
            newLine = ''
            for i in range(len(line) - 1):
                newLine += line[i] + ' ' * eachWidth[i]
            newLine += line[-1]
            newLine += ' ' * (L - len(newLine))
            res.append(newLine)

        lastLine = ''
        for word in lines[-1]:
            lastLine += word + ' '
        lastLine = lastLine[:-1]
        lastLine += ' ' * (L - len(lastLine))
        res.append(lastLine)

        return res


# words = ['This', 'is', 'an', 'example', 'of', 'text', 'justification']
# L = 16

words = ['']
L = 2

words = ["Listen", "to", "many,", "speak", "to", "a", "few."]
L = 6

inst = Solution()
justified = inst.fullJustify(words, L)

for line in justified:
    print(line)
