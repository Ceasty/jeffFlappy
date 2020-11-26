import pygame, sys, random

class Score:

	def __init__(self, Arena):
		self.settings = Arena.settings
		self.score_amount = 0

		self.screen = Arena.screen
		self.screen_rect = Arena.screen.get_rect()
		self.high_score_amount = 0

	def score_display(self, game_state):

		if game_state:

			self.score = self.settings.game_font.render(str(int(self.score_amount)), True, (255,255,255))
			self.score_rect = self.score.get_rect(center = (self.screen_rect.center))
			self.score_rect.y = 75

			self.screen.blit(self.score, self.score_rect)

		if not game_state:
			self.score = self.settings.game_font.render(str(f'Score :{int(self.score_amount)}'), True, (255,255,255))
			self.score_rect = self.score.get_rect(center = (self.screen_rect.center))
			self.score_rect.y = 100
			self.screen.blit(self.score, self.score_rect)

			self.high_score = self.settings.game_font.render(f'High Score : {int(self.high_score_amount)}', True, (255,255,255))
			self.high_score_rect = self.high_score.get_rect(center = (self.screen_rect.center))
			self.high_score_rect.y = 150
			self.screen.blit(self.high_score, self.high_score_rect)

	def update_high_score(self):
		if self.score_amount > self.high_score_amount:
			self.high_score_amount = self.score_amount
		return self.high_score_amount


