import pygame
from snake import Snake
from random import randrange
from my_math import collidingWall, collidingPixels, reflect, negVector, hsv2rgb
import time
import math

pygame.init()

display = (400, 400)
game = pygame.display.set_mode(display)

counter = 0

# block size
blockSize = 10

# pong ball
ballPos = (100, 150)
ballVel = (1.0, 1.5)

# snakeVelocity
snakeVelocity = (0, 0)

gameEnded = False

snake = Snake(20, blockSize, game, display)

while (not gameEnded) and (snake.collidingWall()[1] == 0):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameEnded = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snakeVelocity = (-1, 0)
                #ballPos = (ballPos[0]-1, ballPos[1])
            elif event.key == pygame.K_RIGHT:
                snakeVelocity = (1, 0)
                #ballPos = (ballPos[0]+1, ballPos[1])
            elif event.key == pygame.K_UP:
                snakeVelocity = (0, -1)
                #ballPos = (ballPos[0], ballPos[1]-1)
            elif event.key == pygame.K_DOWN:
                snakeVelocity = (0, 1)
                #ballPos = (ballPos[0], ballPos[1]+1)

    if snake.collidingWall()[1] != 0:
        gameEnded = True
        break

    if counter%10 == 0:
        snake.step(snake.sllist, snakeVelocity)
    snake.show(snake.sllist)

    counter = counter+1

    collide = collidingWall(ballPos, display, blockSize)
    if (collide[1] != 0):
        ballVel = reflect(negVector(ballVel), collide[0])

    collideSnake = snake.overlappingSnake(snake.sllist, ballPos)
    if (collideSnake[1] != 0):
        ballVel = reflect(negVector(ballVel), collideSnake[0])

    collidingFood = collidingPixels(snake.sllist.head()[1], snake.foodPos, blockSize)[1]
    if (collidingFood == 1):
        snake.addBody((255,255,255))
        snake.foodPos = (
            math.floor(randrange(display[0])/blockSize)*blockSize,
            math.floor(randrange(display[1])/blockSize)*blockSize)

    pygame.draw.rect(game,(255,255,255),[snake.foodPos[0], snake.foodPos[1], blockSize, blockSize])
        
    ballPos = (ballPos[0] + ballVel[0], ballPos[1] + ballVel[1])
    pygame.draw.rect(game,(255,0,0),[ballPos[0], ballPos[1], blockSize, blockSize])
    
    pygame.display.update()
    pygame.draw.rect(game,(0,0,0),[0,0,display[0],display[1]])
    time.sleep(0.01)

pygame.quit()