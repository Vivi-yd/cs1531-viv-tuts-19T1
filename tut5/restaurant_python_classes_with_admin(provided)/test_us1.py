import pytest
from restaurant import RestaurantSystem
from AdminSystem import AdminSystem
from AdminUser import AdminUser
from menu import Menu
from item import *


class TestUS1(object):

    def setup_method(self):
        self.admin_system = AdminSystem(AdminUser("isaac", "123"))

    def test_empty_menu(self):
        system = RestaurantSystem(self.admin_system)
        items = system.get_menu_items()
        assert len(items) == 0

    def test_single_item(self):
        menu = Menu()
        menu.add_item("Mocha", 10, True, "Best Mocha", ["Milk", "Chocolate", "Coffee"], ["nut-free", "vegan", "glutten-free"])

        system = RestaurantSystem(self.admin_system, menu)
        items = system.get_menu_items()

        assert len(items) == 1
        assert "Mocha" in items
        assert items["Mocha"] == Item("Mocha", 10, True, "Best Mocha", ["Milk", "Chocolate", "Coffee"], ["nut-free", "vegan", "glutten-free"])


    def test_single_item_alt1(self):
        menu = Menu()
        mocha = Item("Mocha", 10, True, "Best Mocha", ["Milk", "Chocolate", "Coffee"], ["nut-free", "vegan", "glutten-free"])
        menu.add_item(mocha.name, mocha.price, mocha.is_available, mocha.description, mocha.ingredients, mocha.tags)

        system = RestaurantSystem(self.admin_system, menu)
        items = system.get_menu_items()

        assert len(items) == 1
        assert "Mocha" in items
        assert items["Mocha"] == mocha


    # Alternative if you have not validated the __eq__ implementation in class Item (but really should)
    def test_single_tiem_alt2(self):
        menu = Menu()
        menu.add_item("Mocha", 10, True, "Best Mocha", ["Milk", "Chocolate", "Coffee"], ["nut-free", "vegan", "glutten-free"])

        system = RestaurantSystem(self.admin_system, menu)
        items = system.get_menu_items()

        assert len(items) == 1
        assert "Mocha" in items

        item = items["Mocha"]
        assert item.name             == "Mocha"
        assert item.price            == 10
        assert item.is_available     == True
        assert item.description      == "Best Mocha"
        assert set(item.ingredients) == {"Milk", "Chocolate", "Coffee"}
        assert set(item.tags)        == {"nut-free", "vegan", "glutten-free"}


    def test_multiple_items(self):
        menu = Menu()
        
        # Assumes that Item class has been implemented correctly
        test_items = []
        test_items.append(Item("Burger", 20, True, "Delicious Beef Burger", ["Lettuce", "Tomato", "Beef"], ["nut-free"]))
        test_items.append(Item("Salad", 15, False, "Vegetable salad", ["Lettuce", "Tomato", "Cucumber"], ["nut-free", "vegan", "glutten-free"]))
        test_items.append(Item("Mocha", 10, True, "Best Mocha", ["Milk", "Chocolate", "Coffee"], ["nut-free", "vegan", "glutten-free"]))
        
        # Add to menu
        for item in test_items:
            menu.add_item(item.name, item.price, item.is_available, item.description, item.ingredients, item.tags)
    
        system = RestaurantSystem(self.admin_system, menu) 
        menu_items = system.get_menu_items()

        assert len(menu_items) == 3
        for item in test_items:
            assert item.name in menu_items
            assert menu_items[item.name] == item

        ## OR use dict comprehension
        assert menu_items == {item.name: item for item in test_items}

