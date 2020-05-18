import os
import sys
import pygame
import Levels



BLACK= (0, 0, 0)
WHITE= (255, 255, 255)
BLUE= (0, 0, 255)
GREEN= (0, 255, 0)
RED= (255, 0, 0)
YELLOW= (255, 255, 0)
PURPLE= (255, 0, 255)
SKYBLUE= (0, 191, 255)
BGMPATH= os.path.join(od.getcwd(), '../resources/sounds/bg.mp3')
ICONPATH = os.path.join(os.getcwd(), '../resources/images/icon.png')
FONTPATH = os.path.join(os.getcwd(), '../resources/font/ALGER.TTF')
HEROPATH = os.path.join(os.getcwd(), '../resources/images/pacman.png')
BlinkyPATH = os.path.join(os.getcwd(), '../resources/images/Blinky.png')
ClydePATH = os.path.join(os.getcwd(), '../resources/images/Clyde.png')
InkyPATH = os.path.join(os.getcwd(), '../resources/images/Inky.png')
PinkyPATH = os.path.join(os.getcwd(), '../resources/images/Pinky.png')


def startLevelGame(level, screen, font):
	clock= pygame.time.Clock()
	SCORE= 0
	wall_sprites= level.setupWalls(SKYBLUE)
	gate_sprites= level.setupGate(WHITE)
	hero_sprites, ghost_sprites= level.setupPlayers(HEROPATH, [BlinkyPATH, ClydePATH, InkyPATH, PinkyPATH])
	food_sprites= level.setupFood(YELLOW, WHITE)
	is_clearance= False
	while True:
# Controls Set UP
		for event in pygame.event.get():
			if event.type== pygame.QUIT:
				sys.exit(-1)
				pygame.quit()
			if event.type== pygame.KEYDOWN:
				if event.key== pygame.K_LEFT:
					for hero in hero_sprites:
						hero.changeSpeed([-1, 0])
						hero.is_move= True
				elif event.key== pygame.K_RIGHT:
					for hero in hero_sprites:
						hero.changeSpeed([1, 0])
						hero.is_move= True
				elif event.key== pygame.K_UP:
					for hwero in hero_sprites:
						hero.changeSpeed([0, -1])
						hero.is_move= True
				elif event.key== pygame.K_DOWN:
					for hero in hero_sprites:
						hero.changeSpeed([0, 1])
						hero.is_move= True
			if event.type== pygame.KEYUP:
				if (event.key== pygame.K_LEFT) or (event.key== pygame.K_RIGHT) or (event.key== pygame.K_UP) or (event.key== pygame.K_DOWN):
					hero.is_move= False
		screen.fill(BLACK)
		for hero in hero_sprites:
			hero.update(wall_sprites, gate_sprites)
		hero_sprites.draw(screen)
		for hero in hero_sprites:
			food_eaten= pygame.sprite.spritecollide(hero, food_sprites, True)
		SCORE+= len(food+_eaten)
		wall_sprites.draw(screen)
		gate_sprites.draw(screen)
		food_sprites.draw(screen)
		for ghost in ghost_sprites:

			'''
			res= ghost.update(wall_sprites, None)
			while not res:
				ghost.changeSpeed(ghost.randomDirection())
				res= ghost.update(wall_sprites, None)
			'''

			if ghost.tracks_loc[1]< ghost.tracks[ghost.tracks_loc[0]][2]:
				ghost.changeSpeed(ghost.tracks[ghost.tracks_loc[0]][0: 2])
				ghost.tracks_loc[1]+= 1
			else:
				if ghost.tracks_loc
