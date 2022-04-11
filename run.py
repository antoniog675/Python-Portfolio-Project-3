from random import randint
import string
import random

HIDDEN_BOARD = [[" "] * 6 for i in range(6)] #Randomly places ships for user, computer will try and guess this...
GUESS_BOARD = [[" "] * 6 for i in range(6)] #User guessing board for computers fleet/ so this is basicallt the computers board...
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
    while True:
        try: 
            row = input("Enter the row of the ship 1-6: ")
            if row in '123456':
                row = int(row) - 1
                break
            elif row != '123456':
                print("Enter a valid number between 1-6")
        except ValueError:
            print('Enter a valid number between 1-6')
    while True:
        try: 
            column = input("Enter the column of the ship A-F:").upper()
            if column in 'ABCDEF':
                column = LETTERS_TO_NUMBERS[column]
                break
        except KeyError:
            print('Enter a valid letter between A-F')
    return row, column

def computers_guess():
    row = randint(0,5)
    column = chr(random.randint(ord('a'), ord('f'))).upper()
    column = LETTERS_TO_NUMBERS[column]
    # lowerchar = string.ascii_lowercase
    # randchar = random.choice(lowerchar)
    print(row, column)
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

def count_computer_hit_ships(board):
    """
    This will be the count for the computer, if they hit all ships first
    game over
    """
    count = 0
    for row in board:
        for column in row:
            if column == '*':
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
    place_ships(HIDDEN_BOARD) #Computers board with random ships
    place_ships(COMPUTER_HIDDEN_BOARD) #Users board randomly selected for them
    turns = 5
    while turns > 0:
        print('Guess a battleship location')
        print_board(COMPUTER_HIDDEN_BOARD)
        print_board(GUESS_BOARD)
        row, column = user_guess()
        if GUESS_BOARD[row][column] == "~":
            print("You guessed that one already.")
            continue
        elif GUESS_BOARD[row][column] == "X":
            print("You guessed that one already.")
            continue
        elif HIDDEN_BOARD[row][column] == "X":
            print("HIT!")
            GUESS_BOARD[row][column] = "X"
            turns -= 1
        else:
            print("YOU MISSED!")
            GUESS_BOARD[row][column] = "~"
            turns -= 1
        computer_guess_location = computers_guess()
        computer_guess_validate(computer_guess_location)
        print(f'Computer guessed {computer_guess_location}')

        player_ship_count = count_hit_ships(GUESS_BOARD)
        computer_ship_count = count_computer_hit_ships(COMPUTER_HIDDEN_BOARD)


        print(f'Player it ships: {player_ship_count} \nComputer hit ships: {computer_ship_count} \n')
        print("You have " + str(turns) + " turn(s) left \n")
        win_lose_or_tie(player_ship_count, computer_ship_count, turns)
    
def computer_guess_validate(board):
    row, column = board
    if COMPUTER_HIDDEN_BOARD[row][column] == "~":
        print("Getting new value if already guessed")
        get_new_computer_guess = computers_guess()
        computer_guess_validate(get_new_computer_guess)
            # print("You guessed that one already.") Create loop to call computer guess function again
    elif COMPUTER_HIDDEN_BOARD[row][column] == "*":
        print("Getting new value if hit")
        get_new_computer_guess = computers_guess()
        computer_guess_validate(get_new_computer_guess)
        pass #Get new computer inputs
    elif COMPUTER_HIDDEN_BOARD[row][column] == "X":
        print("COMPUTER HIT YOUR SHIP!")
        COMPUTER_HIDDEN_BOARD[row][column] = "*"
    else:
        print("COMPUTER MISSED!")
        COMPUTER_HIDDEN_BOARD[row][column] = "~"   
    # if count_computer_hit_ships(COMPUTER_HIDDEN_BOARD) == 5:
    #     print("COMPUTER HAS WON....BETTER LUCK NEXT TIME...")
        

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

def win_lose_or_tie(player_ship_count, computer_ship_count, turns):
    if (player_ship_count and computer_ship_count > 0 and player_ship_count == computer_ship_count) or (turns == 0):
        outcome = print("It is a tie!")
        print(f'Player it ships: {player_ship_count} \nComputer hit ships: {computer_ship_count} \n')
        end_of_game(outcome)
    elif player_ship_count == 1 or player_ship_count > computer_ship_count:
        outcome = print("Congratulations, you beat the computer!")
        end_of_game(outcome)
    elif computer_ship_count == 1 or computer_ship_count > player_ship_count:
        outcome = print("The Computer has won this round....better luck next time")
        end_of_game(outcome)

def end_of_game(outcome):
    print_board(COMPUTER_HIDDEN_BOARD)
    print_board(GUESS_BOARD)
    play_or_exit = input("Do you wish to play again? Y/N ").upper()
    if play_or_exit == "Y":
        get_user_inputs()
    elif play_or_exit == "N":
        exit()

print("Welcome to Battleships!\n")
get_user_inputs() 
#This will call on the get_user_inputs() function and get user name
#and if they're ready to play the game.
