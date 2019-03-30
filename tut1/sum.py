
"""
For a given number, find the sum of n + n^2 + n^3 + … + n^n
"""
n = int(input("give me a number: "))

s = 0
for i in range(1, n+1):
    s = s + n**i

print(s)