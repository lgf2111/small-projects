def add_drink_type(drink_id, description, price, quantity):
    drinks[drink_id] = {'description': description, 'price': price, 'quantity': quantity}


def replenish_drink(drink_id, quantity):
    drinks[drink_id]['quantity'] += quantity


drinks = {'IM': {'description': 'Iced Milo', 'price': 1.5, 'quantity': 30},
          'HM': {'description': 'Hot Milo', 'price': 1.2, 'quantity': 20},
          'IC': {'description': 'Iced Cofee', 'price': 1.5, 'quantity': 2},
          'HC': {'description': 'Hot Coffee', 'price': 1.2, 'quantity': 0},
          '1P': {'description': '100 Plus', 'price': 1.3, 'quantity': 50},
          'CC': {'description': 'Coca Cola', 'price': 1.3, 'quantity': 50}}


verify = input("Are you a vendor (Y/N)? ").upper()
if verify:
    if verify == "Y":
        while True:
            print(
"""Welcome to ABC Vending Machine.
Select from following choices to continue:
1. Add Drink Type
2. Replenish Drink
0. Exit"""
        )
            
            while True:
                choice = input("\rEnter choice: ")
                if choice:
                    if choice in ["1", "2", "0"]:
                        break
                    else:
                        print("Invalid option")
                    
            if choice == "1":
                while True:
                    drink_id = input("Enter drink id: ").upper()
                    if drink_id:
                        if drink_id not in drinks:
                            break
                        else:
                            print("Drink id exists!")

                while True:
                    description = input("Enter description of drink: ")
                    if description:
                        break

                while True:
                    price = input("Enter price: $")
                    if price:
                        try:
                            price = str(float(price))
                            if len(price.split(".")[1]) <= 2:
                                price = float(price)
                                break
                        except ValueError:
                            True
                        print("Invalid price")
                        
                while True:
                    quantity = input("Enter quantity: ")
                    if quantity:
                        if quantity.isdigit():
                            quantity = int(quantity)
                            break
                        else:
                            print("Invalid quantity")
                            
                add_drink_type(drink_id, description, price, quantity)
                print(drinks[drink_id]['description'] + " has been added!")
                
            elif choice == "2":
                for drink in drinks:
                    if drinks[drink]['quantity'] > 0:
                        print(f"{drink}. {drinks[drink]['description']} (S${drinks[drink]['price']:.1f})\tQty: {drinks[drink]['quantity']}")
                    else:
                        print(f"{drink}. {drinks[drink]['description']} (S${drinks[drink]['price']:.1f})\t***out of stock***")
                while True:
                    drink_id = input("Enter drink id: ").upper()
                    if drink_id:
                        if drink_id in drinks:
                            if drinks[drink_id]['quantity'] < 5:
                                break
                            else:
                                print("No need to replenish. Quantity is greater than 5.")
                        else:
                            print("No drink with this drink id. Try again.")
                        
                while True:
                    quantity = input("Enter quantity: ")
                    if quantity:
                        if quantity.isdigit():
                            quantity = int(quantity)
                            break
                        else:
                            print("Invalid quantity")
                
                replenish_drink(drink_id, quantity)
                print(drinks[drink_id]['description'] + " has been top up!")

            elif choice == "0":
                exit()
                        
    elif verify == "N":
        print("Welcome to ABC Vending Machine.\nSelect from following choices to continue:")
        for drink in drinks:
            if drinks[drink]['quantity'] > 0:
                print(f"{drink}. {drinks[drink]['description']} (S${drinks[drink]['price']:.1f})\tQty: {drinks[drink]['quantity']}")
            else:
                print(f"{drink}. {drinks[drink]['description']} (S${drinks[drink]['price']:.1f})\t***out of stock***")
        print("0. Exit / Payment")
        drinks_ = drinks
        order = []
        while True:
            choice = input("Enter choice: ").upper()
            if choice:
                if choice in drinks_:
                    if drinks_[choice]['quantity'] > 0:
                        drinks_[choice]['quantity'] -= 1
                        order.append(choice)
                        print("No. of drinks selected =", len(order))
                    else:
                        print(drinks_[choice]['description'] + " is out of stock")
                elif choice == "0":
                    if order:
                        price = sum(map(lambda id: drinks_[id]['price'], order))
                        print(f"Please pay: ${price:.2f}\nIndicate your payment:")
                        while True:
                            pay = 0
                            for note in [10, 5, 2]:
                                if pay >= price:
                                    break
                                else:
                                    while True:
                                        amount = input("Enter no. of $" + str(note) + " notes: ")
                                        if amount:
                                            if amount.isdigit():
                                                pay += note * int(amount)
                                                break
                                            else:
                                                print("Invalid no.")
                            
                            if pay >= price:
                                drinks = drinks_
                                print("Please collect your change: ${change:.2f}".format(change = pay - price))
                                exit("Drinks paid. Thank you.")
                                
                            else:
                                print("Not enough to pay for the drinks\nTake back your cash!")
                                cancel = input("Do you want to cancel the purchase? Y/N: ")
                                if cancel:
                                    if cancel == "Y":
                                        exit("Purchase is cancelled. Thank you.")
                                    elif cancel == "N":
                                        continue

                    else:
                        exit()
                else:
                    print("Invalid choice")
