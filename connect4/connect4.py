import numpy as np
import random
 
# Function to create a new connect four board
def connectfour_board():
    return np.zeros((6, 7))
 
# Function to check if a drop in a column is valid
def drop_valid(board, play):
    return 0 <= play <= 6 and board[5][play] == 0
 
# Function to drop a token into the board
def drop_board(board, row, play, player):
    board[row][play] = player
 
# Function to find the next open row in a column
def newopen_row(board, play):
    for r in range(6):
        if board[r][play] == 0:
            return r
 
# Function to flip the board for better visualization
def flip_board(board):
    print(np.flip(board, 0))
 
# Function to check if there is a winner
def check_winner(board, player):
    # Check vertical
    for r in range(3):
        for c in range(7):
            if board[r][c] == player and board[r+1][c] == player and board[r+2][c] == player and board[r+3][c] == player:
                return True
 
    # Check horizontal winner
    for r in range(6):
        for c in range(4):
            if board[r][c] == player and board[r][c+1] == player and board[r][c+2] == player and board[r][c+3] == player:
                return True
 
    # Check diagonal winner
    for r in range(3, 6):
        for c in range(4):
            if board[r][c] == player and board[r-1][c+1] == player and board[r-2][c+2] == player and board[r-3][c+3] == player:
                return True
 
    # Check diagonal winner
    for r in range(3):
        for c in range(4):
            if board[r][c] == player and board[r+1][c+1] == player and board[r+2][c+2] == player and board[r+3][c+3] == player:
                return True
 
    return False
 
# Function for CPU move
def cpu_move(board):
    c_move = [col for col in range(7) if drop_valid(board, col)]
    return random.choice(c_move)
 
# Choosing game mode
def choose_mode():
    while True:
        mode = input("Choose the game mode, (1 for Player vs Player) or (2 for Player vs CPU): ")
        if mode in ["1", "2"]:
            return mode
        else:
            print("This is not a valid mode")
 
# Create the initial board
board = connectfour_board()
flip_board(board)
 
# Choose game mode
mode = choose_mode()
 
# Main game loop
connectgame_over = False
turn = 0
try:
    while not connectgame_over:
        # Player 1's turn
        if turn == 0:
            play = input("Player 1, take your go (0-6) or press Q to quit: ").strip()
            if play.lower() == 'q':
                print("Player 1 has quit the game.")
                break
            if not play.isdigit() or not drop_valid(board, int(play)):
                print("Invalid input. Please enter a number from 0 to 6.")
                continue
            play = int(play)
            row = newopen_row(board, play)
            drop_board(board, row, play, 1)
            if check_winner(board, 1):
                print("Player 1 wins!")
                connectgame_over = True
        else:
            # Player 2's turn
            if mode == '1':
                play = input("Player 2, take your go (0-6) or press Q to quit: ").strip()
                if play.lower() == 'q':
                    print("Player 2 has quit the game.")
                    break
                if not play.isdigit() or not drop_valid(board, int(play)):
                    print("Invalid input. Please enter a number from 0 to 6.")
                    continue
                play = int(play)
            else:
                play = cpu_move(board)
            row = newopen_row(board, play)
            drop_board(board, row, play, 2)
            if check_winner(board, 2):
                if mode == "1":
                    print("Player 2 wins!")
                else:
                    print("CPU wins")
                connectgame_over = True
       
        # Print the board
        flip_board(board)
       
        # Switch to the other player's turn
        turn = 1 - turn
except KeyboardInterrupt:
    print("Game Interrupted.")
 

 