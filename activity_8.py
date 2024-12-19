sum = 0
odd = 0 
even = 0

for x in range(1,11):
    num = eval(input(f"Input# {x}: "))
    sum += num 
    if num % 2 == 0:
        even += num
    else:
        odd += num
print(f"The sum of all numbers are: {sum}")
print(f"The sum of all even numbers are: {even}")
print(f"The sum of all odd numbers are: {odd}")