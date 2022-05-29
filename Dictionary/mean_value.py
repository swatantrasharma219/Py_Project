a = {}

b = int(input('Enter the number of elements : '))

for i in range(0,b): # taking user defned dictionary

	c = input('Enter the key : ')	d = float(input('Enter value : '))

	a[c] = d

print('The dictionary is =',a)

s = 0.0 # taking a sum variable 

for i in a.keys():

	s = s + a[i]    # taking sum

print('The mean of values : ',s / len(a)) # for average we devide the sum by lenth
