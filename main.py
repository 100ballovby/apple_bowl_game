import sys
import pygame as pg

pg.init()  # инициализация библиотеки


# Config Variables
W = 1280
H = 720
FPS = 60
clock = pg.time.Clock()


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

