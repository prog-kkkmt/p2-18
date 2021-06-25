import pygame, sys, random, platform
from pygame.locals import *

SIZE = 20
WINDOWWIDTH = 20*SIZE
WINDOWHEIGHT = 21*SIZE + 1
FPS = 10

def terminate():
	pygame.quit()
	sys.exit()

def changeColour(x, y, colour):		#Изменяем цвет области в размере квадрата 20*20 пикслей
	for i in range(x*SIZE, (x+1)*SIZE):
		for j in range(y*SIZE, (y+1)*SIZE):
			pixArray[i][j] = colour
	return None

def getFoodLocation():			#Рандомный спавн еды для змейки
	x = random.randint(0, 19)
	y = random.randint(0, 19)
	while(pixArray[x*SIZE][y*SIZE] != windowSurface.map_rgb(WHITE)):
		x = random.randint(0, 19)
		y = random.randint(0, 19)
	changeColour (x, y, RED)
	return x, y

def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOUR)
    textrect = textobj.get_rect()
    textrect.bottomright = (x, y)
    surface.blit(textobj, textrect)

UP = "U"
DOWN = "D"
LEFT =  "L"
RIGHT =  "R"

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (233, 86, 78)
GREEN = (0, 255, 0)
BLUE = (78, 174, 233)
TEXTCOLOUR = BLACK

pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('S N A K E')
windowSurface.fill(WHITE)

if(platform.system() == 'Windows'):
	font = pygame.font.SysFont("Consolas", 19)

elif(platform.system() == 'Linux'):
	font = pygame.font.SysFont("Ubuntu", 19)

pygame.display.update()

pixArray = pygame.PixelArray(windowSurface)

topScore = '000'
#Общий игровой цикл
while True:
	#Рестарт игры
	snake = [[2, 0, RIGHT], [1, 0, RIGHT], [0, 0, RIGHT]]
	swapper = ''
	windowSurface.fill(WHITE)
	for i in snake:
		changeColour(i[0], i[1], BLUE)
	x, y = getFoodLocation()
	
	#Игровой цикл который запускает игру
	while True:
		#Получаем готовность пользователя
		pixArray = pygame.PixelArray(windowSurface)
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			if event.type == KEYDOWN:
				if event.key == K_LEFT or event.key == ord('a') :
					swapper = LEFT
				elif event.key == K_RIGHT or event.key == ord('d'):
					swapper = RIGHT
				elif event.key == K_DOWN or event.key == ord('s'):
					swapper = DOWN
				elif event.key == K_UP or event.key == ord('w'):
					swapper = UP
			orig = swapper
		
		#Предотвращение движения хвоста змеи в любом направлении
		if ((snake[0][2] == UP and swapper == DOWN) or (snake[0][2] == DOWN and swapper == UP) or (snake[0][2] == RIGHT and swapper == LEFT) or (snake[0][2] == LEFT and swapper == RIGHT)):
			swapper = snake[0][2]
		
		#Управление змейкой
		for i in range(len(snake)):
			snake[i][2], swapper = swapper, snake[i][2]
			if snake[i][2] == RIGHT:
				snake[i][0] += 1
			elif snake[i][2] == LEFT:
				snake[i][0] -= 1
			elif snake[i][2] == DOWN:
				snake[i][1] += 1
			elif snake[i][2] == UP:
				snake[i][1] -= 1
			if snake[i][0] > 19:
				snake[i][0] = 0
			elif snake[i][0] < 0:
				snake[i][0] = 19
			elif snake[i][1] < 0:
				snake[i][1] = 19;
			elif snake[i][1] > 19:
				snake[i][1] = 0

		swapper = orig #Очень важная строка , если ее удалить то можно сломать управление змейкой
		
		
		
		#Game over
		if [snake[0][0], snake[0][1], UP] in snake[1:] or [snake[0][0], snake[0][1], DOWN] in snake[1:] or [snake[0][0], snake[0][1], RIGHT] in snake[1:] or [snake[0][0], snake[0][1], LEFT] in snake[1:]: 
		 	break
		
		
		#Блок кода который помогает змейке "телепортировать себя" при проходе через боковые стенки
		if snake[0][0] == x and snake[0][1] == y:
			x, y = getFoodLocation()
			
			if snake[len(snake) - 1][2] == DOWN:
				if snake[len(snake) - 1][1] >= 1:
					snake.append([snake[len(snake)-1][0], snake[len(snake)-1][1]-1, DOWN])
				else:
					if snake[len(snake) - 1][0] >= 1:
						snake.append([snake[len(snake)-1][0]-1, snake[len(snake)-1][1], RIGHT])
					else:
						snake.append([snake[len(snake)-1][0]+1, snake[len(snake)-1][1], LEFT])
			
			if snake[len(snake) - 1][2] == UP:
				if snake[len(snake) - 1][1] <= 18:
					snake.append([snake[len(snake)-1][0], snake[len(snake)-1][1]+1, UP])
				else:
					if snake[len(snake) - 1][0] >= 1:
						snake.append([snake[len(snake)-1][0]-1, snake[len(snake)-1][1], RIGHT])
					else:
						snake.append([snake[len(snake)-1][0]+1, snake[len(snake)-1][1], LEFT])
			
			if snake[len(snake) - 1][2] == LEFT:
				if snake[len(snake) - 1][0] <= 18:
					snake.append([snake[len(snake)-1][0]+1, snake[len(snake)-1][1], LEFT])
				else:
					if snake[len(snake) - 1][1] >= 1:
						snake.append([snake[len(snake)-1][0], snake[len(snake)-1][1]-1, DOWN])
					else:
						snake.append([snake[len(snake)-1][0], snake[len(snake)-1][1]+1, UP])
			
			if snake[len(snake) - 1][2] == RIGHT:
				if snake[len(snake) - 1][0] >= 1:
					snake.append([snake[len(snake)-1][0]-1, snake[len(snake)-1][1], RIGHT])
				else:
					if snake[len(snake) - 1][0] >= 1:
						snake.append([snake[len(snake)-1][0], snake[len(snake)-1][1]-1, DOWN])
					else:
						snake.append([snake[len(snake)-1][0], snake[len(snake)-1][1]+1, UP])	
		
		windowSurface.fill(WHITE)
		for i in snake:
			changeColour(i[0], i[1], BLUE)
		changeColour(x, y, RED)
		for i in range(400):
			pixArray[i][400] = BLACK
		
		del pixArray
		score = str(len(snake))
		while len(score) < 3:
			score = '0' + score
		while len(topScore) < 3:
			topScore = '0' + topScore
		if int(score) > int(topScore):
			topScore = score
		drawText(score, font, windowSurface, 399, 420)
		drawText(topScore, font, windowSurface, 170, 420)
		drawText("SCORE : ", font, windowSurface, 369, 420)
		drawText("HIGH SCORE : ", font, windowSurface, 140, 420)

		pygame.display.update()
		mainClock.tick(FPS)
