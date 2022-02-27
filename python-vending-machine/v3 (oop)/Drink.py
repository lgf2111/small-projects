class Drink:
    def __init__(self, id=None, description=None, price=None, quantity=None):
        self._id = id if id else ""
        self._description = description if description else ""
        self._price = price if price else 0
        self._quantity = quantity if quantity else 0
        
    def __str__(self):
        return f"{self._id}. {self._description} (S${self._price:.2f}) Qty: {self._quantity}"
        
    def set_id(self, id=None):
        self._id = id if id else "".join([_[0].upper() for _ in self._description.split()])
    def set_description(self, description):
        self._description = description
    def set_price(self, price):
        self._price = price
    def set_quantity(self, quantity):
        self._quantity = quantity
    
    def get_id(self):
        return(self._id)
    def get_description(self):
        return(self._description)
    def get_price(self):
        return(self._price)
    def get_quantity(self):
        return(self._quantity)

    def add_quantity(self, quantity):
        self._quantity += quantity
    
if __name__ == "__main__":
    print(Drink("IM", "Iced Milo", 1.5 ,2))