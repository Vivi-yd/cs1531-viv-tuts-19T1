from order import Order
from item import Item

class Table(object):

    #constructor
    def __init__(self,table_number):
        self._orders = []
        self._table_number = table_number

    @property
    def table_number(self):
        return self._table_number

    @property
    def order_name(self):
        return self._order_name
        
    @order_name.setter
    def order_name(self,name):
        self._order_name = name

    # Clear order for a table
    def clear(self):
        self._orders = []

    # Add a new order for the table
    def add_order(self, item, notes):
        self._orders.append(Order(self._table_number, item, notes))

    # Find the total price of the orders for the table
    def compute_total_price(self):
        total = 0
        for order in self._orders:
            print(order.get_order_price())
            total += order.get_order_price()

        return total

        '''
        Alternatively: return sum(order.price for order in self._orders)
        '''

    # Display the list of orders that this table currentlyhas
    def display(self):
        print('Table {0} for {1} has orders:'.format(self._table_number,self._order_name))
        for order in self._orders:
            print(order)


# table = Table(0)
# table.order_name = 'Sarah'
# i = Item('Mocha',4.50,True,'Chocolate Coffe',['Chocolate','Coffee'],"Uses Lindt White Choc")
# table.add_order(i,"no sugar")
# i = Item("Salad", 15, False, "Vegetable salad", ["Lettuce", "Tomato", "Cucumber"], ["nut-free", "vegan", "glutten-free"])
# table.add_order(i,"no cucumber")
# table.display()
