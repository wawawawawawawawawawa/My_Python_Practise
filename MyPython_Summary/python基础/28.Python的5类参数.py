# python的五类参数：位置参数，关键字参数，默认参数，可变位置参数，可变关键字参数

# 定义函数 f，只有一个参数 a，a 既可能为位置参数，也可能为关键字参数，这取决于调用函数 f 的传参
def f(a):
    print(f'a:{a}')


f(1)  # 这样调用就是位置参数(positional argument)
f(a=1)  # 这样调用就是关键字参数(keyword argument)


# 如果函数的定义如下
def f(a=1):
    print('有默认参数')


f()  # 这样调用就是用的是默认参数
f(2)  # 这样调用就使得a 的值为2


def f(a, *b, **c):
    print(f'a:{a},b:{b},c:{c}')


# 可变位置参数：出现带一个 * 号的参数b为可变位置参数
# 可变关键字参数：出现带两个 * 号的参数c为可变关键字参数
# 可变表示函数被赋值的变量个数是变化的
f(1, 2, 3, w=4, h=5)

# 查看参数
# 借助python的inspect模块查看参数的类型
from inspect import signature

for name, val in signature(f).parameters.items():
    print(name, val.kind)

# 传递规则
# 1.
# 不带默认值的位置参数缺一不可
# 2.
# 关键字参数必须位于位置参数的右边
# 3.
# 对同一个形参不能重复传值
# 4.
# 默认参数的定义应该在位置形参的右边
# 5.
# 可变位置参数不能传入关键字参数
# 6.
# 可变关键字参数不能传入位置参数
