from numpy import* #importing numpy

print('First Matrix')

a = list(map(int,input('Enter elements : ').split()))   #taking list input with sapce separated

b = list(map(int,input('Enter elements : ').split()))

c = list(map(int,input('Enter elements : ').split()))

print('Second Matrix')

d = list(map(int,input('Enter elements : ').split()))   #taking list input with sapce separated

e = list(map(int,input('Enter elements : ').split()))

f = list(map(int,input('Enter elements : ').split()))

g = array([a,b,c])      #passing lists in array funtions

h = array([d,e,f])

print('Matrix a',g,'Transpose of a',g.T,'Matrix b',h,'Transpose of b',h.T,'Sum of matrix',g+h,'Multiplication of matrix',g.dot(h),'Cross product of a and b',g*h,sep = '\n')
