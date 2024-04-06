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

