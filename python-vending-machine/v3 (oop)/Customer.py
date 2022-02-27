class Customer:
    def __init__(self):
        self._order_list = []
    
    def append_order(self, order):
        self._order_list.append(order)

    def get_order(self):
        return self._order_list