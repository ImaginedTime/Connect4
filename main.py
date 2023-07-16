import pygame

pygame.init()

sqSize = 100
cols, rows = 8, 6
vals, sqs = [], []
width, height = (sqSize + 4) * cols, (sqSize + 4) * rows 
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption("Connect 4") 
clickedCol = None
rowToBePlaced = None
selected = False
turn = 1
started, yellowWon, redWon, tie = False, False, False, False

# FONT VARIBALES 
font1 = pygame.font.Font("freesansbold.ttf", 32)
font2 = pygame.font.Font("freesansbold.ttf", 16)

for i in range(rows):
	sqs.append([])
	vals.append([])
	for j in range(cols):
		sqs[i].append(pygame.Rect((sqSize + 5)*j, (sqSize + 5)*i, sqSize, sqSize))
		vals[i].append(0)

def won():
	if vals.count(0) == 0:
		tie == False
		return

while True:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			pygame.quit()
			break
		if e.type == pygame.K_RETURN:
			started = False
		mouse = pygame.mouse.get_pos()
		if e.type == pygame.MOUSEBUTTONDOWN and mouse[0] > 0 and mouse[1] > 0 and mouse[1] < width and mouse[1] < height:
			started = True
		if started:
			for i in range(rows):
				for j in range(cols):
					if e.type == pygame.MOUSEBUTTONDOWN and mouse[0] < sqs[i][j].right and mouse[1] < sqs[i][j].bottom and mouse[0] > sqs[i][j].left and mouse[1] > sqs[i][j].top :
						clickedCol = j
						for x in range(rows - 1, -1, -1):
							if vals[x][clickedCol] == 0:
								rowToBePlaced = x
								selected = True
								vals[rowToBePlaced][clickedCol] = turn
								turn *= -1
								break

						if not selected:	clickedCol = None
		
	surface.fill((100,100,100))
	if started:
		for i in range(rows):
			for j in range(cols):
				pygame.draw.rect(surface, (150,150,150), sqs[i][j])
				pygame.draw.ellipse(surface, (100,100,100), sqs[i][j])
				if vals[i][j] == 1:
					pygame.draw.ellipse(surface, (255,255,0), sqs[i][j])
				elif vals[i][j] == -1:
					pygame.draw.ellipse(surface, (255,0,0), sqs[i][j])
	else:
		surface.fill((41,44,36))
		startText = font1.render("START", True, (200,200,200))
		pressEnterText = font2.render("Press Enter or Click To Begin", True, (200,200,200))
		surface.blit(startText, (width / 2 - startText.get_rect().width/2, height /2 - startText.get_rect().height/2))
		surface.blit(pressEnterText, (width/2 - pressEnterText.get_rect().width/2, height/2 + pressEnterText.get_rect().height/2 + startText.get_rect().height))

	pygame.display.flip()