import pygame, sys, random
from settings import Settings
from platform import Platform
from bird import Bird
from pipe import Pipe
from score import Score

class Arena:
	def __init__(self):
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode([self.settings.arena_width, self.settings.arena_height])
		self.title = pygame.display.set_caption(self.settings.title)
		self.running = True
		self.game_status = True

		self.clock = pygame.time.Clock()
		self.platform = Platform(self)
		self.bird = Bird(self)
		self.score = Score(self)

		self.pipe = Pipe(self)

	def check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.running = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and self.game_status:
					print(self.pipe.pipe_list)
					self.bird.bird_movement = 0 
					self.bird.bird_movement -= 12

				if event.key == pygame.K_SPACE and self.game_status == False:
					self.game_status = True
					self.score.score_amount = 0
					self.pipe.pipe_list.clear()
					self.bird.replace_bird()

			if event.type == self.bird.BIRDFLAP:

				if self.settings.bird_index < 2:
					self.settings.bird_index += 1

				else:
					self.settings.bird_index = 0

				self.bird.bird, self.bird.bird_rect = self.bird.bird_animation()
			
			if event.type == self.pipe.SPAWNPIPE:
				self.pipe.pipe_list.extend(self.pipe.create_pipe())#Melebarkan List
	def blit_backround(self):
		self.screen.blit(self.settings.background, [0,0])
		#OKOK

	def check_collision(self, pipes):
		for pipe in pipes:
			if self.bird.bird_rect.colliderect(pipe):
				return False
		if self.bird.bird_rect.top <= -100 or self.bird.bird_rect.bottom >= 660:
			return False

		return True



	def update_screen(self):
		self.blit_backround()

		if self.game_status:
			 #Refresh Backround
			self.bird.move_bird()

			self.bird.rotated_bird = self.bird.rotate_bird(self.bird.bird)

			self.bird.blit_bird()
			self.game_status = self.check_collision(self.pipe.pipe_list)
			self.pipe.pipe_list = self.pipe.move_pipes(self.pipe.pipe_list)
			self.remove_pipes(self.pipe.pipe_list)
			self.pipe.blit_pipes(self.pipe.pipe_list)
			self.score.score_display(self.game_status)

		else:
			self.score.update_high_score()
			self.score.score_display(self.game_status)

		self.platform.blit_platform()#Moving and show platform
		pygame.display.update()
			

	def remove_pipes(self, pipes):
		for pipe in pipes:
			if pipe.right <= 0:
				pipes.remove(pipe)
				self.score.score_amount += 0.5

	def run_game(self):
		while self.running:

			self.check_events()
			self.update_screen()

		self.clock.tick(120)

flappyGame = Arena()
flappyGame.run_game()
