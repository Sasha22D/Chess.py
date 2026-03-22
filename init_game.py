import pygame

window = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Chess.py")
clock = pygame.time.Clock()
case_size = 90

white_pawn_image = pygame.image.load("./assets/wp.png").convert_alpha()
white_pawn_image = pygame.transform.scale(white_pawn_image, (90, 90))
black_pawn_image = pygame.image.load("./assets/bp.png").convert_alpha()
black_pawn_image = pygame.transform.scale(black_pawn_image, (90, 90))

white_rook_image = pygame.image.load("./assets/wr.png").convert_alpha()
white_rook_image = pygame.transform.scale(white_rook_image, (90, 90))
black_rook_image = pygame.image.load("./assets/br.png").convert_alpha()
black_rook_image = pygame.transform.scale(black_rook_image, (90, 90))

white_knight_image = pygame.image.load("./assets/wn.png").convert_alpha()
white_knight_image = pygame.transform.scale(white_knight_image, (90, 90))
black_knight_image = pygame.image.load("./assets/bn.png").convert_alpha()
black_knight_image = pygame.transform.scale(black_knight_image, (90, 90))

white_bishop_image = pygame.image.load("./assets/wb.png").convert_alpha()
white_bishop_image = pygame.transform.scale(white_bishop_image, (90, 90))
black_bishop_image = pygame.image.load("./assets/bb.png").convert_alpha()
black_bishop_image = pygame.transform.scale(black_bishop_image, (90, 90))

white_queen_image = pygame.image.load("./assets/wq.png").convert_alpha()
white_queen_image = pygame.transform.scale(white_queen_image, (90, 90))
black_queen_image = pygame.image.load("./assets/bq.png").convert_alpha()
black_queen_image = pygame.transform.scale(black_queen_image, (90, 90))

white_king_image = pygame.image.load("./assets/wk.png").convert_alpha()
white_king_image = pygame.transform.scale(white_king_image, (90, 90))
black_king_image = pygame.image.load("./assets/bk.png").convert_alpha()
black_king_image = pygame.transform.scale(black_king_image, (90, 90))

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

def render_pieces(board):
    for i in range(0, 8):
        for j in range(0, 8):
            case = board[i][j]
            if case == "p":
                window.blit(white_pawn_image, (j * 90, i * 90))
            elif case == "P":
                window.blit(black_pawn_image, (j * 90, i * 90))
            elif case == "r":
                window.blit(white_rook_image, (j * 90, i * 90))
            elif case == "R":
                window.blit(black_rook_image, (j * 90, i * 90))
            elif case == "n":
                window.blit(white_knight_image, (j * 90, i * 90))
            elif case == "N":
                window.blit(black_knight_image, (j * 90, i * 90))
            elif case == "b":
                window.blit(white_bishop_image, (j * 90, i * 90))
            elif case == "B":
                window.blit(black_bishop_image, (j * 90, i * 90))
            elif case == "q":
                window.blit(white_queen_image, (j * 90, i * 90))
            elif case == "Q":
                window.blit(black_queen_image, (j * 90, i * 90))
            elif case == "k":
                window.blit(white_king_image, (j * 90, i * 90))
            elif case == "K":
                window.blit(black_king_image, (j * 90, i * 90))

def render_board(board):
    rowPair = True
    for i in range(8):
        if rowPair == True:
            for j in range(8):
                if j % 2 == 0:
                    pygame.draw.rect(window, "beige", (i * case_size, j * case_size, case_size, case_size))
                else:
                    pygame.draw.rect(window, "aquamarine4", (i * case_size, j * case_size, case_size, case_size))
            rowPair = False
        elif rowPair == False:
            for j in range(8):
                if j % 2 != 0:
                    pygame.draw.rect(window, "beige", (i * case_size, j * case_size, case_size, case_size))
                else:
                    pygame.draw.rect(window, "aquamarine4", (i * case_size, j * case_size, case_size, case_size))
            rowPair = True
    render_pieces(board)