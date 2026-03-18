from utils import is_white_piece, is_black_piece

def	black_rook_possible_moves(pos: tuple[int, int], board):
	moves_list = []
	y = int(pos[0] / 90)
	x = int(pos[1] / 90)

	i = x + 1
	while i <= 7 and board[i][y] == "0":
		moves_list.append([i, y])
		i += 1
	if i <= 7 and is_white_piece(i, y, board):
		moves_list.append([i, y])
	i = x - 1
	while i >= 0 and board[i][y] == "0":
		moves_list.append([i, y])
		i -= 1
	if i >= 0 and is_white_piece(i, y, board):
		moves_list.append([i, y])
	i = y + 1
	while i <= 7 and board[x][i] == "0":
		moves_list.append([x, i])
		i += 1
	if i <= 7 and is_white_piece(x, i, board):
		moves_list.append([x, i])
	i = y - 1
	while i >= 0 and board[x][i] == "0":
		moves_list.append([x, i])
		i -= 1
	if i >= 0 and is_white_piece(x, i, board):
		moves_list.append([x, i])
	return moves_list

def	white_rook_possible_moves(pos: tuple[int, int], board):
	moves_list = []
	y = int(pos[0] / 90)
	x = int(pos[1] / 90)

	i = x + 1
	while i <= 7 and board[i][y] == "0":
		moves_list.append([i, y])
		i += 1
	if i <= 7 and is_black_piece(i, y, board):
		moves_list.append([i, y])
	i = x - 1
	while i >= 0 and board[i][y] == "0":
		moves_list.append([i, y])
		i -= 1
	if i >= 0 and is_black_piece(i, y, board):
		moves_list.append([i, y])
	i = y + 1
	while i <= 7 and board[x][i] == "0":
		moves_list.append([x, i])
		i += 1
	if i <= 7 and is_black_piece(x, i, board):
		moves_list.append([x, i])
	i = y - 1
	while i >= 0 and board[x][i] == "0":
		moves_list.append([x, i])
		i -= 1
	if i >= 0 and is_black_piece(x, i, board):
		moves_list.append([x, i])
	return moves_list

def rook_possible_moves(pos: tuple[int, int], board):
	if board[int(pos[1] / 90)][int(pos[0] / 90)] == "R":
		return black_rook_possible_moves(pos, board)
	else:
		return white_rook_possible_moves(pos, board)