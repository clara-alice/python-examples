# list unpacking
def print_all(*arguments):
    for argument in arguments:
        print(argument)

print_all(1, 2, 3, 4, 5)


# dict unpacking
def print_keys(**arguments):
    print(arguments)

print_keys(key1 = 1, key2 = 2)


