from random import randint

HIDDEN_BOARD = [[" "] * 6 for i in range(6)]
GUESS_BOARD = [[" "] * 6 for i in range(6)]
# PLAYER_GUESS_BOARD = [[" "] * 6 for i in range(6)]
# COMPUTER_GUESS_BOARD = [[" "] * 6 for i in range(6)]
LETTERS_TO_NUMBERS = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5}

def print_board(board):
    print("-" * 15)
    # if board == PLAYER_BOARD:
    #     print(" Player board")
    # else:
    #     if board == PLAYER_GUESS_BOARD:
    #         print("Computer board")
    print("COMPUTER BOARD")
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
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0,5), randint(0,5)
        board[ship_row][ship_column] = 'X'
        
def user_guess(): 
    # Wrap in try and except to get valid input, will crash if nothin is entered.
    while True:
        try: 
            row = input("Enter the row of the ship: ")
            if row in '123456':
                row = int(row) - 1
                break
        except ValueError:
            print('Enter a valid letter between 1-6')
    while True:
        try: 
            column = input("Enter the column of the ship: \n").upper()
            if column in 'ABCDEF':
                column = LETTERS_TO_NUMBERS[column]
                break
        except KeyError:
            print('Enter a valid letter between A-F')
    return row, column

def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

# place_ships(PLAYER_BOARD)
# turns = 10
# print_board(PLAYER_BOARD)
# print_board(COMPUTER_BOARD)

def play_game():
    place_ships(HIDDEN_BOARD)
    turns = 5
    while turns > 0:
        print('Guess a battleship location')
        print_board(GUESS_BOARD)
        row, column = user_guess()
        if GUESS_BOARD[row][column] == "~":
            print("You guessed that one already.")
        elif HIDDEN_BOARD[row][column] == "X":
            print("Hit")
            GUESS_BOARD[row][column] = "X" 
            turns -= 1  
        else:
            print("MISS!")
            GUESS_BOARD[row][column] = "~"   
            turns -= 1     
        if count_hit_ships(GUESS_BOARD) == 5:
            print("You win!")
            break
        print("You have " + str(turns) + " turns left")
        if turns == 0:
            print("You ran out of turns")
    
    



def get_user_inputs():
    """
    This function is going to get the users input to run the main game, if
    will keep looping if user give anything else except a 'Y' or 'N'
    """
    user_name = input("What is your name?: ")
    print(f"Welcome {user_name}, are you ready to play the game?")
    start_game = input("Enter 'Y' to begin or 'N' to exit: ").upper()
    if start_game == "Y":
        play_game()
    elif start_game == "N":
        exit()
    else:
        print("Uh oh, please enter a valid input")
        get_user_inputs()

print("Welcome to Battleships!\n")
get_user_inputs() #This will call on the get_user_inputs() function and get user name
                  #and if they're ready to play the game.
