from random import random, randint


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


def rotCase(case,direction,nbRot):
    caseTemp = Case()
    if(direction):#clock-wise
        if (case.down == 1):
            if(nbRot == 1):
                caseTemp.left = 1
            if(nbRot == 2):
                caseTemp.up = 1
            if(nbRot == 3):
                caseTemp.right = 1
        if (case.up == 1):
            if (nbRot == 1):
                caseTemp.right = 1
            if (nbRot == 2):
                caseTemp.down = 1
            if (nbRot == 3):
                caseTemp.left = 1
        if (case.left == 1):
            if (nbRot == 1):
                caseTemp.up = 1
            if (nbRot == 2):
                caseTemp.right = 1
            if (nbRot == 3):
                caseTemp.down = 1
        if (case.right == 1):
            if (nbRot == 1):
                caseTemp.down = 1
            if (nbRot == 2):
                caseTemp.left = 1
            if (nbRot == 3):
                caseTemp.up = 1
    else:#anti-clock-wise
        if (case.down == 1):
            if (nbRot == 1):
                caseTemp.right = 1
            if (nbRot == 2):
                caseTemp.up = 1
            if (nbRot == 3):
                caseTemp.left = 1
        if (case.up == 1):
            if (nbRot == 1):
                caseTemp.left = 1
            if (nbRot == 2):
                caseTemp.down = 1
            if (nbRot == 3):
                caseTemp.right = 1
        if (case.left == 1):
            if (nbRot == 1):
                caseTemp.down = 1
            if (nbRot == 2):
                caseTemp.right = 1
            if (nbRot == 3):
                caseTemp.up = 1
        if (case.right == 1):
            if (nbRot == 1):
                caseTemp.up = 1
            if (nbRot == 2):
                caseTemp.left = 1
            if (nbRot == 3):
                caseTemp.down = 1
    return caseTemp


def rotation(panel,direction,nbRot):
    panelTemp = [[Case() for i in range(int(sizeOfPanel))] for j in range(int(sizeOfPanel))]
    for i in range(0,8):
        for j in range(0,8):
            if panel[i][j].up == 1 or panel[i][j].right == 1 or panel[i][j].left == 1 or panel[i][j].down == 1:
                if(direction):
                    if (nbRot == 1):
                        panelTemp[j][int(sizeOfPanel) - 1 - i] = rotCase(panel[i][j], direction, nbRot)
                    if (nbRot == 2):
                        panelTemp[int(sizeOfPanel)-1-i][int(sizeOfPanel)-1-j] = rotCase(panel[i][j], direction, nbRot)
                    if (nbRot == 3):
                        panelTemp[int(sizeOfPanel)-1-j][i] = rotCase(panel[i][j], direction, nbRot)
                else:
                    if (nbRot == 1):
                        panelTemp[int(sizeOfPanel) - 1 - j][i] = rotCase(panel[i][j], direction, nbRot)
                    if (nbRot == 2):
                        panelTemp[int(sizeOfPanel) - 1 - i][int(sizeOfPanel) - 1 - j] = rotCase(panel[i][j], direction, nbRot)
                    if (nbRot == 3):
                        panelTemp[j][int(sizeOfPanel) - 1 - i] = rotCase(panel[i][j], direction, nbRot)
    return panelTemp


def rotate(pos,panel,panelNb):
    if(pos == panelNb):
        return panel
    elif(pos >panelNb):
        return rotation(panel,1,pos-panelNb)
    else:
        return rotation(panel,0,panelNb-pos)


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
sizeOfPanel = sizeOfGrid/2

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
grid[int(sizeOfGrid/2)-1][int(sizeOfGrid/2)-1].up = 1
grid[int(sizeOfGrid/2)-1][int(sizeOfGrid/2)-1].left = 1
grid[int(sizeOfGrid/2)-1][int(sizeOfGrid/2)].up = 1
grid[int(sizeOfGrid/2)-1][int(sizeOfGrid/2)].right = 1
grid[int(sizeOfGrid/2)][int(sizeOfGrid/2)-1].down = 1
grid[int(sizeOfGrid/2)][int(sizeOfGrid/2)-1].left = 1
grid[int(sizeOfGrid/2)][int(sizeOfGrid/2)].down = 1
grid[int(sizeOfGrid/2)][int(sizeOfGrid/2)].right = 1

print("Initialising the 4 panels\n ")
#init all 4 panels with their walls
panel1 = [[Case() for i in range(int(sizeOfPanel))] for j in range(int(sizeOfPanel))]
panel2 = [[Case() for i in range(int(sizeOfPanel))] for j in range(int(sizeOfPanel))]
panel3 = [[Case() for i in range(int(sizeOfPanel))] for j in range(int(sizeOfPanel))]
panel4 = [[Case() for i in range(int(sizeOfPanel))] for j in range(int(sizeOfPanel))]

#init panel4's walls
panel4[6][3].down = 1
panel4[6][3].right = 1
panel4[7][4].right = 1
panel4[2][0].down = 1
panel4[1][3].right = 1
panel4[1][4].down = 1
panel4[4][1].down = 1
panel4[5][1].right = 1
panel4[1][6].down = 1
panel4[2][6].left = 1
panel4[7][5].left = 1
panel4[3][7].down = 1
panel4[4][7].right = 1

#init panel3's walls
panel3[3][1].right = 1
panel3[3][1].down = 1
panel3[1][5].down = 1
panel3[1][5].left = 1
panel3[3][7].down = 1
panel3[5][6].right = 1
panel3[5][6].up = 1
panel3[6][2].up = 1
panel3[6][2].left = 1
panel3[7][3].right = 1

#init panel2's walls
panel2[0][1].right = 1
panel2[1][5].right = 1
panel2[1][5].down = 1
panel2[1][7].down = 1
panel2[3][1].up = 1
panel2[3][1].left = 1
panel2[4][6].right = 1
panel2[4][6].up = 1
panel2[6][4].down = 1
panel2[6][4].left = 1

#init panel1's walls
panel1[0][3].right = 1
panel1[2][5].right = 1
panel1[2][5].down = 1
panel1[4][2].right = 1
panel1[4][2].up = 1
panel1[5][7].left = 1
panel1[5][7].down = 1
panel1[4][0].down = 1
panel1[6][1].up = 1
panel1[6][1].left = 1

#randomly place the panels on the grid
gridPosPanels = [0,0,0,0] #stores the panels in the right placement order
gridNbPanels = [0,0,0,0] #stores what panels are placed where
gridPanels = [panel1,panel2,panel3,panel4]
randomP1 = random()
randomP2 = random()
randomP3 = random()
randomP4 = random()
listPanelNumbers = [randomP1, randomP2, randomP3, randomP4]
listRandom = [randomP1, randomP2, randomP3, randomP4]
listRandom.sort()
for i in range(0,4):
    for j in range(0,4):
        if listPanelNumbers[j] == listRandom[i]:
            gridPosPanels[i] = gridPanels[j]
            gridNbPanels[i] = j
            print(j)

#generate walls according to the random layout
for i in range(int(sizeOfPanel)):
    print()
    for j in range(int(sizeOfPanel)):
        print(gridPosPanels[1][i][j].down,end ='')
for i in range(0,4):
    gridPosPanels[i] = rotate(i,gridPosPanels[i],gridNbPanels[i])


print("\n")


# TODO: Insert walls


# Verifications

# up - down - left - right
for i in range(int(sizeOfPanel)):
    print()
    for j in range(int(sizeOfPanel)):
        print(gridPosPanels[1][i][j].down,end ='')
 

# isup - isdown - isleft - isright
print("\n\nisWall?")
print(isright(sizeOfGrid-1,sizeOfGrid-1,grid))

