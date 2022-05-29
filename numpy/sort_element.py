from numpy import*                                       # importing module

a = list(map(int,input('Enter a elements : ').split()))

arr = array(a)

print('Before sorting :',arr)

arr = sort(arr)                                         # using sort function

print('After sorting :',arr)
