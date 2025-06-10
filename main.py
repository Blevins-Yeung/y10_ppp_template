import colorama
from colorama import Fore, Back, Style

PLAYER_1_TILE = Fore.BLUE + Style.BRIGHT + "O" + Style.RESET_ALL
PLAYER_2_TILE = Fore.RED + Style.BRIGHT + "O" + Style.RESET_ALL
VALID_COLUMNS = ["A", "B", "C", "D", "E", "F", "G"]

def startup():
    global player_1
    global player_2

    player_1 = input("Player 1, enter your name: ")
    player_2 = input("Player 2, enter your name: ")
    
def make_grid():
    return [[" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "]]

def input_column(current_player):
    column = input(f"{current_player}, which column would you like to drop your tile in (A-G)? ").upper()
    return column

def check_column(column, grid):
    if column in VALID_COLUMNS:
        if grid[0][ord(column) - 65] == " ":
            return True
        else:
            return False
    else:
        return False

def drop_tile(column, grid, current_player):
    column = ord(column) - 65
    for i in range(5, -1, -1):
        if grid[i][column] == " ":
            if current_player == player_1:
                grid[i][column] = PLAYER_1_TILE
                break
            else:
                grid[i][column] = PLAYER_2_TILE
                break
    return grid
        
def print_grid(grid):
    print(" A B C D E F G ")
    for row in grid:
        print("|", end = "")
        for square in row:
            print(square +"|", end = "")#, end = " "
        print()
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        
def check_horizontal(grid):
    winning_player = None
    win = False
    check_all = False
    while win == False and check_all == False:
        for row in range(6):
            for column in range(4):
                if grid[row][column] == PLAYER_1_TILE:
                    if grid[row][column + 1] == PLAYER_1_TILE:
                        if grid[row][column + 2] == PLAYER_1_TILE:
                            if grid[row][column + 3] == PLAYER_1_TILE:
                                win = True
                                winning_player = "1"
                            else:
                                if row == 5 and column == 3:
                                    check_all = True
                        else:
                            if row == 5 and column == 3:
                                 check_all = True
                    else:
                        if row == 5 and column == 3:
                            check_all = True
                elif grid[row][column] == PLAYER_2_TILE:
                    if grid[row][column + 1] == PLAYER_2_TILE:
                        if grid[row][column + 2] == PLAYER_2_TILE:
                            if grid[row][column + 3] == PLAYER_2_TILE:
                                win = True
                                winning_player = "2"
                            else:
                                if row == 5 and column == 3:
                                    check_all = True
                        else:
                            if row == 5 and column == 3:
                                check_all = True
                    else:
                        if row == 5 and column == 3:
                            check_all = True
                else:
                    if row == 5 and column == 3:
                        check_all = True
    return win, winning_player

def check_vertical(grid):
    win = False
    check_all = False
    while win == False and check_all == False:
        for row in range(3):
            for column in range(7):
                if grid[row][column] == PLAYER_1_TILE:
                    if grid[row + 1][column] == PLAYER_1_TILE:
                        if grid[row + 2][column] == PLAYER_1_TILE:
                            if grid[row + 3][column] == PLAYER_1_TILE:
                                win = True
                            else:
                                if row == 2 and column == 6:
                                    check_all = True
                        else:
                            if row == 2 and column == 6:
                                 check_all = True
                    else:
                        if row == 2 and column == 6:
                            check_all = True
                elif grid[row][column] == PLAYER_2_TILE:
                    if grid[row + 1][column] == PLAYER_2_TILE:
                        if grid[row + 2][column] == PLAYER_2_TILE:
                            if grid[row + 3][column] == PLAYER_2_TILE:
                                win = True
                            else:
                                if row == 2 and column == 6:
                                    check_all = True
                        else:
                            if row == 2 and column == 6:
                                check_all = True
                    else:
                        if row == 2 and column == 6:
                            check_all = True
                else:
                    if row == 2 and column == 6:
                        check_all = True
    return win

def check_diagonal_right(grid):
    win = False
    check_all = False
    while win == False and check_all == False:
        for row in range(3):
            for column in range(4):
                if grid[row][column] == PLAYER_1_TILE:
                    if grid[row + 1][column + 1] == PLAYER_1_TILE:
                        if grid[row + 2][column + 2] == PLAYER_1_TILE:
                            if grid[row + 3][column + 3] == PLAYER_1_TILE:
                                win = True
                            else:
                                if row == 2 and column == 3:
                                    check_all = True
                        else:
                            if row == 2 and column == 3:
                                check_all = True
                    else:
                        if row == 2 and column == 3:
                            check_all = True
                    
                elif grid[row][column] == PLAYER_2_TILE:
                    if grid[row + 1][column + 1] == PLAYER_2_TILE:
                        if grid[row + 2][column + 2] == PLAYER_2_TILE:
                            if grid[row + 3][column + 3] == PLAYER_2_TILE:
                                win = True
                            else:
                                if row == 2 and column == 3:
                                    check_all = True
                        else:
                            if row == 2 and column == 3:
                                check_all = True                    
                    else:
                        if row == 2 and column == 3:
                            check_all = True                    
                else:
                    if row == 2 and column == 3:
                        check_all = True
    return win

def check_diagonal_left(grid):
    win = False
    check_all = False
    while win == False and check_all == False:
        for row in range(3):
            for column in range(6, 2, -1):
                if grid[row][column] == PLAYER_1_TILE:
                    if grid[row + 1][column - 1] == PLAYER_1_TILE:
                        if grid[row + 2][column - 2] == PLAYER_1_TILE:
                            if grid[row + 3][column - 3] == PLAYER_1_TILE:
                                win = True
                            else:
                                if row == 2 and column == 3:
                                    check_all = True
                        else:
                            if row == 2 and column == 3:
                                check_all = True
                    else:
                        if row == 2 and column == 3:
                            check_all = True
                    
                elif grid[row][column] == PLAYER_2_TILE:
                    if grid[row + 1][column - 1] == PLAYER_2_TILE:
                        if grid[row + 2][column - 2] == PLAYER_2_TILE:
                            if grid[row + 3][column - 3] == PLAYER_2_TILE:
                                win = True
                            else:
                                if row == 2 and column == 3:
                                    check_all = True
                        else:
                            if row == 2 and column == 3:
                                check_all = True                    
                    else:
                        if row == 2 and column == 3:
                            check_all = True                    
                else:
                    if row == 2 and column == 3:
                        check_all = True
    return win

def get_next_player(current_player):
    if current_player == None:
        next_player = player_1
    elif current_player == player_1:
        next_player = player_2
    else:
        next_player = player_1
    
    return next_player

def player_turn(current_player):
    column_valid = False
    while column_valid == False:
        column = input_column(current_player)
        column_valid = check_column(column)
    


def main():
    end_game = False
    current_player = None
    startup()
    grid = make_grid() 
    print_grid(grid)
    while end_game == False:
        current_player = get_next_player(current_player)
        column_validity = False
        while column_validity == False:
            column = input_column(current_player)
            column_validity = check_column(column, grid)
        grid = drop_tile(column, grid, current_player)
        print_grid(grid)
        end_game = check_horizontal(grid) or check_vertical(grid) or check_diagonal_right(grid) or check_diagonal_left(grid)


main()



