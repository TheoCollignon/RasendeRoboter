import globals
from Case import Case
from Grid import Grid
from Visual import Visual


globals.initialize()

grid = Grid([[Case() for i in range(globals.sizeOfGrid)] for j in range(globals.sizeOfGrid)])

visual = Visual(grid)
