class Solution(object):
    def original_digits(self, s):
        self.D = {
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
        self.summarise_string(s)
        self.counts = [0] * 10

        # Process words with unique identifier
        self.identify('z', 0)
        self.identify('w', 2)
        self.identify('u', 4)
        self.identify('x', 6)
        self.identify('g', 8)

        # Non-unique
        self.identify('o', 1)
        self.identify('h', 3)
        self.identify('f', 5)
        self.identify('v', 7)
        self.identify('i', 9)

        # Prepare answer
        ans = ''
        for i, count in enumerate(self.counts):
            ans += str(i) * count
        return ans

    def identify(self, unique_identifier, i):
        word = self.D[i]
        if self.summary.get(unique_identifier, 0) > 0:
            self.counts[i] = self.summary[unique_identifier]
            for char in word:
                self.summary[char] -= self.counts[i]

    def summarise_string(self, s):
        self.summary = {}
        for char in s:
            self.summary[char] = self.summary.get(char, 0) + 1

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
