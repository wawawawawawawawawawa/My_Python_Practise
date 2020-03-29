# len(s)：返回对象中元素的个数

# max(iterable,*[, key, default]) ：返回最大值
# 这里的 * 代表关键字参数，后面跟的必须是关键字参数， [] 则是可选参数的意思，可有可无
a = [{'name': 'xiaoming', 'age': 18, 'gender': 'male'}, {'name': ': xiaohong', 'age': 20, 'gender': 'female'}]
print(max(a, key=lambda x: x['age']))
# 后面的default参数：当传入的列表为空时，若参数default被赋值，则返回default，否则会抛出空序列的异常

# round(number[,ndigits]):四舍五入，ndigits代表小数点后保留几位
print(round(10.222, 2))

# sum(iterable, /. start=0):求和，“ / ”代表位置参数不能是关键字参数
a = [1, 3, 5, 7]
print(sum(a))
print(sum(a, 10))  # 求和的初始值为10


# abs(x, /):求绝对值或者复数的模
print(abs(-6))

# divmod(a, b):分别取商和余数
print(divmod(10, 3))

# hash(object):返回对象的hash地址
# id(object): 返回对象的内存地址

# 逻辑运算
# all(iterable):接收一个迭代器，如果迭代器的所有元素为真，返回True，否则返回False
print(all([1, 2, 3, 4]))


# any(iterable):接收一个迭代器，如果迭代器有一个元素为真，返回True，否则返回False

# 进制转换
# ascii(object):调用对象的repr()方法，获得该方法的返回值
# __repr__()方法是类的实例化对象用来做“自我介绍”的方法，默认情况下，它会返回当前对象的“类名+object # at+内存地址”，而如果对该方法进行重写，可以为其制作自定义的自我描述信息。
class Student():
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return 'id = ' + self.id + ', name = ' + self.name


xiaoming = Student('001', 'xiaoming')
print(xiaoming)
ascii(xiaoming)

# bin(x): 将10进制转换为二进制
print("{}转换为二进制为{}".format(10, bin(10)))
print(f'10转换为二进制为{bin(10)}')

# oct(x): 将10进制转换为八进制
print("{}转换为八进制为{}".format(10, oct(10)))
print(f'10转换为八进制为{oct(10)}')

# hex(x): 将10进制转换为十六进制
print("{}转换为十六进制为{}".format(10, hex(10)))
print(f'10转换为十六进制为{hex(10)}')
