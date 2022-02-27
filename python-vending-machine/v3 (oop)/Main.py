from Menu import Menu
from Vendor import Vendor
from Customer import Customer

verify = input("Are you a vendor (Y/N)? ").upper()

if verify == "Y":
    vendor = Vendor()
    print("Welcome to ABC Vending Machine.\nSelect from following choices to continue:")
    print(*[f"{i+1}. {vendor.get_options()[i]}" for i in range(len(vendor.get_options()))], sep="\n")
    print("0. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        while True:
            drink_id = input("Enter drink id: ").upper()
            if drink_id in Menu().get_drinks_id():
                print("Drink id already exists!")
            else:
                break
        description = input("Enter description of drink: ")
        while True:
            try:
                price = float(input("Enter price: "))
                break
            except ValueError:
                pass
        while True:
            try:
                quantity = int(input("Enter quantity: "))
                break
            except ValueError:
                pass
        vendor.add_drink_type(drink_id, description, price, quantity)
    if choice == "2":
        print(Menu().get_menu())
        while True:
            drink_id = input("Enter drink id: ").upper()
            if drink_id not in Menu().get_drinks_id():
                print("No drink with this drink id, please try again.")
            else:
                break
        if Menu().get_drinks_quantity()[Menu().get_drinks_id().index(drink_id)] > 5:
            print("No ned to replenish, quantity is greater than 5.")
        while True:
            try:
                quantity = int(input("Enter quantity: "))
                break
            except ValueError:
                pass
        vendor.replenish_drink(drink_id, quantity)
        print(f"{Menu().get_drinks_description()[Menu().get_drinks_id().index(drink_id)]} has been topped up!")

if verify == "N":
    customer = Customer()
    print("Welcome to ABC Vending Machine.\nSelect from following choices to continue:")
    print(Menu().get_menu())
    print("0. Exit / Payment")
    while True:
        choice = input("Enter choice: ").upper()
        if choice in Menu().get_drinks_id():
            index = Menu().get_drinks_id().index(choice)
            if (customer.get_order().count(Menu().get_drinks_description()[index]) < Menu().get_drinks_quantity()[index]):
                customer.append_order(Menu().get_drinks_description()[index])
            else:
                print(f"{Menu().get_drinks_description()[index]} is out of stock")
        elif choice == "0":
            break
    while customer.get_order():
        amount = [sum(Menu().get_drinks_price()[Menu().get_drinks_description().index(_)] for _ in customer.get_order()), 0]
        print(f"Please pay: ${amount[0]:.2f}\nIndicate your payment:")
        for n in [10, 5, 2]:
            try:
                amount[1] += int(input(f"Enter no. of ${n} notes: ")) * n
                if amount[1] > amount[0]: 
                    change = amount[1] - amount[0]
                    print(f"Please collect your change: ${change:.2f}\nDrinks paid, thank you.")
                    exit()        
            except ValueError:
                pass
        else:
            print("Not enough to pay for the drinks.\nTake back your cash!")
            cancel = input("Do you want to cancel the purchase? (Y/N): ").upper()
            if cancel == "Y":
                print("Purchase was cancelled, thank you.")
                exit()
            elif cancel == "N":
                continue