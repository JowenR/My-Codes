# Input 
name = input("Enter Your Name: ")
purchased = input("Did you purchase a grocery today? (Y/N): ")

if purchased == 'Y':
    item = input("What did you purchase: ")
    price = eval(input("Item price: "))
    age = eval(input("Age: "))
    payment = eval(input("Payment: "))

    # Tax and discount
    tax_rate = 0.123
    discount_rate = 0.038
    senior_discount_rate = 0.123

    taxed_price = price + (price * tax_rate)

    if price > 4000:
        taxed_price -= (price * discount_rate)

    if 60 < age <= 150:
        taxed_price -= (taxed_price * senior_discount_rate)

    change = payment - taxed_price

    # Output
    print(f"\nHello {name}, Here is your receipt.")
    print(f"Item: {item}")
    print(f"Untaxed Price: {price}")
    print(f"Total Price (with taxes and discounts): {round(taxed_price, 2)}")
    print(f"Payment: {payment}")
    print(f"Change: {round(change, 2)}")

else:
    print("No purchase made today.")


