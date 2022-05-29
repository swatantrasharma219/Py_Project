a = {}

b = list(map(str,input('Enter keys : ').split())) # it takes string input with space separated .

c = list(map(str,input('Enter value : ').split()))

if len(b) >= len(c):

	a = dict(zip(b,c)) #zip is use for merging ,it does the the first list 1st element as key and second list 1st element as value and so on.	print('After merging : ',a)

else:

	print('Number of keys do not smaller than number of values.')
