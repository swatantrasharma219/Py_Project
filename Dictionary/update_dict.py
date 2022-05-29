a = {}

b = int(input('Enter the number of elements : '))

for i in range(0,b):

	c = input('Enter key : ')	d = input('Enter value : ')

	a[c] = d

print('The dictionary is :',a)

e = input('Please type the key to update the value : ')

for i,j in a.items(): # this loop compare i as key of a dic and j as a value of a dic

	if i in e:          # checking if i is present in e

		f = input('Enter value : ')

		a[i] = f          # overwrite to the value of this key

		print('After updating :',a)

		break

if i not in e:        # when the key is not available in the dictionary 

	print('Invalid key.')
