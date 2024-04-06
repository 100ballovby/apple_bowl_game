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
	elif obj.colliderect(pl):
		obj.x = r.randint(40, s_width - 40)  # поменять яблоку Х
		obj.y = -50  # поменять яблоку У
