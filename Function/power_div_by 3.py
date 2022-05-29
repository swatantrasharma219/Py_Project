# Q:- Find if the inputed power is divisible by 3 or not if , divided by three then print True otherwise False

cube = lambda x : x**3                                  # defining lambda function

by_three = lambda y : True if (y % 3) == 0 else False   # defining lambda funtion and calling another lambda funtion 

a = int(input('Enter a number : '))

print(by_three(a))                                      # function calling
