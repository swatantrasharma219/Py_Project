from numpy import*

a = list(map(int,input('Enter elements : ').split()))

b = list(map(int,input('Enter elements : ').split()))

c = list(map(int,input('Enter elements : ').split()))

arr = array([a,b,c])    # merging list into numpy array

print(type(arr))

def b(e):  # define funtion

	x = int(input('Enter a element which you want to find : '))	for i in range(len(e)):

		for j in range(len(e[i])):

			if x == e[i][j]:

				print('Row = ',i + 1,'\nColumn = ',j + 1)   #printing row and column

b(arr)    # function calling
