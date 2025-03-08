import pygame
import circleshape

# import the connect_database function
# and the database_version variable
# from database.py into the current file
#from database import connect_database, database_version

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            updatable.update(dt)

            for asteroid in asteroids:
                if asteroid.check_collision(player):
                    print("Game over!")
                    return

                for shot in shots:
                    if shot.check_collision(asteroid):
                        shot.kill()
                        asteroid.split()

            screen.fill("black")

            for item in drawable:
                item.draw(screen)

            pygame.display.flip()

            dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()