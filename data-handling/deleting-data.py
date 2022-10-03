a = 1
del a
# print(a) # throw error

a = [1, 2, 3]
del a[1]
a.remove(3)
a.pop()

print(a)

a = [1, 2, 3]
a.clear()

print(a)
