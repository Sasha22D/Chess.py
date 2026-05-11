import pygame
from board import ChessBoard
# from pieces import *
from init_game import *

def	main():
    pygame.init()
    running = True
    board = ChessBoard()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                board.selected_piece = board.get_piece(pos[1] // board.CASE_SIZE, pos[0] // board.CASE_SIZE)
                if board.selected_piece:
                    board.possible_moves = board.selected_piece.get_moves(board)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

main()