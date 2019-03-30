class Age(object):
    def __init__(self, age):
        self.age = int(age)
        if self.age < 0:
            raise IllegalAge(self.age)

    def __str__(self):
        return str(self.age)

class  IllegalAge(Exception):
    def __init__(self, age):
        super().__init__()
        self.age = age

ans = input("Please enter your age: ")

try:
    age = Age(ans)

except ValueError as err:
    print("this is not an integer: %s is not a valid age" % ans)
except IllegalAge as err:
    print("You can't be negative years old. %s is not a valid age." % err.age)
else:
    print("I see that you are %s years old." % age)
