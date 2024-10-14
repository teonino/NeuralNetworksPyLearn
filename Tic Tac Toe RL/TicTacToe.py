import numpy as np
import random

#%% Initialization Board
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
        print("Placement impossible, essayez à nouveau")
        return False

#%% Game Logic
PLAYER_X = 1
PLAYER_O = -1

def play_game():
    board = initialize_board()
    current_player = PLAYER_X
    game_over = False
    
    while not game_over:
        display_board(board)
        print(f"Au tour du joueur {current_player}")
        
        row, col = map(int,input("Entrez la ligne et la colonne (0, 1 ou 2 separé par un espace): ").split())
        
        if make_move(board, row, col, current_player):
            if check_win(board, current_player):
                display_board(board)
                print(f"Le joueur {current_player} a gagné !")
                game_over = True
            elif check_draw(board):
                display_board(board)
                print("Egalité !")
                game_over = True
            else:
                current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X
        else:
            print("Placement impossible, essayez à nouveau !")
            
play_game()
#%% Simple AI Player
def random_ai_move(board):
    empty_cells = [(i, j)] for i in range(3) for j in range (3) if board[i][j]==0]
    
    if empty_cells:
        return random.choice(empty_cells)
    return None

def play_game():
    board = initialize_board()
    current_player = PLAYER_X
    game_over = False