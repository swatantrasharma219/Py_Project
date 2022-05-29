from numpy import*            # importing module

a = []                        # declaring list 

r,c = map(int,input('Enter row and column : ').split())

for i in range(r):

	for j in range(c):		if i == j:

			a.append(1.0)

		else:

			a.append(0.0)

print('The array is \n',array(a).reshape(r,c))  # reshape is use for create the array row and column wise
