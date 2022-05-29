from numpy import* #importing numpy

r,c = list(map(int,input('Enter row and column : ').split()))

m1 = list(map(int,input('Enter elements : ').split()))

m1 = array(m1).reshape(r,c) #here we use reshape for the dimensions like -> reshape(2,2), it denotes the array have two dimensions

print('The array =',m1)
