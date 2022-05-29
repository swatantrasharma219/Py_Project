a = {}

b = int(input('Enter number of elements : '))

for i in range(0,b): # making user defined dictionary

	c = input('Enter key : ')	d = int(input('Enter value : '))

	a[c] = d #storing value in key

print('The dictionary is =',a)

s = 0 #taking a sum variable 

for i in a.keys():

	s = s + a[i] #adding every value into s(variable)

print('The sum of values =',s)
