# Python program to illustrate functions
# Functions can return another function

def  create_adder(x) :
    def adder(y) :
        return x+y
    return adder

add_15 = create_adder(15)

print(add_15(10))
#-------------------------------------------------------------------------------------------------------------

def hello_decorator(func) :
    def inner1() :
        print('This is before function Execution.')

        func()

        print('This is after Function Execution.')

    return inner1()

def function_to_be_used() :
    print('This is Inside Function')

function_to_be_used  = hello_decorator(function_to_be_used)

function_to_be_used()

