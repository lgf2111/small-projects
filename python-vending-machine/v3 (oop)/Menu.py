from Drink import Drink

class Menu:
    def __init__(self):
        self._drinks = [
                        Drink("IM", "Iced Milo", 1.5, 2),
                        Drink("HM", "Hot Milo", 1.2, 20),
                        Drink("IC", "Iced Coffee", 1.5, 2),
                        Drink("HC", "Hot Coffee", 1.2, 0),
                        Drink("1P", "100 Plus", 1.1, 50),
                        Drink("CC", "Coca Cola", 1.3, 50),
                        ]
        self._origin = len(self._drinks)
        
    def get_menu(self):
        menu = ""
        width = [0,0,0,0]
        for drink in self._drinks:
            drink = [len(str(_)) for _ in [drink.get_id(), drink.get_description(), drink.get_price(), drink.get_quantity()]]
            width[0] = drink[0] if drink[0] > width[0] else width[0]
            width[1] = drink[1] if drink[1] > width[1] else width[1]
            width[2] = drink[2] if drink[2] > width[2] else width[2]
            width[3] = drink[3] if drink[3] > width[3] else width[3]
        for drink in self._drinks:
            if drink.get_quantity() > 0:
                menu += f"{drink.get_id().ljust(width[0])}. " +\
                        f"{drink.get_description().ljust(width[1])} " +\
                        f"(S${drink.get_price():.2f}) ".ljust(width[2]) +\
                        f"Qty: {drink.get_quantity()}".ljust(width[3]) + "\n"
            else:
                menu += f"{drink.get_id().ljust(width[0])}. " +\
                        f"{drink.get_description().ljust(width[1])} " +\
                        f"(S${drink.get_price():.2f}) ".ljust(width[2]) +\
                        f"***out of stock***".ljust(width[3]) + "\n"
        return menu.rstrip()
    
    def get_drinks_id(self):
        return [drink.get_id() for drink in self._drinks]
    
    def get_drinks_description(self):
        return [drink.get_description() for drink in self._drinks]
    
    def get_drinks_price(self):
        return [drink.get_price() for drink in self._drinks]

    def get_drinks_quantity(self):
        return [drink.get_quantity() for drink in self._drinks]
    
    def add_drink_type(self, drink):
        self._drinks.append(drink)
        self.rewrite()
        
    def replenish_drink(self, drink_id, quantity):
        self._drinks[self.get_drinks_id().index(drink_id)].add_quantity(quantity)
        self.rewrite()
    
    def rewrite(self):
        total = len(self._drinks)
        with open(__file__, 'r') as f:
            content = f.readlines()
            new = "\n".join(f'{" "*24}Drink("{drink.get_id()}", "{drink.get_description()}", {drink.get_price()}, {drink.get_quantity()}),' for drink in self._drinks)
            new += f"\n{' '*24}]\n\n" if total > self._origin else "\n"
            new_f = "".join(content[:5]) + new + "".join(content[total+5:])
        with open(__file__, 'w') as f:
            f.write(new_f)
    
if __name__ == "__main__":
    Menu().rewrite()