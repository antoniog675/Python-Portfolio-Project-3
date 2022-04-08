import random

PLAYER_BOARD = [[" "] * 6 for i in range(6)]
COMPUTER_BOARD = [[" "] * 6 for i in range(6)]
# PLAYER_GUESS_BOARD = [[" "] * 6 for i in range(6)]
# COMPUTER_GUESS_BOARD = [[" "] * 6 for i in range(6)]
LETTERS_TO_NUMBERS = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5}

def print_board(board):
    print("-" * 15)
    print("  User board")
    print("-" * 15)
    print("  A B C D E F")
    print("  +-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def place_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,5), randint(0,5)
        while board [ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0,5), randint(0,5)
        board[ship_row][ship_column] = 'X'
        
def user_guess(): 
    # Wrap in try and except to get valid input, will crash if nothin is entered.
    row = input("Please enter a ship row 1-6: ")
    while row not in '123456':
        print('Please enter valid row')
        row = input("Please enter a ship row 1-6: ")
    column = input("Please enter a ship column A-F: ").upper()
    while column not in 'ABCEDF':
        print("Please enter a valid column: ").upper()
    return int(row) -1, LETTERS_TO_NUMBERS[column]



def get_user_inputs():
    """
    This function is going to get the users input to run the main game, if
    will keep looping if user give anything else except a 'Y' or 'N'
    """
    user_name = input("What is your name?: ")
    print(f"Welcome {user_name}, are you ready to play the game?")
    start_game = input("Enter 'Y' to begin or 'N' to exit: ").upper()
    if start_game == "Y":
        print_board(PLAYER_BOARD)
    elif start_game == "N":
        exit()
    else:
        print("Uh oh, please enter a valid input")
        get_user_inputs()

# def run_game():
#     print("Lets begin")

print("Welcome to Battleships!\n")
get_user_inputs()