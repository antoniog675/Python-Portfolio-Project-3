def get_user_inputs():
    print("Are you ready to play the game?")
    start_game = input("Enter 'Y' to begin or 'N' to exit: ").upper()
    if start_game == "Y":
        run_game()
    elif start_game == "N":
        exit()
    else:
        print("Uh oh, please enter a valid input")
        get_user_inputs()

def run_game():
    print("Lets begin")

print("Welcome to Battleships!\n")
get_user_inputs()


    
        

