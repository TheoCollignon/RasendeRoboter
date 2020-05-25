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


def rotCase(case,direction,nbRot):#rotates one case
    caseTemp = Case()
    if case.target != 0:
        caseTemp.target = case.target
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


def rotation(panel,direction,nbRot):#adds the rotated cases on the panel to complete its rotation
    panelTemp = [[Case() for i in range(int(sizeOfPanel))] for j in range(int(sizeOfPanel))]
    for i in range(0,8):
        for j in range(0,8):
            if panel[i][j].up == 1 or panel[i][j].right == 1 or panel[i][j].left == 1 or panel[i][j].down == 1:
                if(direction):
                    if (nbRot == 1):
                        panelTemp[j][int(sizeOfPanel) - 1 - i] = rotCase(panel[i][j], direction, nbRot)
                    elif (nbRot == 2):
                        panelTemp[int(sizeOfPanel)-1-i][int(sizeOfPanel)-1-j] = rotCase(panel[i][j], direction, nbRot)
                    elif (nbRot == 3):
                        panelTemp[int(sizeOfPanel)-1-j][i] = rotCase(panel[i][j], direction, nbRot)
                else:
                    if (nbRot == 1):
                        panelTemp[int(sizeOfPanel) - 1 - j][i] = rotCase(panel[i][j], direction, nbRot)
                    elif (nbRot == 2):
                        panelTemp[int(sizeOfPanel) - 1 - i][int(sizeOfPanel) - 1 - j] = rotCase(panel[i][j], direction, nbRot)
                    elif (nbRot == 3):
                        panelTemp[j][int(sizeOfPanel) - 1 - i] = rotCase(panel[i][j], direction, nbRot)
    return panelTemp


def rotate(pos,panel,panelNb):#rotation of a panel
    if(pos == panelNb):
        return panel
    elif(pos >panelNb):
        return rotation(panel,1,pos-panelNb)
    else:
        return rotation(panel,0,panelNb-pos)


def placePanelWalls(grid,panel,pos):#places the panel's walls on the grid, taking in account its position
    for i in range (0,8):
        for j in range(0,8):
            if panel[i][j].up == 1 or panel[i][j].right == 1 or panel[i][j].left == 1 or panel[i][j].down == 1:
                if pos == 0:
                    grid[i][j] = panel[i][j]
                elif pos == 1:
                    grid[i][j+8] = panel[i][j]
                elif pos == 2:
                    grid[i+8][j] = panel[i][j]
                else:
                    grid[i+8][j+8] = panel[i][j]
    return grid


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

# init grid
grid = [[Case() for i in range(sizeOfGrid)] for j in range(sizeOfGrid)]
for i in range (0,sizeOfGrid):
    for j in range(0, sizeOfGrid):
        case = Case()
        grid[i][j] = case

print("Initialising the 4 panels\n ")
#init all 4 panels with their walls
panel1 = [[Case() for i in range(int(sizeOfPanel))] for j in range(int(sizeOfPanel))]
panel2 = [[Case() for i in range(int(sizeOfPanel))] for j in range(int(sizeOfPanel))]
panel3 = [[Case() for i in range(int(sizeOfPanel))] for j in range(int(sizeOfPanel))]
panel4 = [[Case() for i in range(int(sizeOfPanel))] for j in range(int(sizeOfPanel))]

#init panel4's walls
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

#init panel3's walls
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

#init panel2's walls
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

#init panel1's walls
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

#generate walls according to the random layout on each panel
for i in range(0,4):
    gridPosPanels[i] = rotate(i,gridPosPanels[i],gridNbPanels[i])

#PLacing every wall on the final grid
for i in range (0,4):
    grid = placePanelWalls(grid,gridPosPanels[i],i)

#adding the central and the border walls
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

grid[int(sizeOfGrid/2)-1][int(sizeOfGrid/2)-1].up = 1
grid[int(sizeOfGrid/2)-1][int(sizeOfGrid/2)-1].left = 1
grid[int(sizeOfGrid/2)-1][int(sizeOfGrid/2)].up = 1
grid[int(sizeOfGrid/2)-1][int(sizeOfGrid/2)].right = 1
grid[int(sizeOfGrid/2)][int(sizeOfGrid/2)-1].down = 1
grid[int(sizeOfGrid/2)][int(sizeOfGrid/2)-1].left = 1
grid[int(sizeOfGrid/2)][int(sizeOfGrid/2)].down = 1
grid[int(sizeOfGrid/2)][int(sizeOfGrid/2)].right = 1

#placing the pawns randomly on the grid
for i in range(0,4):
    isPlaced = False
    while(not isPlaced):
        randomNumber = randint(0,15)
        randomNumber2 = randint(0,15)
        if grid[randomNumber][randomNumber2].target == 0 and not ((randomNumber2 > 6 and randomNumber < 9) and (randomNumber2 > 6 and randomNumber2 < 9)):
            isPlaced = True
            grid[randomNumber][randomNumber2].pawn = i

print("\n")


# Verifications

# up - down - left - right
for i in range(int(sizeOfGrid)):
    print()
    for j in range(int(sizeOfGrid)):
        print(grid[i][j].up,end ='')
 

# isup - isdown - isleft - isright
print("\n\nisWall?")
print(isright(sizeOfGrid-1,sizeOfGrid-1,grid))

def on_click_event(event):
    j = (int)(event.x/50)
    i = (int)(event.y/50)
    print("clicked at", event.x, event.y, " / case ", i, j)
    if grid[i][j].pawn == 0:
        print("blue pawn")
    if grid[i][j].pawn == 1:
        print("orange pawn")
    if grid[i][j].pawn == 2:
        print("green pawn")
    if grid[i][j].pawn == 3:
        print("red pawn")

#affichage graphique
def chest():
    can.bind("<Button-1>", on_click_event)
    global x1,x2,y1,y2,couleur #coordonnees
    j,i=0,0
    while x1<800 and y1 < 800 : # 800 car 50*16 case
        k = i%16 
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
        can.create_rectangle(x1+2,y1+2,x2,y2,fill=couleur) # case

        if grid[k][j].target > 0:
            if grid[k][j].target==1:
                can.create_image(x1+2, y1+2, image=img1, anchor='nw')
            if grid[k][j].target==2:
                can.create_image(x1+2, y1+2, image=img2, anchor='nw')
            if grid[k][j].target==3:
                can.create_image(x1+2, y1+2, image=img3, anchor='nw')
            if grid[k][j].target==4:
                can.create_image(x1+2, y1+2, image=img4, anchor='nw')
            if grid[k][j].target==5:
                can.create_image(x1+2, y1+2, image=img5, anchor='nw')
            if grid[k][j].target==6:
                can.create_image(x1+2, y1+2, image=img6, anchor='nw')
            if grid[k][j].target==7:
                can.create_image(x1+2, y1+2, image=img7, anchor='nw')
            if grid[k][j].target==8:
                can.create_image(x1+2, y1+2, image=img8, anchor='nw')
            if grid[k][j].target==9:
                can.create_image(x1+2, y1+2, image=img9, anchor='nw')
            if grid[k][j].target==10:
                can.create_image(x1+2, y1+2, image=img10, anchor='nw')
            if grid[k][j].target==11:
                can.create_image(x1+2, y1+2, image=img11, anchor='nw')
            if grid[k][j].target==12:
                can.create_image(x1+2, y1+2, image=img12, anchor='nw')
            if grid[k][j].target==13:
                can.create_image(x1+2, y1+2, image=img13, anchor='nw')
            if grid[k][j].target==14:
                can.create_image(x1+2, y1+2, image=img14, anchor='nw')
            if grid[k][j].target==15:
                can.create_image(x1+2, y1+2, image=img15, anchor='nw')
            if grid[k][j].target==16:
                can.create_image(x1+2, y1+2, image=img16, anchor='nw')

        if grid[k][j].down == 1:
            can.create_line(x1+5,y2,x2,y2,fill="black",width=5)
        if grid[k][j].right == 1:
            can.create_line(x2, y1, x2, y2, fill="black", width=5)
        if grid[k][j].left == 1:
            can.create_line(x1+5, y1, x1+5, y2, fill="black", width=5)
        if grid[k][j].up == 1:
            can.create_line(x1+5,y1+5, x2, y1+5, fill="black", width=5)
        j,x1,x2=j+1,x1+50,x2+50
        if j == 16:
            y1,y2=y1+50,y2+50
            i,j,x1,x2=i+1,0,0,50


       

x1,y1,x2,y2=0,0,50,50 
couleur ='white'

fen = Tk()
can = Canvas(fen,width=800,heigh=800,bg='ivory')

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
label = Label(image=img1)
label.image = img1 # keep a reference!

b1 = Button(fen, text='Jouer :D', command=chest)
can.pack(side=TOP,padx=5,pady=5)
b1.pack(side = LEFT, padx = 3, pady = 3)
fen.mainloop()

#affichage fin : fin test