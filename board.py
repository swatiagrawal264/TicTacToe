class Board:
    def __init__(self):
        self.grid = [["_"for _ in range(3)] for _ in range(3)]
        self.count_move = 0
        
    
    def make_move(self,row,col,symbol):
        if not (0 <= row < 3 and 0<= col < 3) or self.grid[row][col] != '_':
            raise ValueError("Invalid Move!")
        self.grid[row][col] = symbol
        self.count_move += 1
    
    def hasWinner(self):
        #check all rows
        for row in range(3):
            if self.grid[row][0] != "_" and  self.grid[row][0]==self.grid[row][1]==self.grid[row][2]:
                return True
        #check all cols
        for col in range(3):
            if self.grid[0][col] != "_" and self.grid[0][col] == self.grid[1][col] == self.grid[2][col]:
                return True 
        #check both diagonals
        if self.grid[0][0] != "_" and self.grid[0][0] == self.grid[1][1] == self.grid[2][2]:
            return True 
        return self.grid[0][2] != "_" and self.grid[0][2]== self.grid[1][1] == self.grid[2][0]
    
    def isFull(self):
        return self.count_move == 9
        
    def print_board(self):
        for row in self.grid:
            print(" ".join(row))
        