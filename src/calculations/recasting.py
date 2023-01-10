import math

def recasting_coordinates(x, y, z):
    delta_base = math.atan(y/x)
    x = math.sqrt(pow(x, 2) + pow(y, 2))
    y = z

    return x, y, delta_base