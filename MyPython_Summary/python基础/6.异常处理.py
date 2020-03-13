# Python中的程序错误至少包括两种，一种是语法错误，另一种则是异常
# 所谓的语法错误，就是代码不符合编程规范，无法被识别与执行，比如：
# if name is not None   #这里末尾缺少了冒号，程序会报invalid syntax
#     print(name)
# 而异常则是指程序语法正确，也可以被执行，但在执行过程中遇到了错误，跑出了异常

try:
    s = input('please enter two number separated by comma:')
    num1 = int(s.split(',')[0].strip())
    num2 = int(s.split(',')[1].strip())

except ValueError as err:
    print('Value Error:{}'.format(err))

print('continue')

# except block只接受与他相匹配的异常类型并执行，如果程序抛出的异常并不匹配，那么程序照样会终止并退出
# 在难以保证程序覆盖所有的异常类型时可以在最后一个except block 声明其处理类型是Exception
# 和try，except放一起使用的常有finally，无论发生什么情况，finally block 中的语句都会被执行

# 一个常见的场景是文件的读取
import sys
try:
    f = open('./resource/in.txt', 'r')
except OSError as err:
    print('OS Error :{}'.format(err))
except:
    print('Unexpected error:', sys.exc_info()[0])
finally:
    f.close()


# 用户自定义异常，此处定义MyinputError类
class MyInputError(Exception):
    """
    Exception raised when there're error in input
    """
    def __init__(self, value):  # 自定义异常类型的初始化
        self.value = value

    def __str__(self):  # 自定义异常类型的string表达形式
        return "{} is invalid input".format(repr(self.value))   # 这里的repr()和str()一样是转换为字符串，不过str()是给人看的，repr()是给解释器看的

try:
    raise MyInputError(1) # 抛出MyInputError这个异常
except MyInputError as err:
    print('error:{}'.format(err))


