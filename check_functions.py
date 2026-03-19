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

def is_check(pos: tuple[int, int], board):
    col = int(pos[0] / 90)
    row = int(pos[1] / 90)

    if board[row][col] == "K":
        if is_white_bishop_check(row, col, board) == True:
            return True
        if is_white_rook_check(row, col, board) == True:
            return True
    elif board[row][col] == "k":
        if is_black_bishop_check(row, col, board) == True:
            return True
        if is_black_rook_check(row, col, board) == True:
            return True
    return False