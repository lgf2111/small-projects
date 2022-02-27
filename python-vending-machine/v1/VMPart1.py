verify = input("Are you a vendor (Y/N)? ")

if verify == "Y":
    print(
"""Welcome to ABC Vending Machine.
Select from following choices to continue:
1. Add Drink Type
2. Replenish Drink
0. Exit
Enter choice:"""    
    )
    
if verify == "N":
    print(
"""Welcome to ABC Vending Machine.
Select from following choices to continue:
IM. Iced Milo (S$1.5)
HM. Hot Milo (S$1.2)
IC. Iced Coffee (S$1.5)
HC. Hot Coffee (S$1.2)
1P. 100 Plus (S$1.1)
CC. Coca Cola (S$1.3)
0. Exit / Payment"""
    )
    drink_list = ["IM", "HM", "IC", "HC", "1P", "CC"]
    drink_price = [1.5, 1.2, 1.5, 1.2, 1.1, 1.3]
    choices = []
    counter = 0
    while True:
        choice = input("Enter choice: ").upper()
        if choice in drink_list:
            choices.append(choice)
            counter += 1
            print("No. of drinks selected =", counter)
        elif choice != "0":
            print("Invalid option")
        else:
            if counter:
                break
            else:
                exit()

    price = 0
    for choice in choices:
        price += drink_price[drink_list.index(choice)]
    print(f"Please pay: ${price:.2f}\nIndicate your payment:")
    while True:
        pay = 0
        for note in [10, 5, 2]:
            if pay >= price:
                break
            else:
                pay += note * int(input("Enter no. of $" + str(note) + " notes: "))
            
        if pay >= price:
            print("Please collect your change: ${change:.2f}".format(change = pay - price))
            exit("Drinks paid. Thank you.")
            
        else:
            print("Not enough to pay for the drinks\nTake back your cash!")
            cancel = input("Do you want to cancel the purchase? Y/N: ")
            if cancel == "Y":
                exit("Purchase is cancelled. Thank you.")
            elif cancel == "N":
                continue
