import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return "This was a small asteroid!"
        # Split into two smaller asteroids
        new_radius = self.radius / 2
        random_angle = random.uniform(20,50)
        new_velocity = self.velocity * 1.2
        rotated_velocity = new_velocity.rotate(random_angle)
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = rotated_velocity
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = rotated_velocity.rotate(-random_angle)
        return [asteroid1, asteroid2]

        