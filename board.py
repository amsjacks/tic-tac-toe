class Board(object):
    clean_board = {"A1": " ", "A2": " ", "A3": " ",
                   "B1": " ", "B2": " ", "B3": " ",
                   "C1": " ", "C2": " ", "C3": " "}

    def __init__(self, x_symb="X", y_symb="O"):
        self.positions = Board.clean_board
        self.x_symb = x_symb
        self.y_symb = y_symb

    def at_position(self, square):
        return self.positions[square]

    def is_full(self):
        return not " " in self.positions

    def is_valid_square(self, square):
        return square in Board.clean_board

    def show_board(self):
        print("      A     B     C  ")
        print("   |_____|_____|_____")
        print("   |     |     |     ")
        print(" 1 |  {}  |  {}  |  {}  ".format(self.positions["A1"], self.positions["B1"], self.positions["C1"]))
        print("   |_____|_____|_____")
        print("   |     |     |     ")
        print(" 2 |  {}  |  {}  |  {}  ".format(self.positions["A2"], self.positions["B2"], self.positions["C2"]))
        print("   |_____|_____|_____")
        print("   |     |     |     ")
        print(" 3 |  {}  |  {}  |  {}  ".format(self.positions["A3"], self.positions["B3"], self.positions["C3"]))
        print("   |_____|_____|_____")

    def move(self, symbol, square):
        if self.positions[square] == " ":
            self.positions[square] = symbol
        else:
            new_square = input("I'm sorry, that square is already occupied. Please select another:")
            self.move(symbol, new_square)
