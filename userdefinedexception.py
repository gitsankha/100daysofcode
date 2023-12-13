#syntax
#class CustorError(Exception):
#	pass
#raise CustomError("Example of Custom exceptions in Python")


class MyError(Exception):
	
	#initializer
	def __init__(self,value):
		self.value = value
	
	#__str__ is to print the value
	def __str__(self):
		return(repr(self.value))
		

try:
	raise(MyError(3*2))
except MyError as error:
	print("A New Exception occurred:",error.value)
