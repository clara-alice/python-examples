# tuple is immutable, list isn't


# list + functions + methods
list1 = [1, 2, 3, 4, 'test']
list1.append('test 2')
list1.reverse()

print(len(list1))
print(list1)

# tuple
tuple1 = (1, 2, 3, 4, 5, (1, 2, 3, 4, 5, 6, (1, 2, 3, 4)))
print(tuple1)

# picking values
print(list1[2])
print(tuple1[5][6])

print(list1[-1])
print(tuple1[-1])

# slicing
list2 = [1, 2, 3, 4]
list3 = list2[1:-1]
print(list3)
print(list2[::-1])

