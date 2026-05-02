import pygame
import copy
from pawn_moves import pawn_possible_moves
from bishop_moves import bishop_possible_moves
from rook_moves import rook_possible_moves
from knight_moves import knight_possible_moves
from queen_moves import queen_possible_moves
from king_moves import king_possible_moves
from init_game import init_board, render_board, clock, CASE_SIZE
from check_functions import is_check
from utils import is_white_piece

def	detect_selected_piece(pos: tuple[int, int], board: list[list[str]]) -> list[list[int]]:
    moves_list = []
    col = pos[0] // CASE_SIZE
    row = pos[1] // CASE_SIZE

    if board[row][col] == "0":
        return moves_list
    elif board[row][col] == "p" or board[row][col] == "P":
        moves_list = pawn_possible_moves(pos, board)
    elif board[row][col] == "r" or board[row][col] == "R":
        moves_list = rook_possible_moves(pos, board)
    elif board[row][col] == "b" or board[row][col] == "B":
        moves_list = bishop_possible_moves(pos, board)
    elif board[row][col] == "n" or board[row][col] == "N":
        moves_list = knight_possible_moves(pos, board)
    elif board[row][col] == "q" or board[row][col] == "Q":
        moves_list = queen_possible_moves(pos, board)
    elif board[row][col] == "k" or board[row][col] == "K":
        moves_list = king_possible_moves(pos, board)
    return moves_list

def check_legal_move(pos: tuple[int, int], pos_second_click: tuple[int, int], board: list[list[str]]) -> bool:
    col_second = pos_second_click[0] // CASE_SIZE
    row_second = pos_second_click[1] // CASE_SIZE
    board_copy = copy.deepcopy(board)
    board_copy = move_selected_piece(pos, pos_second_click, board_copy)
    is_white = is_white_piece(row_second, col_second, board_copy)

    for i in range(8):
        for j in range(8):
            if is_white and board_copy[i][j] == "k":
                if is_check((j * 90, i * 90), board_copy):
                    return False
            elif is_white == False and board_copy[i][j] == "K":
                if is_check((j * 90, i * 90), board_copy):
                    return False

    return True

def	check_move(pos: tuple[int, int], pos_second_click: tuple[int, int], moves_list, board: list[list[str]]) -> bool:
    col = pos_second_click[0] // CASE_SIZE
    row = pos_second_click[1] // CASE_SIZE

    if moves_list == None:
        return False
    for move in moves_list:
        if row == move[0] and col == move[1]:
            if check_legal_move(pos, pos_second_click, board):
                return True
    return False

def move_selected_piece(pos: tuple[int, int], pos_second_click: tuple[int, int], board):
    col = pos[0] // CASE_SIZE
    row = pos[1] // CASE_SIZE
    col_second = pos_second_click[0] // CASE_SIZE
    row_second = pos_second_click[1] // CASE_SIZE

    board[row_second][col_second] = board[row][col]
    board[row][col] = "0"
    return board

def	detect_click(pos: tuple[int, int], board):
    clicked = False
    moves_list = detect_selected_piece(pos, board)

    while clicked == False:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos_second_click = pygame.mouse.get_pos()
                if check_move(pos, pos_second_click, moves_list, board):
                    board = move_selected_piece(pos, pos_second_click, board)
                    clicked = True
                else:
                    detect_click(pos_second_click, board)
                    clicked = True
    return board

def	main():
    pygame.init()
    running = True
    board = []

    board = init_board(board)
    render_board(board)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                detect_click(pos, board)
                render_board(board)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

main()