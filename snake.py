from sllist import SingleLinkedList
from my_math import hsv2rgb, collidingPixels, collidingWall
import pygame
import math

class Snake:
    def __init__(self, initialLength, iniPosition, blockSize, game, display):
        self.sllist = SingleLinkedList()
        self.snakeVelocity = (0, 0)
        self.blockSize = blockSize
        self.display = display
        self.game = game

        if display is not None:
            self.foodPos = (display[0]/2, display[1]/2)

        for x in range(initialLength):
            self.sllist.prepend(((0, 0), iniPosition, hsv2rgb(x*(360/initialLength),1,1)))

    def show(self, sllist):
        if sllist.head() is not None:
            pygame.draw.rect(self.game,sllist.head()[2],[sllist.head()[1][0], sllist.head()[1][1], self.blockSize, self.blockSize])
            self.show(sllist.tail())

    def step(self, snake, direction):
        if not snake.head() is None:
            vel = snake.head()[0]
            snake.update((
                direction,
                (snake.head()[1][0] + vel[0]*self.blockSize, snake.head()[1][1] + vel[1]*self.blockSize),
                snake.head()[2]
            ))
            snake = snake.tail()
            self.step(snake, vel)

    def addBody(self, color):
        self.sllist.prepend((
            (self.sllist.head()[0][0], self.sllist.head()[0][1]), 
            (
                self.sllist.head()[1][0] + self.sllist.head()[0][0]*self.blockSize,
                self.sllist.head()[1][1] + self.sllist.head()[0][1]*self.blockSize), 
                color
            )
        )

    def overlappingWall(self):
        return collidingWall(self.sllist.head()[1], self.display, self.blockSize)

    def overlappingSnake(self, sllist, position):
        overlapping = False
        if not sllist.head() is None:
            collide = collidingPixels(sllist.head()[1], position, self.blockSize)
            if collide[1] == 1:
                return collide
            else:
                return self.overlappingSnake(sllist.tail(), position)
        else:
            return ((0, 0), 0)