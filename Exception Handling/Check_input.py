def ankush(num):         # defining a function

    try:                # it is try block, it runs when no error is raised

        val = int(num)

        print("Input is an integer number.")

        print("Input number is: ", val)

    except ValueError:  # it is exception block, it raised when the program gives a error

        try:

            val = float(num)

            print("Input is an float number.")

            print("Input number is: ", val)

        except ValueError:

            print("This is not a number. Please enter a valid number.")

a = input('Enter a number : ')

ankush(a)              # function calling
