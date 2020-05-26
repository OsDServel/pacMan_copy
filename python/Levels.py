
import pygame
from Sprites import *


NUMLEVELS= 1



class Level1():
	def __init__(self):
		self.info= 'level1'

	def setupWalls(self, wall_color):
		self.wall_sprites= pygame.sprite.Group()
		wall_positions= [[0, 0, 6, 600],
						 [0, 0, 600, 6],
						 [0, 600, 606, 6],
						 [600, 0, 6, 606],
						 [300, 0, 6, 66],
						 [60, 60, 186, 6],
						 [360, 60, 186, 6],
						 [60, 120, 66, 6],
						 [60, 120, 6, 126],
						 [180, 120, 246, 6],
						 [300, 120, 6, 66],
						 [480, 120, 66, 6],
						 [540, 120, 6, 126],
						 [120, 180, 126, 6],
						 [120, 180, 6, 126],
						 [360, 180, 126, 6],
						 [480, 180, 6, 126],
						 [180, 240, 6, 126],
						 [180, 360, 246, 6],
						 [420, 240, 6, 126],
						 [240, 240, 42, 6],
						 [324, 240, 42, 6],
						 [240, 240, 6, 66],
						 [240, 300, 126, 6],
						 [360, 240, 6, 66],
						 [0, 300, 66, 6],
						 [540, 300, 66, 6],
						 [60, 360, 66, 6],
						 [60, 360, 6, 186],
						 [480, 360, 66, 6],
						 [540, 360, 6, 186],
						 [120, 420, 366, 6],
						 [120, 420, 6, 66],
						 [480, 420, 6, 66],
						 [180, 480, 246, 6],
						 [300, 480, 6, 66],
						 [120, 540, 126, 6],
						 [360, 540, 126, 6]]
		for wall_position in wall_positions:
			wall= Wall(*wall_position, wall_color)
			self.wall_sprites.add(wall)
		return self.wall_sprites

	def setupGate(self, gate_color):
		self.gate_sprites= pygame.sprite.Group()
		self.gate_sprites.add(Wall(282, 242, 42, 2, gate_color))
		return self.gate_sprites

	def setupPlayers(self, hero_image_path, ghost_images_path):
		self.hero_sprites= pygame.sprite.Group()
		self.ghost_sprites= pygame.sprite.Group()
		self.hero_sprites.add(Player(287, 439, hero_image_path))
		for each in ghost_images_path:
			role_name== 'Blinky':
			player= Player(287, 199, each)
			player.is_move= True
			player.tracks= [[0, -0.5, 4], [0.5, 0, 9], [0, 0.5, 11], [0.5, 0, 3], [0, 0.5, 7], [-0.5, 0, 11], [0, 0.5, 3],
							[0.5, 0, 15], [0, -0.5, 15], [0.5, 0, 3], [0, -0.5, 11], [-0.5, 0, 3], [0, -0.5, 11], [-0.5, 0, 3],
							[0, -0.5, 3], [-0.5, 0, 7], [0, -0.5, 3], [0.5, 0, 15], [0, 0.5, 15], [-0.5, 0, 3], [0, 0.5, 3],
							[-0.5, 0, 3], [0, -0.5, 7], [-0.5, 0, 3], [0, 0.5,7], [-0.5, 0, 11], [0, -0.5, 7], [0.5, 0, 5]]
			self.ghost_sprites.add(player)
