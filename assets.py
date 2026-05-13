import pygame

def load_pieces_images(case_size: int) -> dict[str, pygame.Surface]:
	pieces = {
		"wr": "./assets/wr.png",
		"wn": "./assets/wn.png",
		"wb": "./assets/wb.png",
		"wq": "./assets/wq.png",
		"wk": "./assets/wk.png",
		"wp": "./assets/wp.png",
		"br": "./assets/br.png",
		"bn": "./assets/bn.png",
		"bb": "./assets/bb.png",
		"bq": "./assets/bq.png",
		"bk": "./assets/bk.png",
		"bp": "./assets/bp.png"
	}
	images = {}
	for key, path in pieces.items():
		img = pygame.image.load(path)
		images[key] = pygame.transform.scale(img, (case_size, case_size))
	return images