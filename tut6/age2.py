class Age(object):
    def __init__(self, age):
        self.age = int(age)
        if self.age < 0:
            raise ValueError("%d is not a valid age. Age must be positive or zero." % self.age)

    def __str__(self):
        return str(self.age)

ans = input("Please enter your age: ")
try:
    age = Age(ans)
except ValueError as err:
    print("You entered incorrect age input: %s" % ans)
else:
    print("I see that you are %s years old." % age)