from random import randint
import random
import sys
import os
# NEW_BRANCH
HIDDEN_BOARD = [[" "] * 6 for i in range(6)]
# This will create a board for the computer where their ships will be placeddd

GUESS_BOARD = [[" "] * 6 for i in range(6)]
# This is users guessing board, so on the terminal it will appear as computer
# board, as we are trying to guess THEIR board, which is players guessing board

COMPUTER_HIDDEN_BOARD = [[" "] * 6 for i in range(6)]
# This will be players board, were they will be able to see where their
# own ships are placed

COMPUTER_GUESS_BOARD = [[" "] * 6 for i in range(6)]
# This is where the computer will placed their c

LETTERS_TO_NUMBERS = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}


def print_board(board):
    """
    This function will print out the board for the user and computer
    if Statement below will just name the board, which board is which
    """
    print("-" * 15)
    if board == COMPUTER_HIDDEN_BOARD:
        print(" PLAYER BOARD")
    else:
        if board == GUESS_BOARD:
            print("COMPUTER BOARD")
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
        ship_row, ship_column = randint(0, 5), randint(0, 5)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 5), randint(0, 5)
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
        except ValueError:
            print('Enter a valid number between 1-6')
    while True:
        try:
            column = input("Enter the column of the ship A-F: ").upper()
            if column in 'ABCDEF':
                column = LETTERS_TO_NUMBERS[column]
                break
        except KeyError:
            print('Enter a valid letter between A-F')
    return row, column


def computers_guess():
    """
    This function when called will generate 2 integers which will
    then be used to place the computers guess on the board
    """
    row = randint(0, 5)
    column = chr(random.randint(ord('a'), ord('f'))).upper()
    column = LETTERS_TO_NUMBERS[column]
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
    This function will start the game, it will place the ships in the
    hidden board which will be used to compare against the 'GUESS_BOARD', this
    function calls the user_guess() function to get the users input. After
    comparing the user input against the hidden board it will either add
    a splash '~' for a miss or 'X' for a direct hit. If the same ship
    location has already been called it will notify the user that that
    position cannot be called, users will keep their turn.
    """
    place_ships(HIDDEN_BOARD)  # Computers board with random ships
    place_ships(COMPUTER_HIDDEN_BOARD)  # Players ships placed randomly for them
    turns = 10
    while turns > 0:
        print_board(COMPUTER_HIDDEN_BOARD)
        print_board(GUESS_BOARD)
        print('\nGuess a battleship location')
        row, column = user_guess()
        os.system('clear')
        if GUESS_BOARD[row][column] == "~" or GUESS_BOARD[row][column] == "X":
            os.system('clear')
            print("\nYou already guessed that point!")
            print("Guess a again")
            continue
        elif HIDDEN_BOARD[row][column] == "X":
            print("\nHIT!")
            GUESS_BOARD[row][column] = "X"
            turns -= 1
        else:
            print("\nYOU MISSED!")
            GUESS_BOARD[row][column] = "~"
            turns -= 1
        computer_guess_location = computers_guess()
        computer_guess_validate(computer_guess_location)
        print(f'Computer guessed {computer_guess_location}\n')

        player_ship_count = count_hit_ships(GUESS_BOARD)
        computer_ship_count = count_computer_hit_ships(COMPUTER_HIDDEN_BOARD)
        win_lose_or_tie(player_ship_count, computer_ship_count, turns)


def continue_game(x):
    """
    This function is used to give users a bit of breathing area,
    will let them know what is going on and afterwards ask them if
    they wish to continue, if 'Y' the new board will be printed out
    with the the hit/missed points, if 'N' it will just close the game
    """
    if x == "Y":
        os.system('clear')
    elif x == "N":
        print("GAME OVER, YOU QUIT THE GAME")
        sys.exit()
    else:
        return continue_game(input("Please enter Y/N: ").upper())


def computer_guess_validate(board):
    """
    This function will get the computers guess, if it has already
    been guessed, 'X', then it will get a new point until it is valid,
    it will then place a '~' if missed or '*' if hit.
    """
    row, column = board
    if COMPUTER_HIDDEN_BOARD[row][column] == "~" or COMPUTER_HIDDEN_BOARD[row][column] == "*":
        get_new_computer_guess = computers_guess()
        computer_guess_validate(get_new_computer_guess)
        print("getting new computer guess")
    elif COMPUTER_HIDDEN_BOARD[row][column] == "X":
        print("COMPUTER HIT YOUR SHIP")
        COMPUTER_HIDDEN_BOARD[row][column] = "*"
    else:
        print("COMPUTER MISSED!")
        COMPUTER_HIDDEN_BOARD[row][column] = "~"


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
        print("You have left the game...")
        sys.exit()
    else:
        print("Uh oh, please enter a valid input")
        get_user_inputs()


def win_lose_or_tie(player_ship_count, computer_ship_count, turns):
    """
    This function will decide the outcome and print a message announcing the
    winner or if it is a tie
    """
    if player_ship_count or computer_ship_count != 5:
        print(f'Player hit ships: {player_ship_count}')
        print(f'Computer hit ships: {computer_ship_count} \n')
        if (player_ship_count or computer_ship_count == 5) or (turns == 0):
            if(player_ship_count == 5)\
                    or (player_ship_count > computer_ship_count and turns == 0):
                print("Congratulations, you beat the computer!")
                results()
                sys.exit()
            elif computer_ship_count == 5 \
                    or (computer_ship_count > player_ship_count and turns == 0):
                print("The Computer has won this round....better luck next time")
                results()
                sys.exit()
            elif (player_ship_count == computer_ship_count) and (turns == 0):
                print("It is a tie!")
                print(f'Player hit ships: {player_ship_count}')
                print(f'Computer hit ships: {computer_ship_count} \n')
                results()
                sys.exit()
        print("You have " + str(turns) + " turn(s) left \n")
        print_new_board = input("Do you want to continue? Y/N:").upper()
        os.system('clear')
        continue_game(print_new_board)
    # else: statement for if both computer and player get 5 at the same time

def results():
    print("END RESULTS")
    print_board(COMPUTER_HIDDEN_BOARD)
    print_board(GUESS_BOARD)


print("Welcome to Battleships!\n")
get_user_inputs()
