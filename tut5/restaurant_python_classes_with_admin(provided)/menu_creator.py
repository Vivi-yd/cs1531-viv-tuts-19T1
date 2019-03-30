from menu import Menu

def create_menu():
    menu = Menu()
    menu.add_item("Burger", 20, True, "Delicious Beef Burger", ["Lettuce", "Tomato", "Beef"], ["nut-free"])
    menu.add_item("Salad", 15, False, "Vegetable salad", ["Lettuce", "Tomato", "Cucumber"], ["nut-free", "vegan", "glutten-free"])
    menu.add_item("Mocha", 10, True, "Best Mocha", ["Milk", "Chocolate", "Coffee"], ["nut-free", "vegan", "glutten-free"])

    return menu

# menu = create_menu()
# for i in menu.display():
#     print(i)
# menu.print_menu()
