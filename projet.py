from random import random, randint
from tkinter import *


class Case:
    right = 0
    down = 0
    left = 0
    up = 0
    target = 0
    pawn = -1

    def __init__(self):
        self.right = 0
        self.down = 0
        self.left = 0
        self.up = 0
        self.target = 0


def rotCase(case, direction, nbRot):  # rotates one case
    caseTemp = Case()
    if case.target != 0:
        caseTemp.target = case.target
    if (direction):  # clock-wise
        if (case.down == 1):
            if (nbRot == 1):
                caseTemp.left = 1
            if (nbRot == 2):
                caseTemp.up = 1
            if (nbRot == 3):
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
    else:  # anti-clock-wise
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


def rotation(panel, direction, nbRot):  # adds the rotated cases on the panel to complete its rotation
    panelTemp = [[Case() for i in range(int(sizeOfPanel))] for j in range(int(sizeOfPanel))]
    for i in range(0, 8):
        for j in range(0, 8):
            if panel[i][j].up == 1 or panel[i][j].right == 1 or panel[i][j].left == 1 or panel[i][j].down == 1:
                if (direction):
                    if (nbRot == 1):
                        panelTemp[j][int(sizeOfPanel) - 1 - i] = rotCase(panel[i][j], direction, nbRot)
                    elif (nbRot == 2):
                        panelTemp[int(sizeOfPanel) - 1 - i][int(sizeOfPanel) - 1 - j] = rotCase(panel[i][j], direction,
                                                                                                nbRot)
                    elif (nbRot == 3):
                        panelTemp[int(sizeOfPanel) - 1 - j][i] = rotCase(panel[i][j], direction, nbRot)
                else:
                    if (nbRot == 1):
                        panelTemp[int(sizeOfPanel) - 1 - j][i] = rotCase(panel[i][j], direction, nbRot)
                    elif (nbRot == 2):
                        panelTemp[int(sizeOfPanel) - 1 - i][int(sizeOfPanel) - 1 - j] = rotCase(panel[i][j], direction,
                                                                                                nbRot)
                    elif (nbRot == 3):
                        panelTemp[j][int(sizeOfPanel) - 1 - i] = rotCase(panel[i][j], direction, nbRot)
    return panelTemp


def rotate(pos, panel, panelNb):  # rotation of a panel
    if (pos == panelNb):
        return panel
    elif (pos > panelNb):
        return rotation(panel, 1, pos - panelNb)
    else:
        return rotation(panel, 0, panelNb - pos)


def placePanelWalls(grid, panel, pos):  # places the panel's walls on the grid, taking in account its position
    for i in range(0, 8):
        for j in range(0, 8):
            if panel[i][j].up == 1 or panel[i][j].right == 1 or panel[i][j].left == 1 or panel[i][j].down == 1:
                if pos == 0:
                    grid[i][j] = panel[i][j]
                elif pos == 1:
                    grid[i][j + 8] = panel[i][j]
                elif pos == 2:
                    grid[i + 8][j] = panel[i][j]
                else:
                    grid[i + 8][j + 8] = panel[i][j]
    return grid


def isleft(i, j, gridparam):
    if gridparam[i][j].left == 1:
        return 1
    elif j - 1 >= 0:
        if gridparam[i][j - 1].right == 1:
            return 1
        elif gridparam[i][j - 1].pawn != -1:
            return 1
    return 0


def isright(i, j, gridparam):
    if gridparam[i][j].right == 1:
        return 1
    elif j + 1 < sizeOfGrid:
        if gridparam[i][j + 1].left == 1:
            return 1
        elif gridparam[i][j + 1].pawn != -1:
            return 1
    return 0


def isup(i, j, gridparam):
    if gridparam[i][j].up == 1:
        return 1
    elif i - 1 >= 0:
        if gridparam[i - 1][j].down == 1:
            return 1
        elif gridparam[i - 1][j].pawn != -1:
            return 1
    return 0


def isdown(i, j, gridparam):
    if gridparam[i][j].down == 1:
        return 1
    elif i + 1 < sizeOfGrid:
        if gridparam[i + 1][j].up == 1:
            return 1
        elif gridparam[i + 1][j].pawn != -1:
            return 1
    return 0

def updateGrid(i,j,i2,j2, pawnId):
    can.create_rectangle(j*50 + 2, i*50 + 2, (j+1)*50, (i+1)*50, fill="white")  # case
    couleur = "white"
    if pawnId == 0:
        couleur = "blue"
    if pawnId == 1:
        couleur = "orange"
    if pawnId == 2:
        couleur = "green"
    if pawnId == 3:
        couleur = "red"
    can.create_rectangle(j2 * 50 + 2, i2 * 50 + 2, (j2 + 1) * 50, (i2 + 1) * 50, fill=couleur)  # case

    x1 = j * 50
    x2 = (j + 1) * 50
    y1 = i * 50
    y2 = (i + 1) * 50

    if grid[i][j].target > 0:
        if grid[i][j].target == 1:
            can.create_image(x1 + 2, y1 + 2, image=img1, anchor='nw')
        if grid[i][j].target == 2:
            can.create_image(x1 + 2, y1 + 2, image=img2, anchor='nw')
        if grid[i][j].target == 3:
            can.create_image(x1 + 2, y1 + 2, image=img3, anchor='nw')
        if grid[i][j].target == 4:
            can.create_image(x1 + 2, y1 + 2, image=img4, anchor='nw')
        if grid[i][j].target == 5:
            can.create_image(x1 + 2, y1 + 2, image=img5, anchor='nw')
        if grid[i][j].target == 6:
            can.create_image(x1 + 2, y1 + 2, image=img6, anchor='nw')
        if grid[i][j].target == 7:
            can.create_image(x1 + 2, y1 + 2, image=img7, anchor='nw')
        if grid[i][j].target == 8:
            can.create_image(x1 + 2, y1 + 2, image=img8, anchor='nw')
        if grid[i][j].target == 9:
            can.create_image(x1 + 2, y1 + 2, image=img9, anchor='nw')
        if grid[i][j].target == 10:
            can.create_image(x1 + 2, y1 + 2, image=img10, anchor='nw')
        if grid[i][j].target == 11:
            can.create_image(x1 + 2, y1 + 2, image=img11, anchor='nw')
        if grid[i][j].target == 12:
            can.create_image(x1 + 2, y1 + 2, image=img12, anchor='nw')
        if grid[i][j].target == 13:
            can.create_image(x1 + 2, y1 + 2, image=img13, anchor='nw')
        if grid[i][j].target == 14:
            can.create_image(x1 + 2, y1 + 2, image=img14, anchor='nw')
        if grid[i][j].target == 15:
            can.create_image(x1 + 2, y1 + 2, image=img15, anchor='nw')
        if grid[i][j].target == 16:
            can.create_image(x1 + 2, y1 + 2, image=img16, anchor='nw')

    if grid[i][j].down == 1:
        can.create_line(x1 + 2, y2, x2, y2, fill="purple", width=5)
    if grid[i][j].right == 1:
        can.create_line(x2, y1, x2, y2, fill="purple", width=5)
    if grid[i][j].left == 1:
        can.create_line(x1 + 2, y1, x1 + 2, y2, fill="purple", width=5)
    if grid[i][j].up == 1:
        can.create_line(x1 + 2, y1 + 2, x2, y1 + 2, fill="purple", width=5)

def goLeft(i, j, gridparam, needVisualUpdate):
    if gridparam[i][j].pawn == -1:
        print('return')
        return
    iIter = i
    jIter = j
    if (isleft(iIter, jIter, gridparam) == 0):
        pawnID = gridparam[i][j].pawn
        gridparam[i][j].pawn = -1
        jIter = j - 1
        gridparam[i][jIter].pawn = pawnID
        if (needVisualUpdate == 1) :
            updateGrid(i, j, i, jIter, pawnID)
        goLeft(iIter, jIter, gridparam, needVisualUpdate)

def goRight(i, j, gridparam, needVisualUpdate):
    if gridparam[i][j].pawn == -1:
        return
    iIter = i
    jIter = j
    if (isright(iIter, jIter, gridparam) == 0):
        pawnID = gridparam[i][j].pawn
        gridparam[i][j].pawn = -1
        jIter = j + 1
        gridparam[i][jIter].pawn = pawnID
        if (needVisualUpdate == 1):
            updateGrid(i, j, i, jIter, pawnID)
        goRight(iIter, jIter, gridparam, needVisualUpdate)


def goUp(i, j, gridparam, needVisualUpdate):
    if gridparam[i][j].pawn == -1:
        return
    iIter = i
    jIter = j
    if (isup(iIter, jIter, gridparam) == 0):
        pawnID = gridparam[i][j].pawn
        gridparam[i][j].pawn = -1
        iIter = i - 1
        gridparam[iIter][j].pawn = pawnID
        if (needVisualUpdate == 1):
            updateGrid(i, j, iIter, j, pawnID)
        goUp(iIter, jIter, gridparam, needVisualUpdate)


def goDown(i, j, gridparam, needVisualUpdate):
    if gridparam[i][j].pawn == -1:
        return
    iIter = i
    jIter = j
    if (isdown(iIter, jIter, gridparam) == 0):
        pawnID = gridparam[i][j].pawn
        gridparam[i][j].pawn = -1
        iIter = i + 1
        gridparam[iIter][j].pawn = pawnID
        if (needVisualUpdate == 1):
            updateGrid(i, j, iIter, j, pawnID)
        goDown(iIter, jIter, gridparam, needVisualUpdate)


print("PROJECT INITIALIZATION\n")
sizeOfGrid = 16
sizeOfPanel = sizeOfGrid / 2

click = 1
lastX = -1
lastY = -1

# init grid
grid = [[Case() for i in range(sizeOfGrid)] for j in range(sizeOfGrid)]
for i in range(0, sizeOfGrid):
    for j in range(0, sizeOfGrid):
        case = Case()
        grid[i][j] = case

print("Initialising the 4 panels\n ")
# init all 4 panels with their walls
panel1 = [[Case() for i in range(int(sizeOfPanel))] for j in range(int(sizeOfPanel))]
panel2 = [[Case() for i in range(int(sizeOfPanel))] for j in range(int(sizeOfPanel))]
panel3 = [[Case() for i in range(int(sizeOfPanel))] for j in range(int(sizeOfPanel))]
panel4 = [[Case() for i in range(int(sizeOfPanel))] for j in range(int(sizeOfPanel))]

# init panel4's walls
panel4[1][4].target = 9
panel4[2][6].target = 11
panel4[5][1].target = 13
panel4[6][3].target = 15
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

# init panel3's walls
panel3[1][5].target = 10
panel3[3][1].target = 12
panel3[5][6].target = 14
panel3[6][2].target = 16
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

# init panel2's walls
panel2[1][5].target = 1
panel2[3][1].target = 3
panel2[4][6].target = 5
panel2[6][4].target = 8
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

# init panel1's walls
panel1[2][5].target = 2
panel1[4][2].target = 4
panel1[5][7].target = 6
panel1[6][1].target = 7
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

# randomly place the panels on the grid
gridPosPanels = [0, 0, 0, 0]  # stores the panels in the right placement order
gridNbPanels = [0, 0, 0, 0]  # stores what panels are placed where
gridPanels = [panel1, panel2, panel3, panel4]
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
            print(j)

# generate walls according to the random layout on each panel
for i in range(0, 4):
    gridPosPanels[i] = rotate(i, gridPosPanels[i], gridNbPanels[i])

# PLacing every wall on the final grid
for i in range(0, 4):
    grid = placePanelWalls(grid, gridPosPanels[i], i)

# adding the central and the border walls
for i in range(sizeOfGrid):
    for j in range(sizeOfGrid):
        if i == 0:
            grid[i][j].up = 1
        if i == sizeOfGrid - 1:
            grid[i][j].down = 1
        if j == 0:
            grid[i][j].left = 1
        if j == sizeOfGrid - 1:
            grid[i][j].right = 1

grid[int(sizeOfGrid / 2) - 1][int(sizeOfGrid / 2) - 1].up = 1
grid[int(sizeOfGrid / 2) - 1][int(sizeOfGrid / 2) - 1].left = 1
grid[int(sizeOfGrid / 2) - 1][int(sizeOfGrid / 2)].up = 1
grid[int(sizeOfGrid / 2) - 1][int(sizeOfGrid / 2)].right = 1
grid[int(sizeOfGrid / 2)][int(sizeOfGrid / 2) - 1].down = 1
grid[int(sizeOfGrid / 2)][int(sizeOfGrid / 2) - 1].left = 1
grid[int(sizeOfGrid / 2)][int(sizeOfGrid / 2)].down = 1
grid[int(sizeOfGrid / 2)][int(sizeOfGrid / 2)].right = 1

# placing the pawns randomly on the grid
for i in range(0, 4):
    isPlaced = False
    while (not isPlaced):
        randomNumber = randint(0, 15)
        randomNumber2 = randint(0, 15)
        if grid[randomNumber][randomNumber2].target == 0 and not ((randomNumber2 > 6 and randomNumber < 9) and (randomNumber2 > 6 and randomNumber2 < 9)) and grid[randomNumber][randomNumber2].pawn==-1:
            isPlaced = True
            grid[randomNumber][randomNumber2].pawn = i

print("\n")


#Jeu 
targetColor ="notDefined"
currentTarget = "-2"
nbTurn=0
nbMovePlayed=0
listPositionPawn = [] #X Y idColor
def game():
    #initialisation du tour
    global nbMovePlayed,targetColor,currentTarget,listPositionPawn
    nbMovePlayed = 0 # nombre de coup courant
    randomNumber = randint(1,16)
    while(currentTarget == randomNumber):
        randomNumber= randint(1,16)
    currentTarget = randomNumber
    can.create_image(360,360, image=listImg[currentTarget+16], anchor='nw')
    #on va chercher la couleur
    targetColor = "notDefined"
    if(currentTarget == 1 or currentTarget == 4 or currentTarget == 15 or currentTarget==16 ):
        targetColor="green"
    if(currentTarget == 2 or currentTarget == 3 or currentTarget == 10 or currentTarget==11 ):
        targetColor="blue"
    if(currentTarget == 5 or currentTarget == 6 or currentTarget == 13 or currentTarget==14 ):
        targetColor="red"
    if(currentTarget == 7 or currentTarget == 8 or currentTarget == 9 or currentTarget==12 ):
        targetColor="orange"
    #on a couleur + symbole

    #On enregistre les positions des pions 
    listPositionPawn.clear()
    for i in range(16):
        for j in range(16):
            if(grid[i][j].pawn > -1):
                listPositionPawn.append([i,j,grid[i][j].pawn])
    print(listPositionPawn)




    print(currentTarget)
    print(targetColor)
    changeText()


    #label = Label(image=img1)
    #label.image = img1  # keep a reference!
# fin jeu



targetX= -1
targetY= -1
def getCoordTarget():
    global targetX,targetY
    for i in range(16) :
        for j in range(16) :
            if(grid[i][j].target == currentTarget) :
                targetX= i
                targetY= j

pawnX = -1
pawnY = -1
def getCoordPawn(pawnId):
    global pawnX,pawnY
    for i in range(16):
        for j in range(16):
            if gridIa[i][j].pawn == pawnId:
                pawnX = i
                pawnY = j



def displayEndOfTheGame():
    global nbMovePlayedTotal
    can.delete("all")
    changeText()
    can.pack()
    endMessage = "Fin de la partie ! Voici votre score : " + str(nbMovePlayedTotal)
    endMessageIa = "Score de l'ia : " + "Ecrire le score de l'ia ici "

    can.create_text(400,400, text=endMessage)
    can.create_text(400,500, text=endMessageIa)
    b2.config(state ="disabled")  
    can.config(state ="disabled")





def replacePawns():
    global listPositionPawn
    gridbis = []
    for i in range(16):
        for j in range(16):
            if(grid[i][j].pawn > -1 ):
                gridbis.append([i,j])
                grid[i][j].pawn = -1

    for i in range(0, 4):
        isPlaced = False
        while (not isPlaced):
            randomNumber = randint(0, 15)
            randomNumber2 = randint(0, 15)
            if grid[randomNumber][randomNumber2].target == 0 and not ((randomNumber2 > 6 and randomNumber < 9) and (randomNumber2 > 6 and randomNumber2 < 9)):
                isPlaced = True
                grid[randomNumber][randomNumber2].pawn = i
                updateGrid(gridbis[i][0],gridbis[i][1],randomNumber,randomNumber2,i)
    listPositionPawn.clear()
    for i in range(16):
        for j in range(16):
            if(grid[i][j].pawn > -1):
                listPositionPawn.append([i,j,grid[i][j].pawn])







nbMovePlayedTotal=[]
def on_click_event(event):
    global click, lastY, lastX,nbTurn,nbMovePlayed
    i = (int)(event.x / 50)
    j = (int)(event.y / 50)
    print("clicked at", event.x, event.y, " / case ", i, j)
    # if grid[i][j].pawn == 0:
    #    print("blue pawn")
    # if grid[i][j].pawn == 1:
    #    print("orange pawn")
    # if grid[i][j].pawn == 2:
    #    print("green pawn")
    # if grid[i][j].pawn == 3:
    #    print("red pawn")
    if click == 1:
        if grid[j][i].pawn > -1:
            lastX = i
            lastY = j
            click = 2
            print('PAWN')
    else:
        if i == lastX:
            if lastY < j:
                goDown(lastY, lastX, grid, 1)
                print('go Down')
                nbMovePlayed+=1
            if lastY > j:
                goUp(lastY, lastX, grid, 1)
                print('go Up')
                nbMovePlayed+=1
        if j == lastY:
            if lastX < i:
                goRight(lastY, lastX, grid, 1)
                print('go Right')
                nbMovePlayed+=1
            if lastX > i:
                goLeft(lastY, lastX, grid, 1)
                print('go Left')
                nbMovePlayed+=1
        click = 1
    changeText()
    if(verifIfPawnIsOnTarget()):
        print("je suis la wesh")
        nbTurn+=1
        nbMovePlayedTotal.append(nbMovePlayed)
        if(nbTurn < 2):
            #va afficher une nouvelle target
            replacePawns()
            game()
        else:
            print("fin du jeu")
            print("score : ")
            print(nbMovePlayedTotal)
            displayEndOfTheGame()
            
    


def verifIfPawnIsOnTarget():
    #on doit recuperer l'emplacement de la cible:
    global currentTarget,targetColor
    targetX,targetY = 0,0
    pawnX,pawnY = 0,0

    idColor = -1 
    if targetColor == "blue":
        idColor = 0
    if targetColor == "orange":
        idColor = 1
    if targetColor == "green":
        idColor = 2
    if targetColor == "red":
        idColor = 3

    for i in range(16) :
        for j in range(16) :
            if(grid[i][j].target == currentTarget) :
                targetX= i
                targetY= j
    #on doit recuperer l'emplacement du bon pion de la bonne couleur:
            if(grid[i][j].pawn == idColor) :
                pawnX= i
                pawnY= j
    if(targetX == pawnX and targetY == pawnY ):
        return True
    return False





# affichage graphique
def chest():
    global x1, x2, y1, y2, couleur,b1  # coordonnees
    can.bind("<Button-1>", on_click_event)
    j, i = 0, 0
    while x1 < 800 and y1 < 800:  # 800 car 50*16 case
        k = i % 16
        if grid[k][j].pawn == -1:
            couleur = "white"
        if grid[k][j].pawn == 0:
            couleur = "blue"
        if grid[k][j].pawn == 1:
            couleur = "orange"
        if grid[k][j].pawn == 2:
            couleur = "green"
        if grid[k][j].pawn == 3:
            couleur = "red"
        can.create_rectangle(x1 + 2, y1 + 2, x2, y2, fill=couleur)  # case

        if grid[k][j].target > 0:
            if grid[k][j].target == 1:
                can.create_image(x1 + 2, y1 + 2, image=img1, anchor='nw')
            if grid[k][j].target == 2:
                can.create_image(x1 + 2, y1 + 2, image=img2, anchor='nw')
            if grid[k][j].target == 3:
                can.create_image(x1 + 2, y1 + 2, image=img3, anchor='nw')
            if grid[k][j].target == 4:
                can.create_image(x1 + 2, y1 + 2, image=img4, anchor='nw')
            if grid[k][j].target == 5:
                can.create_image(x1 + 2, y1 + 2, image=img5, anchor='nw')
            if grid[k][j].target == 6:
                can.create_image(x1 + 2, y1 + 2, image=img6, anchor='nw')
            if grid[k][j].target == 7:
                can.create_image(x1 + 2, y1 + 2, image=img7, anchor='nw')
            if grid[k][j].target == 8:
                can.create_image(x1 + 2, y1 + 2, image=img8, anchor='nw')
            if grid[k][j].target == 9:
                can.create_image(x1 + 2, y1 + 2, image=img9, anchor='nw')
            if grid[k][j].target == 10:
                can.create_image(x1 + 2, y1 + 2, image=img10, anchor='nw')
            if grid[k][j].target == 11:
                can.create_image(x1 + 2, y1 + 2, image=img11, anchor='nw')
            if grid[k][j].target == 12:
                can.create_image(x1 + 2, y1 + 2, image=img12, anchor='nw')
            if grid[k][j].target == 13:
                can.create_image(x1 + 2, y1 + 2, image=img13, anchor='nw')
            if grid[k][j].target == 14:
                can.create_image(x1 + 2, y1 + 2, image=img14, anchor='nw')
            if grid[k][j].target == 15:
                can.create_image(x1 + 2, y1 + 2, image=img15, anchor='nw')
            if grid[k][j].target == 16:
                can.create_image(x1 + 2, y1 + 2, image=img16, anchor='nw')

        if grid[k][j].down == 1:
            can.create_line(x1 + 2, y2, x2, y2, fill="purple", width=5)
        if grid[k][j].right == 1:
            can.create_line(x2, y1, x2, y2, fill="purple", width=5)
        if grid[k][j].left == 1:
            can.create_line(x1 + 2, y1, x1 + 2, y2, fill="purple", width=5)
        if grid[k][j].up == 1:
            can.create_line(x1 + 2, y1 + 2, x2, y1 + 2, fill="purple", width=5)
        j, x1, x2 = j + 1, x1 + 50, x2 + 50
        if j == 16:
            y1, y2 = y1 + 50, y2 + 50
            i, j, x1, x2 = i + 1, 0, 0, 50
    b1.config(state ="disabled")         
    game()



# Verifications

# up - down - left - right
for i in range(int(sizeOfGrid)):
    print()
    for j in range(int(sizeOfGrid)):
        print(isdown(i, j, grid), end='')

# pawn
for i in range(int(sizeOfGrid)):
    print()
    for j in range(int(sizeOfGrid)):
        print(grid[i][j].pawn, end='')

# isup - isdown - isleft - isright
print("\n\nisWall?")
print(isright(sizeOfGrid - 1, sizeOfGrid - 1, grid))

x1, y1, x2, y2 = 0, 0, 50, 50
couleur = 'white'

fen = Tk()
global can
can = Canvas(fen, width=800, heigh=800, bg='ivory')

# Permet d'afficher les images, on a besoin de garder une référence sinon elle ne s'affichent pas

img1 = PhotoImage(file="img/1.gif")
img2 = PhotoImage(file="img/2.gif")
img3 = PhotoImage(file="img/3.gif")
img4 = PhotoImage(file="img/4.gif")
img5 = PhotoImage(file="img/5.gif")
img6 = PhotoImage(file="img/6.gif")
img7 = PhotoImage(file="img/7.gif")
img8 = PhotoImage(file="img/8.gif")
img9 = PhotoImage(file="img/9.gif")
img10 = PhotoImage(file="img/10.gif")
img11 = PhotoImage(file="img/11.gif")
img12 = PhotoImage(file="img/12.gif")
img13 = PhotoImage(file="img/13.gif")
img14 = PhotoImage(file="img/14.gif")
img15 = PhotoImage(file="img/15.gif")
img16 = PhotoImage(file="img/16.gif")
img17 = PhotoImage(file="img/17.gif")
img18 = PhotoImage(file="img/18.gif")
img19 = PhotoImage(file="img/19.gif")
img20 = PhotoImage(file="img/20.gif")
img21 = PhotoImage(file="img/21.gif")
img22 = PhotoImage(file="img/22.gif")
img23 = PhotoImage(file="img/23.gif")
img24 = PhotoImage(file="img/24.gif")
img25 = PhotoImage(file="img/25.gif")
img26 = PhotoImage(file="img/26.gif")
img27 = PhotoImage(file="img/27.gif")
img28 = PhotoImage(file="img/28.gif")
img29 = PhotoImage(file="img/29.gif")
img30 = PhotoImage(file="img/30.gif")
img31 = PhotoImage(file="img/31.gif")
img32 = PhotoImage(file="img/32.gif")
label = Label(image=img1)
label.image = img1  # keep a reference!

global listImg
listImg =[]
listImg.append(img1)#jamais afficher
listImg.append(img1)
listImg.append(img2)
listImg.append(img3)
listImg.append(img4)
listImg.append(img5)
listImg.append(img6)
listImg.append(img7)
listImg.append(img8)
listImg.append(img9)
listImg.append(img10)
listImg.append(img11)
listImg.append(img12)
listImg.append(img13)
listImg.append(img14)
listImg.append(img15)
listImg.append(img16)
listImg.append(img17)
listImg.append(img18)
listImg.append(img19)
listImg.append(img20)
listImg.append(img21)
listImg.append(img22)
listImg.append(img23)
listImg.append(img24)
listImg.append(img25)
listImg.append(img26)
listImg.append(img27)
listImg.append(img28)
listImg.append(img29)
listImg.append(img30)
listImg.append(img31)
listImg.append(img32)

def reset():
    global nbMovePlayed
    if(nbMovePlayed ==0 ):
        return
    nbMovePlayed = 0
    gridbis = []
    changeText()
    for i in range(16):
        for j in range(16):
            if(grid[i][j].pawn > -1 ):
                gridbis.append([i,j])
                grid[i][j].pawn = -1

    for i in range(4):
        grid[listPositionPawn[i][0]][listPositionPawn[i][1]].pawn = listPositionPawn[i][2]
        updateGrid(gridbis[i][0],gridbis[i][1],listPositionPawn[i][0],listPositionPawn[i][1],listPositionPawn[i][2])




b1 = Button(fen, text='Jouer', command=chest)
b2 = Button(fen, text='Reset', command=reset)

can.pack(side=TOP, padx=5, pady=5)
b1.pack(side=LEFT, padx=3, pady=3)
b2.pack(side=LEFT, padx=3, pady=3)
  
# text1= Text(fen, height=1,width=50)
text_value = "turn : " + str(nbTurn) +"                   move : " + str(nbMovePlayed) + "                total : 0"
# print(text_value)
# text1.insert(INSERT,text_value)
# text1.config(state ="disabled")
# text1.pack()
def changeText():
    total = 0
    for i in nbMovePlayedTotal:
        total += i
    text_value = "turn : " + str(nbTurn) +"                   move : " + str(nbMovePlayed) + "              total : " + str(total)
    text.set(text_value) 

text = StringVar()
text.set(text_value)
label = Label(fen, textvariable=text)


label.pack()




fen.mainloop()

# affichage fin : fin test
gridIa = []
def beforeIaSetup(): # Pour setup l'ia, comme ça on évite des répétitions de boucles inutiles
    global gridIa
    gridIa= grid
    getCoordTarget()

#Ia 
def IaBrutForce(limite):
    global currentTarget,targetColor,targetX,targetY,pawnX,pawnY
    if(targetX == pawnX and targetY == pawnY):
        print("tro b1")
        return True
    if limite == 0 : #pas cool
        return False
    for i in range(4): # parcours 4 pions
        getCoordPawn(i) # va récupéré les coords du pions en attribut
        #on regarde si il y'a des murs
        if( !isUp(pawnX,pawnY,gridIa) ) :
            
            IaBrutForce(limite--)
        if( !isdown(pawnX,pawnY,gridIa) ) :

            IaBrutForce(limite--)
        if( !isRight(pawnX,pawnY,gridIa) ) :

            IaBrutForce(limite--)
        if( !isLeft(pawnX,pawnY,gridIa) ) :
            
            IaBrutForce(limite--)







#fin ia

