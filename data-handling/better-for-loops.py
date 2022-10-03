inventory_names = ['a', 'b', 'c']
inventory_numbers = [123, 12, 44]

for name, number in list(zip(inventory_names, inventory_numbers)):
    print(name, ':', number)

for index, name in enumerate(inventory_names):
    print(f'[{index}] -> {name}')

for index, inventory_entry in enumerate(zip(inventory_names, inventory_numbers)):
    name, number = inventory_entry
    print(f'[{index}] -> {name}: {number}')
