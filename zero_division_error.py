#an exception handling example
try:
	f = open("myfile","w")
	a , b  = [int(x) for x in input("Enter two numbers:").split()]
	c = a/b
	f.write("Writing %d into myfile" %c)
except ZeroDivisionError:
	print('Division by zero happened')
	print('Please do not enter 0 in input')
finally:
	f.close()
	print('File closed')
