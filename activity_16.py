#WHILE LOOP 
#TYPES OF LOOP 
#FOR LOOP - use if you have certain or definite amout of times to repeart a code block 
#WHILE LOOP - use if you are uncertain on the amount of times to repeat a code block 

#boolean variable / trigger 

tuloy = True 

#habang si tuloy ay naka set sa true, continue lng sa pag repeat ng code. 
#continue to ask for a number, once user types the number ZERO (0) terminate the loop and get the summation of all the
#number(s) given
sum = 0
while tuloy == True:
    num = eval(input("Enter any number --->  "))

    if num == 0:
        print("LOOP STOPPED")
        print(f"The sum of all the numbers given is {sum}")
        break
        tuloy = False 
    else:
        sum += num 
        continue