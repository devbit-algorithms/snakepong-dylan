import math

# https://code.activestate.com/recipes/576919-python-rgb-and-hsv-conversion/
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

# https://www.fabrizioduroni.it/2017/08/25/how-to-calculate-reflection-vector.html
def reflect(vel, nor):
    if nor[0] == 0 and nor[1] == 0:
        return vel
    else:
        return (2*dot(vel,nor)*nor[0]-vel[0], 2*dot(vel,nor)*nor[1]-vel[1])

def dot(a, b):
    return a[0]*b[0]+a[1]*b[1]

def negVector(vec):
    return (-vec[0], -vec[1])

def collidingWall(pos, display, blockSize):
    if pos[0] < 0:
        return ((1, 0), 1)
    if pos[0] > display[0] - blockSize:
        return ((-1, 0), 1)
    if pos[1] < 0:
        return ((0, 1), 1)
    if pos[1] > display[1] - blockSize:
        return ((0, -1), 1)
    return ((0, 0), 0)

def collidingPixels(posA, posB, blockSize):
    if (posA[0] < posB[0] + blockSize and
        posA[0] + blockSize > posB[0] and
        posA[1] < posB[1] + blockSize and
        posA[1] + blockSize > posB[1]):
        xInd = posB[0] - posA[0]
        yInd = posB[1] - posA[1]

        if (xInd < 0 and xInd < -abs(yInd)):
            return ((1, 0), 1)
        if (xInd > 0 and xInd > abs(yInd)):
            return ((-1, 0), 1)
        if (yInd < 0):
            return ((0, 1), 1)
        if (yInd > 0):
            return ((0, -1), 1)
        return ((0, 0), 1)

    return ((0, 0), 0)