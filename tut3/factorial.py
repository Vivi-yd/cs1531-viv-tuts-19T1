"""
Q1: Write a function that computes the factorial of a given integer n. 
You may assume that n is non-negative. (Note: 0! = 1). If n is not specified, 
then it should compute the factorial of 5. e.g., 
"""

def factorial(n=5):
    if n <= 0:
        return 1
    else:
        return n* factorial(n-1)

print(factorial())


