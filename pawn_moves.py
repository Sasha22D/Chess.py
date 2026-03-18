def pawn_possible_moves(pos : tuple[int, int], board):
	moves_list = []
	col = int(pos[0] / 90)
	row = int(pos[1] / 90)

	if board[row][col] == "p":
		if board[row + 1][col] == "0":
			moves_list.append([row + 1, col])
		if col - 1 >= 0 and board[row + 1][col - 1] != "0":
			moves_list.append([row + 1, col - 1])
		if col + 1 <= 7 and board[row + 1][col + 1] != "0":
			moves_list.append([row + 1, col + 1])
	elif board[row][col] == "P":
		if board[row - 1][col] == "0":
			moves_list.append([row - 1, col])
		if col - 1 >= 0 and board[row - 1][col - 1] != "0":
			moves_list.append([row - 1, col - 1])
		if col + 1 <= 7 and board[row - 1][col + 1] != "0":
			moves_list.append([row - 1, col + 1])
	return moves_list
