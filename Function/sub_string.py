def sub_str(a,b):     # define function

	for i in a[:]:		if i.startswith(b):

			continue         # skip the condition

		else:

			a.remove(i)     # removing the element from list a

	print('Sub string from starting :',a)

x = list(map(str,input('Enter the list : ').split())) #  taking list elements by sapace separated 

y = input('Enter sub element : ')

sub_str(x,y)    #calling function
