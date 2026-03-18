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
