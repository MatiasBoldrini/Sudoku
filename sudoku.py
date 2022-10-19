class NumberIsInRow(Exception):
    pass


class NumberIsInColumn(Exception):
    pass


class InvalidSquareException(Exception):
    pass


class UserHasWon(Exception):
    pass


class Sudoku():
    def __init__(self):
        self.rows = 8
        self.columns = 8
        self.board = [
            [1, 0, 0, 5, 0, 0, 0, 0, 3],
            [0, 3, 7, 0, 0, 1, 0, 0, 4],
            [0, 0, 0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 0, 9, 4, 0, 0, 0],
            [0, 0, 4, 0, 0, 0, 0, 3, 2],
            [0, 0, 0, 3, 2, 5, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 2, 0, 0],
            [7, 4, 0, 0, 0, 0, 0, 0, 0],
            [8, 0, 0, 0, 0, 3, 1, 0, 0],
        ]

    def set_number(self, number, row, column):
        # iterate over board lists
        self.check_square(number, row, column)
        self.check_column(number, column)
        self.check_row(number, row)
        self.board[row][column] = number
        self.check_if_user_won()

    def check_if_user_won(self):
        if all(0 not in x for x in self.board):  # check every item != 0
            raise UserHasWon()

    def check_square(self, number, row, column):
        def find_nearest_subSquare(row1, nearestRow=0):
            """
            It finds the nearest subsquare to the given row and column, and then checks if the number is
            already in that subsquare

            :param row1: the row of the square we're checking
            :param nearestRow: the nearest row that is divisible by 3, defaults to 0 (optional)
            :return: The board is being returned.
            """
            if row1 < nearestRow + 3:
                return nearestRow
            return find_nearest_subSquare(row1, nearestRow+3)
        column = find_nearest_subSquare(column)
        row = find_nearest_subSquare(row)
        for iterable_row in range(row, row+3):  # each subsquare has 3 elements
            for iterable_column in range(column, column+3):
                if number == self.board[iterable_row][iterable_column]:
                    raise InvalidSquareException()

    def check_row(self, number, row=0):
        if number in self.board[row]:
            raise NumberIsInRow()

    def check_column(self, number, column, row=0):
        # It's checking if the number is in the column.
        if number == self.board[row][column]:
            raise NumberIsInColumn
        if (row == len(self.board) - 1):
            return None
        return self.check_column(number, column, row + 1)

    def __str__(self) -> str:
        # print a user-friendly board
        table = ''
        size = 9
        width = 3
        height = 3
        cell_length = len(str(size))
        format_int = '{0:0' + str(cell_length) + 'd}'
        for i, row in enumerate(self.board):
            if i == 0:
                table += ('+-' + '-' * (cell_length + 1)
                          * width) * height + '+' + '\n'
            table += (('| ' + '{} ' * width) * height + '|').format(*
                                                                    [format_int.format(x) if x != None and x != 0 else ' ' * cell_length for x in row]) + '\n'
            if i == size - 1 or i % height == height - 1:
                table += ('+-' + '-' * (cell_length + 1)
                          * width) * height + '+' + '\n'
        return table


if __name__ == '__main__':  # pragma: no cover
    sudoku = Sudoku()
