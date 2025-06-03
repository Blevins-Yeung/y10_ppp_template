# testing
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

def drop_tile(column, grid):
    for i in range(6):
        pass

def update_grid(grid):
    pass

def print_grid(grid):
    
    print(" A B C D E F G ")
    for row in grid:
        print("|", end = "")
        for square in row:
            print(square +"|", end = "")#, end = " "
        print()
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        

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
        column = input_column(current_player)
        column_validity = check_column(column, grid)
        if column_validity == True:
            drop_tile()







main()



