a = {}

b = int(input('Enter the number of elements : '))

for i in range(0,b):

	c = input('Enter key : ')	d = input('Enter value : ')

	a[c] = d

print('The dictionary is :',a)

print('After sorting through keys : ')

for i in sorted(a.keys()): # sorted() is used for sorting dictionary in ascending order

	print((i,a[i]))          # printing i as key and a[i] as value
