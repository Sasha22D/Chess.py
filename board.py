from pieces import *

class ChessBoard:

    CASE_SIZE = 90

    def __init__(self) -> None:
        self.board = self._create_initial_board()
        self.selected_piece = None
        self.possible_moves = []

    def _create_initial_board(self) -> list[list[Piece | None]]:
        return [
            [
                Rook("black", (0, 0)),
                Knight("black", (0, 1)),
                Bishop("black", (0, 2)),
                Queen("black", (0, 3)),
                King("black", (0, 4)),
                Bishop("black", (0, 5)),
                Knight("black", (0, 6)),
                Rook("black", (0, 7)),
            ],
            [
                Pawn("black", (1, 0)),
                Pawn("black", (1, 1)),
                Pawn("black", (1, 2)),
                Pawn("black", (1, 3)),
                Pawn("black", (1, 4)),
                Pawn("black", (1, 5)),
                Pawn("black", (1, 6)),
                Pawn("black", (1, 7)),
            ],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [
                Pawn("white", (6, 0)),
                Pawn("white", (6, 1)),
                Pawn("white", (6, 2)),
                Pawn("white", (6, 3)),
                Pawn("white", (6, 4)),
                Pawn("white", (6, 5)),
                Pawn("white", (6, 6)),
                Pawn("white", (6, 7)),
            ],
            [
                Rook("white", (7, 0)),
                Knight("white", (7, 1)),
                Bishop("white", (7, 2)),
                Queen("white", (7, 3)),
                King("white", (7, 4)),
                Bishop("white", (7, 5)),
                Knight("white", (7, 6)),
                Rook("white", (7, 7)),
            ],
        ]

    def get_piece(self, row: int, col: int) -> Piece | None:
        return self.board[row][col]

    def move_piece(self, from_pos: tuple[int, int], to_pos: tuple[int, int]) -> None:
        from_col, from_row = from_pos
        to_col, to_row = to_pos
        self.board[to_row][to_col] = self.board[from_row][from_col]
        self.board[from_row][from_col] = None

    def is_white_piece(self, row: int, col: int) -> bool:
        return self.board[row][col].color == "white"

    def is_black_piece(self, row: int, col: int) -> bool:
        return self.board[row][col].color == "black"

    def is_empty_case(self, row: int, col: int) -> bool:
        return self.board[row][col] == None