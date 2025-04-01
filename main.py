# testing

def startup():
    global player_1
    global player_2

    player_1 = input("Player 1: Enter your name ")
    player_2 = input("Player 2: Enter your name ")
    
def make_grid():
    pass



def input_column(player):
    column = input(f"{player_1} which column would you like to drop your tile in (A-G)? ")


def check_column(column):
    pass

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

def player_turn(player):
    input_column()
    

def main():
    startup()
    grid = make_grid()
    print_grid(grid)
    end_game = False
    current_player = None
    while end_game == False:
        current_player = get_next_player(current_player)








