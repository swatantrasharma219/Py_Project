try:          # it executed when program runs without error

	a = float(input('Enter a number : '))	b = float(input('Enter another number : '))

	c = a / b

	print(a,'devide by',b,'=',round(c,2))   # rounding decimal point upto two

except ZeroDivisionError:         # it raised when input number b = 0

	print(a,'cannot be devide by',b)
