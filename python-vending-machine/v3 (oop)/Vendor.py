from Menu import Menu
from Drink import Drink

class Vendor(Drink):
    def __init__(self):
        self._options = ["Add Drink Type", "Replenish Drink"]
    
    def add_drink_type(self, drink_id, description, price, quantity):
        Menu().add_drink_type(Drink(drink_id, description, price, quantity))
    
    def replenish_drink(self, drink_id, quantity):
        Menu().replenish_drink(drink_id, quantity)
    
    def get_options(self):
        return self._options
    
if __name__ == "__main__":
    Vendor().add_drink_type("IM", "Iced Milo", 1.5 ,2)