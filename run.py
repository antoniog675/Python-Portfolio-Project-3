from random import randint
import string
import random

HIDDEN_BOARD = [[" "] * 6 for i in range(6)] #Computer ships revealed
GUESS_BOARD = [[" "] * 6 for i in range(6)] #User guessing game for computers fleet
COMPUTER_HIDDEN_BOARD = [[" "] * 6 for i in range(6)] #Users board, ships hidden, users will be able to see they're own board
COMPUTER_GUESS_BOARD = [[" "] * 6 for i in range(6)] #Computer will be using this for its guess's
LETTERS_TO_NUMBERS = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5}

def print_board(board):
    print("-" * 15)
    if board == COMPUTER_HIDDEN_BOARD:
        print(" PLAYER BOARD")
    else:
        if board == GUESS_BOARD:
            print("  GUESS BOARD")
    print("-" * 15)
    print("  A B C D E F")
    print("  +-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def place_ships(board):
    """
    This function will place 5 random points on the COMPUTERS board
    """
    for ship in range(5):
        ship_row, ship_column = randint(0,5), randint(0,5)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0,5), randint(0,5)
        board[ship_row][ship_column] = 'X'
        
def user_guess(): 
    """
    This function will take in the users input for row and column and validate
    it and see if it matches where the ships are placed.
    """
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

def computers_guess():
    row = randint(0,6)
    print(row)
    column = chr(random.randint(ord('a'), ord('f'))).upper()
    column = LETTERS_TO_NUMBERS[column]
    # lowerchar = string.ascii_lowercase
    # randchar = random.choice(lowerchar)
    return row, column

def count_hit_ships(board):
    """
    This function will keep track of the hit ships, if marked with 'X'
    it will increment the count, if not it will stay the same.
    """
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

def play_game():
    """
    This function will start the game, it will place the ships in the hidden board
    which will be used to compare against the 'GUESS_BOARD', this function calls
    the user_guess() function to get the users input. After comparing the user input
    against the hidden board it will either add a splash '~' for a miss or 'X' for a 
    direct hit. If the same ship location has already been called it will notify the user
    that that position cannot be called, users will keep their turn.
    """
    place_ships(HIDDEN_BOARD)
    place_ships(COMPUTER_HIDDEN_BOARD) #Users board randomly selected for them
    turns = 5
    while turns > 0:
        print('Guess a battleship location')
        print_board(COMPUTER_HIDDEN_BOARD)
        print_board(GUESS_BOARD)
        row, column = user_guess()
        print(row,column)
        if GUESS_BOARD[row][column] == "~":
            print("You guessed that one already.")
        elif HIDDEN_BOARD[row][column] == "X":
            print("HIT!")
            GUESS_BOARD[row][column] = "X" 
            turns -= 1
        else:
            print("MISS!")
            GUESS_BOARD[row][column] = "~"   
            turns -= 1
        if count_hit_ships(GUESS_BOARD) == 5:
            print("You hit all 5 ships! CONGRATULATIONS!")
            break
        computer_guess_location = computers_guess()
        print(f'Computer guessed {computer_guess_location}')

        print("You have " + str(turns) + " turns left")
        if turns == 0:
            print("GAME OVER! You ran out of turns, you did not hit all the ships...")
            play_or_exit = input("Do you wish to play again? Y/N ").upper()
            if play_or_exit == "Y":
                play_game()
            elif play_or_exit == "N":
                exit()

# def computer_guess_validate():
#     row, column = computers_guess()
#     if COMPUTER_HIDDEN_BOARD[row][column] == "~":
#             print("You guessed that one already.")
#     elif COMPUTER_GUESS_BOARD[row][column] == "X":
#         print("COMPUTER HIT YOUR SHIP!")
#         COMPUTER_HIDDEN_BOARD[row][column] = "*" 
#         turns -= 1
#     else:
#         print("COMPUTER MISSED!")
#         COMPUTER_HIDDEN_BOARD[row][column] = "~"   
#         turns -= 1
#     if count_hit_ships(COMPUTER_HIDDEN_BOARD) == 5:
#         print("COMPUTER HAS WON....BETTER LUCK NEXT TIME...")

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
get_user_inputs() 
#This will call on the get_user_inputs() function and get user name
#and if they're ready to play the game.
