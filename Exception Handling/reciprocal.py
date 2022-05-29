try:

	n = int(input('Enter a number : '))	assert n % 2 == 0            # it is use to check if inputed number is divisiable by zero or not 

except:                        # if assert gives error then except block raised

	print('It is a odd number')

else:                          # if code run successfully then else block exhecuted

	r = 1 / n

	print('Reciprocal of the number is :',r)
