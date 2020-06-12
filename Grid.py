import globals
from Case import Case
from Panel import Panel
from Visual import Visual

from random import random, randint
import copy


class Grid:
    tabCase = 0
    panel1 = 0
    panel2 = 0
    panel3 = 0
    panel4 = 0

    def __init__(self, tabCaseArg):
        self.tabCase = copy.deepcopy(tabCaseArg)
        self.initPanels()
        self.placePanelRandom()
        self.addMiddleWalls()
        self.placePawnsRandom()

    def placePanelWalls(self, panel, pos):  # places the panel's walls on the grid, taking in account its position
        for i in range(0, 8):
            for j in range(0, 8):
                if panel.tabCase[i][j].up == 1 or panel.tabCase[i][j].right == 1 or panel.tabCase[i][j].left == 1 or \
                        panel.tabCase[i][j].down == 1:
                    if pos == 0:
                        self.tabCase[i][j] = panel.tabCase[i][j]
                    elif pos == 1:
                        self.tabCase[i][j + 8] = panel.tabCase[i][j]
                    elif pos == 2:
                        self.tabCase[i + 8][j] = panel.tabCase[i][j]
                    else:
                        self.tabCase[i + 8][j + 8] = panel.tabCase[i][j]
        return self.tabCase

    def placePanelRandom(self):
        # randomly place the panels on the grid
        gridPosPanels = [0, 0, 0, 0]  # stores the panels in the right placement order
        gridNbPanels = [0, 0, 0, 0]  # stores what panels are placed where
        gridPanels = [self.panel1, self.panel2, self.panel3, self.panel4]
        randomP1 = random()
        randomP2 = random()
        randomP3 = random()
        randomP4 = random()
        listPanelNumbers = [randomP1, randomP2, randomP3, randomP4]
        listRandom = [randomP1, randomP2, randomP3, randomP4]
        listRandom.sort()

        for i in range(0, 4):
            for j in range(0, 4):
                if listPanelNumbers[j] == listRandom[i]:
                    gridPosPanels[i] = gridPanels[j]
                    gridNbPanels[i] = j

        # generate walls according to the random layout on each panel
        for i in range(4):
            #print(gridNbPanels[i])
            gridPosPanels[i] = gridPosPanels[i].rotate(i, gridNbPanels[i])

        # PLacing every wall on the final grid
        self.panel1 = self.placePanelWalls(gridPosPanels[0], 0)
        self.panel2 = self.placePanelWalls(gridPosPanels[1], 1)
        self.panel3 = self.placePanelWalls(gridPosPanels[2], 3)
        self.panel4 = self.placePanelWalls(gridPosPanels[3], 2)

    # adding the central and the border walls
    def addMiddleWalls(self):

        self.tabCase[int(globals.sizeOfGrid / 2) - 1][int(globals.sizeOfGrid / 2) - 1].up = 1
        self.tabCase[int(globals.sizeOfGrid / 2) - 1][int(globals.sizeOfGrid / 2) - 1].down = 1
        self.tabCase[int(globals.sizeOfGrid / 2) - 1][int(globals.sizeOfGrid / 2) - 1].left = 1
        self.tabCase[int(globals.sizeOfGrid / 2) - 1][int(globals.sizeOfGrid / 2) - 1].right = 1

        self.tabCase[int(globals.sizeOfGrid / 2) - 1][int(globals.sizeOfGrid / 2)].up = 1
        self.tabCase[int(globals.sizeOfGrid / 2) - 1][int(globals.sizeOfGrid / 2)].down = 1
        self.tabCase[int(globals.sizeOfGrid / 2) - 1][int(globals.sizeOfGrid / 2)].left = 1
        self.tabCase[int(globals.sizeOfGrid / 2) - 1][int(globals.sizeOfGrid / 2)].right = 1

        self.tabCase[int(globals.sizeOfGrid / 2)][int(globals.sizeOfGrid / 2) - 1].up = 1
        self.tabCase[int(globals.sizeOfGrid / 2)][int(globals.sizeOfGrid / 2) - 1].down = 1
        self.tabCase[int(globals.sizeOfGrid / 2)][int(globals.sizeOfGrid / 2) - 1].left = 1
        self.tabCase[int(globals.sizeOfGrid / 2)][int(globals.sizeOfGrid / 2) - 1].right = 1

        self.tabCase[int(globals.sizeOfGrid / 2)][int(globals.sizeOfGrid / 2)].up = 1
        self.tabCase[int(globals.sizeOfGrid / 2)][int(globals.sizeOfGrid / 2)].down = 1
        self.tabCase[int(globals.sizeOfGrid / 2)][int(globals.sizeOfGrid / 2)].left = 1
        self.tabCase[int(globals.sizeOfGrid / 2)][int(globals.sizeOfGrid / 2)].right = 1

        for i in range(globals.sizeOfGrid):
            for j in range(globals.sizeOfGrid):
                if i == 0:
                    self.tabCase[i][j].up = 1
                if i == globals.sizeOfGrid - 1:
                    self.tabCase[i][j].down = 1
                if j == 0:
                    self.tabCase[i][j].left = 1
                if j == globals.sizeOfGrid - 1:
                    self.tabCase[i][j].right = 1

    def placePawnsRandom(self):
        # placing the pawns randomly on the grid
        for i in range(0, 4):
            isPlaced = False
            while not isPlaced:
                randomNumber = randint(0, 15)
                randomNumber2 = randint(0, 15)
                if self.tabCase[randomNumber][randomNumber2].target == 0 and not (
                        (randomNumber2 > 6 and randomNumber < 9) and (6 < randomNumber2 < 9)) and \
                        self.tabCase[randomNumber][randomNumber2].pawn == -1:
                    isPlaced = True
                    self.tabCase[randomNumber][randomNumber2].pawn = i

    def initPanels(self):
        print("Initialising the 4 panels\n ")
        # init all 4 panels with their walls
        self.panel1 = Panel(
            [[Case() for i in range(int(globals.sizeOfPanel))] for j in range(int(globals.sizeOfPanel))])
        self.panel2 = Panel(
            [[Case() for i in range(int(globals.sizeOfPanel))] for j in range(int(globals.sizeOfPanel))])
        self.panel3 = Panel(
            [[Case() for i in range(int(globals.sizeOfPanel))] for j in range(int(globals.sizeOfPanel))])
        self.panel4 = Panel(
            [[Case() for i in range(int(globals.sizeOfPanel))] for j in range(int(globals.sizeOfPanel))])

        # init panel4's walls
        self.panel4.tabCase[1][4].target = 9
        self.panel4.tabCase[2][6].target = 11
        self.panel4.tabCase[5][1].target = 13
        self.panel4.tabCase[6][3].target = 15
        self.panel4.tabCase[6][3].down = 1
        self.panel4.tabCase[6][3].right = 1
        self.panel4.tabCase[7][4].right = 1
        self.panel4.tabCase[2][0].down = 1
        self.panel4.tabCase[1][3].right = 1
        self.panel4.tabCase[1][4].down = 1
        self.panel4.tabCase[4][1].down = 1
        self.panel4.tabCase[5][1].right = 1
        self.panel4.tabCase[1][6].down = 1
        self.panel4.tabCase[2][6].left = 1
        self.panel4.tabCase[7][5].left = 1
        self.panel4.tabCase[3][7].down = 1
        self.panel4.tabCase[4][7].right = 1

        # init panel3's walls
        self.panel3.tabCase[1][5].target = 10
        self.panel3.tabCase[3][1].target = 12
        self.panel3.tabCase[5][6].target = 14
        self.panel3.tabCase[6][2].target = 16
        self.panel3.tabCase[3][1].right = 1
        self.panel3.tabCase[3][1].down = 1
        self.panel3.tabCase[1][5].down = 1
        self.panel3.tabCase[1][5].left = 1
        self.panel3.tabCase[3][7].down = 1
        self.panel3.tabCase[5][6].right = 1
        self.panel3.tabCase[5][6].up = 1
        self.panel3.tabCase[6][2].up = 1
        self.panel3.tabCase[6][2].left = 1
        self.panel3.tabCase[7][3].right = 1

        # init panel2's walls
        self.panel2.tabCase[1][5].target = 1
        self.panel2.tabCase[3][1].target = 3
        self.panel2.tabCase[4][6].target = 5
        self.panel2.tabCase[6][4].target = 8
        self.panel2.tabCase[0][1].right = 1
        self.panel2.tabCase[1][5].right = 1
        self.panel2.tabCase[1][5].down = 1
        self.panel2.tabCase[1][7].down = 1
        self.panel2.tabCase[3][1].up = 1
        self.panel2.tabCase[3][1].left = 1
        self.panel2.tabCase[4][6].right = 1
        self.panel2.tabCase[4][6].up = 1
        self.panel2.tabCase[6][4].down = 1
        self.panel2.tabCase[6][4].left = 1

        # init panel1's walls
        self.panel1.tabCase[2][5].target = 2
        self.panel1.tabCase[4][2].target = 4
        self.panel1.tabCase[5][7].target = 6
        self.panel1.tabCase[6][1].target = 7
        self.panel1.tabCase[0][3].right = 1
        self.panel1.tabCase[2][5].right = 1
        self.panel1.tabCase[2][5].down = 1
        self.panel1.tabCase[4][2].right = 1
        self.panel1.tabCase[4][2].up = 1
        self.panel1.tabCase[5][7].left = 1
        self.panel1.tabCase[5][7].down = 1
        self.panel1.tabCase[4][0].down = 1
        self.panel1.tabCase[6][1].up = 1
        self.panel1.tabCase[6][1].left = 1

        '''
        for i in range(int(globals.sizeOfPanel)):
            print()
            for j in range(int(globals.sizeOfPanel)):
                print(self.panel1[i][j].down, end='')
        '''

    def isLeft(self, i, j):
        if self.tabCase[i][j].left == 1:
            return 1
        elif j - 1 >= 0:
            if self.tabCase[i][j - 1].right == 1:
                return 1
            elif self.tabCase[i][j - 1].pawn != -1:
                return 1
        return 0

    def isRight(self, i, j):
        if self.tabCase[i][j].right == 1:
            return 1
        elif j + 1 < globals.sizeOfGrid:
            if self.tabCase[i][j + 1].left == 1:
                return 1
            elif self.tabCase[i][j + 1].pawn != -1:
                return 1
        return 0

    def isUp(self, i, j):
        if self.tabCase[i][j].up == 1:
            return 1
        elif i - 1 >= 0:
            if self.tabCase[i - 1][j].down == 1:
                return 1
            elif self.tabCase[i - 1][j].pawn != -1:
                return 1
        return 0

    def isDown(self, i, j):
        if self.tabCase[i][j].down == 1:
            return 1
        elif i + 1 < globals.sizeOfGrid:
            if self.tabCase[i + 1][j].up == 1:
                return 1
            elif self.tabCase[i + 1][j].pawn != -1:
                return 1
        return 0

    def goLeft(self, i, j, needVisualUpdate):
        if self.tabCase[i][j].pawn == -1:
            return
        iIter = i
        jIter = j
        if self.isLeft(iIter, jIter) == 0:
            pawnID = self.tabCase[i][j].pawn
            self.tabCase[i][j].pawn = -1
            jIter = j - 1
            self.tabCase[i][jIter].pawn = pawnID
            if needVisualUpdate == 1:
                visual_instance = Visual.getInstance()
                visual_instance.updateGrid(i, j, i, jIter, pawnID)
            self.goLeft(iIter, jIter, needVisualUpdate)

    def goRight(self, i, j, needVisualUpdate):
        if self.tabCase[i][j].pawn == -1:
            return
        iIter = i
        jIter = j
        if self.isRight(iIter, jIter) == 0:
            pawnID = self.tabCase[i][j].pawn
            self.tabCase[i][j].pawn = -1
            jIter = j + 1
            self.tabCase[i][jIter].pawn = pawnID
            if needVisualUpdate == 1:
                visual_instance = Visual.getInstance()
                visual_instance.updateGrid(i, j, i, jIter, pawnID)
            self.goRight(iIter, jIter, needVisualUpdate)

    def goUp(self, i, j, needVisualUpdate):
        if self.tabCase[i][j].pawn == -1:
            return
        iIter = i
        jIter = j
        if self.isUp(iIter, jIter) == 0:
            pawnID = self.tabCase[i][j].pawn
            self.tabCase[i][j].pawn = -1
            iIter = i - 1
            self.tabCase[iIter][j].pawn = pawnID
            if needVisualUpdate == 1:
                visual_instance = Visual.getInstance()
                visual_instance.updateGrid(i, j, iIter, j, pawnID)
            self.goUp(iIter, jIter, needVisualUpdate)

    def goDown(self, i, j, needVisualUpdate):
        if self.tabCase[i][j].pawn == -1:
            return
        iIter = i
        jIter = j
        if self.isDown(iIter, jIter) == 0:
            pawnID = self.tabCase[i][j].pawn
            self.tabCase[i][j].pawn = -1
            iIter += 1
            self.tabCase[iIter][j].pawn = pawnID
            if needVisualUpdate == 1:
                visual_instance = Visual.getInstance()
                visual_instance.updateGrid(i, j, iIter, j, pawnID)
            self.goDown(iIter, jIter, needVisualUpdate)

    def replacePawns(self):
        gridbis = []
        for i in range(16):
            for j in range(16):
                if self.tabCase[i][j].pawn > -1:
                    gridbis.append([i, j])
                    self.tabCase[i][j].pawn = -1

        for i in range(0, 4):
            isPlaced = False
            while not isPlaced:
                randomNumber = randint(0, 15)
                randomNumber2 = randint(0, 15)
                if self.tabCase[randomNumber][randomNumber2].target == 0 and not (
                        (randomNumber2 > 6 and randomNumber < 9) and (6 < randomNumber2 < 9)):
                    isPlaced = True
                    self.tabCase[randomNumber][randomNumber2].pawn = i
                    visual_instance = Visual.getInstance()
                    visual_instance.updateGrid(gridbis[i][0], gridbis[i][1], randomNumber, randomNumber2, i)
        globals.listPositionPawn.clear()
        for i in range(16):
            for j in range(16):
                if self.tabCase[i][j].pawn > -1:
                    globals.listPositionPawn.append([i, j, self.tabCase[i][j].pawn])

    def getCoordTarget(self):
        for i in range(16):
            for j in range(16):
                if self.tabCase[i][j].target == globals.currentTarget:
                    globals.targetX = i
                    globals.targetY = j

    def getCoordPawn(self, pawnId, gridf):
        for i in range(16):
            for j in range(16):
                if gridf[i][j].pawn == pawnId:
                    globals.pawnX = i
                    globals.pawnY = j
