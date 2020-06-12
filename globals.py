global b1
global b2
global can
global click
global couleur
global currentTarget
global iterations
global lastX
global lastY
global listeChemin
global listeCheminGagnant
global listImg
global listLongestWay
global listPawnIa
global listPositionPawn
global listShortestWay
global longestWay
global nbMovePlayed
global nbMovePlayedTotal
global nbTurn
global pawnX
global pawnY
global sizeOfGrid
global sizeOfPanel
global shortestWay
global targetColor
global targetColorIa
global targetX
global targetY
global x1
global x2
global y1
global y2

def initialize():
    global b1
    global b2
    global can
    global click
    global couleur
    global currentTarget
    global iterations
    global lastX
    global lastY
    global listeChemin
    global listeCheminGagnant
    global listImg
    global listLongestWay
    global listPawnIa
    global listPositionPawn
    global listShortestWay
    global longestWay
    global nbMovePlayed
    global nbMovePlayedTotal
    global nbTurn
    global pawnX
    global pawnY
    global sizeOfGrid
    global sizeOfPanel
    global shortestWay
    global targetColor
    global targetColorIa
    global targetX
    global targetY
    global x1
    global x2
    global y1
    global y2

    click = 1
    currentTarget = -2
    iterations = 1
    lastX = -1
    lastY = -1
    listeChemin = []
    listeCheminGagnant = []
    listImg = []
    listLongestWay = []
    listPawnIa = []
    listPositionPawn = []
    listShortestWay = []
    longestWay = -10
    nbMovePlayed = 0
    nbMovePlayedTotal = []
    nbTurn = 0
    pawnX = -1
    pawnY = -1
    shortestWay = 1000000
    sizeOfGrid = 16
    sizeOfPanel = 8
    targetColor = "notDefined"
    x1 = 0
    x2 = 0
    y1 = 50
    y2 = 50
