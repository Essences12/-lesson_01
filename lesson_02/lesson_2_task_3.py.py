import math


def square(side):
    return math.ceil(side * side)


side = 5
print(f"Площадь квадрата со стороной {side}: {square(side)}")