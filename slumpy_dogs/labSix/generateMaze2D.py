import random

def randomMaze():
    length = random.randrange(15, 45+1, 2)
    maze = [[1 for i in range(length)] for j in range(length)]
    for i in range(length):
        for j in range(length):
                maze[i][j] = random.randint(0,1)
    return maze

def printMaze(maze):
    for line in maze:
        print(*line)