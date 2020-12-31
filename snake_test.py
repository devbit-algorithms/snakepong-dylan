from my_math import hsv2rgb, collidingWall
from sllist import SingleLinkedList
from snake import Snake

# if the block is overlapping the wall
def test_collision_wall_A():
    blockSize = 10
    display = (100, 100)
    blockPos = (100, 50)
    collision = collidingWall(blockPos, display, blockSize)
    assert collision == ((-1, 0), 1)

# if the block is right next to the wall but not overlapping
def test_collision_wall_B():
    blockSize = 15
    display = (100, 100)
    blockPos = (100-blockSize, 50)
    collision = collidingWall(blockPos, display, blockSize)
    assert collision == ((0, 0), 0)

def test_collision_snake_A():
    snake = Snake(2, (100, 100), 10, None, None)
    collision = snake.overlappingSnake(snake.sllist, (100, 90))
    assert collision == ((0, 0), 0)

def test_collision_snake_B():
    snake = Snake(2, (100, 100), 10, None, None)
    collision = snake.overlappingSnake(snake.sllist, (100, 91))
    assert collision == ((0, 1), 1)

def test_collision_snake_C():
    snake = Snake(2, (100, 100), 10, None, None)
    collision = snake.overlappingSnake(snake.sllist, (100, 109))
    assert collision == ((0, -1), 1)

