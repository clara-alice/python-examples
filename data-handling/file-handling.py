# 1
file = open('test.txt')
print(list(file))
file.close()

# 2
with open('test.txt') as file:
    # print(list(file))
    # print(file.read())

    for line in list(file):
        print(line)

with open('test.txt', 'a') as file:
    file.write('bbbbbbbbbbbbbbbbbbbb\n')
