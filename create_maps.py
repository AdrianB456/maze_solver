import pygame, pickle, os, sys, glob
pygame.init()

def input_file():
	user_input = input('What will be the name of the file? ')
	while user_input == '':
		print('That name can\'t be aplied. \n')
		user_input = input('What will be the name of the file? ')

	return user_input

def file_exists(file_name):
	exists = False

	path = os.getcwd()
	files = glob.glob(path + '\\maps\\*.pkl')
	for file_path in files:
		if file_name in file_path:
			exists = True

	return exists


file_name = input_file() + '.pkl'
files_in_directory = glob.glob(os.getcwd() + '\\maps\\*.pkl')

overwrite = False
while file_exists(file_name) and not overwrite:
	user_input = input('That file name already exists. Want to overwrite it? [n/y] ')

	while user_input != 'y' and user_input != 'n':
		print('That is not a valid answere. \n')
		user_input = input('That file name already exists. Want to overwrite it? [n/y] ')

	if user_input == 'y':
		overwrite = True

	else: file_name = input_file() + '.pkl'

file = os.path.join('maps', file_name)

parameter = [60, 60]
rect_size = 10

start_pos = [0, 0]
finish = [59, 59]


if not (0 <= finish[0] < parameter[0] and 0 <= finish[1] < parameter[1]):
	print('Error: The coordinate of the finish point was either to low or to high for the parameter') 
	sys.exit()

if not (0 <= start_pos[0] < parameter[0] and 0 <= start_pos[1] < parameter[1]):
	print('Error: The coordinate of the starting point was either to low or to high for the parameter') 
	sys.exit()

x_screen = parameter[0] * rect_size
y_screen = parameter[1] * rect_size

white = (244, 244, 244)
black = (24, 24, 24)
gray = (160, 160, 160)
green = (24, 244, 24)

screen = pygame.display.set_mode((x_screen, y_screen))

def get_cord(pos):
	x_pos = pos[0] * rect_size + rect_size / 2
	y_pos = pos[1] * rect_size + rect_size / 2
	return (x_pos, y_pos)

def ocupied(pos):
	ocupied = False

	if pos == start_pos or pos == finish:
		ocupied = True

	for wall_pos in walls_pos:
		if pos == wall_pos:
			ocupied = True

	return ocupied

start_rect = pygame.Rect(0, 0, rect_size, rect_size)
start_rect.center = get_cord(start_pos)
finish_rect = pygame.Rect(0, 0, rect_size, rect_size)
finish_rect.center = get_cord(finish)

run = True
walls_pos = []
walls_rect = []
for wall in walls_pos:
	pos = get_cord(wall)
	wall_rect = pygame.Rect(0, 0, rect_size, rect_size)
	wall_rect.center = pos
	walls_rect.append(wall_rect)


clock = pygame.time.Clock()
while run:
	screen.fill((244, 244, 244))
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			run = False
			pygame.quit()
			sys.exit()

		if ev.type == pygame.KEYDOWN:
			if ev.key == pygame.K_RETURN:
				dictionary = {
					'start_pos':start_pos,
					'rect_size': rect_size,
					'finish': finish,
					'parameter': parameter,
					'walls_pos': walls_pos
				}

				with open(file, 'wb+') as f:
					pickle.dump(dictionary, f)

				print('saved')

		elif ev.type == pygame.MOUSEBUTTONDOWN:
			if ev.button == 1:
				mouse_pos = pygame.mouse.get_pos()
				wall_pos = [mouse_pos[0] // rect_size, mouse_pos[1] // rect_size]

				wall_rect = pygame.Rect(0, 0, rect_size, rect_size)
				wall_rect.center = get_cord(wall_pos)
				if not ocupied(wall_pos):
					walls_pos.append(wall_pos)
					walls_rect.append(wall_rect)


			elif ev.button == 3:
				mouse_pos = pygame.mouse.get_pos()
				wall_pos = [mouse_pos[0] // rect_size, mouse_pos[1] // rect_size]
				try:
					wall_index = walls_pos.index(wall_pos)
					walls_rect.pop(wall_index)
					walls_pos.pop(wall_index)

				except: pass


	pygame.draw.rect(screen, gray, start_rect)
	pygame.draw.rect(screen, green, finish_rect)

	for wall in walls_rect:
		pygame.draw.rect(screen, black, wall)
	pygame.display.update()
	clock.tick(30)

