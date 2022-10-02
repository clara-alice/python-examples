word1 = 'word 1'
word2 = "word 2"
print(word1, word2)

hello_world = 'hello, ' + 'world!'

quote1 = '"hello"'
quote2 = "'hello'"
quote3 = "\"hello\""
print(quote1, quote2, quote3)

big_string = '''
big string
this is not a comment
'''

print(big_string)

name = 'Bob'
age = 40

greeting_string1 = 'Hello {}, you are {} years old'.format(name, age)
greeting_string2 = f'Hello {name}, you are {age} years old'

print(greeting_string1)
print(greeting_string2)
