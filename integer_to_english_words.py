class Solution(object):
    def number_to_words(self, num):
        # Handle simple scenario
        if 0 == num:
            return 'Zero'
        self.DICT = {
            '1': 'One',
            '2': 'Two',
            '3': 'Three',
            '4': 'Four',
            '5': 'Five',
            '6': 'Six',
            '7': 'Seven',
            '8': 'Eight',
            '9': 'Nine',
            '10': 'Ten',
            '11': 'Eleven',
            '12': 'Twelve',
            '13': 'Thirteen',
            '14': 'Fourteen',
            '15': 'Fifteen',
            '16': 'Sixteen',
            '17': 'Seventeen',
            '18': 'Eighteen',
            '19': 'Nineteen',
            '20': 'Twenty',
            '30': 'Thirty',
            '40': 'Forty',
            '50': 'Fifty',
            '60': 'Sixty',
            '70': 'Seventy',
            '80': 'Eighty',
            '90': 'Ninety',
        }

        segments = self.split(str(num))

        weights = [
            ['Billion'],
            ['Million'],
            ['Thousand'],
            [],
        ]
        ans = []
        for seg in segments:
            raw = self.say(seg)
            weight = weights.pop()
            if raw != []:
                ans.append(' '.join(raw + weight))
        return ' '.join(ans[::-1]).strip()

    def split(self, num):
        num_ = list(num)
        segments = []
        while len(num_) >= 3:
            cur = ''
            for i in range(3):
                cur = num_.pop() + cur
            segments.append(cur)
        cur = ''
        while num_:
            cur = num_.pop() + cur
        if '' != cur:
            segments.append(cur)
        return segments

    def say(self, num):
        num = '0' * (3 - len(num)) + num
        left, mid, right = num
        ans = []
        if left != '0':
            ans.append(self.DICT[left] + ' Hundred')
        if mid != '0':
            if mid != '1':
                ans.append(self.DICT[mid + '0'])
                if right != '0':
                    ans.append(self.DICT[right])
            else:
                ans.append(self.DICT[mid + right])
        else:
            if right != '0':
                ans.append(self.DICT[right])
        return ans
