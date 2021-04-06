import operator

li = [1, 2, 4, 8]

print('The Original List is: ', end="")
for i in range(0, len(li)) :
    print(li[i], end='')

print('\r')

operator.setitem(li, 3, 3)

print('List after setitem(): ', end="")
for i in range(0, len(li)) :
    print(li[i], end="")

print("\r")

operator.delitem(li, 1)

print('List after delitem(): ', end='')
for i in range(0, len(li)) :
    print(li[i], end="")

print('\r')


print('The 4th element of the list: ', end="")
print(operator.getitem(li, 2))      # 2 is index of the modified list

# Python program to illustrate
# Finding common member in list
# using 'in' operator
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]

for item in list1 :
    if item in list2:
        print("Overlapping")
else :
    print("Not Overlapping")

