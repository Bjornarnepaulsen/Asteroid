import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOT_SPEED, PLAYER_SHOT_COOLDOWN
from shots import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.color = (255, 255, 255)  # White
        rotation = 0
        self.rotation = rotation
        timer = 0.0
        self.timer = timer

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED

    def shoot(self, position):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        velocity = forward * PLAYER_SHOT_SPEED
        shot = Shot(self.position.x, self.position.y, velocity)
        return shot


    def update(self, dt):
        

        if self.timer > 0:
            self.timer -= dt
        

        keys = pygame.key.get_pressed()

        dt_seconds = dt # convert milliseconds to seconds

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
        
        # Shooting
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot(self.position)
            self.timer = PLAYER_SHOT_COOLDOWN
            
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    pygame.draw.polygon
    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, self.color, points,2)
