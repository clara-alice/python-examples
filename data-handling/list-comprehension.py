list1 = [num for num in range(0, 100)]
print(list1)

list2 = [(num, num * 2, num * 3) if num < 10 else (num, num, num) for num in range(0, 100)]
print(list2)


f = lambda x: x * 2
list3 = [[f(x) for x in range(32)] for y in range(16)]
print(list3)

