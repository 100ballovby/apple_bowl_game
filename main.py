import sys
import pygame as pg
import random as r
import game_logic as gl

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
player = pg.Rect(0, H - 30, 100, 20)  # x, y, width, height
player.centerx = W // 2  # автоматически определить центр игрока по центру экрана
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

	apple.y += 5
	if apple.bottom > H:  # если координата нижнего края яблока больше высоты экрана
		apple.x = r.randint(40, W - 40)  # поменять яблоку Х
		apple.y = -50  # поменять яблоку У

	keys = pg.key.get_pressed()  # отслеживаю нажатие кнопок
	p_speed = 0
	if keys[pg.K_LEFT]:
		p_speed = -10
	elif keys[pg.K_RIGHT]:
		p_speed = 10

	gl.player_motion(player, p_speed, W)


