from utils import is_white_piece, is_black_piece

def	black_bishop_possible_moves(pos: tuple[int, int], board):
	moves_list = []
	y = int(pos[0] / 90)
	x = int(pos[1] / 90)
	
	i = x + 1
	j = y + 1
	while i <= 7 and j <= 7 and board[i][j] == "0":
		moves_list.append([i, j])
		i += 1
		j += 1
	if i <= 7 and j <= 7 and is_white_piece(i, j, board):
		moves_list.append([i, j])
	i = x - 1
	j = y - 1
	while i >= 0 and j >= 0 and board[i][j] == "0":
		moves_list.append([i, j])
		i -= 1
		j -= 1
	if i >= 0 and j >= 0 and is_white_piece(i, j, board):
		moves_list.append([i, j])
	i = x + 1
	j = y - 1
	while i <= 7 and j >= 0 and board[i][j] == "0":
		moves_list.append([i, j])
		i += 1
		j -= 1
	if i <= 7 and j >= 0 and is_white_piece(i, j, board):
		moves_list.append([i, j])
	i = x - 1
	j = y + 1
	while i >= 0 and j <= 7 and board[i][j] == "0":
		moves_list.append([i, j])
		i -= 1
		j += 1
	if i >= 0 and j <= 7 and is_white_piece(i, j, board):
		moves_list.append([i, j])
	return moves_list

def	white_bishop_possible_moves(pos: tuple[int, int], board):
	moves_list = []
	y = int(pos[0] / 90)
	x = int(pos[1] / 90)
	
	i = x + 1
	j = y + 1
	while i <= 7 and j <= 7 and board[i][j] == "0":
		moves_list.append([i, j])
		i += 1
		j += 1
	if i <= 7 and j <= 7 and is_black_piece(i, j, board):
		moves_list.append([i, j])
	i = x - 1
	j = y - 1
	while i >= 0 and j >= 0 and board[i][j] == "0":
		moves_list.append([i, j])
		i -= 1
		j -= 1
	if i <= 7 and j >= 0 and is_black_piece(i, j, board):
		moves_list.append([i, j])
	i = x + 1
	j = y - 1
	while i <= 7 and j >= 0 and board[i][j] == "0":
		moves_list.append([i, j])
		i += 1
		j -= 1
	if i <= 7 and j >= 0 and is_black_piece(i, j, board):
		moves_list.append([i, j])
	i = x - 1
	j = y + 1
	while i >= 0 and j <= 7 and board[i][j] == "0":
		moves_list.append([i, j])
		i -= 1
		j += 1
	if i >= 0 and j <= 7 and is_black_piece(i, j, board):
		moves_list.append([i, j])
	return moves_list

def bishop_possible_moves(pos: tuple[int, int], board):
	if board[int(pos[1] / 90)][int(pos[0] / 90)] == "B":
		return black_bishop_possible_moves(pos, board)
	else:
		return white_bishop_possible_moves(pos, board)
