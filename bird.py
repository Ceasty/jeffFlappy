import pygame, sys, random

class Bird():
	def __init__(self, Arena):
		self.screen = Arena.screen
		self.screen_rect = Arena.screen.get_rect()


		self.settings = Arena.settings

		self.bird = self.settings.bird
		self.bird_rect = self.bird.get_rect()
		self.bird_movement = 0

		self.BIRDFLAP = pygame.USEREVENT + 1
		pygame.time.set_timer(self.BIRDFLAP, 200)

		self.replace_bird()

	def blit_bird(self):
		self.screen.blit(self.rotated_bird, self.bird_rect)

	def move_bird(self):
		self.bird_movement += self.settings.gravity
		self.bird_rect.centery += self.bird_movement

	def replace_bird(self):
		self.bird_rect.midleft = self.screen_rect.midleft
		self.bird_rect.x += 50
		self.bird_movement = 0

	def rotate_bird(self, bird):
		self.rotated_bird = pygame.transform.rotozoom(self.bird, self.bird_movement*2 , 1)
		return self.rotated_bird

	def bird_animation(self):
		self.bird = self.settings.bird_frames[self.settings.bird_index]
		self.bird_rect = self.bird.get_rect(center = (75 , self.bird_rect.centery))
		return self.bird, self.bird_rect





		