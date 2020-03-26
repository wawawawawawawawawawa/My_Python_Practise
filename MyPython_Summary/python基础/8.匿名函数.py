# 匿名函数的格式
# lambda argument1,argument2,...argumentN:expression
# 匿名函数的关键字是lambda，之后是一系列参数，然后用冒号隔开，最后则是由这些参数组成的表达式
square = lambda x: x**2
print(square(3))

# 需要注意的是匿名函数lambda与常规函数的两个区别：
# 第一：lamnda是一个表达式(expression),并不是一个语句(statement)
# 所谓的表达式，就是用一系列“公式”去表达一个东西，比如x + 2、 x**2等等；
# 而所谓的语句，则一定是完成了某些功能，比如赋值语句x = 1完成了赋值，print 语句print(x)完成了打印，条件语句 if x < 0:完成了选择功能等等

# lambda可以用在列表内，常规函数不能
[(lambda x: x*x)(x) for x in range(10)]

# lambda可以用作某些函数的参数，而常规函数def不能
l = [(1, 30), (5, 20), (3, 70)]
l.sort(key=lambda x: x[1])
print(l)

# 第二：lambda的主体是只有一行的简单表达式，并不能扩展成一个多行的代码块

# 如果对一个列表中的所有元素做平方操作
squared = map(lambda x: x**2, [1, 2, 3, 4])
# 这里的函数map(function, iterable)的第一个参数是函数对象，第二个参数一个可以遍历的集合，他表示对iterable的每一个元素，都运用function这个函数

# Python的函数式编程：所谓的函数式编程，是指代码中每一块都是不可变的(immutable),都由纯函数(pure function)的形式组成。这里的
# 纯函数是指函数本身相互独立，互不影响，对于相同的输入总有相同的输出


# 列表的值加倍非纯函数版本,这里会改变源列表，所以每次得到的结果不一样
def multiply_2(l):
    for index in range(len(l)):
        l[index] *= 2
    return l


# 纯函数版本是创建一个新的列表，使得每次的结果一致
def multiply_2_pure(l):
    new_list = []
    for item in l:
        new_list.append(item)
    return new_list


# filter函数：filter(function,iterable)函数和map函数类似，他是返回True或者False,最后将返回True的元素组成一个新的可遍历的集合
# 举个栗子，比如要返回一个列表中所有的偶数
l = [1, 2, 3, 4, 5, 6]
new_list = filter(lambda x: x % 2 == 0, l)


# reduce(function, iterable)函数，它通常用来对一个集合做一些累积操作，function同样是一个函数对象，规定他有两个参数，
# 表示对iterable中的每个元素以及上一次调用的结果，运用function进行计算，最后返回一个单独的数值
# 举个例子，想要计算某个列表元素的乘积
from  functools import reduce
l = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, l)
