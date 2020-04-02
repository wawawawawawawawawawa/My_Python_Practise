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
# print(f'10转换为二进制为{bin(10)}')

# oct(x): 将10进制转换为八进制
print("{}转换为八进制为{}".format(10, oct(10)))
# print(f'10转换为八进制为{oct(10)}')

# hex(x): 将10进制转换为十六进制
print("{}转换为十六进制为{}".format(10, hex(10)))
# print(f'10转换为十六进制为{hex(10)}')


# 函数作用域，查找顺序遵守LEGB规则
# 优先从它所属函数(local)内查找
# 若找不到，且他位于一个内嵌函数中，就再到它的父函数(enclosing)中查找
# 如果还找不到，再去全局作用域(global)查找
# 如果还找不到，再去内置作用域(build-in)查找
# 还是找不到，报错


# bytes([source[,encoding[,errors]]]):将一个字符串转换成字节类型
s = "apple"
print(bytes(s, encoding='utf-8'))

# str(object=''):将字符类型，数值类型等转换为字符串类型
i = 100
print(str(i))


# chr(i):查看十进制数对应的ASCLL字符
# ord(c):查看某个ASCLL字符对应的十进制数
print(chr(65), ord('A'))


# dict():创建数据字典
# dict(**kwarg)
# dict(mapping, **kwarg)
# dict(iterable, **kwarg)
print(dict())
print(dict(a = 'a', b = 'b'))
print(dict(zip(['a', 'b'], [1, 2])))
print(dict([('a', 1), ('b', 2)]))


# frozenset([iterable]):创建一个不可修改的冻结集合，一旦创建不允许增删元素
print(frozenset([1, 2, 2, 5, 6, 5]))
print(isinstance(frozenset([1, 2, 2, 5, 6, 5]),frozenset))#它不是一个set对象，是一个frozenset对象


# 普通的set创建后可以使用add方法再插入元素，也可以使用pop方法移除集合的第一个

# list([iterable]):返回可变序列类型：列表
m = map(lambda i: str(i),[188, 22, 88])   # 这里将列表内的每个元素都转换为字符串类型
list(m)


# range(stop);range(start, stop [,step]):生成不可变序列
a = [1,4,2,3,1]
for i in range(0,len(a),2):
	print(a[i])
# slice(stop);slice(start,stop, [,step]):返回一个由range(start, stop, step) 所指定索引集的 slice 对象
# print(a[slice[0, 5, 2]])
# print(a[slice[2]])


# tuple([iterable]):创建一个不可修改的元租对象
# type(object):查看对象的类型的函数


# zip(*iterable):创建一个迭代器，聚合每个可迭代对象的元素
a = range(5)
b = list('abcde')
print([(x,y) for x, y in zip(a, b)])

# classmethod:classmethod修饰符对应的函数不需要实例化，不需要self参数
# 第一个参数需要是表示自身类的cls参数，能调用类的属性，方法，实例等


# delattr(object, name):删除对象的属性，在不需要某个或某些属性时，就用这个方法
class Student():
	def __init__(self, id = None, name = None):
		self.id = id
		self.name = name

xiaoming = Student(1, '小明')
delattr(xiaoming, 'id')
print(hasattr(xiaoming,'id'))

# getattr(object,name[,default]):获取对象的属性
# isinstance(object, classinfo):判断object是不是类classinfo的实例
print(isinstance(xiaoming, Student))


# issubclass(class, classinfo):判断class是不是classinfo的子类
# classinfo取值可能为元组，若class是元组内某个元素类型的子类，也会返回True
print(issubclass(int, (int, float)))


# callable:判断对象是不是可被调用，能被调用的对象就是一个callable对象，比如函数str，int等都是可被调用的
# 如果一个类生成的实例想要可以被调用，必须从写__call__方法：
class Student():
	def __init__(self, id = None, name = None):
		self.id = id
		self.name = name

	def __call__(self):
		print("i can be called")


t = Student(2, "哈哈")
print(callable(t))


# 五个常用的高阶函数
# 1.filter(function,iterable):过滤掉不满足函数function的元素，重新返回一个迭代器
class Student():
	def __init__(self, name, sex, height):
		self.name = name
		self.sex = sex
		self.height = height


def height_condition(stu):
	if stu.sex == 'male':
		return stu.height > 1.75
	else:
		return stu.height > 1.65


students = [Student('xiaoming', 'male', 1.74),
			Student('xiaohong', 'female', 1.68),
			Student('xiaoli', 'male', 1.80)]

students_satisfy = filter(height_condition, students)
for stu in students_satisfy:
	print(stu.name)

# 2.map(function,iterable,...):将function映射于iterable中的每一项，并返回一个新的迭代器
mylst = [1, 2, 3, 4, 5]
result = map(lambda x: x + 1, mylst)
for i in result:
	print(i)

# map函数支持传入多个可迭代对象，输出元素个数等于较短序列长度
# 找到同时满足第一个列表的元素为奇数，第二个列表对应位置的元素为偶数的元素
xy = map(lambda x, y: x % 2 == 1 and y % 2 == 0, [1, 3, 2, 4, 1], [3, 2, 1, 2])
for i in xy:
	print(i)


# 利用map实现加法运算
def vector_add(x, y):
	return list(map(lambda i, j: i + j, x, y))


lst1 = [1, 2, 3, 4, 5, 6]
lst3 = [1, 2]
print(vector_add(lst1, lst3))

# 3.reduce(function，iterable[,initializer])
# 实现规约
# reduce函数中第一个参数是function，function函数，参数必须为2，是可迭代对象iterable中连续两项
# 计算过程从左到右依次规约，直到最终为单个值并返回
from functools import reduce

print(reduce(lambda x, y: x + y, list(range(10))))

# 4.reversed(seq):重新生成一个反向迭代器，对输入的序列实现反转


# 5.sorted(iterable,*,key=None,reverse=False):实现对序列化对象的排序
# key参数和reverse参数必须为关键字参数，都可省略
# 如果可迭代对象的元素也是一个复合对象(如字典)，那么sorted的key函数就会被用到
a = [{'name': 'xiaoming', 'age': 20, 'gender': 'male'},
	 {'name': 'xiaohong', 'age': 18, 'gender': 'female'},
	 {'name': 'xiaoli', 'age': 19, 'gender': 'male'}]

print(sorted(a, key=lambda x: x['age'], reverse=False))

# 迭代器
# iter(object):返回一个严格意义上的可迭代对象
# 只要 iterable 对象支持可迭代协议，即自定义了__iter__函数，便都能配合for依次迭代输入其元素
# next(iterator,[,default]):返回可迭代对象的下一个元素
it = iter([1, 2, 3, 4])
print(next(it))
# enumerate(iterable,start=0):返回可枚举对象，也是一个迭代器
s = ["a", "b", "v"]
for i, v in enumerate(s):
	print(i, v)















