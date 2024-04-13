import pygame as pg
from pygame.locals import *
import random as r


pg.init()
w, h = 1280, 720
screen = pg.display.set_mode((w, h))
running = True


img = pg.image.load('angry-birds.png').convert_alpha()
img_rect = img.get_rect()  # превращаю картинку в игровой объект
img_rect.center = w // 2, h // 2
moving = False

speed_x = 5
speed_y = 5

while running:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
		elif event.type == pg.MOUSEBUTTONDOWN:
			if img_rect.collidepoint(event.pos):  # если курсор находится в рамках картинки
				moving = True
		elif event.type == pg.MOUSEBUTTONUP:
			moving = False
		elif event.type == pg.MOUSEMOTION and moving:
			img_rect.move_ip(event.rel)  # квадрат изображения должен следовать за положением курсора

	screen.fill((255, 255, 255))
	screen.blit(img, img_rect)
	pg.draw.rect(screen, (255, 0, 0), img_rect, 1)
	pg.display.update()

	#img_rect.x += speed_x
	#img_rect.y += speed_y

	if img_rect.right >= w:
		speed_x *= -1
	elif img_rect.left <= 0:
		speed_x *= -1
	elif img_rect.top <= 0:
		speed_y *= -1
	elif img_rect.bottom >= h:
		speed_y *= -1

