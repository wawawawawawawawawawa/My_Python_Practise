# def 是函数的声明，是可执行语句，意味着函数直到被调用前都是不存在的。当程序调用函数时，def语句才会创建一个新的函数对象，并赋予名字
def find_largest_element(l):
    if not isinstance(l, list):
        print('input is not type of list')
        return
    if len(l) == 0:    # 这里注意isinstance的用法
        print('empty input')
        return
    largest_element = l[0]
    for item in l:
        if item > largest_element:
            largest_element = item
    print('largest element is :{}'.format(largest_element))
find_largest_element([8, 1, -3, 2, 0])

# 在函数最后，可以返回调用结果(return或yield)，也可以不返回
# 需要注意的是，主程序调用函数时，必须保证这个函数已经定义过，不然会报错
# 但是如果在函数内部调用其他函数，函数间哪个声明在前，哪个在后就无所谓，因为def是可执行语句，函数调用前都不存在，只需保证调用时函数已经声明好即可


def my_func(message):
    my_sub_func(message)


def my_sub_func(message):
    print('Got a massage:{}'.format(message))

my_func('hello world')
# Python是dynamically typed的，可以接受任何数据类型，对于函数参数来说同样适用


def my_sum(a, b):
    return a + b
print(my_sum([1, 2], [3, 4]))
# 当然，两个数据类型不同的参数输入会报错，python可以不考虑输入的数据类型，我们把这种行为称为多态

# 函数的嵌套
# 作用一：能够保证内部函数的隐私，内部函数只能被外部函数所调用和访问，不会暴露在全局作用域，例如数据库的连接，密码等是隐私的
# def connect_DB():
#     def get_DB_configuration():
#         ...
#         return host, username, password
#     conn = connector.connect(get_DB_configuration())
#     return conn
# 作用二：合理的应用函数嵌套，能够提高程序的运行效率


def factorial(input):
    # validation check
    if not isinstance(input, int):
        raise Exception('input must be an integer')
    if input < 0:
        raise Exception('input must be greater or equal to 0')

    def inner_factorial(input):
        if input <= 1:
            return 1
        return input * inner_factorial(input - 1)
    return inner_factorial(input)
print(factorial(5))
# 这里计算一个数的阶乘，使用函数的嵌套，输入的合法检查只用一次就行


# 在函数内部可以访问全局变量但是不可以改变全局变量的值，这是因为Python解释器会默认函数内部的变量为局部变量，但是又发现
# 局部变量没有申明所以报错，要想修改全局变量必须增加global的申明
# 类似的，对于嵌套函数，内部函数可以访问外部函数定义的变量，但是无法修改，若要修改，需要加上nonlocal这个关键字
def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner:{}'.format(x))
    inner()
    print("outer:{}".format(x))

outer()
# 闭包(closure):闭包和嵌套函数类似，不过外部函数返回的是一个函数，而不是具体的值


