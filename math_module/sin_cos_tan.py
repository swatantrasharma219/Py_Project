from math import*           # importing math module

a = float(input('Enter the degree : '))

b = sin(radians(a))         # converting radians to degrees

c = cos(radians(a))         # sin,cos,tan for their own convertion

d = tan(radians(a))

print('The value of sin',a,'=',round(b,2))  # rounding the decimal value upto two points

print('The value of cos',a,'=',round(c,2))

print('The value of tan',a,'=',round(d,2))
