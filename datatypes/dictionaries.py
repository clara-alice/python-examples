# basics
test_dict = {
    'a': 10,
    'b': 11,
}

print(test_dict['a'])
print(test_dict.items())
print(test_dict.keys())
print(len(test_dict))

# converting
print(list(test_dict))
print(tuple(test_dict))
print(str(test_dict))

# indexing
print(test_dict.get('a')) # doesnt crash
print(test_dict['a']) # crash

# update
test_dict.update({'c': (1, 2, 3)})
test_dict.update(d = 'test', e = 'two')

print(test_dict)
