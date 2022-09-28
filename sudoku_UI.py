import os
import time
from sudoku import *

# IMPORTED FROM https://github.com/jeffsieu/py-sudoku

def format_board_ascii(board):
    table = ''
    size = 9
    width = 3
    height = 3
    cell_length = len(str(size))
    format_int = '{0:0' + str(cell_length) + 'd}'
    for i, row in enumerate(board):
        if i == 0:
            table += ('+-' + '-' * (cell_length + 1)
                      * width) * height + '+' + '\n'
        table += (('| ' + '{} ' * width) * height + '|').format(*
                                                                [format_int.format(x) if x != None and x != 0 else ' ' * cell_length for x in row]) + '\n'
        if i == 0 or i == size - 1 or i % height == height - 1:
            table += ('+-' + '-' * (cell_length + 1)
                      * width) * height + '+' + '\n'

    return table
# END


def mainMenu():
    sudoku = Sudoku()
    while True:
        line = format_board_ascii(sudoku.board).splitlines()
        for i in range(len(line)):
            print('                       ' + line[i])
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
    except KeyboardInterrupt:
        os.system("clear")
        print(errorColor + """
              
               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#
              """+ colorEnd)
        print(errorColor + "Aun no has terminado" + colorEnd)
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
    os.system("reset")
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
