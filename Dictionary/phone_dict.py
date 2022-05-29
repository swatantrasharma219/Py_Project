a = {}

c = int(input('Enter the number of person : '))

for i in range(0,c):

	e = input('Enter name : ')	f = input('Enter ph.no : ')

	a[e] = f

print('The phone directory is : ',a)

b = input('Enter person name to find ph.no : ')

b = b.split() #separating the string with space

for i in range(0,len(b)):

	if b[i] in a.keys():

		print('Here is the data :',b[i],'->',a[b[i]]) #b[i],it prints the key and a[b[i]],it prints the value of this key

	else:

		print(b[i],'is a invalid data.')  #if there is not existing key ,it prints invalid data
