global b1
global b2
global bFacile,bMoyen,bDifficile
global bFacile_w,bMoyen_w,bDifficile_w
global difficulty
global can
global click
global couleur
global currentTarget
global endMessageIa
global gameOver
global iterations
global lastX
global lastY
global label
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
global nbTurnTotalToFinishTheGame
global pawnX
global pawnY
global scoreIA
global scoreJoueurTotal
global sizeOfGrid
global sizeOfPanel
global shortestWay
global targetColor
global targetColorIa
global targetX
global targetY
global text1
global x1
global x2
global y1
global y2

def initialize():
    global b1
    global b2
    global bFacile,bMoyen,bDifficile
    global bFacile_w,bMoyen_w,bDifficile_w
    global difficulty
    global can
    global click
    global couleur
    global currentTarget
    global endMessageIa
    global gameOver
    global iterations
    global lastX
    global lastY
    global label
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
    global nbTurnTotalToFinishTheGame
    global pawnX
    global pawnY
    global scoreIA
    global scoreJoueurTotal
    global sizeOfGrid
    global sizeOfPanel
    global shortestWay
    global targetColor
    global targetColorIa
    global targetX
    global targetY
    global text1
    global x1
    global x2
    global y1
    global y2

    
    click = 1
    difficulty = -1
    currentTarget = -2
    gameOver = False
    endMessageIa = ""
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
    nbTurnTotalToFinishTheGame = 2
    pawnX = -1
    pawnY = -1
    shortestWay = 1000000
    scoreIA = 0
    scoreJoueurTotal = 0
    sizeOfGrid = 16
    sizeOfPanel = 8
    targetColor = "notDefined"
    x1 = 0
    x2 = 0
    y1 = 50
    y2 = 50
