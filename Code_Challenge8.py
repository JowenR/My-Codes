sum = 0
even = 0
odd = 0

for x in range(1, 11):
    num = int(input(f"Input #{x}: "))
    sum += num

    if num % 2 == 0:
        even += num
        print(f"{num} is even.")
    else:
        odd += num
        print(f"{num} is odd.")

print(f"The sum of all the numbers given/provided is {sum}")
