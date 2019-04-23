from item import Item
class Order(object):

    def __init__(self, table_number, item, notes="",prepared=False,):
        self._table_number  = table_number
        self._is_prepared   = prepared
        self._item = item
        self._notes = notes

        # self._name        = name
        # self._description = description
        # self._price       = price


    # Order is ready
    def update_preparation_status(self):
        self._is_prepared = True

    # Get order price
    def get_order_price(self):
        return self._item._price

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, new_item):
        self._price = new_item

    @property
    def is_prepared(self):
        return self._is_prepared

    def __str__(self):
        return str(self._item) + "Special Notes: " + self._notes

# i = Item('Mocha',4.50,True,'Chocolate Coffe',['Chocolate','Coffee'],"Uses Lindt White Choc")
# o = Order(0,i,"2 sugar")
# print("{}:{}".format(o,o.get_order_price()))