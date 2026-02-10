import pygame

pygame.init()
window = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Chess.py")
clock = pygame.time.Clock()
running = True

case_size = 90

board = []

def	init_board():
    global board
    board = [
        ["r", "n", "b", "k", "q", "b", "n", "r"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        ["0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0"],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["R", "N", "B", "Q", "K", "B", "N", "R"]
	]

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
			print(board[detect_case_y(pos) - 1][detect_case_x(pos) - 1])
	render_board()
	init_board()
	pygame.display.flip()
	clock.tick(60)

pygame.quit()