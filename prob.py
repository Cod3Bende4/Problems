def no_of_paths(x,y):
    print(x,y)

    if x == 1 or y == 1:
        return 1

    temp = (no_of_paths(x-1, y) + no_of_paths(x, y-1))

    return temp


print(no_of_paths(4,4))
