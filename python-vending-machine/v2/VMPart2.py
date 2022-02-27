DRINK_MENU = {"IM": {"Description": "Iced Milo", "Price": 1.5, "Quantity": 2},
              "HM": {"Description": "Hot Milo", "Price": 1.2, "Quantity": 20},
              "IC": {"Description": "Iced Coffee", "Price": 1.5, "Quantity": 2},
              "HC": {"Description": "Hot Coffee", "Price": 1.2, "Quantity": 0},
              "1P": {"Description": "100 Plus", "Price": 1.1, "Quantity": 50},
              "CC": {"Description": "Coca Cola", "Price": 1.3, "Quantity": 50}}

VENDOR_MENU = ["Add Drink Type", "Replenish Drink"]

WIDTH = max([len(f"{Drink}. {DRINK_MENU[Drink]['Description']} (S${DRINK_MENU[Drink]['Price']:.2f})") for Drink in DRINK_MENU]) + 1

while True:
    _ = input("Are you a vendor (Y/N)? ").upper()

    if _ == "Y":
        print("Welcome to ABC Vending Machine.\nSelect from following choices to continue:")
        print(*[f"{i+1}. {VENDOR_MENU[i]}" for i in range(len(VENDOR_MENU))], sep="\n")
        print("0. Exit")
        _ = input("Enter choice:")
        if _.isdigit():
            _ = int(_)
            if _ in range(len(VENDOR_MENU)+1):
                if _ == 1:
                    def add_drink_type(drink_id, description, price, quantity):
                        DRINK_MENU[drink_id] = {"Description": description, "Price": price, "Quantity": quantity}
                    _ = ["","","",""]
                    while not _[0]:
                        _[0] = input("Enter drink id: ").upper()
                        if _[0] in DRINK_MENU:
                            print("Drink Id exists!")
                            _[0] = ""
                    _[1] = input("Enter description of drink: ")
                    while type(_[2]) != float:
                        _[2] = input("Enter price: $")
                        try:
                            _[2] = float(_[2])
                            if len(str(_[2]).split(".")[1]) > 2 or _[2] < 0:
                                print("Invalid input")
                                _[2] = ""
                        except ValueError:
                            print("Invalid input")
                            _[2] = ""
                    while type(_[3]) != int:
                        _[3] = input("Enter quantity: ")
                        if _[3].isdigit():
                            _[3] = int(_[3])
                            if _[3] < 0:
                                print("Invalid input")
                                _[3] = ""
                        else:
                            print("Invalid input")
                    add_drink_type(*_)
                    print(f"{DRINK_MENU[_[0]]['Description']} has been added!")
                elif _ == 2:
                    def replenish_drink(drink_id, quantity):
                        DRINK_MENU[drink_id]["Quantity"] += quantity
                    for Drink in DRINK_MENU:
                        _ = f"{Drink}. {DRINK_MENU[Drink]['Description']} (S${DRINK_MENU[Drink]['Price']:.2f})".ljust(WIDTH)
                        _ += f"Qty: {DRINK_MENU[Drink]['Quantity']}" if DRINK_MENU[Drink]['Quantity'] != 0 else "***out of stock***"
                        print(_)
                    _ = ["",""]
                    while not _[0]:
                        _[0] = input("Enter drink id:").upper()
                        if _[0] not in DRINK_MENU:
                            print("No drink with this drink id. Please try again.")
                            _[0] = ""
                        else:
                            if DRINK_MENU[_[0]]["Quantity"] > 5:
                                print("No need to replenish, quantity is greater than 5.")
                                _[0] = ""
                    while type(_[1]) != int:
                        _[1] = input("Enter quantity: ")
                        if _[1].isdigit():
                            _[1] = int(_[1])
                            if _[1] <= 0:
                                print("Invalid input")
                                _[1] = ""
                        else:
                            print("Invalid input")
                            _[1] = ""
                    replenish_drink(*_)
                    print(f"{DRINK_MENU[_[0]]['Description']} has been top up!")
                else:
                    break
            
    elif _ == "N":
        CHECKOUT = [[],[]]
        print("Welcome to ABC Vending Machine.\nSelect from following choices to continue:")
        for Drink in DRINK_MENU:
            _ = f"{Drink}. {DRINK_MENU[Drink]['Description']} (S${DRINK_MENU[Drink]['Price']:.2f})".ljust(WIDTH)
            _ += f"Qty: {DRINK_MENU[Drink]['Quantity']}" if DRINK_MENU[Drink]['Quantity'] != 0 else "***out of stock***"
            print(_)
        print("0. Exit / Payment")
        while True:
            _ = input("Enter choice: ").upper()
            if _ != "0":
                for Drink in DRINK_MENU:
                    if Drink == _:
                        if CHECKOUT[0].count(DRINK_MENU[Drink]["Description"]) < DRINK_MENU[Drink]["Quantity"]:
                            CHECKOUT[0].append(DRINK_MENU[Drink]["Description"])
                            CHECKOUT[1].append(DRINK_MENU[Drink]["Price"])
                            print(f"No. of drinks selected: {len(CHECKOUT[0])}")
                        else:
                            print(f"{DRINK_MENU[Drink]['Description']} is out of stock")
                        break
                else:
                    print("Invalid option")
            else:
                break

        while CHECKOUT[0]:
            PAYMENT = [sum(CHECKOUT[1]), 0]
            print(f"Please pay: ${sum(CHECKOUT[1]):.2f}\nIndicate your payment:")
            for note in [10,5,2]:
                _ = input(f"Enter no. of ${note} notes: ")
                if _.isdigit():
                    PAYMENT[1] += int(_) * note
                    if PAYMENT[1] >= PAYMENT[0]:
                        break
            else:
                print("Not enough to pay for the drinks,\nTake back your cash!")
                _ = input("Do you want to cancel the purchase? (Y/N): ").upper()
                if _ == "Y":
                    print("Purchase is cancelled. Thank you.")
                    exit()
                elif _ == "N":
                    continue
            print(f"Please collect your change: ${PAYMENT[1]-PAYMENT[0]:.2f}\nDrinks paid. Thank you.")
            exit()