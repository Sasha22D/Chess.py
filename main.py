import pygame

window = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Chess.py")
clock = pygame.time.Clock()
case_size = 90

def	init_board(board):
	board = [
		["r", "n", "b", "q", "k", "b", "n", "r"],
		["p", "p", "p", "p", "p", "p", "p", "p"],
		["d", "0", "d", "0", "0", "0", "0", "0"],
		["0", "0", "0", "0", "0", "0", "0", "0"],
		["0", "0", "0", "0", "0", "0", "0", "0"],
		["0", "0", "0", "0", "0", "0", "0", "0"],
		["P", "P", "P", "P", "P", "P", "P", "P"],
		["R", "N", "B", "K", "Q", "B", "N", "R"]
	]
	return board

def pawn_possible_move(pos : tuple[int, int], board):
	moves_list = []
	y = int(pos[0] / 90)
	x = int(pos[1] / 90)
	if board[x][y] == "p":
			if board[x + 1][y] == "0":
				moves_list.append([x + 1, y])
			if (board[x + 1][y - 1] != "0"):
				moves_list.append([x + 1, y - 1])
			if (board[x + 1][y + 1] != "0"):
				moves_list.append([x + 1, y + 1])
	return moves_list

def detect_case_y(pos: tuple[int, int]):
	case = pos[0]
	i = 0
	while (case > 0):
		case -= case_size
		i += 1
	return i

def detect_case_x(pos: tuple[int, int]):
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

def	main():
	pygame.init()
	running = True
	board = []

	board = init_board(board)
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEBUTTONUP:
				pos = pygame.mouse.get_pos()
				print(pawn_possible_move(pos, board))
		render_board()
		pygame.display.flip()
		clock.tick(60)

	pygame.quit()

main()