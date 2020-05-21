class Case:
    right = 0
    down = 0
    left = 0
    up = 0

    def __init__(self, right, down, left, up):
        self.right = right
        self.down = down
        self.left = left
        self.up = up


print("PROJECT INITIALIZATION\n")
sizeOfGrid = 16

# init grid with initial border
grid = [[Case(0, 0, 0, 0) for i in range(sizeOfGrid)] for j in range(sizeOfGrid)]
for i in range(sizeOfGrid):
    for j in range(sizeOfGrid):
        case = Case(0,0,0,0)
        if(i==0):
            case.up = 1
        elif (i == sizeOfGrid-1):
            case.down = 1
        elif (j == 0):
            case.left = 1
        elif (j == sizeOfGrid-1):
            case.right = 9
        grid[i][j] = case

'''
# Verification : up - down - left - right
for i in range(sizeOfGrid):
    print()
    for j in range(sizeOfGrid):
        print(grid[i][j].down,end ='')
'''

print("\n")
print("Checking sizeOfGrid:")
print(len(grid))
