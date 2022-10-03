list1 = [1, 2, 4, 9, 2, 9, 5]
print(sorted(list1, reverse = True))

list2 = [('a', 30), ('b', 123), ('c', 9)]
sort_function = lambda item: item[1]
print(sorted(list2, key = sort_function))
