from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from board import ChessBoard
import pygame

class Piece:
    def __init__(self, color: str, position: tuple[int, int], image: pygame.Surface) -> None:
        self.color = color
        self.position = position
        self.image = image

    def render_piece(self, board: ChessBoard, window: pygame.display) -> None:
        if self != None:
            window.blit(self.image, (self.position[1] * board.CASE_SIZE, self.position[0] * board.CASE_SIZE))

    def get_moves(self, board: ChessBoard) -> list[list[int]]:
        raise NotImplementedError("Chaque pièce doit implémenter get_moves")

    def is_enemy(self, piece: Piece) -> bool:
        if piece == None:
            return False
        return self.color != piece.color

class Pawn(Piece):
    def get_moves(self, board: ChessBoard) -> list[list[int]]:
        moves_list = []
        row, col = self.position
        if self.color == "white":
            if row - 1 >= 0:
                if board.board[row - 1][col] == None:
                    moves_list.append([row - 1, col])
                if col - 1 >= 0:
                    target = board.get_piece(row - 1, col - 1)
                    if self.is_enemy(target):
                        moves_list.append([row - 1, col - 1])
                if col + 1 <= 7:
                    target = board.get_piece(row - 1, col + 1)
                    if self.is_enemy(target):
                        moves_list.append([row - 1, col + 1])
            if row - 2 >= 0 and row == 6:
                if board.board[row - 2][col] == None and board.board[row - 1][col] == None:
                    moves_list.append([row - 2, col])
        else:
            if row + 1 <= 7:
                if board.board[row + 1][col] == None:
                    moves_list.append([row + 1, col])
                if col - 1 >= 0:
                    target = board.get_piece(row + 1, col - 1)
                    if self.is_enemy(target):
                        moves_list.append([row + 1, col - 1])
                if col + 1 <= 7:
                    target = board.get_piece(row + 1, col + 1)
                    if self.is_enemy(target):
                        moves_list.append([row + 1, col + 1])
            if row + 2 <= 7 and row == 1:
                if board.board[row + 2][col] == None and board.board[row + 1][col] == None:
                    moves_list.append([row  + 2, col])
        return moves_list

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
                elif self.is_enemy(target):
                    moves_list.append([current_row, current_col])
                    break
                else:
                    break
        return moves_list

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
                elif self.is_enemy(target):
                    moves_list.append([current_row, current_col])
                    break
                else:
                    break
        return moves_list

class Knight(Piece):
    directions = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (2, -1), (2, 1), (1, -2), (1, 2)
    ]

    def get_moves(self, board: ChessBoard) -> list[list[int]]:
        moves_list = []
        row, col = self.position
        for delta_row, delta_col in self.directions:
            current_row, current_col = row + delta_row, col + delta_col
            if 0 <= current_row <= 7 and 0 <= current_col <= 7:
                target = board.get_piece(current_row, current_col)
                if target == None or self.is_enemy(target):
                    moves_list.append([current_row, current_col])
        return moves_list

class Queen(Piece):
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
            while 0 <= current_row <= 7 and 0 <= current_col <= 7:
                target = board.get_piece(current_row, current_col)
                if board.is_empty_case(current_row, current_col):
                    moves_list.append([current_row, current_col])
                    current_row += delta_row
                    current_col += delta_col
                elif self.is_enemy(target):
                    moves_list.append([current_row, current_col])
                    break
                else:
                    break
        return moves_list

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
                if self.is_enemy(target):
                    moves_list.append([current_row, current_col])
                if board.is_empty_case(current_row, current_col):
                    moves_list.append([current_row, current_col])
        return moves_list