
    if is_tied():
        print("The game is tied!")
    elif win("X"):
        print("Congratulations, {}! You have won!".format(x_player))
    else:
        print("Congratulations, {}! You have won!".format(o_player))

    play_again = input("Would you like to play again? (Y/N) : ")
    if play_again.casefold() == "y".casefold():
        run_game(game_count+1, p1, p2)
    else:
        print("Goodbye!")


# Prompt users for their names
print("Welcome to Tic Tac Toe!")
p1 = input("First player, please enter your name: ")
print("Thank you {}!".format(p1))
p2 = input("Second player, please enter your name: ")
print("Thank you, {}!".format(p2))

# Run the first game
run_game(0, p1, p2)



