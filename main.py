import sys
import pygame as pg
import random as r
import game_logic as gl

pg.init()  # инициализация библиотеки

auto = False

# Config Variables
W = 1280
H = 720
FPS = 60
clock = pg.time.Clock()
speed = 10
player_speed = 0
object_speed = speed


# scores
score, miss = 0, 0
pg.font.init()  # инициализация механизма отображения шрифтов
score_font = pg.font.SysFont('Arial', 32)


# COLORS
GRAY = (237, 237, 237)
RED = (214, 32, 32)
BROWN = (128, 97, 61)

# Screen Config
screen = pg.display.set_mode((W, H))  # создаем экран игры размером 1280x720
pg.display.set_caption('Catch an Apple Game')  # название игры в окне игры


# Game Objects
player_img = pg.image.load('assets/bowl.png').convert_alpha()
player_img = pg.transform.scale(player_img, (120, 40))
apple_img = pg.image.load('assets/apple.png').convert_alpha()
bg_image = pg.image.load('assets/bg.jpg').convert()
heart_img = pg.image.load('assets/heart.png').convert_alpha()
heart_rect = heart_img.get_rect()

player = player_img.get_rect()
player.centerx = W // 2  # автоматически определить центр игрока по центру экрана
player.y = H - 50
apple = apple_img.get_rect()
apple.x, apple.y = r.randint(40, W - 40), -50


# Game loop
game_over = False
while not game_over:  # бесконечный цикл для работы игры
	if miss >= 3:
		game_over = True

	clock.tick(FPS)
	for event in pg.event.get():  # pg.event.get() - обработчик событий в игре
		if event.type == pg.QUIT:
			pg.quit()
			sys.exit()

	screen.blit(bg_image, (0, 0))  # вместо screen.fill

	screen.blit(player_img, player)
	screen.blit(apple_img, apple)

	score_text = score_font.render(f'Score: {score}', True, (107, 237, 185))
	screen.blit(score_text, (10, 70))  # расположить score_text в координатах 10;10
	lives = 3 - miss
	for i in range(lives):
		heart_rect.x = 10 + (i * heart_rect.width)
		heart_rect.y = 5
		screen.blit(heart_img, heart_rect)


	pg.display.update()  # обновление экрана игры

	apple_catch = gl.opponent_motion(apple, object_speed, W, H, player)
	if apple_catch == 'miss':
		miss += 1
	elif apple_catch == 'catch':
		score += 10

	if not auto:
		keys = pg.key.get_pressed()  # отслеживаю нажатие кнопок
		if keys[pg.K_LEFT]:
			player_speed = -speed
		elif keys[pg.K_RIGHT]:
			player_speed = speed
		else:
			player_speed = 0
	else:
		if apple.x > player.x:
			player.x += 5
		elif apple.x < player.x:
			player.x -= 5

	gl.player_motion(player, player_speed, W)


