import pygame
from sllist import SingleLinkedList
import time

pygame.init()

display = (400, 400)
game = pygame.display.set_mode(display)

# block size
blockSize = 10

velocityX = 0
velocityY = 0

# (velocity), (position), (color)
snake = SingleLinkedList()
snake.prepend(((0, 0), (100, 100), (255,255,255)))
snake.prepend(((0, 0), (100, 100),  (0,255,255)))
snake.prepend(((0, 0), (100, 100),  (255,0,255)))
snake.prepend(((0, 0), (100, 100),  (255,255,0)))
snake.prepend(((0, 0), (100, 100),  (255,0,0)))
snake.prepend(((0, 0), (100, 100),  (0,255,0)))
snake.prepend(((0, 0), (100, 100),  (0,0,255)))

snake.printToConsole()

gameEnded = False

def showSnake(snake):
    if snake.head() is not None:
        pixel(snake.head()[1], snake.head()[2])
        showSnake(snake.tail())

def step(snake, direction):
    if not snake.head() is None:
        vel = snake.head()[0]
        snake.update((
            direction,
            (snake.head()[1][0]+vel[0]*blockSize, snake.head()[1][1]+vel[1]*blockSize),
            snake.head()[2]
        ))
        snake = snake.tail()
        step(snake, vel)

def addBody(snake, color):
    snake.prepend((
        (snake.head()[0][0], snake.head()[0][1]), 
        (snake.head()[1][0] + snake.head()[0][0]*blockSize,snake.head()[1][1] + snake.head()[0][1]*blockSize), 
        color))

def pixel(pos, color):
    pygame.draw.rect(game,color,[pos[0], pos[1], blockSize, blockSize])

def collidingWall(snake):
    position = snake.head()[1]
    return position[0] <= 0 or position[0] >= display[0] - 1 or position[1] <= 0 or position[1] >= display[1] - 1

while (not gameEnded) and (not collidingWall(snake)):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameEnded = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocityX = -1
                velocityY = 0
            elif event.key == pygame.K_RIGHT:
                velocityX = 1
                velocityY = 0
            elif event.key == pygame.K_UP:
                velocityY = -1
                velocityX = 0
            elif event.key == pygame.K_DOWN:
                velocityY = 1
                velocityX = 0
            elif event.key == pygame.K_SPACE:
                addBody(snake, (0,0,255))

    if collidingWall(snake):
        gameEnded = True
        break

    step(snake, (velocityX, velocityY))

    showSnake(snake)
    pygame.display.update()
    pygame.draw.rect(game,(0,0,0),[0,0,display[0],display[1]])
    time.sleep(0.1)

pygame.quit()