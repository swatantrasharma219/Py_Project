from numpy import*              # importing module 

a = list(map(int,input('Enter the elements : ').split()))

b = int(input('Enter a number which you want to count : '))

arr = array(a)        # storing in array

if b in arr:

	print(b,'has',count_nonzero(arr == b),'times')      # count_nonzero funtion collect true elements , and condition go through itelse:

	print(b,'is not available.')
