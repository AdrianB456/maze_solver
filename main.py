import pygame, random, sys, os, pickle
import numpy as np
import matplotlib.pyplot as plt
pygame.init()


done = False
while not done:
	file = input('Which is the name of the file?')
	try:
		with open(os.path.join('maps', f'{file}.pkl'), 'rb+') as f:
			content = pickle.load(f)
		done = True
	except:
		print('That was not an option')

initial_state = content['start_pos']
finish = content['finish']
walls = content['walls_pos']
parameter = content['parameter']
rect_size = content['rect_size']

x_screen = parameter[0] * rect_size
y_screen = parameter[1] * rect_size

white = (244, 244, 244)
black = (24, 24, 24)
gray = (160, 160, 160)
green = (24, 244, 24)

screen = pygame.display.set_mode((x_screen, y_screen))
clock = pygame.time.Clock()


def get_pos(state):
	x_pos = state[0] * rect_size + rect_size / 2
	y_pos = state[1] * rect_size + rect_size / 2
	return (x_pos, y_pos)

agent_rect = pygame.Rect(0, 0, rect_size, rect_size)
finish_rect = pygame.Rect(0, 0, rect_size, rect_size)
finish_rect.center = get_pos(finish)
walls_rect = []
for wall in walls:
	wall_rect = pygame.Rect(0, 0, rect_size, rect_size)
	wall_rect.center = get_pos(wall)
	walls_rect.append(wall_rect)

q_table = np.zeros([parameter[0], parameter[1], 4])
epsilon = 0.005
discount = 0.9
learning_rate = 0.1
episodes = int(q_table.size * 0.5) + len(walls) * 2 + 1000
moves_limit = sum(parameter) * 5
epsilon_decade = epsilon / episodes

show_episode = sum(parameter) * 7

dict_rewards = {'ep': [], 'avg': [], 'min': [], 'max': []}
ep_rewards = []

for episode in range(1, episodes):
	episode_reward = 0

	epsilon -= epsilon_decade
	state = list(initial_state)
	all_states = [state]
	done = False

	moves = 0
	if episode % show_episode == 0:
		print(episode)
		moves_limit += sum(parameter) * 5
		show = True
	else: 
		show = False

	if episode % show_episode == 0:
		dict_rewards['ep'].append(episode)
		dict_rewards['avg'].append(sum(ep_rewards)/len(ep_rewards))
		dict_rewards['min'].append(min(ep_rewards))
		dict_rewards['max'].append(max(ep_rewards))
		ep_rewards = []

	while not done:
		for ev in pygame.event.get():
			if ev.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		new_state = [0, 0]
		if random.random() <= epsilon:
			action = random.randint(0, 3)
		else:
			action = np.argmax(q_table[state[0]][state[1]])

		if action == 0:
			new_state[0] = state[0] - 1
			new_state[1] = state[1]
		elif action == 1:
			new_state[0] = state[0] + 1
			new_state[1] = state[1]
		elif action == 2:
			new_state[1] = state[1] + 1
			new_state[0] = state[0]
		elif action == 3:
			new_state[1] = state[1] - 1
			new_state[0] = state[0]

		reward = -1

		times_same_place = 0
		for old_state in all_states:
			if old_state == new_state:
				times_same_place += 1

		if times_same_place > 2: reward *= 2

		if new_state == finish:
			done = True
			reward = q_table.size
			print('Made it in episode ' + str(episode) + '.')
		for wall in walls:
			if new_state == wall:
				done = True
				reward = -q_table.size

		try: q_table[new_state[0]][new_state[1]]
		except: 
			done = True
			reward = -q_table.size

		if new_state[0] < 0 or new_state[1] < 0: 
			done = True
			reward = -q_table.size

		episode_reward += reward

		if not done:
			max_next_q = np.max(q_table[new_state[0]][new_state[1]])
			old_q = q_table[state[0]][state[1]][action]
			
			new_q = (1 - learning_rate) * old_q + learning_rate * (reward + discount * max_next_q)
			q_table[state[0]][state[1]][action] = new_q
		if done: 
			q_table[state[0]][state[1]][action] = reward

		moves += 1
		if moves >= moves_limit:
			done = True

		state = [new_state[0], new_state[1]]
		all_states.append(state)

		position = get_pos(state)
		agent_rect.center = position

		if show:
			screen.fill(white)
			for wall_rect in walls_rect:
				pygame.draw.rect(screen, black, wall_rect)
			pygame.draw.rect(screen, green, finish_rect)
			pygame.draw.rect(screen, gray, agent_rect)
			pygame.display.update()
			pygame.time.wait(30)

	ep_rewards.append(episode_reward)

plt.plot(dict_rewards['ep'], dict_rewards['avg'], label='average')
plt.plot(dict_rewards['ep'], dict_rewards['min'], label='minimum')
plt.plot(dict_rewards['ep'], dict_rewards['max'], label='maximum')
plt.legend(loc=4)
plt.show()

done = False
state = list(initial_state)

move = False

while not done:
	screen.fill(white)
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if ev.type == pygame.KEYDOWN:
			if ev.key == pygame.K_RETURN:
				move = True

	if move:
		action = np.argmax(q_table[state[0]][state[1]])

		if action == 0:
			state[0] -= 1
		elif action == 1:
			state[0] += 1
		elif action == 2:
			state[1] += 1
		elif action == 3:
			state[1] -= 1

	if state == finish:
		done = True
	for wall in walls:
		if state == wall:
			done = True

	position = get_pos(state)
	agent_rect.center = position

	try: q_table[state[0]][state[1]]
	except: 
		done = True

	if state[0] < 0 or state[1] < 0: 
		done = True

	for wall_rect in walls_rect:
		pygame.draw.rect(screen, black, wall_rect)
	pygame.draw.rect(screen, green, finish_rect)
	pygame.draw.rect(screen, gray, agent_rect)
	pygame.display.update()
	pygame.time.wait(50)


pygame.quit()
