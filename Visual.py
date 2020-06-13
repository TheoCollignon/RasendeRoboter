import globals
from IA import IA

from tkinter import *
from random import randint


class Visual:
    __instance = None
    grid = 0
    img1 = 0
    img2 = 0
    img3 = 0
    img4 = 0
    img5 = 0
    img6 = 0
    img7 = 0
    img8 = 0
    img9 = 0
    img10 = 0
    img11 = 0
    img12 = 0
    img13 = 0
    img14 = 0
    img15 = 0
    img16 = 0
    img17 = 0
    img18 = 0
    img19 = 0
    img20 = 0
    img21 = 0
    img22 = 0
    img23 = 0
    img24 = 0
    img25 = 0
    img26 = 0
    img27 = 0
    img28 = 0
    img29 = 0
    img30 = 0
    img31 = 0
    img32 = 0
    text_value = ""
    fen = 0

    @staticmethod
    def getInstance():
        """ Static access method. """
        return Visual.__instance

    def __init__(self, grid):
        if Visual.__instance is not None:
            raise Exception("This class is a singleton")
        else:
            self.grid = grid
            Visual.__instance = self
            self.beforeLaunchGame()
            self.setImg()
            self.launchGame()

    # affichage graphique
    def chest(self):
        #Choisir la difficulté : 
        while(True):
            bFacile = Button(self.fen, text="Blue", command=lambda: globals.can.config(bg="blue"))
            bFacile_w = globals.can.create_window(40, 20, window=bFacile)

            bMoyen = Button(self.fen, text="Blue", command=lambda: globals.can.config(bg="blue"))
            bMoyen_w = globals.can.create_window(40, 200, window=bMoyen)

            bDifficile = Button(self.fen, text="Blue", command=lambda: globals.can.config(bg="blue"))
            bDifficile_w = globals.can.create_window(400, 400)
            self.fen.mainloop()


        #fin difficulté
        globals.can.bind("<Button-1>", self.on_click_event)
        j, i = 0, 0
        while globals.x1 < 800 and globals.y1 < 800:  # 800 car 50*16 case
            k = i % 16
            if self.grid.tabCase[k][j].pawn == -1:
                globals.couleur = "white"
            if self.grid.tabCase[k][j].pawn == 0:
                globals.couleur = "blue"
            if self.grid.tabCase[k][j].pawn == 1:
                globals.couleur = "orange"
            if self.grid.tabCase[k][j].pawn == 2:
                globals.couleur = "green"
            if self.grid.tabCase[k][j].pawn == 3:
                globals.couleur = "red"
            globals.can.create_rectangle(globals.x1 + 2, globals.y1 + 2, globals.x2, globals.y2,
                                         fill=globals.couleur)  # case

            if self.grid.tabCase[k][j].target > 0:
                if self.grid.tabCase[k][j].target == 1:
                    globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img1, anchor='nw')
                if self.grid.tabCase[k][j].target == 2:
                    globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img2, anchor='nw')
                if self.grid.tabCase[k][j].target == 3:
                    globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img3, anchor='nw')
                if self.grid.tabCase[k][j].target == 4:
                    globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img4, anchor='nw')
                if self.grid.tabCase[k][j].target == 5:
                    globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img5, anchor='nw')
                if self.grid.tabCase[k][j].target == 6:
                    globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img6, anchor='nw')
                if self.grid.tabCase[k][j].target == 7:
                    globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img7, anchor='nw')
                if self.grid.tabCase[k][j].target == 8:
                    globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img8, anchor='nw')
                if self.grid.tabCase[k][j].target == 9:
                    globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img9, anchor='nw')
                if self.grid.tabCase[k][j].target == 10:
                    globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img10, anchor='nw')
                if self.grid.tabCase[k][j].target == 11:
                    globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img11, anchor='nw')
                if self.grid.tabCase[k][j].target == 12:
                    globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img12, anchor='nw')
                if self.grid.tabCase[k][j].target == 13:
                    globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img13, anchor='nw')
                if self.grid.tabCase[k][j].target == 14:
                    globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img14, anchor='nw')
                if self.grid.tabCase[k][j].target == 15:
                    globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img15, anchor='nw')
                if self.grid.tabCase[k][j].target == 16:
                    globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img16, anchor='nw')

            if self.grid.tabCase[k][j].down == 1:
                globals.can.create_line(globals.x1 + 2, globals.y2, globals.x2, globals.y2, fill="purple", width=5)
            if self.grid.tabCase[k][j].right == 1:
                globals.can.create_line(globals.x2, globals.y1, globals.x2, globals.y2, fill="purple", width=5)
            if self.grid.tabCase[k][j].left == 1:
                globals.can.create_line(globals.x1 + 2, globals.y1, globals.x1 + 2, globals.y2, fill="purple",
                                        width=5)
            if self.grid.tabCase[k][j].up == 1:
                globals.can.create_line(globals.x1 + 2, globals.y1 + 2, globals.x2, globals.y1 + 2, fill="purple",
                                        width=5)
            j, globals.x1, globals.x2 = j + 1, globals.x1 + 50, globals.x2 + 50
            if j == 16:
                globals.y1, globals.y2 = globals.y1 + 50, globals.y2 + 50
                i, j, globals.x1, globals.x2 = i + 1, 0, 0, 50
        globals.b1.config(state="disabled")
        self.game()

    def reset(self):
        if globals.nbMovePlayed == 0:
            return
        globals.nbMovePlayed = 0
        gridbis = []
        self.changeText()
        for i in range(16):
            for j in range(16):
                if self.grid.tabCase[i][j].pawn > -1:
                    gridbis.append([i, j])
                    self.grid.tabCase[i][j].pawn = -1

        for i in range(4):
            self.grid.tabCase[globals.listPositionPawn[i][0]][globals.listPositionPawn[i][1]].pawn = \
                globals.listPositionPawn[i][2]
            self.updateGrid(gridbis[i][0], gridbis[i][1], globals.listPositionPawn[i][0],
                            globals.listPositionPawn[i][1],
                            globals.listPositionPawn[i][2])

    def verifIfPawnIsOnTarget(self):
        # on doit recuperer l'emplacement de la cible:
        globals.targetX, globals.targetY = 0, 0
        globals.pawnX, globals.pawnY = 0, 0

        idColor = -1
        if globals.targetColor == "blue":
            idColor = 0
        if globals.targetColor == "orange":
            idColor = 1
        if globals.targetColor == "green":
            idColor = 2
        if globals.targetColor == "red":
            idColor = 3

        for i in range(16):
            for j in range(16):
                if self.grid.tabCase[i][j].target == globals.currentTarget:
                    globals.targetX = i
                    globals.targetY = j
                # on doit recuperer l'emplacement du bon pion de la bonne couleur:
                if self.grid.tabCase[i][j].pawn == idColor:
                    globals.pawnX = i
                    globals.pawnY = j
        if globals.targetX == globals.pawnX and globals.targetY == globals.pawnY:
            return True
        return False

    def on_click_event(self, event):
        globals.nbMovePlayedTotal = []
        i = int(event.x / 50)
        j = int(event.y / 50)
        # print("clicked at", event.x, event.y, " / case ", i, j)
        if globals.click == 1:
            if self.grid.tabCase[j][i].pawn > -1:
                globals.lastX = i
                globals.lastY = j
                globals.click = 2
                # print('PAWN')
        else:
            if i == globals.lastX:
                if globals.lastY < j:
                    self.grid.goDown(globals.lastY, globals.lastX, 1)
                    globals.nbMovePlayed += 1
                if globals.lastY > j:
                    self.grid.goUp(globals.lastY, globals.lastX, 1)
                    globals.nbMovePlayed += 1
            if j == globals.lastY:
                if globals.lastX < i:
                    self.grid.goRight(globals.lastY, globals.lastX, 1)
                    globals.nbMovePlayed += 1
                if globals.lastX > i:
                    self.grid.goLeft(globals.lastY, globals.lastX, 1)
                    globals.nbMovePlayed += 1
            globals.click = 1
        self.changeText()
        if self.verifIfPawnIsOnTarget():
            # print("je suis la wesh")
            globals.nbTurn += 1
            globals.nbMovePlayedTotal.append(globals.nbMovePlayed)
            if globals.nbTurn < 2:
                # va afficher une nouvelle target
                self.replacePawns()
                self.game()
            else:
                # print("fin du jeu")
                print("score : ")
                print(globals.nbMovePlayedTotal)
                self.displayEndOfTheGame()

    def updateGrid(self, i, j, i2, j2, pawnId):
        globals.can.create_rectangle(j * 50 + 2, i * 50 + 2, (j + 1) * 50, (i + 1) * 50, fill="white")  # case
        globals.couleur = "white"
        if pawnId == 0:
            globals.couleur = "blue"
        if pawnId == 1:
            globals.couleur = "orange"
        if pawnId == 2:
            globals.couleur = "green"
        if pawnId == 3:
            globals.couleur = "red"
        globals.can.create_rectangle(j2 * 50 + 2, i2 * 50 + 2, (j2 + 1) * 50, (i2 + 1) * 50,
                                     fill=globals.couleur)  # case

        globals.x1 = j * 50
        globals.x2 = (j + 1) * 50
        globals.y1 = i * 50
        globals.y2 = (i + 1) * 50

        if self.grid.tabCase[i][j].target > 0:
            if self.grid.tabCase[i][j].target == 1:
                globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img1, anchor='nw')
            if self.grid.tabCase[i][j].target == 2:
                globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img2, anchor='nw')
            if self.grid.tabCase[i][j].target == 3:
                globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img3, anchor='nw')
            if self.grid.tabCase[i][j].target == 4:
                globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img4, anchor='nw')
            if self.grid.tabCase[i][j].target == 5:
                globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img5, anchor='nw')
            if self.grid.tabCase[i][j].target == 6:
                globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img6, anchor='nw')
            if self.grid.tabCase[i][j].target == 7:
                globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img7, anchor='nw')
            if self.grid.tabCase[i][j].target == 8:
                globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img8, anchor='nw')
            if self.grid.tabCase[i][j].target == 9:
                globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img9, anchor='nw')
            if self.grid.tabCase[i][j].target == 10:
                globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img10, anchor='nw')
            if self.grid.tabCase[i][j].target == 11:
                globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img11, anchor='nw')
            if self.grid.tabCase[i][j].target == 12:
                globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img12, anchor='nw')
            if self.grid.tabCase[i][j].target == 13:
                globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img13, anchor='nw')
            if self.grid.tabCase[i][j].target == 14:
                globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img14, anchor='nw')
            if self.grid.tabCase[i][j].target == 15:
                globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img15, anchor='nw')
            if self.grid.tabCase[i][j].target == 16:
                globals.can.create_image(globals.x1 + 2, globals.y1 + 2, image=self.img16, anchor='nw')

        if self.grid.tabCase[i][j].down == 1:
            globals.can.create_line(globals.x1 + 2, globals.y2, globals.x2, globals.y2, fill="purple", width=5)
        if self.grid.tabCase[i][j].right == 1:
            globals.can.create_line(globals.x2, globals.y1, globals.x2, globals.y2, fill="purple", width=5)
        if self.grid.tabCase[i][j].left == 1:
            globals.can.create_line(globals.x1 + 2, globals.y1, globals.x1 + 2, globals.y2, fill="purple", width=5)
        if self.grid.tabCase[i][j].up == 1:
            globals.can.create_line(globals.x1 + 2, globals.y1 + 2, globals.x2, globals.y1 + 2, fill="purple",
                                    width=5)

    def game(self):
        # Jeu
        globals.targetColor = "notDefined"
        globals.currentTarget = -2
        globals.nbTurn = 0
        globals.nbMovePlayed = 0
        globals.listPositionPawn = []  # X Y idColor

        # initialisation du tour
        globals.nbMovePlayed = 0  # nombre de coup courant
        randomNumber = randint(1, 16)
        while globals.currentTarget == randomNumber:
            randomNumber = randint(1, 16)
        globals.currentTarget = randomNumber
        globals.can.create_image(360, 360, image=globals.listImg[globals.currentTarget + 16], anchor='nw')
        # on va chercher la couleur
        globals.targetColor = "notDefined"
        if (
                globals.currentTarget == 1 or globals.currentTarget == 4 or globals.currentTarget == 15
                or globals.currentTarget == 16):
            globals.targetColor = "green"
        if (
                globals.currentTarget == 2 or globals.currentTarget == 3 or globals.currentTarget == 10
                or globals.currentTarget == 11):
            globals.targetColor = "blue"
        if (
                globals.currentTarget == 5 or globals.currentTarget == 6 or globals.currentTarget == 13
                or globals.currentTarget == 14):
            globals.targetColor = "red"
        if (
                globals.currentTarget == 7 or globals.currentTarget == 8 or globals.currentTarget == 9
                or globals.currentTarget == 12):
            globals.targetColor = "orange"
        # on a couleur + symbole

        # On enregistre les positions des pions
        globals.listPositionPawn.clear()
        for i in range(16):
            for j in range(16):
                if self.grid.tabCase[i][j].pawn > -1:
                    globals.listPositionPawn.append([i, j, self.grid.tabCase[i][j].pawn])
        # print(listPositionPawn)
        #

        # print(currentTarget)
        # print(targetColor)
        self.changeText()

        # fin jeu

        ia = IA(self.grid)
        print('iterati : ', globals.iterations)

    def beforeLaunchGame(self):

        globals.x1, globals.y1, globals.x2, globals.y2 = 0, 0, 50, 50
        globals.couleur = 'white'

        self.fen = Tk()
        # TODO: remettre en 800 800
        globals.can = Canvas(self.fen, width=800, heigh=750, bg='ivory')

    def setImg(self):

        # Permet d'afficher les images, on a besoin de garder une référence sinon elle ne s'affichent pas
        self.img1 = PhotoImage(file="img/1.gif")
        self.img2 = PhotoImage(file="img/2.gif")
        self.img3 = PhotoImage(file="img/3.gif")
        self.img4 = PhotoImage(file="img/4.gif")
        self.img5 = PhotoImage(file="img/5.gif")
        self.img6 = PhotoImage(file="img/6.gif")
        self.img7 = PhotoImage(file="img/7.gif")
        self.img8 = PhotoImage(file="img/8.gif")
        self.img9 = PhotoImage(file="img/9.gif")
        self.img10 = PhotoImage(file="img/10.gif")
        self.img11 = PhotoImage(file="img/11.gif")
        self.img12 = PhotoImage(file="img/12.gif")
        self.img13 = PhotoImage(file="img/13.gif")
        self.img14 = PhotoImage(file="img/14.gif")
        self.img15 = PhotoImage(file="img/15.gif")
        self.img16 = PhotoImage(file="img/16.gif")
        self.img17 = PhotoImage(file="img/17.gif")
        self.img18 = PhotoImage(file="img/18.gif")
        self.img19 = PhotoImage(file="img/19.gif")
        self.img20 = PhotoImage(file="img/20.gif")
        self.img21 = PhotoImage(file="img/21.gif")
        self.img22 = PhotoImage(file="img/22.gif")
        self.img23 = PhotoImage(file="img/23.gif")
        self.img24 = PhotoImage(file="img/24.gif")
        self.img25 = PhotoImage(file="img/25.gif")
        self.img26 = PhotoImage(file="img/26.gif")
        self.img27 = PhotoImage(file="img/27.gif")
        self.img28 = PhotoImage(file="img/28.gif")
        self.img29 = PhotoImage(file="img/29.gif")
        self.img30 = PhotoImage(file="img/30.gif")
        self.img31 = PhotoImage(file="img/31.gif")
        self.img32 = PhotoImage(file="img/32.gif")
        label = Label(image=self.img1)
        label.image = self.img1  # keep a reference!

        globals.listImg = []
        globals.listImg.append(self.img1)  # jamais afficher
        globals.listImg.append(self.img1)
        globals.listImg.append(self.img2)
        globals.listImg.append(self.img3)
        globals.listImg.append(self.img4)
        globals.listImg.append(self.img5)
        globals.listImg.append(self.img6)
        globals.listImg.append(self.img7)
        globals.listImg.append(self.img8)
        globals.listImg.append(self.img9)
        globals.listImg.append(self.img10)
        globals.listImg.append(self.img11)
        globals.listImg.append(self.img12)
        globals.listImg.append(self.img13)
        globals.listImg.append(self.img14)
        globals.listImg.append(self.img15)
        globals.listImg.append(self.img16)
        globals.listImg.append(self.img17)
        globals.listImg.append(self.img18)
        globals.listImg.append(self.img19)
        globals.listImg.append(self.img20)
        globals.listImg.append(self.img21)
        globals.listImg.append(self.img22)
        globals.listImg.append(self.img23)
        globals.listImg.append(self.img24)
        globals.listImg.append(self.img25)
        globals.listImg.append(self.img26)
        globals.listImg.append(self.img27)
        globals.listImg.append(self.img28)
        globals.listImg.append(self.img29)
        globals.listImg.append(self.img30)
        globals.listImg.append(self.img31)
        globals.listImg.append(self.img32)

        globals.b1 = Button(self.fen, text='Jouer', command=self.chest)
        globals.b2 = Button(self.fen, text='Reset', command=self.reset)

        globals.can.pack(side=TOP, padx=5, pady=5)
        globals.b1.pack(side=LEFT, padx=3, pady=3)
        globals.b2.pack(side=LEFT, padx=3, pady=3)
   



        # text1= Text(self.fen, height=1,width=50)
        self.text_value = "turn : " + str(globals.nbTurn) + "                   move : " + str(
            globals.nbMovePlayed) + "                total : 0"

    # print(text_value)
    # text1.insert(INSERT,text_value)
    # text1.config(state ="disabled")
    # text1.pack()

    # TODO: A COMPLETER
    def changeText(self):
        total = 0
        for i in globals.nbMovePlayedTotal:
            total += i
        self.text_value = "turn : " + str(globals.nbTurn) + "                   move : " + str(
            globals.nbMovePlayed) + "              total : " + str(total)

    def launchGame(self):
        self.fen.mainloop()

    def displayEndOfTheGame(self):
        globals.can.delete("all")
        self.changeText()
        globals.can.pack()
        endMessage = "Fin de la partie ! Voici votre score : " + str(globals.nbMovePlayedTotal)
        endMessageIa = "Score de l'ia : " + "Ecrire le score de l'ia ici "

        globals.can.create_text(400, 400, text=endMessage)
        globals.can.create_text(400, 500, text=endMessageIa)
        globals.b2.config(state="disabled")
        globals.can.config(state="disabled")
