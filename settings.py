import pygame, sys, random


class Settings():
	def __init__(self):

		#Arena Settings
		self.arena_width = 432
		self.arena_height = 768
		self.title = 'Flappy Bird'
		self.game_font = pygame.font.Font('04B_19.ttf',40)

		#Variable
		self.gravity = 0.5
		self.score = 0
		self.high_score = 0

		#Background Settings
		self.background = pygame.image.load('image/background-day.png')
		self.background = pygame.transform.scale(self.background, (self.arena_width,self.arena_height)) #Resize Backround as the windows size

		#Platform Settings
		self.platform = pygame.image.load('image/base.png')
		self.platform = pygame.transform.scale(self.platform, (504,168)) # Scale agar pas

		#Bird Settings 


		self.bird_down = pygame.transform.scale(pygame.image.load('image/bluebird-downflap.png'), (51, 36))
		self.bird_mid = pygame.transform.scale(pygame.image.load('image/bluebird-midflap.png'), (51, 36))
		self.bird_up = pygame.transform.scale(pygame.image.load('image/bluebird-upflap.png'), (51, 36))
		self.bird_frames = [self.bird_down, self.bird_mid, self.bird_up]
		self.bird_index = 0

		self.bird = self.bird_frames[self.bird_index]
		#self.bird = pygame.image.load('image/bluebird-midflap.png')
		#self.bird = pygame.transform.scale(self.bird, (51, 36))

		#Pipe Settings
		self.pipe = pygame.image.load('image/pipe-green.png')
		self.pipe = pygame.transform.scale(self.pipe, (78,470))