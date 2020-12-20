import pygame
from sllist import LinkedList
import time

pygame.init()

display = (400, 400)
game = pygame.display.set_mode(display)

# initial position
blockPosX = 100
blockPosY = 100

# block size
blockSize = 20

# how fast and in what direction does the snake move
velocityX = 0
velocityY = 0

#snake = LinkedList()

gameEnded = False
while not gameEnded:
    for event in pygame.event.get():
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

    blockPosX += velocityX
    blockPosY += velocityY
    print(velocityX)
    print(velocityY)

    pygame.draw.rect(game,(255,255,255),[blockPosX, blockPosY, blockSize, blockSize])
    pygame.display.update()
    pygame.draw.rect(game,(0,0,0),[0,0,display[0],display[1]])
    time.sleep(0.5)

pygame.quit()