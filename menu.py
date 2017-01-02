from game import Game

class Menu(object):
    def __init__(self):
        print("Welcome to Tic Tac Toe!")
        self.p1 = input("First player, please enter your name: ")
        print("Thank you {}!".format(self.p1))
        self.p2 = input("Second player, please enter your name: ")
        print("Thank you, {}!".format(self.p2))
        self.game_count = 0

    def run_menu(self):
        print("-------TIC TAC TOE-------")
        print("  1.  Play tic-tac-toe")
        print("  2.  View {}'s profile".format(self.p1))
        print("  3.  View {}'s profile".format(self.p2))
        print("  4.  View scores")
        response = input("Please type the number of what you would like to do: ")
        if response[0] == "1":
            self.game_count += 1
            game = Game(self.p1,self.p2,self,self.game_count)
            game.run_game()
        else:
            print("I'm sorry, but that option is not available at this time.")
            self.run_menu(self.game_count)