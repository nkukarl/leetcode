class Solution:
    def is_valid_sudoku(self, board):
        """

        Args:
            board: An Array of strings

        Returns (bool):

        """
        grid_size = 9
        block_boundary = [0, 3, 6]
        block_size = 3

        if len(board) != grid_size:
            return False
        if len(board[0]) != grid_size:
            return False

        row_number = col_number = grid_size

        # Check each row
        for r_id in range(row_number):
            row = board[r_id]
            if not self._check_row_column_block(row):
                return False

        # Check each column
        for c_id in range(col_number):
            col = ''
            for r_id in range(row_number):
                col += board[r_id][c_id]
            if not self._check_row_column_block(col):
                return False

        # Check each block
        for r_id in block_boundary:
            for c_id in block_boundary:
                block = ''
                for r_shift in range(0, block_size):
                    for c_shift in range(0, block_size):
                        block += board[r_id + r_shift][c_id + c_shift]
                if not self._check_row_column_block(block):
                    return False

        return True

    def _check_row_column_block(self, raw_collection):
        """

        Args:
            raw_collection: A string representing numbers in
                a row, a column or a block

        Returns (bool):

        """

        try:
            collection = list(map(int, raw_collection.replace('.', '')))
        except ValueError: # Might contain invalid literal for int()
            return False
        else:
            return len(set(collection)) == len(collection)
