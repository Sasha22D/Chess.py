import pygame
from pawn_moves import pawn_possible_moves
from bishop_moves import bishop_possible_moves
from rook_moves import rook_possible_moves
from knight_moves import knight_possible_moves
from queen_moves import queen_possible_moves
from king_moves import king_possible_moves

window = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Chess.py")
clock = pygame.time.Clock()
case_size = 90

def	init_board(board):
    board = [
        ["r", "n", "b", "q", "k", "b", "n", "r"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        ["0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0"],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["R", "N", "B", "K", "Q", "B", "N", "R"]
    ]
    return board

def render_board():
    rowPair = True
    for i in range(8):
        if rowPair == True:
            for j in range(8):
                if j % 2 == 0:
                    pygame.draw.rect(window, "beige", (i * case_size, j * case_size, case_size, case_size))
            rowPair = False
        elif rowPair == False:
            for j in range(8):
                if j % 2 != 0:
                    pygame.draw.rect(window, "beige", (i * case_size, j * case_size, case_size, case_size))
            rowPair = True

def	detect_selected_piece(pos: tuple[int, int], board):
    moves_list = []
    col = int(pos[0] / 90)
    row = int(pos[1] / 90)

    if board[row][col] == "0":
        return moves_list
    if board[row][col] == "p" or board[row][col] == "P":
        moves_list = pawn_possible_moves(pos, board)
    if board[row][col] == "r" or board[row][col] == "R":
        moves_list = rook_possible_moves(pos, board)
    if board[row][col] == "b" or board[row][col] == "B":
        moves_list = bishop_possible_moves(pos, board)
    if board[row][col] == "n" or board[row][col] == "N":
        moves_list = knight_possible_moves(pos, board)
    if board[row][col] == "q" or board[row][col] == "Q":
        moves_list = queen_possible_moves(pos, board)
    if board[row][col] == "k" or board[row][col] == "K":
        moves_list = king_possible_moves(pos, board)
    return moves_list

def	check_move(pos: tuple[int, int], moves_list):
    col = int(pos[0] / 90)
    row = int(pos[1] / 90)

    if moves_list == None:
        return 0
    for move in moves_list:
        if row == move[0] and col == move[1]:
            return 1
    return 0

def	detect_click(board):
    clicked = False
    pos = pygame.mouse.get_pos()
    moves_list = detect_selected_piece(pos, board)

    while clicked == False:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos_second_click = pygame.mouse.get_pos()
                if (check_move(pos_second_click, moves_list) == 1):
                    # move_pieces()
                    print(check_move(pos_second_click, moves_list))
                    clicked = True
                else:
                    print(check_move(pos_second_click, moves_list))
                    clicked = True

def	main():
    pygame.init()
    running = True
    board = []

    board = init_board(board)
    for row in range(0, 8):
        print(row + 1, end='')
        print(board[row])
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                detect_click(board)
        render_board()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

main()