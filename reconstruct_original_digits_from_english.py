class Solution(object):
    def original_digits(self, s):
        summary = self.summarise_string(s)
        counts = [0] * 10

        # Unique char in word
        if summary.get('z', 0) > 0:
            counts[0] = count = summary['z']
            for char in 'zero':
                summary[char] -= count
        if summary.get('w', 0) > 0:
            counts[2] = count = summary['w']
            for char in 'two':
                summary[char] -= count
        if summary.get('u', 0) > 0:
            counts[4] = count = summary['u']
            for char in 'four':
                summary[char] -= count
        if summary.get('x', 0) > 0:
            counts[6] = count = summary['x']
            for char in 'six':
                summary[char] -= count
        if summary.get('g', 0) > 0:
            counts[8] = count = summary['g']
            for char in 'eight':
                summary[char] -= count

        # Non-unique
        if summary.get('o', 0) > 0:
            counts[1] = count = summary['o']
            for char in 'one':
                summary[char] -= count
        if summary.get('h', 0) > 0:
            counts[3] = count = summary['h']
            for char in 'three':
                summary[char] -= count
        if summary.get('f', 0) > 0:
            counts[5] = count = summary['f']
            for char in 'five':
                summary[char] -= count
        if summary.get('v', 0) > 0:
            counts[7] = count = summary['v']
            for char in 'seven':
                summary[char] -= count
        if summary.get('i', 0) > 0:
            counts[9] = count = summary['i']
            for char in 'nine':
                summary[char] -= count
        ans = ''
        for i, count in enumerate(counts):
            ans += str(i) * count
        return ans

    def summarise_string(self, s):
        summary = {}
        for char in s:
            summary[char] = summary.get(char, 0) + 1
        return summary

    def summarise_numbers(self):
        """
        This function is used to summarise the occurrences of
        characters in 'zero' to 'nine' and help determine the
        unique identifiers.

        summary = {
            'e': 9, 's': 2, 'r': 3, 'u': 1, 'z': 1, 'n': 4, 'f': 2, 'v': 2,
            'h': 2, 'g': 1, 'x': 1, 'w': 1, 'o': 4, 'i': 4, 't': 3,
        }

        This implies:
        'z' is the unique identifier for 'zero' -> 0
        'w' is the unique identifier for 'two' -> 2
        'u' is the unique identifier for 'four' -> 4
        'x' is the unique identifier for 'six' -> 6
        'g' is the unique identifier for 'eight' -> 8

        After removing all the 'o' used to construct 'zero', 'two' and 'four',
        'o' is the unique identifier of 'one' -> 1

        After removing all the 'h' use to construct 'eight',
        'h' is the unique identifier of 'three' -> 3

        After removing all the 'f' use to construct 'four',
        'f' is the unique identifier of 'five' -> 5

        After removing all the 'v' use to construct 'five',
        'v' is the unique identifier of 'seven' -> 7

        After removing all the 'i' use to construct 'five', 'six' and 'eight',
        'i' is the unique identifier of 'three' -> 9

        """
        D = {
            0: 'zero',
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
        }
        summary = {}
        for key, value in D.items():
            chars = list(value)
            for char in chars:
                summary[char] = summary.get(char, 0) + 1
        return summary
