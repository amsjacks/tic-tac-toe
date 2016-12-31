def run_game(game_count, p1, p2):
    # Initialize a bunch of game-specific vars
    clear_board()
    x_player = p1
    o_player = p2
    turn_count = 0
    if not game_count % 2 == 0:
        # Turn taking for successive games
        x_player = p2
        o_player = p1

    show_board()
    while (not x_win()) and (not o_win()):
        if turn_count % 2 == 0:
            square = input("{}, please enter the code for where you would like to place your X (e.g., A1, C2): "
                           .format(x_player))
            move("X", square) # Could put the symbol in a global var so that can be customized
        else:
            square = input("{}, please enter the code for where you would like to place your O (e.g., A1, C2): "
                           .format(o_player))
            move("O", square)
        turn_count += 1
        show_board()

    if x_win():
        print("Congratulations, {}! You have won!".format(x_player))
    else:
        print("Congratulations, {}! You have won!".format(o_player))

    play_again = input("Would you like to play again? (Y/N) : ")
    if play_again.casefold() == "y".casefold():
        run_game(game_count+1, p1, p2)
    else:
        print("Goodbye!")


def show_board():
    print("      A     B     C  ")
    print("   |_____|_____|_____")
    print("   |     |     |     ")
    print(" 1 |  {}  |  {}  |  {}  ".format(board["A1"], board["B1"], board["C1"]))
    print("   |_____|_____|_____")
    print("   |     |     |     ")
    print(" 2 |  {}  |  {}  |  {}  ".format(board["A2"], board["B2"], board["C2"]))
    print("   |_____|_____|_____")
    print("   |     |     |     ")
    print(" 3 |  {}  |  {}  |  {}  ".format(board["A3"], board["B3"], board["C3"]))
    print("   |_____|_____|_____")


def clear_board():
    global board
    board = {"A1": " ", "A2": " ", "A3": " ",
            "B1": " ", "B2": " ", "B3": " ",
            "C1": " ", "C2": " ", "C3": " "}

def move(symbol, square):
    global board
    board[square] = symbol

def x_win():
    pass

def o_win():
    pass


# Set up
board = {}

print("Welcome to Tic Tac Toe!")
p1 = input("First player, please enter your name: ")
print("Thank you {}!".format(p1))
p2 = input("Second player, please enter your name: ")
print("Thank you, {}!".format(p2))

# Run the first game
run_game(0, p1, p2)



