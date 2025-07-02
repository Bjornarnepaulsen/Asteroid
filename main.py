# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shots import Shot


#Main loop
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    Player.timer = 0.0
    font = pygame.font.SysFont(None, 36)
    pygame.display.set_caption("Asteroid Game")

    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    shots = pygame.sprite.Group()  # instead of a list
    score = 0
    spawn_rate = ASTEROID_SPAWN_RATE

    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        dt = clock.tick(60) / 1000.0 # Limit to 60 FPS
        if score >= 10:
            spawn_rate += 0.2
            print(f"Spawn rate increased to {spawn_rate:.2f} seconds")
        if score >= 20:
            spawn_rate += 0.2
            print(f"Spawn rate increased to {spawn_rate:.2f} seconds")
        if score >= 30:
            spawn_rate += 0.2
            print(f"Spawn rate increased to {spawn_rate:.2f} seconds")
        else:
            spawn_rate = ASTEROID_SPAWN_RATE
        screen.fill((0, 0, 0))
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                pygame.quit()
                return
        for asteroid in asteroids:
            for sprite in drawable:
                if isinstance(sprite, Shot):
                    if sprite.collides_with(asteroid):
                        asteroid.split()
                        sprite.kill()
                        score += 1
                        print(f"Score: {score}")
        for sprite in drawable:
            sprite.draw(screen)

            score_text = font.render(f"Score: {score}", True, (255, 255, 255))
            screen.blit(score_text, (10, 10))
        pygame.display.flip()
    

   


if __name__ == "__main__":
    main()