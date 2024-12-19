num = eval(input("Enter the column number:  "))
for x in range(1,11):
    for y in range(1,num+1):
        print(f"{x*y}={x+y}",end="\t")
    print()