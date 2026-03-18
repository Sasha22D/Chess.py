import pygame
from pawn_moves import pawn_possible_moves
from bishop_moves import bishop_possible_moves
from rook_moves import rook_possible_moves

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
		moves_list = pawn_possible_moves(pos, board)
	if board[x][y] == "r" or board[x][y] == "R":
		moves_list = rook_possible_moves(pos, board)
	if board[x][y] == "b" or board[x][y] == "B":
		moves_list = bishop_possible_moves(pos, board)
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