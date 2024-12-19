#trigger switch

isRepeat = True

while isRepeat == True:
    name = input("Enter a name:  ")
    print(f"Hi {name}")
    #stopping point
    if name.lower() == "stop":
        print("Loop Terminated")
        break
        isRepeat = False