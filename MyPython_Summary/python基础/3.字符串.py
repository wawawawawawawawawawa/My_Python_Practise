# Python中使用单引号，双引号，三引号的字符串是一模一样的，Python同时支持这三种表达方式，很重的要的是方便在字符串中内嵌带引号的
# 字符串，三引号字符串则主要应用与多行字符串的情形，比如函数的注释等
# 字符串的常用操作:
# 可以把字符串想象成一个有单字符组成的数组，所以Python的字符串同样支持索引，切片和遍历等操作
name = 'jason'
name[0]  # 'j'
name[1:3]  # 'as'
# 特别要注意的是Python的字符串是不可变的(immutable).因此，使用索引方式改变字符串的行为是错误的
# Python中字符串的改变，通常只能通过创建新的字符串来完成，比如上述例子中，想把'hello'的第一个字符'h'，改为大写的'H'，我们可以采用下面的做法：
s = 'hello'
s = 'H' + s[1:]
s = s.replace('h', 'H')
# 上面使用了两种方式：
# 方式一：直接用大写的'H',通过加号操作符，与原字符串切片操作的子字符串拼接而成的新字符串
# 方式二：直接扫描原字符串把小写的'h'替换为‘H’，得到新的字符串
s = ''
for n in range(1000):
    s += str(n)
# 这里并不是在每次拼接字符串都创建新的字符串了，因为从Python2.5开始，每次处理字符串的拼接操作时(str1 += str2)，Python会首先检测
# str1还有没有其他的引用，如果没有的话，就会尝试原地扩充字符串buffer的大小，而不是重新分配一块内存来创建新的字符串并拷贝，上述例子时间复杂度仅为O(n)
# 所以在遇到字符串拼接时使用"+="更方便且不用担心效率问题，对于字符串的拼接还可以使用字符串内置的join函数。string.join(iterable),表示把每个元素都按照指定的格式连接起来
l = []
for n in range(1000):
    l.append(str(n))
l = '#'.join(l)
print(l)
# 字符串的分隔函数split()。string.split(separator),表示把字符串按照separator分割成子字符串，并返回一个分隔后子字符串组合的列表
# 他常常用于对数据的解析处理，比如我们读取了某个文件的路径后，想要调用数据库的API，去读取对应的数据，通常会写成如下：


def query_data(namespace, table):
    """
    given namespace and table, query database to get corresponding
    data
    """
    return data

path = "hive://ads/training_table"
namespace = path.split('//')[1].split('/')[0]  # 返回’ads‘
table = path.split('//')[1].split('/')[1]  # 返回'training_table'
data = query_data(namespace, table)

# 字符串中其他常见函数
# string.strip(str)，表示去掉首尾的str字符串
# string.lstrip(str)，表示只去掉开头的str字符串
# string.rstrip(str)，表示只去掉尾部的str字符串

# 字符串的格式化
# 通常，我们使用一个字符串作为模板，模板中会有格式符，这些格式符作为后续真实值预留位置，以呈现出真实值应该呈现的格式，通常用于程序的输出。logging等
print('no data available for person with id:{},name:{}'.format(id, name))
# 其中的string.format(),就是所谓的格式化函数；而大括号{}就是所谓的格式符，用来为后面的真实值，变量name预留位置


# replace用于字符串的替换
print("I love python".replace(' ', '_'))

# title用于字符串首字符的大写
print("i love python".title())

# find用于返回匹配字符串起始位置的索引
print("i love python".find('python'))
