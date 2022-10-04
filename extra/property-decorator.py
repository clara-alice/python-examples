"""
class Generic:
    def __init__(self):
        self._x = 10

    def getter(self):
        print('get x')
        return self._x

    def setter(self, nvalue):
        print('set x')
        self._x = nvalue

    def deleter(self):
        print('delete x')
        del self._x

    x = property(getter, setter, deleter)
"""
class Generic:
    def __init__(self):
        self._x = 10

    @property
    def x(self):
        print('getter')
        return self._x

    @x.setter
    def x(self, value):
        print('setter')
        self._x = value

    @x.deleter
    def x(self):
        print('deleter')
        del self._x


g = Generic()

g.x = 12
print(g.x)
del g.x
print(g.__dict__)
