import pygame
from constants import *
from player import Player
from turtledemo.penrose import draw

def main():
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)



    while True:
        updatable.update(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()


        dt = clock.tick(60) / 1000
        # print(f"Frame Timing, {dt}s.")




if __name__ == "__main__":
    main()
