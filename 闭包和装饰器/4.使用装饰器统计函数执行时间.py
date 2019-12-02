import time


def set_func(func):
    def call_func():
        print("-----1------")
        start_time = time.time()
        func()
        end_time = time.time()
        print("函数执行的时间为%f" % (end_time - start_time))

    return call_func


@set_func  # 这里相当于test = set_func(test),这里虽然进行了重新赋值，但是由于函数名相同，所以外部调用是一致的
def test():
    print("====test====")
    for i in range(100000):
        pass


test()
