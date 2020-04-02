# "=="操作符比较对象之间的值是否相等
# "is"操作符比较的是对象的身份标识是否相等，即他们是否是同一个对象，是否指向同一个内存地址
# 在Python中，每个对象的身份标识，都能通过函数id(object)获得,'is'操作符相当无比较对象间的ID是否相等
a = 10
b = 10
print(a == b)
print(id(a))
print(id(b))
print(a is b)
# 不过需要注意的是，以上a  is b 的结论只适用于 -5 到256 范围，对于整型数字来说
c = 2577
d = 2577
print(c is d)  # 这里有点问题，试验是一直相等，需要进一步确认

# 比较操作符'is'的速度效率，通常要优于'=='.因为'is'操作符不能被重载，这样Python就不用去寻找程序中是否有其他地方重载了比较
# 操作符，而调用'is'就仅仅是比较两个变量的ID而已

# 但'=='操作符却不同，执行a == b相当于执行a.__eq__(b),而Python大部分的数据类型都会去重载这个函数，比如列表，__eq__函数会去遍历列表中的元素，比较他们的顺序和值是否相等

# 浅拷贝(shallow copy)
# 常见的浅拷贝的方法，是使用数据类型本身的构造器
l1 = [1, 2, 3]
l2 = list(l1)
print(l2)
print(l1 == l2)
print(l1 is l2)
s1 = set([1, 2, 3])
s2 = set(s1)
print(s2)
print(s1 == s2)
print(s1 is s2)
# 这里l2就是l1的浅拷贝，s2是s1的浅拷贝，对于可变序列，还可以通过切片分隔符完成浅拷贝
l1 = [1, 2, 3]
l2 = l1[:]
print(l1 is l2)  # False
# Python中也提供了相应的函数copy.copy()
import copy

l1 = [1, 2, 3]
l2 = copy.copy(l1)
print(l1 is l2)  # False
# 需要注意的是对于元组，使用tuple()或者切片操作符 : 不会创建一份浅拷贝，相反他会返回一个指向相同元组的引用
t1 = (1, 2, 3)
t2 = tuple(t1)
print(t1 == t2)  # True
print(t1 is t2)  # True

# 浅拷贝是指重新分配一块内存你，创建一个新的对象，里面的元素是原对象中子对象的引用，因此如果原对象中的元素可变，浅拷贝通常会带来一些副作用
import copy

l1 = [[1, 2], (30, 40)]
l2 = copy.copy(l1)
l1.append(100)  # 这里对l1列表新增元素100，不会影响到l2，因为整体是两个不同的对象，不共享内存地址
l1[0].append(3)  # 这里由于l2是l1的浅拷贝，l2中的第一个元素和l1中的第一个元素共同指向一个列表，所以会改变l1和l2
# l2[0].append(4)
print(l1)
print(l2)
l1[1] += (50, 60)  # 这里由于是创建新的元组，所以l2不会改变
print(l1)
print(l2)

# 深度拷贝(deep copy):所谓深度拷贝，是指重新分配一块内存，创建一个新的对象，并且将原对象的元素，以递归的方式，通过创建新的子对象拷贝到新对象中

# Python中使用copy.deepcopy()来实现对象的深度拷贝
l1 = [[1, 2], [3, 4]]
l2 = copy.deepcopy(l1)
l1[0].append(3)
print(l1)
print(l2)


# in用于成员检测
# python内置的序列类型，字典类型和集合类型，都支持in操作。对于字典类型in操作判断i是否是字典的键
# 对于自定义类型，判断是否位于序列类型中，需要重写序列类型的魔法方法 __contains__
# 以一个下划线开头的实例变量名，比如_age，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当看到这样的变量时，意思是，"虽然可以被访问，但是，请视为私有变量，不要随意访问。

class Student():
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val


class Students(list):
    def __contains__(self, stu):
        for s in self:
            if s.name == stu.name:
                return True
        return False


s1 = Student('xiaoming')
s2 = Student('xiaohao')
a = Students()
a.extend([s1, s2])
s3 = Student('xiaoming')
print(s3 in a)

# extend和append的区别
# list.append(arg1)参数类型任意，可以往已有列表中添加元素，若添加的是列表，就把该列表当成一个元素存在原列表中，只使list长度增加1
# list.extend(list1):参数必须是列表类型，可以将参数中的列表合并到原列表的末尾，使原来的 list长度增加len(list1)。
lst = [1, 2]
lst.append([3, 4])
print(lst)
lst.extend([3, 4])
print(lst)



