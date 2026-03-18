from utils import is_white_piece, is_black_piece

def	black_rook_possible_moves(pos: tuple[int, int], board):
	moves_list = []
	col = int(pos[0] / 90)
	row = int(pos[1] / 90)

	i = row + 1
	while i <= 7 and board[i][col] == "0":
		moves_list.append([i, col])
		i += 1
	if i <= 7 and is_white_piece(i, col, board):
		moves_list.append([i, col])
	i = row - 1
	while i >= 0 and board[i][col] == "0":
		moves_list.append([i, col])
		i -= 1
	if i >= 0 and is_white_piece(i, col, board):
		moves_list.append([i, col])
	i = col + 1
	while i <= 7 and board[row][i] == "0":
		moves_list.append([row, i])
		i += 1
	if i <= 7 and is_white_piece(row, i, board):
		moves_list.append([row, i])
	i = col - 1
	while i >= 0 and board[row][i] == "0":
		moves_list.append([row, i])
		i -= 1
	if i >= 0 and is_white_piece(row, i, board):
		moves_list.append([row, i])
	return moves_list

def	white_rook_possible_moves(pos: tuple[int, int], board):
	moves_list = []
	col = int(pos[0] / 90)
	row = int(pos[1] / 90)

	i = row + 1
	while i <= 7 and board[i][col] == "0":
		moves_list.append([i, col])
		i += 1
	if i <= 7 and is_black_piece(i, col, board):
		moves_list.append([i, col])
	i = row - 1
	while i >= 0 and board[i][col] == "0":
		moves_list.append([i, col])
		i -= 1
	if i >= 0 and is_black_piece(i, col, board):
		moves_list.append([i, col])
	i = col + 1
	while i <= 7 and board[row][i] == "0":
		moves_list.append([row, i])
		i += 1
	if i <= 7 and is_black_piece(row, i, board):
		moves_list.append([row, i])
	i = col - 1
	while i >= 0 and board[row][i] == "0":
		moves_list.append([row, i])
		i -= 1
	if i >= 0 and is_black_piece(row, i, board):
		moves_list.append([row, i])
	return moves_list

def rook_possible_moves(pos: tuple[int, int], board):
	col = int(pos[0] / 90)
	row = int(pos[1] / 90)

	if board[row][col] == "R":
		return black_rook_possible_moves(pos, board)
	else:
		return white_rook_possible_moves(pos, board)