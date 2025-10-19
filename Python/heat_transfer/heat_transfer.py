from right_pad import pad_right
from matplotlib import pyplot
import random

def initMatrix(width: int, height: int):
    matrix: list[list[float]] = []
    for y in range(height):
        matrix.append([])
        for x in range(width):
            matrix[y].append(0)

    return matrix

def readMatrix(matrix: list[list[float]], padding: int):
    outString = ""

    # top column index
    string = pad_right("", padding + 2)
    for x in range(len(matrix[0])):
        string += pad_right(str(x), padding + 1)

    outString += string + "\n"

    # row index + values
    for y in range(len(matrix)):
        string = pad_right(str(y), padding) + "|"

        for x in range(len(matrix[y])):
            string += " " + pad_right("{:f}".format((matrix[y][x]))[:5], padding)

        outString += string + "\n"

    return outString

def spread(matrix: list[list[float]], spreadFactor: float):
    # spreadFactor is the % of the current cell's value given to adjacent cells

    # -2 to ignore border rows, +1 to start at index 1
    for y in range(len(matrix) - 2):
        for x in range(len(matrix[y]) - 2):
            value = matrix[y+1][x+1]
            # up
            matrix[y][x+1] += value * spreadFactor
            value -= value * spreadFactor
            # down
            matrix[y+2][x+1] += value * spreadFactor
            value -= value * spreadFactor            
            # left
            matrix[y+1][x] += value * spreadFactor
            value -= value * spreadFactor
            # right
            matrix[y+1][x+2] += value * spreadFactor
            value -= value * spreadFactor

            matrix[y+1][x+1] = value

    return matrix

def sumMatrix(matrix: list[list[float]]):
    sum = 0.0

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            sum += matrix[y][x]

    return sum

pyplot.ion()
width = 100
height = 100
matrix: list[list[float]] = initMatrix(width, height)

print(readMatrix(matrix, 5))
graph = pyplot.matshow(matrix, vmin=0, vmax=10)
input()

while True:
    if random.uniform(0, 1) < 0.1:
        matrix[random.randrange(height)][random.randrange(width)] = random.uniform(10, 1000)

    spread(matrix, 0.2)
    # print(readMatrix(spread(matrix, 0.01), 5))
    graph.remove()
    graph = pyplot.matshow(matrix, fignum=0, vmin=0, vmax=10)
    pyplot.pause(0.01)