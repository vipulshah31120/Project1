# Python program to demonstrate
# Adding Elements to a Array

# importing "array" for array creations
import array

# array with int type
arr = array.array('i', [1, 2, 3])

print('Array Before Insertion: ', end='')
for i in range(0, 3) :
    print(arr[i], end='')

print()


# inserting array using
# insert() function
arr.insert(1,4)     #(pos, ele)

print('Array After Insertion: ', end='')
for i in (arr) :
    print(i, end='')
print()


# array with float type
b = array.array('d', [2.5, 3.2, 3.3])

print('Array Before Insertion: ', end='')
for i in range(0, 3) :
    print(b[i], end='')
print()

# adding an element using append()
b.append(4.4)

print('Array After Insertion: ', end='')
for i in (b) :
    print(i, end='')
print()

