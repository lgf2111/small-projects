DRINK_MENU = [["IM", "Iced Milo", 1.5],
              ["HM", "Hot Milo", 1.2],
              ["IC", "Iced Coffee", 1.5],
              ["HC", "Hot Coffee", 1.2],
              ["1P", "100 Plus", 1.1],
              ["CC", "Coca Cola", 1.3]]

VENDOR_MENU = ["Add Drink Type", "Replenish Drink"]

_ = input("Are you a vendor (Y/N)? ").upper()

if _ == "Y":
    print("Welcome to ABC Vending Machine.\nSelect from following choices to continue:")
    print(*[f"{i+1}. {VENDOR_MENU[i]}" for i in range(len(VENDOR_MENU))], sep="\n")
    print("0. Exit")
    input("Enter choice:")
    
elif _ == "N":
    CHECKOUT = [[],[]]
    print("Welcome to ABC Vending Machine.\nSelect from following choices to continue:")
    print(*[f"{drink[0]}. {drink[1]} (S${drink[2]:.2f})" for drink in DRINK_MENU], sep="\n")
    print("0. Exit / Payment")
    while True:
        _ = input("Enter choice: ").upper()
        if _ != "0":
            for drink in DRINK_MENU:
                if drink[0] == _:
                    CHECKOUT[0].append(drink[1])
                    CHECKOUT[1].append(drink[2])
                    print(f"No. of drinks selected: {len(CHECKOUT[0])}")
                    break
            else:
                print("Invalid option")
        else:
            if CHECKOUT[0]:
                break
            else:
                exit()

    while True:
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