from pixboard import *
from math import sqrt


def plot(func, min_x=-10, min_y=-10, max_x=10, max_y=10, scale=20):
    width = (abs(min_x) + abs(max_x)) * scale
    height = (abs(max_y) + abs(min_y)) * scale
    setup(width, height)
    kesk_x = ((abs(min_x) - abs(max_x)) * scale + width) / 2
    kesk_y = ((abs(max_y) - abs(min_y)) * scale + height) / 2

    for e in range(width):
        for i in range(height):
            see = func.replace('x', '(' + str((e - kesk_x) / scale) + ')').replace('y', '(' + str(
                (i - kesk_y) / (-scale)) + ')')
            if eval(see):
                set_pixel(e, i, 'blue')

            if e == kesk_x or i == kesk_y:
                set_pixel(e, i, 'black')

    show()


def kahendsüsteemi(arv):
    n = '01'
    if int(arv) < 2:
        return n[int(arv)]
    else:
        return kahendsüsteemi(int(arv) // 2) + n[int(arv) % 2]


def kümnendsüsteemi(arv):
    vastus = 0
    for e in range(len(arv)):
        if arv[-1 - e] == '1':
            vastus += 2 ** e
    return vastus


def A(x, y):
    return y <= x ** 2 + 4 * x - 7

def B(x, y):
    return y > x ** 3 + sqrt(abs(x))

def C(x, y):
    return not A(x, y) and B(x, y)

def D(x, y):
    dist = sqrt((x + 2) ** 2 + y ** 2)
    return dist < 3 and dist > 2.5

def X(x, y):
    return abs(x) < 1 and abs(y) < 1
