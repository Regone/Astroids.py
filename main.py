# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
import os
from  constants import *
import player
import asteroid
import asteroidfield
import shot

def main():
	pygame.init()
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0

	updateable = pygame.sprite.Group()
	drawable =  pygame.sprite.Group()
	asteroids =  pygame.sprite.Group()
	shots = pygame.sprite.Group()

	player.Player.containers = (updateable,drawable)
	asteroid.Asteroid.containers = (asteroids,updateable,drawable)
	shot.Shot.containers = (shots,updateable,drawable)

 
	asteroidfield.AsteroidField.containers = (updateable)
	astroidsfield = asteroidfield.AsteroidField()
 
	p1 = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0, 0, 0))
		for obj in updateable:
			obj.update(dt)
		for obj in drawable:
			obj.draw(screen)
		for obj in asteroids:
			if(obj.collisionCheck(p1, screen)):
				print("Game over!")
				sys.exit()
			for bullet in shots:
				if(obj.collisionCheck(bullet, screen)):
					obj.split()
					bullet.kill()

		pygame.display.flip()
		dt=clock.tick(60)*0.001



if __name__ == "__main__":
    main()
