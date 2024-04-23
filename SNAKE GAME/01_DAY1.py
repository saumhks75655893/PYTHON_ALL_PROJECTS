# SNAKE GAME
import pygame
from pygame.locals import *
import os


class Game:
    def __init__(self):
        # initialize the pygame module
        pygame.init()

        self.w = 1300
        self.h = 670
        self.surface = pygame.display.set_mode((self.w,self.h))

        self.snake = snake(self.surface)
        self.snake.draw()

    def run(self):

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False


class snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.img_blc = pygame.image.load("resources/block.jpg")
        self.img_blc.convert()
        self.x = 100
        self.y = 100

    def draw(self):
        self.parent_screen.fill((110, 247, 110))
        self.parent_screen.blit(self.img_blc, (self.x, self.y))
        pygame.display.flip()

    def move_up(self):
        self.y = self.y - 10
        self.draw()

    def move_down(self):
        self.y = self.y + 10
        self.draw()

    def move_left(self):
        self.x = self.x - 10
        self.draw()

    def move_right(self):
        self.x = self.x + 10
        self.draw()


if __name__ == "__main__":

    game = Game()
    game.run()
