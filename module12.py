# A simple generator for Fibonacci Numbers
def fib(limit) :
    a, b = 0, 1

    while a<limit :
        yield a
        a, b = b, a + b

x = fib(5)      # Create a generator object

print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())



print("\nUsing for loop")
for i in fib(5) :
    print(i)

#-------------------------------------------------------------------------------------------------------
# lambda functions inside map()
# and filter()
a = [100, 45, 76, 8, 9, 5433, 976642, 22, 97, 64]

filtered = filter(lambda x:x % 2 == 0, a)   # in filter either we use assignment or
print(list(filtered))                       # conditional operator, the pass actual
                                            # parameter will get return



maped = map(lambda x:x % 2 == 0, a)         # in map either we use assignment or
print(list(maped))                          # conditional operator, the result of
                                            # the value will get returned

#--------------------------------------------------------------------------------------------------------

a = 1

def f() :
    print('Inside f() : ', a)

def g() :
    a = 2
    print('Inside g() : ', a)

def h() :
    global a
    a = 3
    print('Inside h(): ', a)

print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)

