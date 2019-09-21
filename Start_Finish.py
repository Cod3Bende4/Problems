
#FOR PROBLEM STATEMENT READ "README.md"

# INPUTS
row,column = input(": ").split(" ")
startX, startY = input("Start: ").split(",")
finishX, finishY = input("Finish: ").split(",")

row = int(row) 
column = int(column)
startX = int(startX)-1
startY = int(startY)-1
finishX  = int(finishX)-1
finishY = int(finishY)-1

# Maze Formation

matrix_array = [["*" for i in range(column)] for i in range(row)]
print("")
matrix_array[startX][startY] = "S"
matrix_array[finishX][finishY] = "F"

# Printing Maze with Start and FINISH on it

for i in range(row):
    for j in range(column):
        print (matrix_array[i][j],end="  ")
    print("\n")

def checkSideElement(x,y):
    temp_array1=[]
    for i in ((x,y-1),(x-1,y),(x+1,y),(x,y+1)):
        try:
            if i[0] < 0 or i[1] < 0:
                pass
            else:
                if matrix_array[i[0]][i[1]]:
                    temp_array1.append(i)
        except:
            pass
    return temp_array1

# print (checkSideElement(1,2))

# to be continued