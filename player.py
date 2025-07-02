import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.color = (255, 255, 255)  # White
        rotation = 0
        self.rotation = rotation

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()

        dt_seconds = dt / 1000  # convert milliseconds to seconds

        # Rotation
        if keys[pygame.K_a]:
            self.rotate(-dt_seconds)
        if keys[pygame.K_d]:
            self.rotate(dt_seconds)

        # Movement
        if keys[pygame.K_w]:
            self.move(dt_seconds)
        if keys[pygame.K_s]:
            self.move(-dt_seconds)
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    pygame.draw.polygon
    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, self.color, points,2)
