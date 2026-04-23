def is_white_piece(row: int, col: int, board: list[list[str]]) -> bool:
    return board[row][col] in "rnbqkp"

def is_black_piece(row: int, col: int, board: list[list[str]]) -> bool:
    return board[row][col] in "RNBQKP"

def is_empty_case(row: int, col: int, board: list[list[str]]) -> bool:
    return board[row][col] == "0"