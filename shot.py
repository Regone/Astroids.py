import pygame
import circleshape

class Shot(circleshape.CircleShape):
    containers = ()
    
    def __init__(self, x, y, radius):
        self.position = pygame.Vector2(x,y)
        self.rotation = 0
        self.radius = radius
        self.velocity = pygame.Vector2(x,y)
        super().__init__(self.position.x, self.position.y,self.radius)
        for cont in Shot.containers:
            cont.add(self)
            
    def draw(self, screen):
        pygame.draw.circle(screen,center=self.position,radius=self.radius,width=2,color="white")
    
    def update(self, dt):
        self.position += (self.velocity * dt)
        
    def rotate(self, targetRotation):
        self.rotation = targetRotation
        self.velocity = pygame.Vector2(0, 1).rotate(self.rotation)