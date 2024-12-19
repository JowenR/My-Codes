for x in range(1, 6):
    for y in range(5, x, -1):
        print(" ", end=" ")
    for z in range(0, x * 2):
        print("*", end=" ")
    print()

for x in range(5, 0, -1):
    for y in range(5, x, -1):
        print(" ", end=" ")
    for z in range(0, x * 2):
        print("^", end=" ")
    print()
