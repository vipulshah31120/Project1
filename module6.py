# Python program showing
# how to take multiple input
# using List comprehension

x, y = [int(x) for x in input("Enter the values: ").split()]
print("First No.: ",x)
print("Second No.: ",y)



z = [int(x) for x in input("Enter Multiple Values: ").split()]
print("Multiple Values are: ",z)




#In case we wish to take input separated by comma(, ), we can use following:

z = [int(x) for x in input("Enter Multiple Values: ").split(',')]
print("Multiple Values are: ",z)




#sep parameter in print()

print('V', 'I', 'P', 'U', 'L', sep='')
print('01','04', '2021', sep='-')
print('shubham', 'gmail.com', sep='@')
