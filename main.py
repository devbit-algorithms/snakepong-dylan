import pygame
from sllist import SingleLinkedList
import math
import time

def hsv2rgb(h, s, v):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = math.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return (r, g, b)

pygame.init()

display = (400, 400)
game = pygame.display.set_mode(display)

counter = 0

# block size
blockSize = 10

# pong ball
ballPos = (100, 150)
ballVel = (1.0, 1.5)

# snake velocity
snakeVelocity = (0, 0)

# (velocity), (position), (color)
snake = SingleLinkedList()

for x in range(20):
    snake.prepend(((0, 0), (100, 100), hsv2rgb(x*(255/10),1,1)))

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

def collidingWall(pos):
    position = pos
    if position[0] <= 0:
        return ((1, 0), 1)
    if position[0] >= display[0] - blockSize:
        return ((-1, 0), 1)
    if position[1] <= 0:
        return ((0, 1), 1)
    if position[1] >= display[1] - blockSize:
        return ((0, -1), 1)
    return ((0, 0), 0)

def collidingPixels(posA, posB):
    if (
        posA[0] < posB[0] + blockSize and
        posA[0] + blockSize > posB[0] and
        posA[1] < posB[1] + blockSize and
        posA[1] + blockSize > posB[1]):
        xInd = posB[0] - posA[0]
        yInd = posB[1] - posA[1]

        print("X: " + str(xInd) + ", Y: " + str(yInd))

        if (xInd < 0 and xInd < -abs(yInd)):
            return ((1, 0), 1)
        elif (xInd > 0 and xInd > abs(yInd)):
            return ((-1, 0), 1)
        elif (yInd < 0):
            return ((0, 1), 1)
        elif (yInd > 0):
            return ((0, -1), 1)

    return ((0, 0), 0)



def overlappingSnake(snake, position):
    overlapping = False
    if not snake.head() is None:
        collide = collidingPixels(snake.head()[1], position)
        if collide[1] == 1:
            return collide
        else:
            return overlappingSnake(snake.tail(), position)
    else:
        return ((0, 0), 0)

def reflect(vel, nor):
    if nor[0] == 0 and nor[1] == 0:
        return vel
    else:
        return (2*dot(vel,nor)*nor[0]-vel[0], 2*dot(vel,nor)*nor[1]-vel[1])

def dot(a, b):
    return a[0]*b[0]+a[1]*b[1]

def negVector(vec):
    return (-vec[0], -vec[1])

while (not gameEnded) and (collidingWall(snake.head()[1])[1] == 0):
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
            elif event.key == pygame.K_SPACE:
                addBody(snake, (0,0,255))

    if collidingWall(snake.head()[1])[1] != 0:
        gameEnded = True
        break

    if counter%10 == 0:
        step(snake, snakeVelocity)
    showSnake(snake)

    counter = counter+1

    collide = collidingWall(ballPos)
    if (collide[1] != 0):
        ballVel = reflect(negVector(ballVel), collide[0])

    collideSnake = overlappingSnake(snake, ballPos)
    if (collideSnake[1] != 0):
        ballVel = reflect(negVector(ballVel), collideSnake[0])
        
    ballPos = (ballPos[0] + ballVel[0], ballPos[1] + ballVel[1])
    pixel(ballPos, (255,0,0))
    
    pygame.display.update()
    pygame.draw.rect(game,(0,0,0),[0,0,display[0],display[1]])
    time.sleep(0.01)

pygame.quit()