class Solution(object):
    def full_justify(self, words, max_width):
        row = []
        width = 0
        rows = []
        for word in words:
            if [] == row:
                row = [word]
                width = len(word)
                continue
            if width + len(word) + 1 <= max_width:
                row.append(word)
                width += len(word) + 1
            else:
                rows.append(row)
                row = [word]
                width = len(word)
        if row != []:
            rows.append(row)
        ans = []
        spacing_char = ' '

        for row in rows[:-1]:
            # If there is only one word in this row, make it left justified.
            if 1 == len(row):
                line = row[0] + spacing_char * (max_width - len(row[0]))
            else:
                text_width = sum([len(word) for word in row])
                # Total spacing width
                spacing_width = max_width - text_width
                gap_count = len(row) - 1
                # Get same gap_width for all gaps
                gap_width = spacing_width // gap_count
                gaps = [spacing_char * gap_width] * gap_count
                # For any additional remaining width
                # start to distribute them from the left
                remaining_width = spacing_width -  gap_width * gap_count
                for rw in range(remaining_width):
                    gaps[rw] += spacing_char
                # Create line using words and gaps
                line = row[0]
                for word, gap in zip(row[1:], gaps):
                    line += gap + word
            ans.append(line)

        # Special treatment for the last line:
        # left justified with no extra spaces inserted between words
        row = rows[-1]
        line_raw = ' '.join(row)
        line = line_raw + spacing_char * (max_width - len(line_raw))
        ans.append(line)

        return ans
