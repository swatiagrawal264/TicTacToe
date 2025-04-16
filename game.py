from board import Board
#from player import Player

class Game:
    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.current_player = player1
    
    def play(self):
        self.board.print_board()
        while not self.board.isFull() and not self.board.hasWinner():
            print(f"{self.current_player.get_name()}'s turn.")
            row = self.valid_input("Enter a row between 0 to 2: ")
            col = self.valid_input("Enter a col between 0 to 2: ")
            try:
                self.board.make_move(row,col,self.current_player.get_symbol())
                self.board.print_board()
                self.switch_player()
            except ValueError as e:
                print(str(e))

        if self.board.hasWinner():
            self.switch_player()
            print(f"Congratulations {self.current_player.get_name()} is the winner")
        else:
            print("Its a tie!!")

    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1
        

    def valid_input(self, message):
        while True:
            try:
                user_input = int(input(message))
                if 0 <= user_input < 3:
                    return user_input
                else:
                    print("Invalid user imput!! input value between 0 and 2")
            except ValueError:
                print("Invalid user imput!! input value between 0 and 2")

    