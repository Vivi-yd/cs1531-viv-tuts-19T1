class Rectangle:
    # define constructor to initialise attribute
    def __init__(self, width, length):
        # specify private attribute
        self._width = width
        self._length = length

    # defining accessor and mutator methods to access and set private fields
    def get_width(self):
        return self._width

    def get_length(self):
        return self._length

    def set_width(self, w):
        self._width = w

    def set_length(self, l):
        self._length = l

    # calculate area
    def area(self):
        return self._width * self._length

    # str function to print area
    def __str__ (self):
        return "this rectangle has area of {}".format(self.area())

r = Rectangle(3, 4)
print(r.__str__())
print(r)

