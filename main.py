import pygame

pygame.init()

display = (400, 400)
game = pygame.display.set_mode(display)

while True:
    pygame.draw.rect(game,(255,255,255),[100,100,10,10])
    pygame.display.update()

pygame.quit()