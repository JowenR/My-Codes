#round
#fahrenheit to celsius 

f = eval(input("Enter the Fahrenheit you want to convert: "))
c = (f-32)* 5 / 9

print(f"{f} degree fahrenheit converted to celsius is {round(c,2)}")

cel = eval(input("Enter the Celcius: "))
fah = (c*9/5) + 32

print(f"{cel} degree celcius converted to fahrenheit is {round(fah)}")