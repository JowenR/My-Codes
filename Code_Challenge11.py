for x in range(1, 5):
    for y in range(4, x, -1):
        print(" ", end=" ")
    for z in range(0, x * 2 - 1):
        print("*", end=" ")
    print()

for x in range(3, 0, -1):
    for y in range(4, x, -1):
        print(" ", end=" ")
    for z in range(0, x * 2 - 1):
        print("*", end=" ")
    print()
