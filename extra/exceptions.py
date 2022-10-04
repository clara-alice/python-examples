def division(a: int, b: int):
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        print('cannot divide by zero')
        result = None
    finally:
        return result

def can_raise(a):
    if a == 'test':
        raise TypeError('cannot print test')
    print(a)

print(division(1, 0))
print(division(4, 3))

can_raise('abc')
can_raise('test')
