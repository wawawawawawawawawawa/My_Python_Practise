def set_func(func):
    def call_func(*args, **kwargs):
        print("这是个装饰过的函数")
        return func(*args, **kwargs)

    return call_func


def set_func1(func):
    def call_func(*args, **kwargs):
        print("这也是个装饰过的函数")
        return func(*args, **kwargs)

    return call_func


@set_func1
@set_func
def test1(*args, **kwargs):
    print("--test1--", args)
    print("-----", kwargs)
    return "ok"


print(test1(11, 22, mm=100))
# 装饰的时候由于set_func1够不到函数，所以先装饰set_func，但是解释器执行的时候从上往下，所以先执行set_func1
