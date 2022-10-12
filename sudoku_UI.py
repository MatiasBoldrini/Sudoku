import os
from sudoku import *
def mainMenu():
    sudoku = Sudoku()
    while True:
        # line = format_board_ascii(sudoku.board).splitlines()
        # for i in range(len(line)):
        #     print('                       ' + line[i])
        print(format_board_ascii(sudoku.board))
        play(sudoku)


def play(sudoku):
    errorColor = '\033[95m'
    correctColor = '\033[92m'
    colorEnd = '\033[0m'
    # print ascii sudoku table

    # check input
    try:
        row = int(input(correctColor + '\n\nSelect a Row (0-8) → ' + colorEnd))
        column = int(
            input(correctColor + 'Select a Column (0-8) ↑ ' + colorEnd))
        number = int(
            input(correctColor + 'Input a number (1-9) ↪ ' + colorEnd))
        assert (0 < number < 10 and 0 <= row < 10 and 0 <= column < 10)
        sudoku.set_number(number, row, column)
    except UserHasWon:
        print(correctColor + 'You WON ' + colorEnd + '\n')
    except NumberIsInRow:
        print(errorColor + 'The specified number is already in the row' + colorEnd + '\n')
    except NumberIsInColumn:
        print(
            errorColor + 'The specified number is already in the column' + colorEnd + '\n')
    except InvalidSquareException:
        print(
            errorColor + 'The specified number is already in the square' + colorEnd + '\n')
    except ValueError:
        print(errorColor + ' Wrong input. Try again.' + colorEnd + '\n')
    except AssertionError:
        print(
            errorColor + 'Wrong number of row / column. Try again.' + colorEnd + '\n')
    else:
        print(correctColor + 'Well Done' + colorEnd)
    


if __name__ == "__main__":
    print("""
    \033[92m
              ██████  █    ██ ▓█████▄  ▒█████   ██ ▄█▀ █    ██ 
            ▒██    ▒  ██  ▓██▒▒██▀ ██▌▒██▒  ██▒ ██▄█▒  ██  ▓██▒
            ░ ▓██▄   ▓██  ▒██░░██   █▌▒██░  ██▒▓███▄░ ▓██  ▒██░
              ▒   ██▒▓▓█  ░██░░▓█▄   ▌▒██   ██░▓██ █▄ ▓▓█  ░██░
            ▒██████▒▒▒▒█████▓ ░▒████▓ ░ ████▓▒░▒██▒ █▄▒▒█████▓ 
            ▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ 
            ░ ░▒  ░ ░░░▒░ ░ ░  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒ ▒░░░▒░ ░ ░ 
            ░  ░  ░   ░░░ ░ ░  ░ ░  ░ ░ ░ ░ ▒  ░ ░░ ░  ░░░ ░ ░ 
                  ░     ░        ░        ░ ░  ░  ░      ░     
                               ░                          
    \033[0m  """)
    mainMenu()
