#open a file
f = open('myfile','w')

#do some processing
a,b = [int(x) for x in input("Enter two numbers: ").split()]
c = a/b
f.write('Writing %d into myfile' %c)

#close the file
f.close()
print("File closed")
