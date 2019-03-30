

class AdminUser(object):

    def __init__(self, username, password):
        self._username = username
        self._password = password


    def authenticate(self, username, password):
        if (self._username == username and self._password == password):
            return True
        else:
            return False