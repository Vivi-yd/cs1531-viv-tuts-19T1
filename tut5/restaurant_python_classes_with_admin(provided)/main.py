from restaurant import RestaurantSystem
from AdminSystem import AdminSystem
from AdminUser import AdminUser
from item import Item

admin_system = AdminSystem(AdminUser("isaac", "123"))
system = RestaurantSystem(admin_system)


items = system.get_menu_items()
for each in sorted(items.keys()):
    menu_item = items[each]
    print("name:",menu_item._name)
    print("status:",menu_item._availability)
    print("price:",menu_item._price)
    
    

# system.add_table_order(0,"Sarah")
# i = Item('Mocha',4.50,True,'Chocolate Coffe',['Chocolate','Coffee'],"Uses Lindt White Choc")
# system.add_order(0, i,"no sugar")
# i = Item("Salad", 15, False, "Vegetable salad", ["Lettuce", "Tomato", "Cucumber"], ["nut-free", "vegan", "glutten-free"])
# system.add_order(0,i,"no cucumber")

# system.add_table_order(1,"Millie")
# system.add_order(1, i, "Extra Cheese")

# system.display_table(0)
# system.display_table(1)


# system.pay_for_table(0)


# admin_system.login("isaac", "123")
# admin_system.view_log()

