from pieces import *

class ChessBoard:

    CASE_SIZE = 90

    def __init__(self, images: dict[str, pygame.Surface]) -> None:
        self.images = images
        self.board = self._create_initial_board()
        self.selected_piece = None
        self.possible_moves = []

    def _create_initial_board(self) -> list[list[Piece | None]]:
        return [
            [
                Rook("black", (0, 0), self.images["br"]),
                Knight("black", (0, 1), self.images["bn"]),
                Bishop("black", (0, 2), self.images["bb"]),
                Queen("black", (0, 3), self.images["bq"]),
                King("black", (0, 4), self.images["bk"]),
                Bishop("black", (0, 5), self.images["bb"]),
                Knight("black", (0, 6), self.images["bn"]),
                Rook("black", (0, 7), self.images["br"]),
            ],
            [
                Pawn("black", (1, 0), self.images["bp"]),
                Pawn("black", (1, 1), self.images["bp"]),
                Pawn("black", (1, 2), self.images["bp"]),
                Pawn("black", (1, 3), self.images["bp"]),
                Pawn("black", (1, 4), self.images["bp"]),
                Pawn("black", (1, 5), self.images["bp"]),
                Pawn("black", (1, 6), self.images["bp"]),
                Pawn("black", (1, 7), self.images["bp"]),
            ],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [
                Pawn("white", (6, 0), self.images["wp"]),
                Pawn("white", (6, 1), self.images["wp"]),
                Pawn("white", (6, 2), self.images["wp"]),
                Pawn("white", (6, 3), self.images["wp"]),
                Pawn("white", (6, 4), self.images["wp"]),
                Pawn("white", (6, 5), self.images["wp"]),
                Pawn("white", (6, 6), self.images["wp"]),
                Pawn("white", (6, 7), self.images["wp"]),
            ],
            [
                Rook("white", (7, 0), self.images["wr"]),
                Knight("white", (7, 1), self.images["wn"]),
                Bishop("white", (7, 2), self.images["wb"]),
                Queen("white", (7, 3), self.images["wq"]),
                King("white", (7, 4), self.images["wk"]),
                Bishop("white", (7, 5), self.images["wb"]),
                Knight("white", (7, 6), self.images["wn"]),
                Rook("white", (7, 7), self.images["wr"]),
            ],
        ]

    def get_piece(self, row: int, col: int) -> Piece | None:
        return self.board[row][col]

    def move_piece(self, from_pos: tuple[int, int], to_pos: tuple[int, int]) -> None:
        from_col, from_row = from_pos
        to_col, to_row = to_pos
        self.board[to_row][to_col] = self.board[from_row][from_col]
        self.board[from_row][from_col] = None

    def render_pieces(self, window: pygame.display):
        for i in range(8):
            for j in range(8):
                if self.board[i][j]:
                    self.board[i][j].render_piece(self, window)

    def is_white_piece(self, row: int, col: int) -> bool:
        return self.board[row][col].color == "white"

    def is_black_piece(self, row: int, col: int) -> bool:
        return self.board[row][col].color == "black"

    def is_empty_case(self, row: int, col: int) -> bool:
        return self.board[row][col] == None