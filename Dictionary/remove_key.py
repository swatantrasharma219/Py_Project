a = {'Rohan' : 18, 'Karan' : 16, 'Harsh' : 17, 'Sourav' : 20}

print ('The dictionay is : ', a)

b = input('Enter key which you want to delete : ')

if b in a.keys(): # checking inputed b is available in keys or not

	del a[b]        # deleting the key using del, it uses like -> del dic_name[key]	print('The dictionary after removing',b,'this key :',a)

else:

	print('The key is not exist.')
