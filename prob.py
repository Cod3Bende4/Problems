def no_of_paths(x,y):

    if x == 1 or y == 1:
        return 1

    return (no_of_paths(x-1, y) + no_of_paths(x, y-1))


print(no_of_paths(4,4))
