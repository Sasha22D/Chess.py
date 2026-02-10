import pygame

pygame.init()
window = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Chess.py")
clock = pygame.time.Clock()
running = True

case_size = 90

white_pawn = pygame.image.load("assets/white_pawn.png")

def detect_case_x(pos: tuple[int, int]):
    case = pos[0]
    i = 0
    while (case > 0):
        case -= case_size
        i += 1
    return i

def detect_case_y(pos: tuple[int, int]):
    case = pos[1]
    i = 0
    while (case > 0):
        case -= case_size
        i += 1
    return i

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

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(detect_case_x(pos), detect_case_y(pos))
    render_board()
    window.blit(white_pawn, (45, 45))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()