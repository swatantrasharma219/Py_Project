def conv(a):                                        # defining function

	print('The Binary number is =',bin(a)[2::])       # bin is used for convert decimal to binary	print('The Octal number is =',oct(a)[2::])        # oct is used for convert decimal to octal

	print('The Hexadecimal number is =',hex(a)[2::])  # hex is used for convert decimal to hexadecimal

x = int(input('Enter a number : '))

conv(x)                                             # function calling
