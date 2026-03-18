def is_white_piece(row, col, board):
    if board[row][col] in "rnbqkp":
        return True
    else:
        return False

def is_black_piece(row, col, board):
    if board[row][col] in "RNBQKP":
        return True
    else:
        return False