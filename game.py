from board import Board


class Game(object):
    def __init__(self, p1, p2, menu, game_count, x_symb="X", o_symb="O"):
        # Turn taking for successive games
        self.menu = menu
        if not game_count % 2 == 0:
            self.x_player = p1
            self.o_player = p2
        else:
            self.x_player = p2
            self.o_player = p1
        self.x_symb = x_symb
        self.o_symb = o_symb
        self.turn_count = 0
        self.board = Board(self.x_symb, self.o_symb)

    def run_game(self):
        self.board.show_board()
        while (not self.win(self.x_symb)) and (not self.win(self.o_symb) and (not self.is_tied())):
            if self.turn_count % 2 == 0:
                square = self.get_move(self.x_player)
                self.board.move(self.x_symb, square)

            else:
                square = self.get_move(self.o_player)
                self.board.move(self.o_symb, square)
            self.turn_count += 1
            self.board.show_board()
        if self.is_tied():
            print("The game is tied!")
        elif self.win(self.x_symb):
            print("Congratulations, {}! You have won!".format(self.x_player))
        else:
            print("Congratulations, {}! You have won!".format(self.o_player))
        del self

    def __del__(self):
        play_again = input("Would you like to play again? (Y/N) : ")
        if play_again.casefold() == "y".casefold():
            self.menu.run_menu()
        else:
            print("Goodbye!")

    # Prompt the user for their next move
    def get_move(self, player):
        square = ""
        while not self.board.is_valid_square(square):
            from_player = input("{}, please enter the code for where you would like to place your marker (e.g., A1, "
                                "C2): ".format(player))
            square = from_player.upper()
        return square

    # Tests whether the player marking with a particular symbol has won
    def win(self, symbol):
        symb_win = False
        if self.board.at_position("A1") == symbol:
            symb_win = (self.board.at_position("A2") == symbol and self.board.at_position("A3") == symbol) or (
                self.board.at_position("B2") == symbol and self.board.at_position("C3") == symbol) or (
                       self.board.at_position("B1") == symbol and self.board.at_position("C1") == symbol)
        elif self.board.at_position("B2") == symbol:
            symb_win = (self.board.at_position("B1") == symbol and self.board.at_position("B3") == symbol) or (
                self.board.at_position("A2") == symbol and self.board.at_position("C2") == symbol) or (
                       self.board.at_position("C1") == symbol and self.board.at_position("A3") == symbol)
        elif self.board.at_position("C3") == symbol:
            symb_win = (self.board.at_position("A3") == symbol and self.board.at_position("B3") == symbol) or (
                self.board.at_position("C1") == symbol and self.board.at_position("C2") == symbol)
        return symb_win

    # Tests whether the game is tied
    def is_tied(self):
        return (self.board.is_full()) and (not self.win("X") and (not self.win("O")))
