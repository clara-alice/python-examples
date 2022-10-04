# translate string into python code
# be careful

# eval
# less powerful: only evaluate code 

# exec
# more powerful: execute any code

print(eval('2+2+(lambda x: x*2)(2)'))


exec('a = 10')
print(exec('''
if a == 10:
    print('hello')
'''))
