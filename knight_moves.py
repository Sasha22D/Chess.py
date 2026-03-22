from utils import is_white_piece, is_black_piece

def black_knight_possible_moves(pos: tuple[int, int], board):
    moves_list = []
    col = int(pos[0] / 90)
    row = int(pos[1] / 90)

    if row - 2 >= 0 and col - 1 >= 0 and (is_white_piece(row - 2, col - 1, board) or board[row - 2][col - 1] == "0"):
        moves_list.append([row - 2, col - 1])
    if row - 2 >= 0 and col + 1 <= 7 and (is_white_piece(row - 2, col + 1, board) or board[row - 2][col + 1] == "0"):
        moves_list.append([row - 2, col + 1])
    if row + 2 <= 7 and col + 1 <= 7 and (is_white_piece(row + 2, col + 1, board) or board[row + 2][col + 1] == "0"):
        moves_list.append([row + 2, col + 1])
    if row + 2 <= 7 and col - 1 >= 0 and (is_white_piece(row + 2, col - 1, board) or board[row + 2][col - 1] == "0"):
        moves_list.append([row + 2, col - 1])

    if col - 2 >= 0 and row - 1 >= 0 and (is_white_piece(row - 1, col - 2, board) or board[row - 1][col - 2] == "0"):
        moves_list.append([row - 1, col - 2])
    if col - 2 >= 0 and row + 1 <= 7 and (is_white_piece(row + 1, col - 2, board) or board[row + 1][col - 2] == "0"):
        moves_list.append([row + 1, col - 2])
    if col + 2 <= 7 and row + 1 <= 7 and (is_white_piece(row + 1, col + 2, board) or board[row + 1][col + 2] == "0"):
        moves_list.append([row + 1, col + 2])
    if col + 2 <= 7 and row - 1 >= 0 and (is_white_piece(row - 1, col + 2, board) or board[row - 1][col + 2] == "0"):
        moves_list.append([row - 1, col + 2])
    return moves_list

def white_knight_possible_moves(pos: tuple[int, int], board):
    moves_list = []
    col = int(pos[0] / 90)
    row = int(pos[1] / 90)

    if row - 2 >= 0 and col - 1 >= 0 and (is_black_piece(row - 2, col - 1, board) or board[row - 2][col - 1] == "0"):
        moves_list.append([row - 2, col - 1])
    if row - 2 >= 0 and col + 1 <= 7 and (is_black_piece(row - 2, col + 1, board) or board[row - 2][col + 1] == "0"):
        moves_list.append([row - 2, col + 1])
    if row + 2 <= 7 and col + 1 <= 7 and (is_black_piece(row + 2, col + 1, board) or board[row + 2][col + 1] == "0"):
        moves_list.append([row + 2, col + 1])
    if row + 2 <= 7 and col - 1 >= 0 and (is_black_piece(row + 2, col - 1, board) or board[row + 2][col - 1] == "0"):
        moves_list.append([row + 2, col - 1])
    
    if col - 2 >= 0 and row - 1 >= 0 and (is_black_piece(row - 1, col - 2, board) or board[row - 1][col - 2] == "0"):
        moves_list.append([row - 1, col - 2])
    if col - 2 >= 0 and row + 1 <= 7 and (is_black_piece(row + 1, col - 2, board) or board[row + 1][col - 2] == "0"):
        moves_list.append([row + 1, col - 2])
    if col + 2 <= 7 and row + 1 <= 7 and (is_black_piece(row + 1, col + 2, board) or board[row + 1][col + 2] == "0"):
        moves_list.append([row + 1, col + 2])
    if col + 2 <= 7 and row - 1 >= 0 and (is_black_piece(row - 1, col + 2, board) or board[row - 1][col + 2] == "0"):
        moves_list.append([row - 1, col + 2])
    return moves_list

def knight_possible_moves(pos: tuple[int, int], board):
    col = int(pos[0] / 90)
    row = int(pos[1] / 90)

    if board[row][col] == "N":
        return black_knight_possible_moves(pos, board)
    else:
        return white_knight_possible_moves(pos, board)