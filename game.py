from board import Board

class Game(object):

    def __init__(self,p1,p2,game_count=1,x_symb="X",y_symb="y"):
        # Turn taking for successive games
        if not game_count %2 == 0:
            self.x_player = p1
            self.y_player = p2
        else:
            self.x_player = p2
            self.y_player = p1
        self.x_symb = x_symb
        self.y_symb = y_symb
        self.turn_count = 0
        self.board = Board(self.x_symb,self.y_symb)


    def run_game(self):
        self.board.show_board()
        while (not self.win(self.x_symb)) and (not self.win(self.y_symb) and (not self.is_tied())):
            if self.turn_count % 2 == 0:
                square = input("{}, please enter the code for where you would like to place your {} (e.g., A1, C2): "
                               .format(self.x_player,self.x_symb))
                # TODO: Add exception if input is not a valid square
                self.board.move(self.x_symb, square)
            else:
                square = input("{}, please enter the code for where you would like to place your {} (e.g., A1, C2): "
                               .format(self.y_player,self.y_symb))
                # TODO: Add exception if input is not a valid square
                self.board.move(self.y_symb, square)
            self.turn_count += 1
            self.board.show_board()
        if self.is_tied():
            print("The game is tied!")
        elif self.win(self.x_symb):
            print("Congratulations, {}! You have won!".format(self.x_player))
        else:
            print("Congratulations, {}! You have won!".format(self.y_player))

    # Tests whether the player marking with a particular symbol has won
    def win(self,symbol):
        symb_win = False
        if self.board["A1"] == symbol:
            self.board = (self.board["A2"] == symbol and self.board["A3"] == symbol) or (
                self.board["B2"] == symbol and self.board["C3"] == symbol) or (self.board["B1"] == symbol and self.board["C1"] == symbol)
        elif self.board["B2"] == symbol:
            symb_win = (self.board["B1"] == symbol and self.board["B3"] == symbol) or (
                self.board["A2"] == symbol and self.board["C2"] == symbol) or (self.board["C1"] == symbol and self.board["A3"] == symbol)
        elif self.board["C3"] == symbol:
            symb_win = (self.board["A3"] == symbol and self.board["B3"] == symbol) or (
                self.board["C1"] == symbol and self.board["C2"] == symbol)
        return symb_win

    # Tests whether the game is tied
    def is_tied(self):
        return (not " " in self.board.values()) and (not self.win("X") and (not self.win("O")))