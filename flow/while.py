x = 0
while x < 10:
    x += 1
    print(x)

counter = 0
list1 = []

while counter <= 100:
    if counter > 50:
        break
    
    if counter % 2 == 0:
        list1.append(counter)
    counter += 1

print(list1)
