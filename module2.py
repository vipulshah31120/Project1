def table(n) :
    for x in range (1, 11) :
        print(n ,'*', x ,'=', x*n)


#----------------------------------------------------------------------------

lst = []    # creating an empty list
n = int(input("Enter Number of Elements: "))
for i in range (0, n) :
    ele = int(input())

    lst.append(ele)     # adding the element

print(lst)

#----------------------------------------------------------------------------

lst1 = []
lst2 = []

lst1 = [int(item) for item in input("Enter the Numbers: ").split()]

lst2 = [item for item in input("Enter the Alphabets:  ").split()]

print(lst1)
print(lst2)