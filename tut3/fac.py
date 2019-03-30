def fact(n):
    if n <= 0:
        return 1
    return n*fact(n-1)


print(fact(3))

def fact2(n):
    ans = 0
    for i in range(n):
        ans = ans*i
    return ans
