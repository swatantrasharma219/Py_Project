def fun(n): #define a funtion

	if n <= 1:

		return 1

	else:

		return n * fun(n - 1)   # it returns n-1 until the value of n <= 1
 
 a = int(input('Enter a number : '))
 
print('The factorial : ',fun(a)) # function calling
