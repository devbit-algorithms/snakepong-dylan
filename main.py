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

snake = SingleLinkedList()
snake.prepend(((0, 0), (100, 100), (255,255,255)))

snake.printToConsole()

gameEnded = False

def showSnake(snake):
    if snake.head() is not None:
        pygame.draw.rect(game,snake.head()[2],[snake.head()[1][0], snake.head()[1][1], blockSize, blockSize])
        showSnake(snake.tail())

while not gameEnded:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameEnded = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocityX = -blockSize
                velocityY = 0
            elif event.key == pygame.K_RIGHT:
                velocityX = blockSize
                velocityY = 0
            elif event.key == pygame.K_UP:
                velocityY = -blockSize
                velocityX = 0
            elif event.key == pygame.K_DOWN:
                velocityY = blockSize
                velocityX = 0

    update = (
        (velocityX, velocityY),
        (snake.head()[1][0] + snake.head()[0][0], snake.head()[1][1] + snake.head()[0][1]),
        (255, 255, 255))

    snake.update(update)

    showSnake(snake)
    pygame.display.update()
    pygame.draw.rect(game,(0,0,0),[0,0,display[0],display[1]])
    time.sleep(0.3)

pygame.quit()