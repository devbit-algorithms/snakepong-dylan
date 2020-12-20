import pygame

pygame.init()

display = (400, 400)
game = pygame.display.set_mode(display)

blockPosX = 100
blockPosY = 100

blockSize = 20

gameEnded = False
while not gameEnded:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    blockPosX += -blockSize
                elif event.key == pygame.K_RIGHT:
                    blockPosX += blockSize
                elif event.key == pygame.K_UP:
                    blockPosY += -blockSize
                elif event.key == pygame.K_DOWN:
                    blockPosY += blockSize
    pygame.draw.rect(game,(255,255,255),[blockPosX,blockPosY,blockSize,blockSize])
    pygame.display.update()

pygame.quit()