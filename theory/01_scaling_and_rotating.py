import pygame as pg
from pygame.locals import *
import random as r


pg.init()
w, h = 1280, 720
screen = pg.display.set_mode((w, h))
running = True


img0 = pg.image.load('angry-birds.png').convert_alpha()
img0_rect = img0.get_rect()  # превращаю картинку в игровой объект
img0_rect.center = w // 2, h // 2

angle = 0
scale = 1

while running:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_r:
				if event.mod & pg.KMOD_LSHIFT:  # если кнопка модифицирована и модификатор - левый шифт
					angle -= 10
				else:
					angle += 10
				img0 = pg.transform.rotozoom(img0, angle, scale)
			if event.key == pg.K_s:
				if event.mod & pg.KMOD_LSHIFT:  # если кнопка модифицирована и модификатор - левый шифт
					scale /= 1.1
				else:
					scale *= 1.1
				img0 = pg.transform.rotozoom(img0, angle, scale)
			img0_rect = img0.get_rect()
			img0_rect.center = w // 2, h // 2


	screen.fill((255, 255, 255))
	screen.blit(img0, img0_rect)
	pg.draw.rect(screen, (255, 0, 0), img0_rect, 1)
	pg.display.update()


