from utils import is_white_piece, is_empty_case
from init_game import CASE_SIZE

def bishop_possible_moves(pos: tuple[int, int], board: list[list[str]]) -> list[list[int]]:
    col = pos[0] // CASE_SIZE
    row = pos[1] // CASE_SIZE
    is_white = is_white_piece(row, col, board)
    moves = []

    directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

    for delta_row, delta_col in directions:
        current_row, current_col = row + delta_row, col + delta_col

        while 0 <= current_row <= 7 and 0 <= current_col <= 7:
            if is_empty_case(current_row, current_col, board):
                moves.append([current_row, current_col])
                current_row += delta_row
                current_col += delta_col
            elif is_white_piece(current_row, current_col, board) != is_white:
                moves.append([current_row, current_col])
                break
            else:
                break

    return moves
