import functools


def title(name):
    print(name)  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    title("functional programming")

    #Closures and Currying
    def outer(outer_arg):
        def inner(inner_arg):
            return inner_arg + outer_arg
        return inner
    func = outer(10)
    print(func(5))
    print(func.__closure__)
    print(func.__closure__[0])
    print(func.__closure__[0].cell_contents)

    #Partial functions
    def func(a, b, c):
        return a, b, c
    p_func = functools.partial(func, 10)
    print(p_func(3, 4))
    p_func1 = functools.partial(func, 10, 12)
    print(p_func1(3))

    #decorator
    def decorator(func):
        @functools.wraps(func)
        def new_func(*args, **kwargs):
            print('decorator was here')
            return func(*args, **kwargs)

        return new_func

    @decorator
    def add(a, b):
        return a + b
    print(add(2, 3))



    #filter
    def over_two(lst1):
        lst2 = [x for x in lst1 if x > 2]
        return lst2

    print(over_two([4, 3, 2, 1]))
    n = [4, 3, 2, 1]
    print(list(filter(lambda x: x > 2, n)))