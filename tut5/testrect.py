from rectangle import Rectangle

class Testrect(object):

    def test_zero_area(self):
        r = Rectangle(1, 1)
        a = r.area()
        assert(a == 0)

    def test_get_width(self):
        r = Rectangle(1, 2)
        assert(r.get_width() == 1)

    def test_set_width(self):
        r = Rectangle(4, 5)
        r.set_width(3)
        assert(r.get_width() == 3)
        


