from locale import normalize
from math import fabs
from operator import truediv
import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def collisionCheck(self, cs, screen):
        distance = self.position.distance_to(cs.position)
        r1 = cs.radius
        r2 = self.radius
        return distance<=r1+r2