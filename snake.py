from sllist import SingleLinkedList
from random import randrange
from my_math import hsv2rgb, collidingPixels
import pygame
import math

class Snake:
    def __init__(self, initialLength, blockSize, game, display):
        self.sllist = SingleLinkedList()
        self.snakeVelocity = (0, 0)
        self.blockSize = blockSize
        self.display = display
        self.game = game
        self.foodPos = (0, 0)

        for x in range(40):
            self.sllist.prepend(((0, 0), (100, 100), hsv2rgb(x*(255/20),1,1)))

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
            (self.sllist.head()[1][0] + self.sllist.head()[0][0]*blockSize,self.sllist.head()[1][1] + self.sllist.head()[0][1]*blockSize), 
            color))

    def collidingWall(self):
        if self.sllist.head()[1][0] <= 0:
            return ((1, 0), 1)
        if self.sllist.head()[1][0] >= self.display[0] - self.blockSize:
            return ((-1, 0), 1)
        if self.sllist.head()[1][1] <= 0:
            return ((0, 1), 1)
        if self.sllist.head()[1][1] >= self.display[1] - self.blockSize:
            return ((0, -1), 1)
        return ((0, 0), 0)

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