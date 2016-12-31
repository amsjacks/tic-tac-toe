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
    while (not win("X")) and (not win("O")):
        if turn_count % 2 == 0:
            square = input("{}, please enter the code for where you would like to place your X (e.g., A1, C2): "
                           .format(x_player))
            # TODO: Add exception if input is not a valid square
            move("X", square)  # TODO: put the symbol in a variable so that can be customized by player
        else:
            square = input("{}, please enter the code for where you would like to place your O (e.g., A1, C2): "
                           .format(o_player))
            # TODO: Add exception if input is not a valid square
            move("O", square)
        turn_count += 1
        show_board()

    if win("X"):
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
    # TODO: throw exception if the square is already occupied
    board[square] = symbol

# Tests whether the player marking with a particular symbol has won
def win(symbol):
    symb_win = False
    if board["A1"] == symbol:
        symb_win = (board["A2"] == symbol and board["A3"] == symbol) or (
            board["B2"] == symbol and board["C3"] == symbol) or (board["B1"] == symbol and board["C1"] == symbol)
    elif board["B2"] == symbol:
        symb_win = (board["B1"] == symbol and board["B3"] == symbol) or (
            board["A2"] == symbol and board["C2"] == symbol) or (board["C1"] == symbol and board["A3"] == symbol)
    elif board["C3"] == symbol:
        symb_win = (board["A3"] == symbol and board["B3"] == symbol) or (board["C1"] == symbol and board["C2"] == symbol)
    return symb_win


# Set up global value
board = {}

# Prompt users for their names
print("Welcome to Tic Tac Toe!")
p1 = input("First player, please enter your name: ")
print("Thank you {}!".format(p1))
p2 = input("Second player, please enter your name: ")
print("Thank you, {}!".format(p2))

# Run the first game
run_game(0, p1, p2)



