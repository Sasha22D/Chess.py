def is_white_piece(i, j, board):
    if board[i][j] in "rnbqkp":
        return True
    else:
        return False