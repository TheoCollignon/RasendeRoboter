import globals

import copy

from Case import Case
from Panel import Panel


class IA:
    tabCase = []

    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)
        self.beforeIaSetup(2)

    def getColorTarget(self):
        if globals.currentTarget == 1 or globals.currentTarget == 4 or globals.currentTarget == 15 or globals.currentTarget == 16:
            globals.targetColorIa = 2
        if globals.currentTarget == 2 or globals.currentTarget == 3 or globals.currentTarget == 10 or globals.currentTarget == 11:
            globals.targetColorIa = 0
        if globals.currentTarget == 5 or globals.currentTarget == 6 or globals.currentTarget == 13 or globals.currentTarget == 14:
            globals.targetColorIa = 3
        if globals.currentTarget == 7 or globals.currentTarget == 8 or globals.currentTarget == 9 or globals.currentTarget == 12:
            globals.targetColorIa = 1

    def beforeIaSetup(self, difficulty):  # Pour setup l'ia, comme ça on évite des répétitions de boucles inutiles
        globals.shortestWay = 100000
        globals.longestWay = -100
        listeChemin = []
        listeChemin.clear()
        listPawnIa = []
        listPawnIa.clear()
        self.getColorTarget()
        self.grid.getCoordTarget()
        # on doit remplir la liste des pawn
        for w in range(4):
            for i in range(16):
                for j in range(16):
                    if self.grid.tabCase[i][j].pawn == w:
                        listPawnIa.append([i, j, w])

        if difficulty == 1:
            print("Difficulté 1 : Première solution")
            for i in range(4):
                if i != globals.targetColorIa:
                    if self.testFirstSolution(globals.targetColorIa, i, 8, listPawnIa, 8, listeChemin):
                        break
        elif difficulty == 2:
            print("Difficulté 2 : Utilisation d'un seul pion")
            self.testPionUnique(globals.targetColorIa, 10, listPawnIa, 10, listeChemin)
        else :
            print("Difficulté 3 : Utilisation de deux pions")
            self.testPionUnique(globals.targetColorIa, 10, listPawnIa, 10, listeChemin)

            if len(globals.listeCheminGagnant) == 0:
                print("pas en 1 pion")

                # pion couleur principal + 3 autres
                pawnColor = globals.targetColorIa
                for i in range(4):
                    if i != pawnColor:
                        self.testDeuxPions(pawnColor, i, 7, listPawnIa, 7, listeChemin)

        # self.IaBrutForce(4, listPawnIa, 0, 4, listeChemin)


    def goUpIa(self, i, j, listPawnIabis, pawnID):
        iIter = i
        jIter = j
        if self.isUpIa(iIter, jIter, listPawnIabis) == 0:
            iIter = i - 1
            listPawnIabis[pawnID] = [iIter, j, pawnID]
            self.goUpIa(iIter, jIter, listPawnIabis, pawnID)

    def goLeftIa(self, i, j, listPawnIabis, pawnID):
        iIter = i
        jIter = j
        if self.isLeftIa(iIter, jIter, listPawnIabis) == 0:
            jIter = j - 1
            listPawnIabis[pawnID] = [i, jIter, pawnID]
            self.goLeftIa(iIter, jIter, listPawnIabis, pawnID)

    def goRightIa(self, i, j, listPawnIabis, pawnID):
        iIter = i
        jIter = j
        if self.isRightIa(iIter, jIter, listPawnIabis) == 0:
            jIter = j + 1
            listPawnIabis[pawnID] = [i, jIter, pawnID]
            self.goRightIa(iIter, jIter, listPawnIabis, pawnID)

    def goDownIa(self, i, j, listPawnIabis, pawnID):
        iIter = i
        jIter = j
        if self.isDownIa(iIter, jIter, listPawnIabis) == 0:
            iIter += 1
            listPawnIabis[pawnID] = [iIter, j, pawnID]
            self.goDownIa(iIter, jIter, listPawnIabis, pawnID)

    def isUpIa(self, i, j, listPawnIa):
        if self.grid.tabCase[i][j].up == 1:
            return 1
        elif i - 1 >= 0:
            if self.grid.tabCase[i - 1][j].down == 1:
                return 1
            for w in range(4):
                if (i - 1) == listPawnIa[w][0] and (j == listPawnIa[w][1]):
                    return 1
        return 0

    def isLeftIa(self, i, j, listPawnIa):
        if self.grid.tabCase[i][j].left == 1:
            return 1
        elif j - 1 >= 0:
            if self.grid.tabCase[i][j - 1].right == 1:
                return 1
            for w in range(4):
                if i == listPawnIa[w][0] and ((j - 1) == listPawnIa[w][1]):
                    return 1
        return 0

    def isRightIa(self, i, j, listPawnIa):
        if self.grid.tabCase[i][j].right == 1:
            return 1
        elif j + 1 <= 15:
            if self.grid.tabCase[i][j + 1].left == 1:
                return 1
            for w in range(4):
                if i == listPawnIa[w][0] and ((j + 1) == listPawnIa[w][1]):
                    return 1
        return 0

    def isDownIa(self, i, j, listPawnIa):
        if self.grid.tabCase[i][j].down == 1:
            return 1
        elif i + 1 <= 15:
            if self.grid.tabCase[i + 1][j].up == 1:
                return 1
            for w in range(4):
                if (i + 1) == listPawnIa[w][0] and (j == listPawnIa[w][1]):
                    return 1
        return 0

    def displayChemin(self, listeChemin):
        color = ''
        direction = ''
        for i in listeChemin:
            if i[0] == 0:
                color = 'Blue'
            if i[0] == 1:
                color = 'Orange'
            if i[0] == 2:
                color = 'Green'
            if i[0] == 3:
                color = 'Red'
            if i[1] == 0:
                direction = 'Up'
            if i[1] == 1:
                direction = 'Down'
            if i[1] == 2:
                direction = 'Right'
            if i[1] == 3:
                direction = 'Left'
            print(color + ' ' + direction + ' | ', end='')
        print()

    def testFirstSolution(self, pion, pion2, limite, listPawnIa, limite_max, listeChemin):
        nbCoup = limite_max - limite
        p = pion
        p2 = pion2
        if limite < 0:
            return False

        # verification
        if globals.targetX == listPawnIa[p][0] and globals.targetY == listPawnIa[p][1]:  # getPawnbyId
            # print("cc : " + str(pawn_color) + " target : " + str(targetColorIa))
            if p == globals.targetColorIa:
                # print("cc : " + str(pawn_color) + " target : " + str(targetColorIa))
                print("tro b1")
                print("nb de coup : " + str(limite_max - limite))

                print("first solution : ", end='')
                self.displayChemin(listeChemin)
                return True
        limite -= 1

        for i in range(4):
            if i == p or i == p2:
                # on regarde si il y'a des murs #0 = up // 1 = bas // 2 = droite // 3 = gauche
                if self.isUpIa(listPawnIa[i][0], listPawnIa[i][1],
                               listPawnIa) == 0:  # si y'a pas de murs,on déplace et on rappel la fonction
                    if nbCoup > 0:
                        if listeChemin[nbCoup - 1][0] == i:
                            if not (listeChemin[nbCoup - 1][1] == 1):
                                listPawnIabis = copy.deepcopy(listPawnIa)
                                listeCheminBis = copy.deepcopy(listeChemin)
                                listeCheminBis.append([i, 0])
                                self.goUpIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                                globals.iterations += 1
                                if self.testFirstSolution(p, p2, limite, listPawnIabis, limite_max, listeCheminBis):
                                    return True
                        else:
                            listPawnIabis = copy.deepcopy(listPawnIa)
                            listeCheminBis = copy.deepcopy(listeChemin)
                            listeCheminBis.append([i, 0])
                            self.goUpIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                            globals.iterations += 1
                            if self.testFirstSolution(p, p2, limite, listPawnIabis, limite_max, listeCheminBis):
                                return True
                    else:
                        listPawnIabis = copy.deepcopy(listPawnIa)
                        listeCheminBis = copy.deepcopy(listeChemin)
                        listeCheminBis.append([i, 0])
                        self.goUpIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                        globals.iterations += 1
                        if self.testFirstSolution(p, p2, limite, listPawnIabis, limite_max, listeCheminBis):
                            return True

                if self.isDownIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIa) == 0:
                    if nbCoup > 0:
                        if listeChemin[nbCoup - 1][0] == i:
                            if not (listeChemin[nbCoup - 1][1] == 0):
                                listPawnIabis = copy.deepcopy(listPawnIa)
                                listeCheminBis = copy.deepcopy(listeChemin)
                                listeCheminBis.append([i, 1])
                                self.goDownIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                                globals.iterations += 1
                                if self.testFirstSolution(p, p2, limite, listPawnIabis, limite_max, listeCheminBis):
                                    return True
                        else:
                            listPawnIabis = copy.deepcopy(listPawnIa)
                            listeCheminBis = copy.deepcopy(listeChemin)
                            listeCheminBis.append([i, 1])
                            self.goDownIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                            globals.iterations += 1
                            if self.testFirstSolution(p, p2, limite, listPawnIabis, limite_max, listeCheminBis):
                                return True
                    else:
                        listPawnIabis = copy.deepcopy(listPawnIa)
                        listeCheminBis = copy.deepcopy(listeChemin)
                        listeCheminBis.append([i, 1])
                        self.goDownIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                        globals.iterations += 1
                        if self.testFirstSolution(p, p2, limite, listPawnIabis, limite_max, listeCheminBis):
                            return True

                if self.isRightIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIa) == 0:
                    if nbCoup > 0:
                        if listeChemin[nbCoup - 1][0] == i:
                            if not (listeChemin[nbCoup - 1][1] == 3):
                                listPawnIabis = copy.deepcopy(listPawnIa)
                                listeCheminBis = copy.deepcopy(listeChemin)
                                listeCheminBis.append([i, 2])
                                self.goRightIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                                globals.iterations += 1
                                if self.testFirstSolution(p, p2, limite, listPawnIabis, limite_max, listeCheminBis):
                                    return True
                        else:
                            listPawnIabis = copy.deepcopy(listPawnIa)
                            listeCheminBis = copy.deepcopy(listeChemin)
                            listeCheminBis.append([i, 2])
                            self.goRightIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                            globals.iterations += 1
                            if self.testFirstSolution(p, p2, limite, listPawnIabis, limite_max, listeCheminBis):
                                return True
                    else:
                        listPawnIabis = copy.deepcopy(listPawnIa)
                        listeCheminBis = copy.deepcopy(listeChemin)
                        listeCheminBis.append([i, 2])
                        self.goRightIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                        globals.iterations += 1
                        if self.testFirstSolution(p, p2, limite, listPawnIabis, limite_max, listeCheminBis):
                            return True

                if self.isLeftIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIa) == 0:
                    if nbCoup > 0:
                        if listeChemin[nbCoup - 1][0] == i:
                            if not (listeChemin[nbCoup - 1][1] == 2):
                                listPawnIabis = copy.deepcopy(listPawnIa)
                                listeCheminBis = copy.deepcopy(listeChemin)
                                listeCheminBis.append([i, 3])
                                self.goLeftIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                                globals.iterations += 1
                                if self.testFirstSolution(p, p2, limite, listPawnIabis, limite_max, listeCheminBis):
                                    return True
                        else:
                            listPawnIabis = copy.deepcopy(listPawnIa)
                            listeCheminBis = copy.deepcopy(listeChemin)
                            listeCheminBis.append([i, 3])
                            self.goLeftIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                            globals.iterations += 1
                            if self.testFirstSolution(p, p2, limite, listPawnIabis, limite_max, listeCheminBis):
                                return True
                    else:
                        listPawnIabis = copy.deepcopy(listPawnIa)
                        listeCheminBis = copy.deepcopy(listeChemin)
                        listeCheminBis.append([i, 3])
                        self.goLeftIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                        globals.iterations += 1
                        if self.testFirstSolution(p, p2, limite, listPawnIabis, limite_max, listeCheminBis):
                            return True

    def IaBrutForce(self, limite, listPawnIa, pawn_color, limite_max, listeChemin):
        nbCoup = limite_max - limite
        if limite < 0:
            return False
        if globals.targetX == listPawnIa[pawn_color][0] and globals.targetY == listPawnIa[pawn_color][
            1]:
            # print("cc : " + str(pawn_color) + " target : " + str(targetColorIa))
            if pawn_color == globals.targetColorIa:
                # print("cc : " + str(pawn_color) + " target : " + str(targetColorIa))
                for w in range(4):
                    print("liste ia quand on a trouvé : " + str(globals.listPawnIa[w][0]) + "  " + str(
                        globals.listPawnIa[w][1]) + " id : " + str(globals.listPawnIa[w][2]))
                print("tro b1")
                print("nb de coup : " + str(limite_max - limite))

                print("LISTE CHEMIN: ", listeChemin)
                globals.listeCheminGagnant.append(listeChemin)
                for i in globals.listeCheminGagnant:
                    if globals.shortestWay > len(i):
                        globals.shortestWay = len(i)
                        globals.listShortestWay = i
                    if globals.longestWay < len(i):
                        globals.longestWay = len(i)
                        globals.listLongestWay = i
                print("shortestWay : ", end='')
                print(globals.listShortestWay)
                print(" longestWay : ", end='')
                print(globals.listLongestWay)
                return True
        limite -= 1

        if (nbCoup + 1) < globals.shortestWay:
            for i in range(4):  # parcours 4 pions
                # on regarde si il y'a des murs #0 = up // 1 = bas // 2 = droite // 3 = gauche
                # si y'a pas de murs,on déplace et on rappel la fonction
                if self.isUpIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIa) == 0:
                    if nbCoup > 0:
                        if listeChemin[nbCoup - 1][0] == i:
                            if not (listeChemin[nbCoup - 1][1] == 1):
                                listPawnIabis = copy.deepcopy(listPawnIa)
                                listeCheminBis = copy.deepcopy(listeChemin)
                                listeCheminBis.append([i, 0])
                                self.goUpIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                                globals.iterations += 1
                                self.IaBrutForce(limite, listPawnIa, pawn_color, limite_max, listeCheminBis)
                        else:
                            listPawnIabis = copy.deepcopy(listPawnIa)
                            listeCheminBis = copy.deepcopy(listeChemin)
                            listeCheminBis.append([i, 0])
                            self.goUpIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                            globals.iterations += 1
                            self.IaBrutForce(limite, listPawnIa, pawn_color, limite_max, listeCheminBis)
                    else:
                        listPawnIabis = copy.deepcopy(listPawnIa)
                        listeCheminBis = copy.deepcopy(listeChemin)
                        listeCheminBis.append([i, 0])
                        self.goUpIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                        globals.iterations += 1
                        self.IaBrutForce(limite, listPawnIa, pawn_color, limite_max, listeCheminBis)
                if self.isDownIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIa) == 0:
                    if nbCoup > 0:
                        print("NBCOUP - 1: ", nbCoup - 1)
                        print("LEN: ", len(listeChemin))
                        if listeChemin[nbCoup - 1][0] == i:
                            if not (listeChemin[nbCoup - 1][1] == 0):
                                listPawnIabis = copy.deepcopy(listPawnIa)
                                listeCheminBis = copy.deepcopy(listeChemin)
                                listeCheminBis.append([i, 1])
                                self.goDownIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                                globals.iterations += 1
                                self.IaBrutForce(limite, listPawnIa, pawn_color, limite_max, listeCheminBis)
                        else:
                            listPawnIabis = copy.deepcopy(listPawnIa)
                            listeCheminBis = copy.deepcopy(listeChemin)
                            listeCheminBis.append([i, 1])
                            self.goDownIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                            globals.iterations += 1
                            self.IaBrutForce(limite, listPawnIa, pawn_color, limite_max, listeCheminBis)
                    else:
                        listPawnIabis = copy.deepcopy(listPawnIa)
                        listeCheminBis = copy.deepcopy(listeChemin)
                        listeCheminBis.append([i, 1])
                        self.goDownIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                        globals.iterations += 1
                        self.IaBrutForce(limite, listPawnIa, pawn_color, limite_max, listeCheminBis)
                # if self.isRightIa(globals.listPawnIa[i][0], globals.listPawnIa[i][1]) == 0:
                if self.isRightIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIa) == 0:
                    if nbCoup > 0:
                        if listeChemin[nbCoup - 1][0] == i:
                            if not (listeChemin[nbCoup - 1][1] == 3):
                                listPawnIabis = copy.deepcopy(listPawnIa)
                                listeCheminBis = copy.deepcopy(listeChemin)
                                listeCheminBis.append([i, 2])
                                # goRightIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                                self.goRightIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                                globals.iterations += 1
                                # IaBrutForce(limite, listPawnIabis, i, limite_max, listeCheminBis)
                                self.IaBrutForce(limite, listPawnIa, pawn_color, limite_max, listeCheminBis)
                        else:
                            listPawnIabis = copy.deepcopy(listPawnIa)
                            listeCheminBis = copy.deepcopy(listeChemin)
                            listeCheminBis.append([i, 2])
                            self.goRightIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                            globals.iterations += 1
                            self.IaBrutForce(limite, listPawnIa, pawn_color, limite_max, listeCheminBis)
                    else:
                        listPawnIabis = copy.deepcopy(listPawnIa)
                        listeCheminBis = copy.deepcopy(listeChemin)
                        listeCheminBis.append([i, 2])
                        self.goRightIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                        globals.iterations += 1
                        self.IaBrutForce(limite, listPawnIa, pawn_color, limite_max, listeCheminBis)
                if self.isLeftIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIa) == 0:
                    if nbCoup > 0:
                        if listeChemin[nbCoup - 1][0] == i:
                            if not (listeChemin[nbCoup - 1][1] == 2):
                                listPawnIabis = copy.deepcopy(listPawnIa)
                                listeCheminBis = copy.deepcopy(listeChemin)
                                listeCheminBis.append([i, 3])
                                self.goLeftIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                                globals.iterations += 1
                                self.IaBrutForce(limite, listPawnIa, pawn_color, limite_max, listeCheminBis)
                        else:
                            listPawnIabis = copy.deepcopy(listPawnIa)
                            listeCheminBis = copy.deepcopy(listeChemin)
                            listeCheminBis.append([i, 3])
                            self.goLeftIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                            globals.iterations += 1
                            self.IaBrutForce(limite, listPawnIa, pawn_color, limite_max, listeCheminBis)
                    else:
                        listPawnIabis = copy.deepcopy(listPawnIa)
                        listeCheminBis = copy.deepcopy(listeChemin)
                        listeCheminBis.append([i, 3])
                        self.goLeftIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                        globals.iterations += 1
                        self.IaBrutForce(limite, listPawnIa, pawn_color, limite_max, listeCheminBis)

    def testPionUnique(self, pion, limite, listPawnIa, limite_max, listeChemin):
        nbCoup = limite_max - limite
        i = pion
        if limite < 0:
            return False

        if globals.targetX == listPawnIa[i][0] and globals.targetY == listPawnIa[i][1]:  # getPawnbyId
            # print("cc : " + str(pawn_color) + " target : " + str(targetColorIa))
            if i == globals.targetColorIa:
                # print("cc : " + str(pawn_color) + " target : " + str(targetColorIa))
                #for w in range(4):
                #    print("liste ia quand on a trouvé : " + str(listPawnIa[w][0]) + "  " + str(listPawnIa[w][1]) + " id : " + str(listPawnIa[w][2]))
                print("tro b1")
                print("nb de coup : " + str(limite_max - limite))

                self.displayChemin(listeChemin)
                globals.listeCheminGagnant.append(listeChemin)
                for y in globals.listeCheminGagnant:
                    if globals.shortestWay > len(y):
                        globals.shortestWay = len(y)
                        globals.listShortestWay = y
                    if globals.longestWay < len(y):
                        globals.longestWay = len(y)
                        globals.listLongestWay = y
                print("shortestWay : ", end='')
                #print(globals.listShortestWay)
                self.displayChemin(globals.listShortestWay)
                print(" longestWay : ", end='')
                #print(globals.listLongestWay)
                self.displayChemin(globals.listLongestWay)
                return True
        limite -= 1

        if (nbCoup + 1) < globals.shortestWay:
            if self.isUpIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIa) == 0:
                listPawnIabis = copy.deepcopy(listPawnIa)
                listeCheminBis = copy.deepcopy(listeChemin)
                listeCheminBis.append([i, 0])
                self.goUpIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                globals.iterations += 1
                self.testPionUnique(i, limite, listPawnIabis, limite_max, listeCheminBis)
            if self.isDownIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIa) == 0:
                listPawnIabis = copy.deepcopy(listPawnIa)
                listeCheminBis = copy.deepcopy(listeChemin)
                listeCheminBis.append([i, 1])
                self.goDownIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                globals.iterations += 1
                self.testPionUnique(i, limite, listPawnIabis, limite_max, listeCheminBis)
            if self.isRightIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIa) == 0:
                listPawnIabis = copy.deepcopy(listPawnIa)
                listeCheminBis = copy.deepcopy(listeChemin)
                listeCheminBis.append([i, 2])
                self.goRightIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                globals.iterations += 1
                self.testPionUnique(i, limite, listPawnIabis, limite_max, listeCheminBis)
            if self.isLeftIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIa) == 0:
                listPawnIabis = copy.deepcopy(listPawnIa)
                listeCheminBis = copy.deepcopy(listeChemin)
                listeCheminBis.append([i, 3])
                self.goLeftIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                globals.iterations += 1
                self.testPionUnique(i, limite, listPawnIabis, limite_max, listeCheminBis)

    def testDeuxPions(self, pion, pion2, limite, listPawnIa, limite_max, listeChemin):
        nbCoup = limite_max - limite

        p = pion
        p2 = pion2
        if limite < 0:
            return False

        # verification
        if globals.targetX == listPawnIa[p][0] and globals.targetY == listPawnIa[p][1]:  # getPawnbyId
            # print("cc : " + str(pawn_color) + " target : " + str(targetColorIa))
            if p == globals.targetColorIa:
                # print("cc : " + str(pawn_color) + " target : " + str(targetColorIa))

                #for w in range(4):
                #    print("liste ia quand on a trouvé : " + str(listPawnIa[w][0]) + "  " + str(
                #        listPawnIa[w][1]) + " id : " + str(listPawnIa[w][2]))
                print("tro b1")
                print("nb de coup : " + str(limite_max - limite))

                self.displayChemin(listeChemin)
                globals.listeCheminGagnant.append(listeChemin)
                for y in globals.listeCheminGagnant:
                    if globals.shortestWay > len(y):
                        globals.shortestWay = len(y)
                        globals.listShortestWay = y
                    if globals.longestWay < len(y):
                        globals.longestWay = len(y)
                        globals.listLongestWay = y
                print("shortestWay : ", end='')
                #print(globals.listShortestWay)
                self.displayChemin(globals.listShortestWay)
                print(" longestWay : ", end='')
                #print(globals.listLongestWay)
                self.displayChemin(globals.listLongestWay)
                return True
        limite -= 1

        if (nbCoup + 1) < globals.shortestWay:
            for i in range(4):
                if i == p or (nbCoup + 2 < globals.shortestWay and i == p2):
                    # on regarde si il y'a des murs #0 = up // 1 = bas // 2 = droite // 3 = gauche
                    if (self.isUpIa(listPawnIa[i][0], listPawnIa[i][1],
                                    listPawnIa) == 0):  # si y'a pas de murs,on déplace et on rappel la fonction
                        if nbCoup > 0:
                            if listeChemin[nbCoup - 1][0] == i:
                                if not (listeChemin[nbCoup - 1][1] == 1):
                                    listPawnIabis = copy.deepcopy(listPawnIa)
                                    listeCheminBis = copy.deepcopy(listeChemin)
                                    listeCheminBis.append([i, 0])
                                    self.goUpIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                                    globals.iterations += 1
                                    self.testDeuxPions(p, p2, limite, listPawnIabis, limite_max, listeCheminBis)
                            else:
                                listPawnIabis = copy.deepcopy(listPawnIa)
                                listeCheminBis = copy.deepcopy(listeChemin)
                                listeCheminBis.append([i, 0])
                                self.goUpIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                                globals.iterations += 1
                                self.testDeuxPions(p, p2, limite, listPawnIabis, limite_max, listeCheminBis)
                        else:
                            listPawnIabis = copy.deepcopy(listPawnIa)
                            listeCheminBis = copy.deepcopy(listeChemin)
                            listeCheminBis.append([i, 0])
                            self.goUpIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                            globals.iterations += 1
                            self.testDeuxPions(p, p2, limite, listPawnIabis, limite_max, listeCheminBis)

                    if self.isDownIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIa) == 0:
                        if nbCoup > 0:
                            if listeChemin[nbCoup - 1][0] == i:
                                if not (listeChemin[nbCoup - 1][1] == 0):
                                    listPawnIabis = copy.deepcopy(listPawnIa)
                                    listeCheminBis = copy.deepcopy(listeChemin)
                                    listeCheminBis.append([i, 1])
                                    self.goDownIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                                    globals.iterations += 1
                                    self.testDeuxPions(p, p2, limite, listPawnIabis, limite_max, listeCheminBis)
                            else:
                                listPawnIabis = copy.deepcopy(listPawnIa)
                                listeCheminBis = copy.deepcopy(listeChemin)
                                listeCheminBis.append([i, 1])
                                self.goDownIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                                globals.iterations += 1
                                self.testDeuxPions(p, p2, limite, listPawnIabis, limite_max, listeCheminBis)
                        else:
                            listPawnIabis = copy.deepcopy(listPawnIa)
                            listeCheminBis = copy.deepcopy(listeChemin)
                            listeCheminBis.append([i, 1])
                            self.goDownIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                            globals.iterations += 1
                            self.testDeuxPions(p, p2, limite, listPawnIabis, limite_max, listeCheminBis)

                    if self.isRightIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIa) == 0:
                        if nbCoup > 0:
                            if listeChemin[nbCoup - 1][0] == i:
                                if not (listeChemin[nbCoup - 1][1] == 3):
                                    listPawnIabis = copy.deepcopy(listPawnIa)
                                    listeCheminBis = copy.deepcopy(listeChemin)
                                    listeCheminBis.append([i, 2])
                                    self.goRightIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                                    globals.iterations += 1
                                    self.testDeuxPions(p, p2, limite, listPawnIabis, limite_max, listeCheminBis)
                            else:
                                listPawnIabis = copy.deepcopy(listPawnIa)
                                listeCheminBis = copy.deepcopy(listeChemin)
                                listeCheminBis.append([i, 2])
                                self.goRightIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                                globals.iterations += 1
                                self.testDeuxPions(p, p2, limite, listPawnIabis, limite_max, listeCheminBis)
                        else:
                            listPawnIabis = copy.deepcopy(listPawnIa)
                            listeCheminBis = copy.deepcopy(listeChemin)
                            listeCheminBis.append([i, 2])
                            self.goRightIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                            globals.iterations += 1
                            self.testDeuxPions(p, p2, limite, listPawnIabis, limite_max, listeCheminBis)

                    if self.isLeftIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIa) == 0:
                        if nbCoup > 0:
                            if listeChemin[nbCoup - 1][0] == i:
                                if not (listeChemin[nbCoup - 1][1] == 2):
                                    listPawnIabis = copy.deepcopy(listPawnIa)
                                    listeCheminBis = copy.deepcopy(listeChemin)
                                    listeCheminBis.append([i, 3])
                                    self.goLeftIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                                    globals.iterations += 1
                                    self.testDeuxPions(p, p2, limite, listPawnIabis, limite_max, listeCheminBis)
                            else:
                                listPawnIabis = copy.deepcopy(listPawnIa)
                                listeCheminBis = copy.deepcopy(listeChemin)
                                listeCheminBis.append([i, 3])
                                self.goLeftIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                                globals.iterations += 1
                                self.testDeuxPions(p, p2, limite, listPawnIabis, limite_max, listeCheminBis)
                        else:
                            listPawnIabis = copy.deepcopy(listPawnIa)
                            listeCheminBis = copy.deepcopy(listeChemin)
                            listeCheminBis.append([i, 3])
                            self.goLeftIa(listPawnIa[i][0], listPawnIa[i][1], listPawnIabis, i)
                            globals.iterations += 1
                            self.testDeuxPions(p, p2, limite, listPawnIabis, limite_max, listeCheminBis)
