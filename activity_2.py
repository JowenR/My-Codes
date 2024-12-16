#Creating Variables
#The input() function allows user input
#The len() function returns the number of items in an object.


name = input("Please enter your name: ")
age = input("Enter your age number: ")
email = input("Enter your email: ")

print()
print("Hi! " + name + " Welcome!! :) \n" + "Your age is " + age + " right? \n" + "Your email address is: " + email)
print("Your name consist of" + len(name) + "characters")

num1 = eval(input("Please input a number: "))
num2 = eval(input("Please input a number: "))

print()
print(num1 + "+" + num2 + "=" + num1 + num2) 



# Comments can be used to explain Python code.
# Comments can be used to make the code more readable.
# Comments can be used to prevent execution when testing code.
# Comments can be activated by using # or in VsCode shortcut ctrl/