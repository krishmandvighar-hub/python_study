##Easy
#1.Factorial using recursion---------------------------------------
#Write a function factorial(n) that returns n!.
n = int(input("enter the num: "))
def factor(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factor(n-1)
print("Factorial: ",factor(n))
    
##2.Fibonacci sequence--------------------------------------------
#Write a recursive function to return the nth Fibonacci number.
def fibonacci(m):
    if m<=1:
        return m
    else:
        return fibonacci(m-1)+ fibonacci(m-2)
                                        
print("Fibonacci sequence: ",fibonacci(7))
#3.Sum of natural numbers
#Find the sum of first n natural numbers using recursion.
m=[45,65,6,5,6,525,5,4]
def sum(m):
    if len(m)==0:
        return 0
    else:
        return m[0]+sum(m[1:])
print("sum of the number: ",sum(m))    
##🟡 Medium
##Reverse a string
##Write a recursive function to reverse a string.

def string(s):
    if len(s) == 0:
        return s
    return s[-1] + string(s[:-1])
print(string("kris"))

    
##Check palindrome
##Use recursion to check if a string is a palindrome.
##Power of a number
##Compute x^n recursively (handle negative powers too if possible).

def power(x, n):
    if n == 0:
        return 1
    
    if n < 0:
        return 1 / power(x, -n)
    
    return x * power(x, n - 1)

print(power(2, 3))   
print(power(2, -2))


##🔴 Hard
##Tower of Hanoi
##Print steps to solve Tower of Hanoi for n disks.
##Generate all subsets (Power Set)
##Given a list, return all possible subsets using recursion.
##Permutations of a string
##Generate all permutations of a string.
