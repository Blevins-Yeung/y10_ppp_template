import colorama
from colorama import Fore, Back, Style

PLAYER_1_TILE = Fore.BLUE + Style.BRIGHT + "O" + Style.RESET_ALL
PLAYER_2_TILE = Fore.RED + Style.BRIGHT + "O" + Style.RESET_ALL
VALID_COLUMNS = ["A", "B", "C", "D", "E", "F", "G"]

def startup():
    print(" _____                              _       ___")
    print("/  __ \                            | |     /   |")
    print("| /  \/ ___  _ __  _ __   ___  ___ | |_   / /| |")
    print("| |    / _ \|  _ \|  _ \ / _ \/ _ || __| / /_| |")
    print("| \__/\ (_) | | | | | | |  __/ (__ | |_  \___  |")
    print(" \____/\___/|_| |_|_| |_|\___|\___| \__|     |_/ \n")

    print("Enter P to play")
    print("Enter Q to quit")

    choice = input().lower().strip()
    while choice != "p" and choice != "q":
        choice = input("Please enter a valid option. " )
    if choice == "p":
        player_1_name = input("Player 1, enter your name: ").strip()
        while len(player_1_name) < 2 or len(player_1_name) > 20:
            if len(player_1_name) < 2:
                print("Your name has to be longer than 1 character.")
                player_1_name = input("Player 1, enter your name: ")
            else:
                print("Your name has to be shorter than 20 characters.")
                player_1_name = input("Player 1, enter your name: ")
        player_2_name = input("Player 2, enter your name: ")
        while len(player_2_name) < 2 or len(player_2_name) > 20 or player_1_name.strip().lower() == player_2_name.strip().lower(): #Check all the conditions
            if len(player_2_name) < 2:
                print("Your name has to be longer than 1 character.")
                player_2_name = input("Player 2, enter your name: ")
            elif len(player_2_name) > 20:
                print("Your name has to be shorter than 20 characters.")
                player_2_name = input("Player 2, enter your name: ")
            else:
                print("Your name has to be different than Player 1's name.")
                player_2_name = input("Player 2, enter your name: ")
        return player_1_name, player_2_name
    else:
        exit()

def make_grid():
    return [[" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "]]

def input_column(current_player):
    column = input(f"{current_player}, which column would you like to drop your tile in (A-G)? ").upper().strip()
    while column not in VALID_COLUMNS:
        if len(column) != 1:
            print("Please input one letter (A-G)")
            column = input(f"{current_player}, which column would you like to drop your tile in (A-G)? ").upper().strip()
        else:
            print("Your input has to be either A or B or C or D or E or F or G.")
            column = input(f"{current_player}, which column would you like to drop your tile in (A-G)? ").upper().strip()
    return column

def check_column(column, grid):
    if column in VALID_COLUMNS:
        if grid[0][ord(column) - 65] == " ": #checks if the slot is empty
            return True
        else:
            return False
    else:
        return False

def drop_tile(column, grid, current_player, player_1_name):
    column = ord(column) - 65
    for i in range(5, -1, -1):
        if grid[i][column] == " ":
            if current_player == player_1_name:
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
    return win

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

def get_next_player(current_player, player_1_name, player_2_name):
    if current_player == None:
        next_player = player_1_name
    elif current_player == player_1_name:
        next_player = player_2_name
    else:
        next_player = player_1_name
    
    return next_player

def player_turn(current_player):
    column_valid = False
    while column_valid == False:
        column = input_column(current_player)
        column_valid = check_column(column)
    
def print_win_message(current_player):
    print(f"{current_player} has won the game!")


def main():
    end_game = False
    current_player = None
    player_1_name, player_2_name = startup()
    grid = make_grid() 
    print_grid(grid)
    while end_game == False:
        current_player = get_next_player(current_player, player_1_name, player_2_name)
        column_validity = False
        while column_validity == False:
            column = input_column(current_player)
            column_validity = check_column(column, grid)
        grid = drop_tile(column, grid, current_player, player_1_name)
        print_grid(grid)
        end_game = check_horizontal(grid) or check_vertical(grid) or check_diagonal_right(grid) or check_diagonal_left(grid)
    print_win_message(current_player)

main()



