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

    def run_game(self,game_count):
        self.board.show_board()
