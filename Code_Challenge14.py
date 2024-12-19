import os

def display_denominations(amount):
    tsn = amount // 1000
    rem_tsn = amount % 1000
    fh = rem_tsn // 500
    rem_fh = rem_tsn % 500
    th = rem_fh // 200
    rem_th = rem_fh % 200
    oh = rem_th // 100
    rem_oh = rem_th % 100
    ft = rem_oh // 50
    rem_ft = rem_oh % 50
    tw = rem_ft // 20
    rem_tw = rem_ft % 20
    tn = rem_tw // 10
    rem_tn = rem_tw % 10
    fv = rem_tn // 5
    rem_fv = rem_tn % 5
    on = rem_fv // 1

    os.system('cls')
    print("Filipino denominations of the amount that you have deposited is as follows:")
    print(f"1000 = {tsn} | 500 = {fh} | 200 = {th}")
    print(f"100 = {oh} | 50 = {ft} | 20 = {tw}")
    print(f"10 = {tn} | 5 = {fv} | 1 = {on}")
    print(f"Amount entered: {amount}")

def main():
    print("Welcome! Let's get you started with an account.")
    username = input("Please enter your username: ")
    print(f"Hi, {username}! Your account has been successfully created.")
    balance = 0

    while True:
        print("\nWhat would you like to do next?")
        print("1. Make a Deposit")
        print("2. Make a Withdrawal")
        print("3. View Current Balance")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            amount = int(input("Enter the amount you wish to deposit: "))
            display_denominations(amount)
            balance += amount
            print(f"You have deposited {amount} PHP. Your new balance is {balance} PHP.")

        elif choice == '2':
            amount = int(input("Enter the amount you wish to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"You have withdrawn {amount} PHP. Your remaining balance is {balance} PHP.")
            else:
                print("You do not have enough balance for this withdrawal.")

        elif choice == '3':
            print(f"Your current balance is {balance} PHP.")

        elif choice == '4':
            print("Thank you for using our service. Have a great day!")
            break

        else:
            print("Invalid selection. Please try again.")

main()

