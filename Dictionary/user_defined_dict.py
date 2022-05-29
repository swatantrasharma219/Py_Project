a = {} #declaring dictionary

b = int(input('Enter the number of elements : '))

for i in range(0,b):

	x = input('Enter key : ')	y = input('Enter value : ')

	a[x] = y #storing value in specified key

print('The dictionary is =',a)
