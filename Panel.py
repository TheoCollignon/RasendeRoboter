import globals

from Case import Case


class Panel:

    """
    A class used to represent a Panel in a Grid

    ...

    Attributes
    ----------
    tabCase : list
        tabCase[i][j] is a 2D array of Case

    Methods
    -------
    rotate(pos, panelNb)
        It rotate the panel

    rotation(direction, nbRot)
        Add the rotated cases on the panel to complete its rotation
    """

    tabCase = 0

    def __init__(self, tabCaseArg):
        self.tabCase = tabCaseArg

    def rotate(self, pos, panelNb):
        if pos == panelNb:
            return self
        elif pos > panelNb:
            var = pos - panelNb
            return self.rotation(1, var)
        else:
            var = panelNb - pos
            return self.rotation(0, var)

    def rotation(self, direction, nbRot):
        tabCase2 = [[Case() for i in range(globals.sizeOfPanel)] for j in range(globals.sizeOfPanel)]
        panelTemp = Panel(tabCase2)
        for i in range(0, 8):
            for j in range(0, 8):
                if self.tabCase[i][j].up == 1 or self.tabCase[i][j].right == 1 or self.tabCase[i][j].left == 1 or \
                        self.tabCase[i][j].down == 1:
                    if direction:
                        if nbRot == 1:
                            panelTemp.tabCase[j][int(globals.sizeOfPanel) - 1 - i] = self.tabCase[i][j].rotCase(
                                direction, nbRot)
                        elif nbRot == 2:
                            panelTemp.tabCase[int(globals.sizeOfPanel) - 1 - i][
                                int(globals.sizeOfPanel) - 1 - j] = self.tabCase[i][j].rotCase(direction, nbRot)
                        elif nbRot == 3:
                            panelTemp.tabCase[int(globals.sizeOfPanel) - 1 - j][i] = self.tabCase[i][j].rotCase(
                                direction, nbRot)
                    else:
                        if nbRot == 1:
                            panelTemp.tabCase[int(globals.sizeOfPanel) - 1 - j][i] = self.tabCase[i][j].rotCase(
                                direction, nbRot)
                        elif nbRot == 2:
                            panelTemp.tabCase[int(globals.sizeOfPanel) - 1 - i][
                                int(globals.sizeOfPanel) - 1 - j] = self.tabCase[i][j].rotCase(direction, nbRot)
                        elif nbRot == 3:
                            panelTemp.tabCase[j][int(globals.sizeOfPanel) - 1 - i] = self.tabCase[i][j].rotCase(
                                direction, nbRot)
        return panelTemp
