for x in range(1, 5):
    for y in range(5, x, -1):
        print(" ", end=" ")
    for z in range(0, x * 2):
        print("*", end=" ")
    print()

for x in range(4):
    for y in range(4):
        print(" ", end=" ")
    for z in range(2):
        print("*", end=" ")
    print()
