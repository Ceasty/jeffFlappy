import pygame, sys, random

class Pipe():
	def __init__(self, Arena):
		self.screen = Arena.screen
		self.screen_rect = self.screen.get_rect()

		self.settings = Arena.settings
		self.pipe = self.settings.pipe
		self.pipe_rect = self.settings.pipe.get_rect()

		self.pipe_list = []
		self.pipe_pos_possible_list = [300, 400, 525]
		self.SPAWNPIPE = pygame.USEREVENT
		pygame.time.set_timer(self.SPAWNPIPE, 1200)

	def create_pipe(self):
		#self.pipe_length = random.choice(self.pipe_pos_possible_list)
		self.pipe_length = random.randint(300, 525)

		#Spawn Top Pipe
		self.pipe_top = self.pipe.get_rect(midbottom = (436, self.pipe_length - 250))
		#self.pipe_top = self.pipe.get_rect(midbottom = (self.screen_rect.center))
		#self.pipe_top.x += 220
		#self.pipe_top.y += (self.pipe_length - 200)


		#Spawn Bottom pipe
		self.pipe_bot = self.pipe.get_rect(midtop = (436, self.pipe_length))

		#self.pipe_bot = self.pipe.get_rect(midtop = (self.screen_rect.center))
		#self.pipe_bot.x += 220
		#self.pipe_bot.y += self.pipe_length

		return self.pipe_bot, self.pipe_top

	def move_pipes(self, pipes):
		for pipe in pipes:
			pipe.centerx -= 4

		return pipes

	def blit_pipes(self, pipes):
		for pipe in pipes:
			if pipe.bottom >= 644:
				self.screen.blit(self.pipe, pipe)

			else :
				flip_pipe = pygame.transform.flip(self.pipe, False, True)
				self.screen.blit(flip_pipe, pipe)

	def remove_pipes(self):
		if self.pipe_rect.midright <= 0:
			self.pipe_list.remove(self.pipe)


