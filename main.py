import sys
import pygame as pg
import random as r

pg.init()  # инициализация библиотеки


# Config Variables
W = 1280
H = 720
FPS = 60
clock = pg.time.Clock()


# COLORS
GRAY = (237, 237, 237)
RED = (214, 32, 32)
BROWN = (128, 97, 61)

# Game Objects
player = pg.Rect(W // 2, H - 30, 100, 20)  # x, y, width, height
apple = pg.Rect(r.randint(40, W - 40), -50, 40, 40)


# Screen Config
screen = pg.display.set_mode((W, H))  # создаем экран игры размером 1280x720
pg.display.set_caption('Catch an Apple Game')  # название игры в окне игры


# Game loop
game_over = False
while not game_over:  # бесконечный цикл для работы игры
	clock.tick(FPS)
	for event in pg.event.get():  # pg.event.get() - обработчик событий в игре
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()

	screen.fill(GRAY)  # зальем экран серым цветом
	pg.draw.rect(screen, BROWN, player)  # рисую игрового персонажа
	pg.draw.ellipse(screen, RED, apple)  # рисую яблоко

	pg.display.update()  # обновление экрана игры

