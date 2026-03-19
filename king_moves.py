from check_functions import is_check
from utils import is_white_piece, is_black_piece

def black_king_possible_moves(pos: tuple[int, int], board):
    moves_list = []
    col = int(pos[0] / 90)
    row = int(pos[1] / 90)

    if row - 1 >= 0:
        if col - 1 >= 0 and not is_check([row - 1, col - 1], board, "black") and (is_white_piece(row - 1, col - 1, board) or board[row - 1][col - 1] == "0"):
            moves_list.append([row - 1, col - 1])
        if not is_check([row - 1, col], board, "black") and (is_white_piece(row - 1, col, board) or board[row - 1][col] == "0"):
            moves_list.append([row - 1, col])
        if col + 1 <= 7 and not is_check([row - 1, col + 1], board, "black") and (is_white_piece(row - 1, col + 1, board) or board[row - 1][col + 1] == "0"):
            moves_list.append([row - 1, col + 1])
    if col - 1 >= 0 and not is_check([row, col - 1], board, "black") and (is_white_piece(row, col - 1, board) or board[row][col - 1] == "0"):
        moves_list.append([row, col - 1])
    if col + 1 <= 7 and not is_check([row, col + 1], board, "black") and (is_white_piece(row, col + 1, board) or board[row][col + 1] == "0"):
        moves_list.append([row, col + 1])
    if row + 1 <= 7:
        if col - 1 >= 0 and not is_check([row + 1, col - 1], board, "black") and (is_white_piece(row + 1, col - 1, board) or board[row + 1][col - 1] == "0"):
            moves_list.append([row + 1, col - 1])
        if not is_check([row + 1, col], board, "black") and (is_white_piece(row + 1, col, board) or board[row + 1][col] == "0"):
            moves_list.append([row + 1, col])
        if col + 1 <= 7 and not is_check([row + 1, col + 1], board, "black") and (is_white_piece(row + 1, col + 1, board) or board[row + 1][col + 1] == "0"):
            moves_list.append([row + 1, col + 1])
    return moves_list

def white_king_possible_moves(pos: tuple[int, int], board):
    moves_list = []
    col = int(pos[0] / 90)
    row = int(pos[1] / 90)

    if row - 1 >= 0:
        if col - 1 >= 0 and not is_check([row - 1, col - 1], board, "white") and (is_black_piece(row - 1, col - 1, board) or board[row - 1][col - 1] == "0"):
            moves_list.append([row - 1, col - 1])
        if not is_check([row - 1, col], board, "white") and (is_black_piece(row - 1, col, board) or board[row - 1][col] == "0"):
            moves_list.append([row - 1, col])
        if col + 1 <= 7 and not is_check([row - 1, col + 1], board, "white") and (is_black_piece(row - 1, col + 1, board) or board[row - 1][col + 1] == "0"):
            moves_list.append([row - 1, col + 1])
    if col - 1 >= 0 and not is_check([row, col - 1], board, "white") and (is_black_piece(row, col - 1, board) or board[row][col - 1] == "0"):
        moves_list.append([row, col - 1])
    if col + 1 <= 7 and not is_check([row, col + 1], board, "white") and (is_black_piece(row, col + 1, board) or board[row][col + 1] == "0"):
        moves_list.append([row, col + 1])
    if row + 1 <= 7:
        if col - 1 >= 0 and not is_check([row + 1, col - 1], board, "white") and (is_black_piece(row + 1, col - 1, board) or board[row + 1][col - 1] == "0"):
            moves_list.append([row + 1, col - 1])
        if not is_check([row + 1, col], board, "white") and (is_black_piece(row + 1, col, board) or board[row + 1][col] == "0"):
            moves_list.append([row + 1, col])
        if col + 1 <= 7 and not is_check([row + 1, col + 1], board, "white") and (is_black_piece(row + 1, col + 1, board) or board[row + 1][col + 1] == "0"):
            moves_list.append([row + 1, col + 1])
    return moves_list
    

def king_possible_moves(pos: tuple[int, int], board):
    col = int(pos[0] / 90)
    row = int(pos[1] / 90)

    if board[row][col] == "K":
        return black_king_possible_moves(pos, board)
    else:
        return white_king_possible_moves(pos, board)