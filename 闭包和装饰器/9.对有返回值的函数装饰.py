def set_func(func):
    def call_func(*args, **kwargs):
        print("这是个装饰过的函数")
        return func(*args, **kwargs)

    return call_func


@set_func
def test1(*args, **kwargs):
    print("--test1--", args)
    print("-----", kwargs)
    return "ok"


print(test1(11, 22, mm=100))
