
import random
import pygame


class Wall(pygame.sprite.Sprite):
	def __init__(self, x, y, width, height, color, **kwargs):
		pygame.sprite.Sprite.__init__(self)
		self.image= pygame.Surface([width, height])
		self.image.fill(color)
		self.rect= self.image.get_rect()
		self.rect.left= x
		self.rect.top= y



class Food(pygame.sprite.Sprite):
	def __init__(self, x, y, width, height, color, bg_color, **kwargs):
		pygame.sprite.Sprite.__init__(self)
		self.image= pygame.Surface([width, height])
		self.image.fill(bg_color)
		self.image.set_colorkey(bg_color)
		pygame.draw.ellipse(self.image, color, [0, 0, width, height])
		self.rect= self.image.get_rect()
		self.rect.left= x
		self.rect.top= 



class Player(pygame.sprite.Sprite):
	def __init__(self, x, y, role_image_path):
		pygame.sprite.Sprite