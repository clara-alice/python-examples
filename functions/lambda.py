print((lambda x: x * 2)(2))

triple = lambda n: n * 3
n = lambda a, b: lambda x: a * x + b
f = n(3, 10)

print(f(2), f(3), f(f(2)))

