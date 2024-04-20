import random as r


def player_motion(obj, sp, s_width):
	"""
	Function defines player moving
	:param obj: player object
	:param sp: speed
	:param s_width: width of screen
	:return: None
	"""
	obj.x += sp

	if obj.left <= 0:  # если координата левого края объекта меньше/равна нулю
		obj.left = 0  # зафиксировать координату левого края объекта в нуле
	elif obj.right >= s_width:  # если координата правого края объекта больше/равна ширине экрана
		obj.right = s_width  # зафиксировать координату правого края объекта на ширине экрана


def opponent_motion(obj, sp, s_width, s_height, pl):
	"""
	Function defines opponent moving
	:param obj: opponent object
	:param sp: opponent speed
	:param s_width: screen width
	:param s_height: screen height
	:param pl: player object
	:return: None
	"""
	obj.y += sp * 0.7
	if obj.bottom > s_height:  # если координата нижнего края яблока больше высоты экрана
		obj.x = r.randint(40, s_width - 40)  # поменять яблоку Х
		obj.y = -50  # поменять яблоку У
		return 'miss'
	elif obj.colliderect(pl):
		obj.x = r.randint(40, s_width - 40)  # поменять яблоку Х
		obj.y = -50  # поменять яблоку У
		return 'catch'


def draw_button(screen, text, x, y, w, h, color):
	import pygame as pg
	mouse_pos = pg.mouse.get_pos()  # сохраняю кортеж с координатами курсора
	click = pg.mouse.get_pressed()  # сохраняю кортеж с информацией о том, какая кнопка мыши была нажата
	#print(f'Позиция курсора: {mouse_pos}')
	#print(f'Нажатые кнопки: {click}')
	btn_rect = pg.Rect(x, y, w, h)
	if btn_rect.collidepoint(mouse_pos):  # если квадрат кнопки пересекается с позицией мыши
		if click[0]:  # если кликнули левой кнопкой мыши по кнопке
			return 'Restart'
		color = (color[0] - 50, color[1] - 50, color[2] - 50)
	pg.draw.rect(screen, color, btn_rect)
	text_surf = text.render('Restart', True, (0, 0, 0))
	text_rect = text_surf.get_rect(center=btn_rect.center)
	screen.blit(text_surf, text_rect)

