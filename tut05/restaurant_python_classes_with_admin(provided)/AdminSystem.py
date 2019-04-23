

class AdminSystem(object):

    def __init__(self, admin):
        self._logs = []
        self._admin = admin
        self._is_authenticated = False

    
    # Simulate login & logout (this will be different when using Flask and Flask-login)
    def login(self, username, password):
        if self._admin.authenticate(username, password):
            self._is_authenticated = True
            return True
        return False


    def logout(self):
        self._is_authenticated = False


    # Apply discount to given table
    def apply_discount(self, table, percent):   
        if not self._is_authenticated:
            return None

        old_price, new_price = self._get_discount(table, percent)

        log = 'Discounted the table {} from ${:.2f} to ${:.2f}'.format(
            table.table_number, old_price, new_price)

        self._logs.append(log)
        print(log)

        return new_price
    

    # Find discounted price for the given table
    def _get_discount(self, table, percent):
        old_price = table.compute_total_price()
        new_price = old_price * (100 - percent) / 100
        new_price = round(new_price, 2)
        
        # return a pair of values
        return old_price, new_price



    # View past discounts
    def view_log(self):
        if not self._is_authenticated:
            return

        for log in self._logs:
            print(log)


    @property
    def is_authenticated(self):
        return self._is_authenticated