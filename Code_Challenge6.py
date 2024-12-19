name = input("Enter your name >>> ")
age = eval(input("Enter your age >>> "))

if age >= 1 and age <= 8:
	print("You are a Toddler")

elif age >= 9 and age <= 14:
	print("You are a Pre Teen")

elif age >= 15 and age <= 18:
	print("You are a Teenager")

elif age >= 19 and age <= 27:
	print("You are a Early Adulthood")

elif age >= 28 and age <= 44:
	print("You are a Middle Age")

elif age >= 45 and age <= 59:
	print("You are a Post Adulthood")

elif age >= 60:
	print("You are a Senior")

else:
	print("Invalid")