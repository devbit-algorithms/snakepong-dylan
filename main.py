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

snake = Snake(20, (100, 100), blockSize, game, display)

while (not gameEnded) and (snake.overlappingWall()[1] == 0):

    # handle events using the build in event handling in pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameEnded = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snakeVelocity = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                snakeVelocity = (1, 0)
            elif event.key == pygame.K_UP:
                snakeVelocity = (0, -1)
            elif event.key == pygame.K_DOWN:
                snakeVelocity = (0, 1)

    # stop game if snake is colliding with wall
    if snake.overlappingWall()[1] != 0:
        gameEnded = True
        break

    # step snake game every 10 loopcounts
    if counter%10 == 0:
        snake.step(snake.sllist, snakeVelocity)
    snake.show(snake.sllist)
    counter = counter+1

    # if the ball collides with the wall, then calculate the
    # reflection vector using the normal of the wall and ball belocity,
    # then assign the reflection vector to the velocity of the ball
    collide = collidingWall(ballPos, display, blockSize)
    if (collide[1] != 0):
        ballVel = reflect(negVector(ballVel), collide[0])

    # the same, but with the snake instead of the wall
    collideSnake = snake.overlappingSnake(snake.sllist, ballPos)
    if (collideSnake[1] != 0):
        ballVel = reflect(negVector(ballVel), collideSnake[0])

    # if the head of the snake is colliding with the food, then add a body to the snake,
    # also assign a new random position to the food
    collidingFood = collidingPixels(snake.sllist.head()[1], snake.foodPos, blockSize)[1]
    if (collidingFood == 1):
        snake.addBody((255,255,255))
        snake.foodPos = (
            math.floor(randrange(display[0])/blockSize)*blockSize,
            math.floor(randrange(display[1])/blockSize)*blockSize)

    # draw the food
    pygame.draw.rect(game,(255,255,255),[snake.foodPos[0], snake.foodPos[1], blockSize, blockSize])
        
    # draw the ball
    ballPos = (ballPos[0] + ballVel[0], ballPos[1] + ballVel[1])
    pygame.draw.rect(game,(255,0,0),[ballPos[0], ballPos[1], blockSize, blockSize])
    
    # update display
    pygame.display.update()
    pygame.draw.rect(game,(0,0,0),[0,0,display[0],display[1]])
    time.sleep(0.01)

pygame.quit()