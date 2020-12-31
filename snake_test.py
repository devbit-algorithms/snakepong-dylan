from my_math import hsv2rgb, collidingWall
from snake import Snake

def test_collision():
    display = (100, 100)
    blockPos = (100, 50)
    blockSize = (10, 10)
    collision = collidingWall(blockPos, display, blockSize)
    assert collision = ((1, 0), 1)

test_collision()