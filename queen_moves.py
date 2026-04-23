from bishop_moves import bishop_possible_moves
from rook_moves import rook_possible_moves
from init_game import CASE_SIZE

def queen_possible_moves(pos: tuple[int, int], board: list[list[str]]) -> list[list[int]]:
    col = pos[0] // CASE_SIZE
    row = pos[1] // CASE_SIZE
    moves_list = []

    if board[row][col] == "Q":
        moves_list = bishop_possible_moves(pos, board)
        moves_list.extend(rook_possible_moves(pos, board))
    else:
        moves_list = bishop_possible_moves(pos, board)
        moves_list.extend(rook_possible_moves(pos, board))

    return moves_list