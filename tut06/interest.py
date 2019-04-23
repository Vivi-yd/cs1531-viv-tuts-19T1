#python program to calculate simple interest
def calculate_simple_interest(p,n,r):
    i = p*(r/100)*n
    return i

def calculate_compound_interest(p,n,r):
    i = p * (1.0 + r/100) ** n - p
    return i