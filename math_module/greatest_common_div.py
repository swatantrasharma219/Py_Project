from math import*             # importing math module

a = int(input('Enter first number : '))

b = int(input('Enter second number : '))

c = gcd(b,a)                  # here gcd is a function of math module which represents the greatest common divisor

print('The gcd of',a,'and',b,'is =',c)
