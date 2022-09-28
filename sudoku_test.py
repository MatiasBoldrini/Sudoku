import unittest
from unittest.mock import patch

import pytest
from sudoku import *
from sudoku_UI import *
#ohla

class Test(unittest.TestCase):

    @patch("builtins.input", side_effect=[0, 0, 1])
    @patch("builtins.print")
    def testCase_is_number_in_SubSquare_Exception(self, mock_print, mock_inputs):
        sudoku = Sudoku()
        play(sudoku)
        mock_print.assert_called_with(
            '\x1b[95mThe specified number is already in the square\x1b[0m\n')
    
    @patch("builtins.input", side_effect=[1, 0, 8])
    @patch("builtins.print")
    def testCase_is_number_in_Column_Exception(self, mock_print, mock_inputs):
        sudoku = Sudoku()
        play(sudoku)
        mock_print.assert_called_with(
            '\x1b[95mThe specified number is already in the column\x1b[0m\n')
    
    @patch("builtins.input", side_effect=[1, 0, 4])
    @patch("builtins.print")
    def testCase_is_number_in_Row_Exception(self, mock_print, mock_inputs):
        sudoku = Sudoku()
        play(sudoku)
        mock_print.assert_called_with(
            '\x1b[95mThe specified number is already in the row\x1b[0m\n')


    @patch("builtins.input", side_effect=[1, 10, 1])
    @patch("builtins.print")
    def testCase_check_column_Exception(self, mock_print, mock_inputs):
        sudoku = Sudoku()
        play(sudoku)
        mock_print.assert_called_with(
            '\x1b[95mWrong number of row / column. Try again.\x1b[0m\n')

    @patch("builtins.input", side_effect=[10, 1, 1])
    @patch("builtins.print")
    def testCase_check_row_Exception(self, mock_print, mock_inputs):
        sudoku = Sudoku()
        play(sudoku)
        mock_print.assert_called_with(
            '\x1b[95mWrong number of row / column. Try again.\x1b[0m\n')

    @patch("builtins.input", side_effect=[1, 10, 'a'])
    @patch("builtins.print")
    def testCase_check_input_2(self, mock_print, mock_inputs):
        sudoku = Sudoku()
        play(sudoku)
        mock_print.assert_called_with(
            '\x1b[95m Wrong input. Try again.\x1b[0m\n')

    # @patch("builtins.input", side_effect=[10, 1, 0])
    # @patch("builtins.print")
    # def testCase_check_square_Exception(self, mock_print, mock_inputs):
    #     sudoku = Sudoku()
        with self.assertRaises(InvalidSquareException):
            sudoku.check_square(number=1, row=1, column=1)

    @patch("builtins.input", side_effect=[1, 0, 2])
    @patch("builtins.print")
    def testCase_check_square(self, mock_print, mock_inputs):
        sudoku = Sudoku()
        play(sudoku)
        mock_print.assert_called_with(
            '\x1b[92mWell Done\x1b[0m')

    @patch("builtins.input", side_effect=[8, 8, 6])
    @patch("builtins.print")
    def testCase_user_has_won(self, mock_print, mock_input):
        sudoku = Sudoku()
        sudoku.board = [
            [1, 8, 9, 5, 4, 7, 6, 2, 3],
            [2, 3, 7, 8, 6, 1, 5, 9, 4],
            [4, 5, 6, 9, 3, 2, 7, 1, 8],
            [3, 2, 1, 6, 9, 4, 8, 5, 7],
            [5, 6, 4, 1, 7, 8, 9, 3, 2],
            [9, 7, 8, 3, 2, 5, 4, 6, 1],
            [6, 1, 3, 4, 8, 9, 2, 7, 5],
            [7, 4, 5, 2, 1, 6, 3, 8, 9],
            [8, 9, 2, 7, 5, 3, 1, 4, 0],
        ]
        play(sudoku)
        mock_print.assert_called_with(
            '\x1b[92mYou WON \x1b[0m\n')


if __name__ == "__main__":
    unittest.main()
