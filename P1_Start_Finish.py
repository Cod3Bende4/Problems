# Problem [Start_Finish]:

# 1. There is a Maze[n*m Matrix]
# 2. There are two poins inside the Maze, one is START and one is FINISH
# 3. Take matrix size as input and take co-ordinates from users as START and FINISH, for example (1,1) for taking first element as START and (n,m) for taking last element as START, same goes for FINISH.
# 4. Calculate number of ways by which one can travel from element to element to reach the FINISH point, starting from START, but one can't travel back to the same element which he had already traveled inside his START-FINISH journey.

# Example 

# Input:

# 2 3		# Maze Size (n*m)
# 1,1		# START
# 2,3		# FINISH

# Output:

# 4		# Number of ways to travel from START to FINISH without forming loop.

# Explaination:

# 		Matrix: 

# 			*(S) *    *
# 			*    *    *(F)

# Total number of ways to go from S to F are 4.

#Solution

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
