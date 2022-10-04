import time

# decorators are functions that decorate other functions


def func():
    print('hello')

def wrapper(fn):
    print('[')
    fn()
    print(']')

wrapper(func)
wrapper(lambda: print('...'))

def function_generator():
    def new_function():
        print('new function')

    return new_function

fn = function_generator()
fn()

def decorator1(fx):
    def dwrapper(*args):
        print('\ndecoration starts')
        fx(*args)
        print('decoration ends')

    return dwrapper

@decorator1
def f(n):
    print(n * 2)

f(2)


def time_decorator(func):
    def wrapper(*args):
        start_time = time.time()
        func(*args)
        duration = time.time() - start_time

        print(f'duration: {duration}')
    
    return wrapper

@decorator1
@time_decorator
def sleep_some():
    time.sleep(1)

@time_decorator

def iterations():
    for i in range(10000):
        pass

# iterations()
# sleep_some()

