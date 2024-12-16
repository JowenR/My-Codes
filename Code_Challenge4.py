name = input("Please enter your username ---> ")
dep = eval(input("Enter your deposit amount ---> "))
print(f"Hello,{name} you have deposited {dep} pesos. Here is your deposit represented in PH Denominations")

T = dep//1000
TH = dep%1000
print(f"{T} - 1000")

F = TH//500
FH = TH%500
print(f"{F} - 500")

TW = FH//200
TWH = FH%200
print(f"{TW} - 200")

O = TWH//100
OH = TWH%100
print(f"{0} - 100")

FT = OH//50
FTY = OH%50
print(f"{FT} - 50")

TT = FTY//20
TTY = FTY%20
print(f"{TT} - 20")

T = TTY//10
TN = TTY%10
print(f"{T} - 10")

FI = TN//5
FIV = TN%5
print(f"{FI} - 5")

ON = FIV//1
ONE = FIV%1
print(f"{ON} - 1")
