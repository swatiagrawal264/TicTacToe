from game import Game
from player import Player

class TicTacToe:
    @staticmethod
    def run():
        Player1 = Player("Jane","O")
        Player2 = Player("John","X")
        game = Game(Player1,Player2)
        game.play()

if __name__ == '__main__':
    TicTacToe.run()
        
        
