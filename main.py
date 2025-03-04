# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import the connect_database function
# and the database_version variable
# from database.py into the current file
#from database import connect_database, database_version

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
    pygame.init()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            clock.tick(60)
            dt = clock.tick(60) / 1000
            screen.fill((0, 0, 0))
            player.update(dt)
            player.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()