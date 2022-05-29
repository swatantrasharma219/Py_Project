from math import*           # importing math module

a = int(input('Enter the log value : '))

b = int(input('Enter the base value : '))

c = log(a,b)                # the log function passes two values first one is the value of log and second one is the base of log

print('The value of log',a,'base',b,'=',round(c,2)) # rounding the value of log upto two decimal
