from utils import is_white_piece, is_black_piece
from init_game import CASE_SIZE

def black_pawn_possible_moves(pos : tuple[int, int], board):
    moves_list = []
    col = pos[0] // CASE_SIZE
    row = pos[1] // CASE_SIZE

    if row + 1 <= 7:
        if board[row + 1][col] == "0":
            moves_list.append([row + 1, col])
        if col - 1 >= 0 and is_white_piece(row + 1, col - 1, board):
            moves_list.append([row + 1, col - 1])
        if col + 1 <= 7 and is_white_piece(row + 1, col + 1, board):
            moves_list.append([row + 1, col + 1])
    if row + 2 <= 7 and row == 1 and board[row + 2][col] == "0":
        moves_list.append([row  + 2, col])
    return moves_list

def white_pawn_possible_moves(pos : tuple[int, int], board):
    moves_list = []
    col = pos[0] // CASE_SIZE
    row = pos[1] // CASE_SIZE

    if row - 1 >= 0:
        if board[row - 1][col] == "0":
            moves_list.append([row - 1, col])
        if col - 1 >= 0 and is_black_piece(row - 1, col - 1, board):
            moves_list.append([row - 1, col - 1])
        if col + 1 <= 7 and is_black_piece(row - 1, col + 1, board):
            moves_list.append([row - 1, col + 1])
    if row - 2 >= 0 and row == 6 and board[row - 2][col] == "0":
        moves_list.append([row - 2, col])
    return moves_list
    

def pawn_possible_moves(pos: tuple[int, int], board):
    col = pos[0] // CASE_SIZE
    row = pos[1] // CASE_SIZE

    if board[row][col] == "P":
        return black_pawn_possible_moves(pos, board)
    else:
        return white_pawn_possible_moves(pos, board)