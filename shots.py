from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS, PLAYER_SHOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.color = (255, 255, 255)  # White
        self.position = pygame.Vector2(x, y)
        self.velocity = velocity

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)