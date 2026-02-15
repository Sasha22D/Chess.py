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
		["0", "0", "0", "0", "R", "0", "0", "0"],
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
		if y - 1 >= 0 and board[x + 1][y - 1] != "0":
			moves_list.append([x + 1, y - 1])
		if y + 1 <= 7 and board[x + 1][y + 1] != "0":
			moves_list.append([x + 1, y + 1])
	elif board[x][y] == "P":
		if board[x - 1][y] == "0":
			moves_list.append([x - 1, y])
		if y - 1 >= 0 and board[x - 1][y - 1] != "0":
			moves_list.append([x - 1, y - 1])
		if y + 1 <= 7 and board[x - 1][y + 1] != "0":
			moves_list.append([x - 1, y + 1])
	return moves_list

def	rook_possible_move(pos: tuple[int, int], board):
	moves_list = []
	y = int(pos[0] / 90)
	x = int(pos[1] / 90)

	i = x + 1
	while i <= 7 and board[i][y] == "0":
		moves_list.append([i, y])
		i += 1
	i = x - 1
	while i >= 0 and board[i][y] == "0":
		moves_list.append([i, y])
		i -= 1
	i = y + 1
	while i <= 7 and board[x][i] == "0":
		moves_list.append([x, i])
		i += 1
	i = y - 1
	while i >= 0 and board[x][i] == "0":
		moves_list.append([x, i])
		i -= 1
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

def	detect_selected_piece(pos: tuple[int, int], board):
	y = int(pos[0] / 90)
	x = int(pos[1] / 90)
	moves_list = []

	if board[x][y] == "0":
		return moves_list
	if board[x][y] == "p" or board[x][y] == "P":
		moves_list = pawn_possible_move(pos, board)
	if board[x][y] == "r" or board[x][y] == "R":
		moves_list = rook_possible_move(pos, board)
	return moves_list

def	check_move(pos: tuple[int, int], moves_list):
	if moves_list == None:
		return 0
	for move in moves_list:
		if int(pos[1] / 90) == move[0] and int(pos[0] / 90) == move[1]:
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
					detect_click(board)

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
				detect_click(board)
		render_board()
		pygame.display.flip()
		clock.tick(60)

	pygame.quit()

main()