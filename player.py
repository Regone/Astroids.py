import pygame
import circleshape
from constants import *
import shot

# Base class for game objects
class Player(circleshape.CircleShape):
	containers = ()

	def __init__(self,x,y):
		self.position = pygame.Vector2(x,y)
		self.rotation = 0
		self.timer = 0
		super().__init__(self.position.x, self.position.y,PLAYER_RADIUS)
		for cont in Player.containers:
			cont.add(self)

	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]

	def draw(self, screen):
		super().draw(screen)
		pygame.draw.polygon(screen, "white", self.triangle(),width=2)

	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt

	def update(self, dt):
		self.timer -= dt
		keys = pygame.key.get_pressed()
		if keys[pygame.K_a]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-dt)
		if keys[pygame.K_SPACE]:
			self.shoot()

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def shoot(self):
		if(self.timer>0):
			return
		bullet = shot.Shot(self.position.x,self.position.y,SHOT_RADIUS)
		bullet.velocity = pygame.Vector2(0,1)
		bullet.rotate(self.rotation)
		bullet.velocity *= PLAYER_SHOOT_SPEED
		self.timer = PLAYER_SHOOT_COOLDOWN