"""
Write a program that takes n words from a user and outputs a string that contains all the words separated by a space. n here is the number of words the user would like to input.
"""
s = ""
num = int(input("how many words? "))
for i in range(num):
    w = input("gimme words: ")
    s += w + " "

print(s, end="")