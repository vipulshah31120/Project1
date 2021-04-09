def myfunc(arg1, *argv) :
    print('First Argument: ', arg1)
    for arg in argv :
        print('Next Argument Through argv: ', arg)

myfunc('Hello', 'i\'m', 'Vipul', 'Shah')


#--------------------------------------------------------------------------------------
def myfunc1(arg1, **kwargs) :
    for key, value in kwargs.items() :
        print("%s == %s" %(key, value))

myfunc1("Hi", first = "Geeks", mid = "for", last = "Geeks")

#--------------------------------------------------------------------------------------
# A Python program to generate squares from 1
# to 100 using yield and therefore generator

# An infinite generator function that prints
# next square number. It starts with 1
def nextsquare() :
    i = 1
    while True :        # An Infinite loop to generate squares
        yield i*i
        i += 1          # Next execution resumes
                         # from this point
for num in nextsquare() :
    if num > 100 :
        break
    print(num)
