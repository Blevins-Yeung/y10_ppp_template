# testing
valid_columns = ["a", "b", "c", "d", "e", "f", "g"]
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
    column = input(f"{current_player} which column would you like to drop your tile in (A-G)? ")
    return column

def check_column(column, row):
    if column in valid_columns:
        if row == 1:
            return False
        else:
            return True
    else:
        return False

def drop_tile(column, row):
    pass

def update_grid(grid):
    pass

def print_grid(grid):
    pass

def check_horizontal():
    pass

def check_vertical():  
    pass

def check_diagonal_left():
    pass

def check_diagonal_right():
    pass

def check_win():
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
        column_valid = check_column(column, row)
    

    

def main():
    startup()
    grid = make_grid()
    print_grid(grid)
    end_game = False
    current_player = None
    while end_game == False:
        current_player = get_next_player(current_player)








