from functools import wraps
import time


def func(message):
    print('Got a message:{}'.format(message))

send_message = func
send_message('hello world1')
# 函数可以作为对象赋予变量


def func1(message):
    return 'Got a message:' + message


def root_call(func, message):
    print(func(message))

root_call(func1, 'hello world2')
# 函数可以作为参数传入另一个函数


def func3(message):
    def get_message(message):
        print('Got a message:{}'.format(message))
    return get_message(message)
func3('hello world3')
# 可以在函数里定义函数，就是函数的嵌套


def func_closure():
    def get_message(message):
        print('Got a message:{}'.format(message))
    return get_message
send_message = func_closure()
send_message('hello world4')
# 函数的返回值可以是函数对象(闭包)


def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()
    return wrapper


def greet():
    print('hello greet')

greet = my_decorator(greet)   # 这里返回了函数wrapper
greet()
# 这里是一个简单的装饰器，变量greet指向了内部函数wrapper()，而内部函数warpper()中又会调用原函数greet()


def my_decorator(func):
    @wraps(func)
    def wrapper():
        print(func.__name__ + 'wrapper of decorator')
        func()
    return wrapper


@my_decorator
def greet():
    """does some test"""
    print('hello greet1')

greet()
print(greet.__doc__)  # 这里如果没有使用 @wrap(func)语法糖的话将会打印wrapper的docstring,为None
# 更优雅的一种写法，称之为语法糖


# 当被装饰的函数有参数时，就需要在warpper上加参数，*args,**kwargs表示接受任意数量和类型的参数
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('wrapper of decorrator')
        func(*args, **kwargs)
    return wrapper


print(greet.__name__)  # 可以发现greet()函数被装饰后他的元信息变了，变成了wrapper()函数，若要保留可以使用@functools.wrap
import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('wrapper of decorrator')
        func(*args, **kwargs)
    return wrapper


# 装饰器的嵌套，执行顺序从里到外
import functools


def my_decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator1')
        func(*args, **kwargs)
    return wrapper


def my_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator2')
        func(*args, **kwargs)
    return wrapper


@my_decorator1
@my_decorator2
def greet(message):
    print(message)


greet('hello world')

# 输出
# execute decorator1
# execute decorator2
# hello world

# 装饰器使用实例
# 1.身份验证
# 比如你在一个网站不登录可以浏览内容，但是留言就必须登录，点击发布时服务器会查询是否登录
"""
def authenticate(func):
    def wrapper(*args, **kwargs):
        request = args[0]
        if check_user_logged_in(request):  # 如果用户处于登录状态
            return func(args,**kwargs)     # 执行函数 post_comment()
        else:
            raise Exception('Authentication failed')
    return wrapper
@authenticate
def post_comment(request,...)  #代表用户发表评论，每次调用之前都查询是否登录
    ...
"""

# 2.日志记录
# 如果怀疑某个函数运行时间过长导致系统的latency(延迟)增加，想测试函数执行时间


def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print('{} took {} ms'.format(func.__name__, (end - start)*1000))
        return res
    return wrapper


@log_execution_time
def calculate_similarity(items):
    pass
# 3.输入合理性检查

# 4.缓存 LRU cache,在Python中的表示形式是@lru_cache,它会缓存进程中的函数参数和结果，当缓存满后删除least recenly used的数据

# 所谓装饰器，就是通过装饰器函数，来修改原函数的一些功能，使得原函数不需要修改













