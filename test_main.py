import pygame
from board import ChessBoard
from pieces import *
from assets import load_pieces_images

window = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Chess.py")
clock = pygame.time.Clock()

def	main():
    pygame.init()
    running = True
    images = load_pieces_images(ChessBoard.CASE_SIZE)
    board = ChessBoard(images)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                board.selected_piece = board.get_piece(pos[1] // board.CASE_SIZE, pos[0] // board.CASE_SIZE)
                if board.selected_piece:
                    board.possible_moves = board.selected_piece.get_moves(board)
        board.render_board(window)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

main()