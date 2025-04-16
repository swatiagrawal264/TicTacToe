# Tic-Tac-Toe (Low-Level Design)

OOP implementation of Tic-Tac-Toe with Python. Focuses on clean class design and game logic.

## Classes & Responsibilities

### 1. `Board`
- **Attributes**:
  - `grid`: 3x3 matrix (stores `_`/X/O)
  - `count_move`: tracks moves
- **Key Methods**:
  - `make_move(row, col, symbol)`: Validates and executes moves
  - `hasWinner()`: Checks rows/columns/diagonals
  - `isFull()`: Checks for ties
  - `print_board()`: Displays current state

### 2. `Player`
- **Attributes**:
  - `name`: Player identifier
  - `symbol`: X or O
- **Methods**:
  - `get_name()`, `get_symbol()`: Accessors

### 3. `Game` (Main Controller)
- **Attributes**:
  - `player1`, `player2`: Player instances
  - `current_player`: Tracks turn
  - `board`: Board instance
- **Key Methods**:
  - `play()`: Main game loop
  - `switch_player()`: Alternates turns
  - `valid_input()`: Handles user input validation

### 4. `TicTacToe` (Entry Point)
- Static `run()` method initializes and starts game

## How to Run
```bash
python tictactoe_demo.py
