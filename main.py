# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, constants
from constants import *
from player import Player

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    print(f'why this no work?  {SCREEN_HEIGHT}, {PLAYER_RADIUS}')
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
        screen.fill(BLACK)
        player.draw(screen)
        pygame.display.flip()
        # divide return of time since last tick by 1000ms to get delta time
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
