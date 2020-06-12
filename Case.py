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
        self.pawn = -1

    def rotCase(self, direction, nbRot):  # rotates one case
        caseTemp = Case()
        if self.target != 0:
            caseTemp.target = self.target
        if (direction):  # clock-wise
            if (self.down == 1):
                if (nbRot == 1):
                    caseTemp.left = 1
                if (nbRot == 2):
                    caseTemp.up = 1
                if (nbRot == 3):
                    caseTemp.right = 1
            if (self.up == 1):
                if (nbRot == 1):
                    caseTemp.right = 1
                if (nbRot == 2):
                    caseTemp.down = 1
                if (nbRot == 3):
                    caseTemp.left = 1
            if (self.left == 1):
                if (nbRot == 1):
                    caseTemp.up = 1
                if (nbRot == 2):
                    caseTemp.right = 1
                if (nbRot == 3):
                    caseTemp.down = 1
            if (self.right == 1):
                if (nbRot == 1):
                    caseTemp.down = 1
                if (nbRot == 2):
                    caseTemp.left = 1
                if (nbRot == 3):
                    caseTemp.up = 1
        else:  # anti-clock-wise
            if (self.down == 1):
                if (nbRot == 1):
                    caseTemp.right = 1
                if (nbRot == 2):
                    caseTemp.up = 1
                if (nbRot == 3):
                    caseTemp.left = 1
            if (self.up == 1):
                if (nbRot == 1):
                    caseTemp.left = 1
                if (nbRot == 2):
                    caseTemp.down = 1
                if (nbRot == 3):
                    caseTemp.right = 1
            if (self.left == 1):
                if (nbRot == 1):
                    caseTemp.down = 1
                if (nbRot == 2):
                    caseTemp.right = 1
                if (nbRot == 3):
                    caseTemp.up = 1
            if (self.right == 1):
                if (nbRot == 1):
                    caseTemp.up = 1
                if (nbRot == 2):
                    caseTemp.left = 1
                if (nbRot == 3):
                    caseTemp.down = 1

        return caseTemp
