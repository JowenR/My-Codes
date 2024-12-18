name = input("Enter your name: ")
print(f" Hello {name}!")

pm = eval(input("Enter your Prelims score: "))
mt = eval(input("Enter your Midterm score: "))
sf = eval(input("Enter your Semifinals score: "))
f = eval(input("Enter your Finals score: "))
q = eval(input("Enter your Quiz score: "))
p = eval(input("Enter your Projects score: "))

g = (pm * 0.15) + (mt * 0.15) + (sf * 0.15) + (f * 0.15) + (q * 0.15) + (p * 0.15)
r = round(g,2)
print(f"Final grade: {r}%")
if g >= 75:
	print("Congrats beh, you passed!")
if g <= 75:
	print("Failed ka beh! Kinulang ka siguro sa goodluck niya")