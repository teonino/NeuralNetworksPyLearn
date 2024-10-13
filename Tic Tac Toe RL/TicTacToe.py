import numpy as np

def initialize_board():
    return np.zeros((3,3), dtype=int)

def display_board(board):
    for row in board:
        print("|".join([str(int(cell)) for cell in row]))
        print("-"*5)
        

def check_win(board,player):
    win_conditions = [
        [board[0,0],board[0,1],board[0,2]],
        [board[1,0],board[1,1],board[1,2]],
        [board[2,0],board[2,1],board[2,2]],
        [board[0,0],board[1,0],board[2,0]],
        [board[0,1],board[1,1],board[2,1]],
        [board[0,2],board[0,2],board[2,2]],
        [board[0,0],board[1,1],board[2,2]],
        [board[0,2],board[1,1],board[2,0]]
    ]
    if[player, player, player] in win_conditions:
        return True
    return False

def check_draw(board):
    return not np.any(board ==0)

def make_move(board,row,col,player):
    if board[row, col] ==0:
        board[row,col]=player
        return True
    else:
        print("Move not Allowed, try again")
        return False
    
board = initialize_board()
display_board(board)