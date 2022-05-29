a = {}

b = list(map(str,input('Enter elements : ').split())) #taking sppace separated input and stored into list through map()

for i in b:

	a[i] = b.count(i)  # count is uses for the occurance of the elemennt , after that a[i] stored it in its valueprint('Frequenncy is ')

for i,j in a.items(): #for printing every pair in new lline

	print(i,':',j)
