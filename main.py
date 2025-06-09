import colorama
from colorama import Fore, Back, Style

player_1_tile = Fore.BLUE + Style.BRIGHT + "O" + Style.RESET_ALL
player_2_tile = Fore.RED + Style.BRIGHT + "O" + Style.RESET_ALL

valid_columns = ["A", "B", "C", "D", "E", "F", "G"]

def startup():
    global player_1
    global player_2

    player_1 = input("Player 1: Enter your name ")
    player_2 = input("Player 2: Enter your name ")
    
def make_grid():
    return [[" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "]]


def input_column(current_player):
    column = input(f"{current_player} which column would you like to drop your tile in (A-G)? ").upper()
    return column

def check_column(column, grid):
    if column in valid_columns:
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
                grid[i][column] = player_1_tile
                break
            else:
                grid[i][column] = player_2_tile
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
        

def check_horizontal():
    

def check_vertical():  
    pass

def check_diagonal_left():
    pass

def check_diagonal_right():
    pass


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







main()



