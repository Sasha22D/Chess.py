from board import ChessBoard
from utils import is_empty_case

class Piece:
    def __init__(self, color: str, position: tuple[int, int]) -> None:
        self.color = color
        self.position = position

    # def get_moves(self, board: ChessBoard) -> list[list[int]]:

class Pawn(Piece):
    def get_moves(self, board: ChessBoard) -> list[list[int]]:
        moves_list = []
        row, col = self.position
        if self.color == "white":
            if row - 1 >= 0:
                if board[row - 1][col] == "0":
                    moves_list.append([row - 1, col])
                if col - 1 >= 0:
                    target = board.get_piece(row - 1, col - 1)
                    if self._is_enemy(target):
                        moves_list.append([row - 1, col - 1])
                if col + 1 <= 7:
                    target = board.get_piece(row - 1, col + 1)
                    if self._is_enemy(target):
                        moves_list.append([row - 1, col + 1])
            if row - 2 >= 0 and row == 6:
                if board[row - 2][col] == "0" and board[row - 1][col] == "0":
                    moves_list.append([row - 2, col])
        else:
            if row + 1 <= 7:
                if board[row + 1][col] == "0":
                    moves_list.append([row + 1, col])
                if col - 1 >= 0:
                    target = board.get_piece(row + 1, col - 1)
                    if self._is_enemy(target):
                        moves_list.append([row + 1, col - 1])
                if col + 1 <= 7:
                    target = board.get_piece(row + 1, col + 1)
                    if self._is_enemy(target):
                        moves_list.append([row + 1, col + 1])
            if row + 2 <= 7 and row == 1:
                if board[row + 2][col] == "0" and board[row + 1][col] == "0":
                    moves_list.append([row  + 2, col])
        return moves_list

    def _is_enemy(self, piece: Piece) -> bool:
        return piece.color != self.color

class Rook(Piece):
    directions = [
        (1, 0), (-1, 0), (0, -1), (0, 1)
    ]

    def get_moves(self, board: ChessBoard) -> list[list[int]]:
        moves_list = []
        row, col = self.position
        for delta_row, delta_col in self.directions:
            current_row, current_col = row + delta_row, col + delta_col
            while 0 <= current_row <= 7 and 0 <= current_col <= 7:
                target = board.get_piece(current_row, current_col)
                if board.is_empty_case(current_row, current_col):
                    moves_list.append([current_row, current_col])
                    current_row += delta_row
                    current_col += delta_col
                elif self._is_enemy(target):
                    moves_list.append([current_row, current_col])
                    break
                else:
                    break
        return moves_list

    def _is_enemy(self, piece: Piece) -> bool:
        return piece.color != self.color

class Bishop(Piece):
    directions = [
        (1, 1), (1, -1), (-1, -1), (-1, 1)
    ]

    def get_moves(self, board: ChessBoard) -> list[list[int]]:
        moves_list = []
        row, col = self.position
        for delta_row, delta_col in self.directions:
            current_row, current_col = row + delta_row, col + delta_col
            while 0 <= current_row <= 7 and 0 <= current_col <= 7:
                target = board.get_piece(current_row, current_col)
                if board.is_empty_case(current_row, current_col):
                    moves_list.append([current_row, current_col])
                    current_row += delta_row
                    current_col += delta_col
                elif self._is_enemy(target):
                    moves_list.append([current_row, current_col])
                    break
                else:
                    break
        return moves_list

    def _is_enemy(self, piece: Piece) -> bool:
        return piece.color != self.color

class Knight(Piece):
    directions = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (2, -1), (2, 1), (1, -2), (1, 2)
    ]

    def get_moves(self, board: ChessBoard) -> list[list[int]]:
        moves_list = []
        col, row = self.position
        for delta_row, delta_col in self.directions:
            current_row, current_col = row + delta_row, col + delta_col
            if 0 <= current_row <= 7 and 0 <= current_col <= 7:
                target = board.get_piece(current_row, current_col)
                if target == "0" or self._is_enemy(target):
                    moves_list.append([current_row, current_col])
        return moves_list

    def _is_enemy(self, piece: Piece) -> bool:
        return piece.color != self.color

class Queen(Piece):
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    def get_moves(self, board: ChessBoard) -> list[list[int]]:
        moves_list = []
        moves_list.append(Bishop.get_moves(board))
        moves_list.append(Rook.get_moves(board))
        return moves_list

    def _is_enemy(self, piece: Piece) -> bool:
        return piece.color != self.color

class King(Piece):
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    def get_moves(self, board: ChessBoard) -> list[list[int]]:
        moves_list = []
        row, col = self.position
        for delta_row, delta_col in self.directions:
            current_row, current_col = row + delta_row, col + delta_col
            if 0 <= current_row <= 7 and 0 <= current_col <= 7:
                target = board.get_piece(current_row, current_col)
                if self._is_enemy(target):
                    moves_list.append([current_row, current_col])
                if board.is_empty_case(current_row, current_col):
                    moves_list.append([current_row, current_col])
        return moves_list

    def _is_enemy(self, piece: Piece) -> bool:
        return piece.color != self.color