def set_func(func):
    def call_func():
        print("这是个装饰过的函数")
        func()

    return call_func


@set_func
def test1():
    print("--test1--")


@set_func
def test2():
    print("--test2--")


test1()
test2()