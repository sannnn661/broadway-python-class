#Python Assignment 1
#1. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn + …
#2. Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
#3. Write a Python program to check whether the input number is prime or not.

num = int(input("enter a num"))
newnum = 0
total =0
for _ in range(num):
    newnum = newnum * + num
    total += newnum

print(total)