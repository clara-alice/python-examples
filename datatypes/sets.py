set1 = {1, 2, 3, 4, 4}
set1.add(1)
set1.add(99)
set1.remove(1)

print(set1)


print({1,2,3}.union({3,4,5}))
print({1,2,3} | {3,4,5})

print({1,2,3}.intersection({3,4,5}))
print({1,2,3} & {3,4,5})

print({1,2,3}.difference({3,4,5}))
print({1,2,3} - {3,4,5})
