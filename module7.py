exp = 10 + 20 *30
print(exp)


# Left-right associativity
print(100 / 10 * 10)
# 100 / 10 * 10 is calculated as
# (100 / 10) * 10 and not
# as 100 / (10 * 10)

a = 10
b = 20

min  = a if a<b else b
print(min)

# Use tuple for selecting an item
print((b, a)  [a<b])    #(if_test_false,if_test_true)[test]


# Use Dictionary for selecting an item
print({True : a , False : b} [a<b])


print(any([False, True, False , False, True]))
print(all([False, True, False , False, True]))