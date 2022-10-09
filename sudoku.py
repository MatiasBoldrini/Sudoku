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
        if all(0 not in x for x in self.board): # check every item != 0
            raise UserHasWon()
    def check_square(self, number, row, column):
        def find_nearest_subSquare(row1, nearestRow=0):
            # recursively find the nearest row or column from left to right
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

    def check_column(self, number, column, row=0):  # Recursively check columns
        if number == self.board[row][column]:
            raise NumberIsInColumn
        if (row == len(self.board) -1):  # check the last element in column
            return None
        return self.check_column(number, column, row + 1)
if __name__ == '__main__':
    sudoku = Sudoku()