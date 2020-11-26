import pygame

class Platform:
	def __init__(self, Arena):
		self.settings = Arena.settings
		self.screen = Arena.screen
		self.platform = self.settings.platform
		self.platform_rect = self.platform.get_rect()
		self.pos_x = 0

	def blit_platform(self):
		self.pos_x -= 1
		self.screen.blit(self.settings.platform, [self.pos_x,660]) #Blit platform sederhana(belom gerak lel)
		self.screen.blit(self.settings.platform, [self.pos_x + 432, 660])

		if self.pos_x <= -(self.settings.arena_width):
			self.pos_x = 0


