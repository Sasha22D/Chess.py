from bishop_moves import white_bishop_possible_moves, black_bishop_possible_moves
from rook_moves import white_rook_possible_moves, black_rook_possible_moves

def queen_possible_moves(pos: tuple[int, int], board):
    moves_list = []
    col = int(pos[0] / 90)
    row = int(pos[1] / 90)

    if board[row][col] == "Q":
        moves_list = black_bishop_possible_moves(pos, board)
        moves_list.extend(black_rook_possible_moves(pos, board))
    else:
        moves_list = white_bishop_possible_moves(pos, board)
        moves_list.extend(white_rook_possible_moves(pos, board))
    return moves_list