class Solution(object):
    def island_perimeter(self, grid):
        # Get raw perimeter by multiplying the number of squares by 4
        perimeter_raw = sum([sum(row) for row in grid]) * 4
        # Need to apply get_overlapped() for each row and column
        # in order to get overlapped edges
        # Transpose grid makes it much easier
        grid_transposed = zip(*grid)  # Yes, this is how you transpose a grid
        overlapped = sum([self.get_overlapped(row) for row in grid]) + \
                     sum([self.get_overlapped(row) for row in grid_transposed])
        return perimeter_raw - overlapped

    def get_overlapped(self, row):
        """

        E.g., row = [1, 1, 1, 0, 0, 1, 1], should return 6.
        Since in the first chunk of 1s, there are 4 overlapped edges.
        And in the second chunk of 1s, there are 2 overlapped edges.

        Returns:

        """
        row = [0] + list(row) + [0]
        overlapped = 0
        count = 0
        for n in row:
            if 1 == n:
                count += 1
            else:
                overlapped += max(0, (count - 1) * 2)
                count = 0
        return overlapped
