# SNAKE GAME

import pygame
from pygame.locals import *
import os


def game():
    pass


if __name__ == "__main__":
    # initialize the pygame module
    pygame.init()

    # initialize the pygame display module
    pygame.display.init()

    surface = pygame.display.set_mode((1200, 650))
    surface.fill((110, 247, 110))
    pygame.display.flip()

    # for the block
    block = pygame.image.load("block.jpg").convert()
    surface.blit(block, (0, 0))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
