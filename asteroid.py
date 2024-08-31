import pygame
import circleshape
from constants import *
import random

class Asteroid(circleshape.CircleShape):
    containers = ()

    def __init__(self, x, y, radius):
        self.position = pygame.Vector2(x,y)
        self.rotation = 0
        self.radius = radius
        self.velocity = pygame.Vector2(x,y)
        super().__init__(self.position.x, self.position.y,self.radius)
        for cont in Asteroid.containers:
            cont.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen,center=self.position,radius=self.radius,width=2,color="white")
    
    def update(self, dt):
        self.position += (self.velocity * dt)
        
    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        angle = random.uniform(20,50)
        a = Asteroid(self.position.x,self.position.y,self.radius-ASTEROID_MIN_RADIUS)
        a.velocity= self.velocity.rotate(angle) *1.2
        a = Asteroid(self.position.x,self.position.y,self.radius-ASTEROID_MIN_RADIUS)
        a.velocity= self.velocity.rotate(-angle) *1.2
        