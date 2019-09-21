row,column = input(": ").split(" ")
row = int(row) 
column = int(column)

matrix_array = []

for i in range(row):
    temp_array = input(">").split(" ")
    for j in range(len(temp_array)):
        temp_array[j] = int(temp_array[j])
    matrix_array.append(temp_array)

print(matrix_array[0][-2])

# for i in range(row):
#     for j in range(column):
#         print (matrix_array[i][j],end=" ")
#     print("")

def checkSideElement(x,y):
    temp_array1=[]
    try:
        temp_array1.append(matrix_array[x][y-1])
        print(matrix_array[0][2])
        print(1)
    except:
        pass
    try:
        temp_array1.append(matrix_array[x-1][y])
        print(2)
    except:
        pass
    try:
        temp_array1.append(matrix_array[x+1][y])
        print(3)
    except:
        pass
    try:
        temp_array1.append(matrix_array[x][y+1])
        print(4)
    except:
        pass
    return temp_array1

print (checkSideElement(0,0))