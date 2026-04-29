from utils import is_white_piece, is_empty_case
from init_game import CASE_SIZE

def pawn_check(pos: tuple[int, int], board: list[list[str]]) -> bool:
    col = pos[0] // CASE_SIZE
    row = pos[1] // CASE_SIZE
    is_white = is_white_piece(row, col, board)

    if is_white:
        if 0 <= row - 1 <= 7 and 0 <= col - 1 <= 7:
            if board[row - 1][col - 1] == "P":
                return True
        if 0 <= row - 1 <= 7 and 0 <= col + 1 <= 7:
            if board[row - 1][col + 1] == "P":
                return True
    else:
        if 0 <= row + 1 <= 7 and 0 <= col + 1 <= 7:
            if board[row + 1][col + 1] == "p":
                return True
        if 0 <= row + 1 <= 7 and 0 <= col - 1 <= 7:
            if board[row + 1][col - 1] == "p":
                return True

    return False

def bishop_check(pos: tuple[int, int], board: list[list[str]]) -> bool:
    col = pos[0] // CASE_SIZE
    row = pos[1] // CASE_SIZE
    is_white = is_white_piece(row, col, board)
    directions = [(-1, -1), (1, 1), (1, -1), (-1, 1)]

    for delta_row, delta_col in directions:
        current_row, current_col = row + delta_row, col + delta_col
        while 0 <= current_row <= 7 and 0 <= current_col <= 7:
            if board[current_row][current_col] == "B" or board[current_row][current_col] == "b":
                if is_white_piece(current_row, current_col, board) != is_white:
                    return True
            elif is_empty_case(current_row, current_col, board) == False:
                break
            current_row += delta_row
            current_col += delta_col

    return False

def rook_check(pos: tuple[int, int], board: list[list[str]]) -> bool:
    col = pos[0] // CASE_SIZE
    row = pos[1] // CASE_SIZE
    is_white = is_white_piece(row, col, board)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for delta_row, delta_col in directions:
        current_row, current_col = row + delta_row, col + delta_col
        while 0 <= current_row <= 7 and 0 <= current_col <= 7:
            if board[current_row][current_col] == "R" or board[current_row][current_col] == "r":
                if is_white_piece(current_row, current_col, board) != is_white:
                    return True
            elif is_empty_case(current_row, current_col, board) == False:
                break
            current_row += delta_row
            current_col += delta_col

    return False

def knight_check(pos: tuple[int, int], board: list[list[str]]) -> bool:
    col = pos[0] // CASE_SIZE
    row = pos[1] // CASE_SIZE
    is_white = is_white_piece(row, col, board)
    directions = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

    for delta_row, delta_col in directions:
        current_row, current_col = row + delta_row, col + delta_col
        if 0 <= current_row <= 7 and 0 <= current_col <= 7:
            if board[current_row][current_col] == "N" or board[current_row][current_col] == "n":
                if is_white_piece(current_row, current_col, board) != is_white:
                    return True
            current_row += delta_row
            current_col += delta_col

    return False

def king_check(pos: tuple[int, int], board: list[list[str]]) -> bool:
    col = pos[0] // CASE_SIZE
    row = pos[1] // CASE_SIZE
    is_white = is_white_piece(row, col, board)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for delta_row, delta_col in directions:
        current_row, current_col = row + delta_row, col + delta_col

        if 0 <= current_row <= 7 and 0 <= current_col <= 7:
            if board[current_row][current_col] == "K" or board[current_row][current_col] == "k":
                if is_white_piece(current_row, current_col, board) != is_white:
                    return True
    
    return False

def queen_check(pos: tuple[int, int], board: list[list[str]]) -> bool:
    col = pos[0] // CASE_SIZE
    row = pos[1] // CASE_SIZE
    is_white = is_white_piece(row, col, board)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for delta_row, delta_col in directions:
        current_row, current_col = row + delta_row, col + delta_col
        while 0 <= current_row <= 7 and 0 <= current_col <= 7:
            if board[current_row][current_col] == "Q" or board[current_row][current_col] == "q":
                if is_white_piece(current_row, current_col, board) != is_white:
                    return True
            elif is_empty_case(current_row, current_col, board) == False:
                break
            current_row += delta_row
            current_col += delta_col

    directions = [(-1, -1), (1, 1), (1, -1), (-1, 1)]

    for delta_row, delta_col in directions:
        current_row, current_col = row + delta_row, col + delta_col
        while 0 <= current_row <= 7 and 0 <= current_col <= 7:
            if board[current_row][current_col] == "Q" or board[current_row][current_col] == "q":
                if is_white_piece(current_row, current_col, board) != is_white:
                    return True
            elif is_empty_case(current_row, current_col, board) == False:
                break
            current_row += delta_row
            current_col += delta_col

    return False

def is_check(pos: tuple[int, int], board: list[list[str]]) -> bool:

    if pawn_check(pos, board):
        return True
    elif rook_check(pos, board):
        return True
    elif knight_check(pos, board):
        return True
    elif bishop_check(pos, board):
        return True
    elif king_check(pos, board):
        return True
    elif queen_check(pos, board):
        return True
    return False