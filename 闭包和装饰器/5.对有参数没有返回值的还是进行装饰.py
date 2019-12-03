def set_func(func):
    def call_func(a):
        print("这是个装饰过的函数")
        func(a)

    return call_func


@set_func
def test(num):
    print("这次的测试参数为%d" % num)


test(15)
