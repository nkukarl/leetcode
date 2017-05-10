class Solution(object):
    def count_battleships(self, board):
        """

        Assumptions:
        <1> You receive a valid board, made of only battleships or empty slots.
        <2> Battleships can only be placed horizontally or vertically.
            In other words, they can only be made of the shape 1xN
            or Nx1, where N can be of any size.
        <3> At least one horizontal or vertical cell separates between
            two battleships - there are no adjacent battleships.

        e.g., a board like the following is valid:
        'XX..X',
        '....X',
        '..X..',
        '..X..',
        'XX.XX',

        e.g., a board like the following is valid:
        'XX..X',
        '...XX',
        '..X..',
        '..X..',
        'XX.XX',

        """
        ship = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != 'X':
                    continue
                # Check whether its left belongs to the same battleship
                if c > 0 and 'X' == board[r][c - 1]:
                    continue
                # Check whether its top belongs to the same battleship
                if r > 0 and 'X' == board[r - 1][c]:
                    continue
                ship += 1
        return ship