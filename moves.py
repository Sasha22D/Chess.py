from utils import is_white_piece

def pawn_possible_moves(pos : tuple[int, int], board):
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

def	rook_possible_moves(pos: tuple[int, int], board):
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

def bishop_possible_moves(pos: tuple[int, int], board):
	moves_list = []
	y = int(pos[0] / 90)
	x = int(pos[1] / 90)
	
	i = x + 1
	j = y + 1
	while board[i][j] == "0":
		moves_list.append([i, j])
		i += 1
		j += 1
	i = x - 1
	j = y - 1
	while board[i][j] == "0":
		moves_list.append([i, j])
		i -= 1
		j -= 1
	i = x + 1
	j = y - 1
	while board[i][j] == "0":
		moves_list.append([i, j])
		i += 1
		j -= 1
	i = x - 1
	j = y + 1
	while board[i][j] == "0":
		moves_list.append([i, j])
		i -= 1
		j += 1
	return moves_list