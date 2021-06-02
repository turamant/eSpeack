import inspect


def simple_coroutine():
    print('-> coroutine started')
    x = yield 43
    print('-> coroutine received',x)


if __name__=='__main__':
    my_coro = simple_coroutine()
    print(inspect.getgeneratorstate(my_coro))
    print("3", my_coro)
    print(inspect.getgeneratorstate(my_coro))
    print("4", next(my_coro))
    print(inspect.getgeneratorstate(my_coro))
    print("5", my_coro.send(42))
    print(inspect.getgeneratorstate(my_coro))
