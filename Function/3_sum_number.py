def three(a,d):                       # funtion define

	e = 0                               # taking sum variable	for i in range(0,len(a)):

		for j in range(i + 1,len(a)):

			for k in range(j + 1 , len(a)):

				e = a[i] + a[j] + a[k]        #adding value

				if(e == d):                   # checking value is available after adding or not

					print("The position of this number by adding =",a[i],a[j],a[k]) # printing the number

x = list(map(int,input('Enter elements : ').split()))

y = int(input("Enter your target : "))

three(x,y)  # function calling
