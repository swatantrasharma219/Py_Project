from numpy import*                  # importing module 

a = list(map(int,input('Enter elements : ').split()))

brr = array(a)

a = sort(a)                          # sorting list

arr = array(a)

b = int(input('Enter a number to check if any number is bigger or not : '))

if arr[len(arr) - 1] < b:

	print(b,'is greater than',brr,'elements')else:

	print(b,'is not greater than',brr,'elements')
