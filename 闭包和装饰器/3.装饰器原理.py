def set_func(func):
    def call_func():
        print("-----1------")
        func()

    return call_func


@set_func  # 这里相当于test = set_func(test),这里虽然进行了重新赋值，但是由于函数名相同，所以外部调用是一致的
def test():
    print("====test====")


test()
