from utils import is_white_piece, is_black_piece

def is_black_bishop_check(row, col, board):
    stash_row = row
    stash_col = col

    row -= 1
    col -= 1
    while row >= 0 and col >= 0 and board[row][col] == "0":
        row -= 1
        col -= 1
    if row >= 0 and col >= 0 and board[row][col] == "B":
        return True
    row = stash_row - 1
    col = stash_col + 1
    while row >= 0 and col <= 7 and board[row][col] == "0":
        row -= 1
        col += 1
    if row >= 0 and col <= 7 and board[row][col] == "B":
        return True
    row = stash_row + 1
    col = stash_col + 1
    while row <= 7 and col <= 7 and board[row][col] == "0":
        row += 1
        col += 1
    if row <= 7 and col <= 7 and board[row][col] == "B":
        return True
    row = stash_row + 1
    col = stash_col - 1
    while row <= 7 and col >= 0 and board[row][col] == "0":
        row += 1
        col -= 1
    if row <= 7 and col >= 0 and board[row][col] == "B":
        return True
    return False

def is_white_bishop_check(row, col, board):
    stash_row = row
    stash_col = col

    row -= 1
    col -= 1
    while row >= 0 and col >= 0 and board[row][col] == "0":
        row -= 1
        col -= 1
    if row >= 0 and col >= 0 and board[row][col] == "b":
        return True
    row = stash_row - 1
    col = stash_col + 1
    while row >= 0 and col <= 7 and board[row][col] == "0":
        row -= 1
        col += 1
    if row >= 0 and col <= 7 and board[row][col] == "b":
        return True
    row = stash_row + 1
    col = stash_col + 1
    while row <= 7 and col <= 7 and board[row][col] == "0":
        row += 1
        col += 1
    if row <= 7 and col <= 7 and board[row][col] == "b":
        return True
    row = stash_row + 1
    col = stash_col - 1
    while row <= 7 and col >= 0 and board[row][col] == "0":
        row += 1
        col -= 1
    if row <= 7 and col >= 0 and board[row][col] == "b":
        return True
    return False

def is_black_rook_check(row, col, board):
    stash_row = row
    stash_col = col

    row -= 1
    while row >= 0 and board[row][col] == "0":
        row -= 1
    if row >= 0 and board[row][col] == "R":
        return True
    row = stash_row + 1
    while row <= 7 and board[row][col] == "0":
        row += 1
    if row <= 7 and board[row][col] == "R":
        return True
    row = stash_row
    col -= 1
    while col >= 0 and board[row][col] == "0":
        col -= 1
    if col >= 0 and board[row][col] == "R":
        return True
    col = stash_col + 1
    while col <= 7 and board[row][col] == "0":
        col += 1
    if col <= 7 and board[row][col] == "R":
        return True
    return False

def is_white_rook_check(row, col, board):
    stash_row = row
    stash_col = col

    row -= 1
    while row >= 0 and board[row][col] == "0":
        row -= 1
    if row >= 0 and board[row][col] == "r":
        return True
    row = stash_row + 1
    while row <= 7 and board[row][col] == "0":
        row += 1
    if row <= 7 and board[row][col] == "r":
        return True
    row = stash_row
    col -= 1
    while col >= 0 and board[row][col] == "0":
        col -= 1
    if col >= 0 and board[row][col] == "r":
        return True
    col = stash_col + 1
    while col <= 7 and board[row][col] == "0":
        col += 1
    if col <= 7 and board[row][col] == "r":
        return True
    return False

def is_black_knight_check(row, col, board):
    if row - 2 >= 0 and col - 1 >= 0 and board[row - 2][col - 1] == "N":
        return True
    if row - 2 >= 0 and col + 1 <= 7 and board[row - 2][col + 1] == "N":
        return True
    if row + 2 <= 7 and col + 1 <= 7 and board[row + 2][col + 1] == "N":
        return True
    if row + 2 <= 7 and col - 1 >= 0 and board[row + 2][col - 1] == "N":
        return True
    return False

def is_white_knight_check(row, col, board):
    if row - 2 >= 0 and col - 1 >= 0 and board[row - 2][col - 1] == "n":
        return True
    if row - 2 >= 0 and col + 1 <= 7 and board[row - 2][col + 1] == "n":
        return True
    if row + 2 <= 7 and col + 1 <= 7 and board[row + 2][col + 1] == "n":
        return True
    if row + 2 <= 7 and col - 1 >= 0 and board[row + 2][col - 1] == "n":
        return True
    return False

def is_black_pawn_check(row, col, board):
    if row + 1 <= 7 and col + 1 <= 7 and board[row + 1][col + 1] == "P":
        return True
    if row + 1 <= 7 and col - 1 >= 0 and board[row + 1][col - 1] == "P":
        return True
    return False

def is_white_pawn_check(row, col, board):
    if row - 1 >= 0 and col - 1 >= 0 and board[row - 1][col - 1] == "p":
        return True
    if row - 1 >= 0 and col + 1 <= 7 and board[row - 1][col + 1] == "p":
        return True
    return False

def is_check(pos: tuple[int, int], board, color):
    col = int(pos[0] / 90)
    row = int(pos[1] / 90)

    if color == "black":
        if is_white_bishop_check(row, col, board) == True:
            return True
        if is_white_rook_check(row, col, board) == True:
            return True
        if is_white_knight_check(row, col, board) == True:
            return True
        if is_white_pawn_check(row, col, board) == True:
            return True
    elif color == "white":
        if is_black_bishop_check(row, col, board) == True:
            return True
        if is_black_rook_check(row, col, board) == True:
            return True
        if is_black_knight_check(row, col, board) == True:
            return True
        if is_black_pawn_check(row, col, board) == True:
            return True
    return False