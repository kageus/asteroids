from circleshape import CircleShape
from constants import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        super().__init__(self.x, self.y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.move(dt)

    def move(self, dt):
        self.position += self.velocity * dt  