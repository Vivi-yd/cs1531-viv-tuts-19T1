from item import Item
from table import Table
from menu import Menu

class RestaurantSystem:

    def __init__(self, admin_system, menu=None, total_number_of_tables=20):
        self._tables = []
        self._order_logs = []
        self._menu = menu  # create an empty menu if `menu` is None
        self._admin_system = admin_system

        for i in range(total_number_of_tables):
            self._tables.append(Table(i))

    def get_menu_items(self):
        return self._menu.get_items()

    # Display menu
    def display_menu(self):
        # return self._menu.display()
        return self._menu

    def display_item(self, name):
        if name == "":
            return "Item name is empty"
        if not self._menu.get_item(name):
            return "Item doesn't exist"
        return self._menu.get_item(name)

    # Add new table order
    def add_table_order(self,table_number,name):
        table = self._get_table(table_number)
        table.order_name = name


    def add_order(self, table_id, item, notes=""):
        if table_id >= len(self._tables) or table_id < 0:
            return "Invalid Table ID"
        self._tables[table_id].add_order(item,notes)
        if item.name == "":
            return "Item name is empty"
        if not self._menu.get_item(item.name): 
            return "Item doesn't exist"
        return "Successful"


    # Display the details of a table
    def display_table(self, table_number):
        table = self._get_table(table_number)
        if table:
            table.display()



    # Print the total price that the diner has pay for their table
    def print_bill(self, table_number):
        table = self._get_table(table_number)

        if table:
            total = table.compute_total_price()
            print('Table: {}, total: {}'.format(table_number, total))



    # Authorise payment for the table
    def pay_for_table(self, table_number):
        table = self._get_table(table_number)
        print(table.order_name + ":" + table._table_number)
        if not table:
            return
        
        total = self._finalise_total(table)
        print('Table: {}, total: ${:.2f}'.format(table_number, total))

        answer = input('Authorise payment? (yes/no) ')
        if answer.lower() == 'yes':
            print('Payment authorised.')
            self._order_logs.append(table)
        else:
            print('Payment not authorised.')
    


    # Find the total the diner has to pay, with any discount applied
    def _finalise_total(self, table):
        answer = input('Apply discounts? (yes/no) ')

        price = table.compute_total_price()

        if answer.lower() != 'yes':
            return price

        percent     = float(input('Discount percentage: %'))
        new_price   = self._authorise_discount(table, percent)

        # if there is no new price, then return the original price instead
        return new_price or price



    # Authorise discount with temporary admin permissions
    # The admin has to enter their username and password everytime
    # a discount has to be applied because the system would be
    # used by non-admins for the most of the time anyways

    def _authorise_discount(self, table, percent):
        username = input("Username: ")
        password = input("Password: ")

        price = None

        if self._admin_system.login(username, password):
            price = self._admin_system.apply_discount(table, percent)
            self._admin_system.logout()

        else:
            print("Login failed")

        return price




    # Get the table corresponding to the given table_number
    def _get_table(self, table_number):
        for table in self._tables:
            if table.table_number == table_number:
                return table
        return None

        '''
        Alternative: return next((t in self._tables if t.table_number == table_number), None)
        '''


