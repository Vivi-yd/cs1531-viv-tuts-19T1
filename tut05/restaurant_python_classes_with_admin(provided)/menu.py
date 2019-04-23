from item import Item


class Menu:

    def __init__(self):
        # self.items = []
        self._items = {}

    def add_item(self, name, price, availability, description, ingredients, tags):
        self._items[name] = Item(name, price, availability, description, ingredients, tags)

    def display(self):
        return self._items.values()

    def print_menu(self):
        for item in self._items.keys():
            print(self.get_item(item))
    
    def get_item(self, name):
        # if name in self._items.keys():
        #     print("menu-item present")
        return self._items[name]

    def get_items(self):
        return self._items