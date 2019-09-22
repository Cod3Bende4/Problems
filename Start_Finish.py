counter = 0

def no_of_paths(x,y):
    global counter
    counter+=1

    # print(x,y)
    if x == 1 or y == 1:
        return 1
    (no_of_paths(x-1, y) + no_of_paths(x, y-1))
    
    return counter - 1

print(no_of_paths(4,3))
