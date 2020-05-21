class Case:
    right = 0
    down = 0
    left = 0
    up = 0
    pawn = -1

    def __init__(self):
        self.right = 0
        self.down = 0
        self.left = 0
        self.up = 0


# TODO: Check if it is working
def isleft(i, j, gridparam):
    if gridparam[i][j].left == 1:
        return 1
    elif j - 1 >= 0:
        if gridparam[i][j - 1].right == 1:
            return 1
    return 0


def isright(i, j, gridparam):
    if gridparam[i][j].right == 1:
        return 1
    elif j + 1 < sizeOfGrid:
        if gridparam[i][j + 1].left == 1:
            return 1
    return 0


def isup(i, j, gridparam):
    if gridparam[i][j].up == 1:
        return 1
    elif i - 1 >= 0:
        if gridparam[i - 1][j].down == 1:
            return 1
    return 0


def isdown(i, j, gridparam):
    if gridparam[i][j].down == 1:
        return 1
    elif i + 1 < sizeOfGrid:
        if gridparam[i - 1][j].up == 1:
            return 1
    return 0


print("PROJECT INITIALIZATION\n")
sizeOfGrid = 16

# init grid with initial border
grid = [[Case() for i in range(sizeOfGrid)] for j in range(sizeOfGrid)]
for i in range(sizeOfGrid):
    for j in range(sizeOfGrid):
        case = Case()
        if i == 0:
            case.up = 1
        if i == sizeOfGrid - 1:
            case.down = 1
        if j == 0:
            case.left = 1
        if j == sizeOfGrid - 1:
            case.right = 1
        grid[i][j] = case

print("\n")
print("Checking sizeOfGrid:")
print(len(grid))

# TODO: Insert walls

'''
# Verifications

# up - down - left - right
for i in range(sizeOfGrid):
    print()
    for j in range(sizeOfGrid):
        print(grid[i][j].right,end ='')
 

# isup - isdown - isleft - isright
print("\n\nisWall?")
print(isright(sizeOfGrid-1,sizeOfGrid-1,grid))
'''
