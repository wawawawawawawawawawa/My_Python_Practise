def set_func(func):
    def call_func():
        print("-----1------")
        func()

    return call_func


@set_func
def test():
    print("====test====")


test()
