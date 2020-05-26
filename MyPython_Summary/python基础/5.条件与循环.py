# python中不支持switch语句，因此有多个条件判断时，我们要使用elif
# if语句可以单独存在，但elif,else都必须和if成对使用

# 省略判断条件的常见写法：
# String：空字符串为False，其余为True
# Int：0解析为False，其余为True
# list/tuple/dict/set：Iterable为空解析为False，其余为True
# Object：None解析为False，其余为True

# 循环语句
# Python中的数据结构只要是可迭代的(iterable),比如列表，集合等，那么都可以使用for循环遍历
# for item in <iterable>:
#     ...

# 字典本身只有键是可迭代的，如果我们要遍历他的值或者键值对，可使用其内置函数values()或者items()实现，其中values()返回字典的值的集合，items
# ()返回键值对的集合
d = {'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'}
for k in d:
    print(k)

for v in d.values():
    print(v)

for k, v in d.items():
    print('key: {},value: {}'.format(k, v))

# 使用索引来遍历时，一般使用range()函数
l = [1, 2, 3, 4, 5, 6]
for index in range(0, len(l)):
    print(l[index])

# 当同时需要索引和元素时，更简洁的方式是通过Python的内置函数enumerate().用它来遍历集合可以返回元素及其对应的索引
for index, items in enumerate(l):
    print('索引{}: {} '.format(index, items))

# 循环语句中continue 和break的使用
# 比如给定两个字典，分别是产品名称到价格的映射，和产品名称到颜色列表的映射，找出价格小于1000且颜色不是红色的所有产品名称和颜色的组合
# name_price:产品名称到价格的映射字典
# name_color:产品名称到颜色的映射字典
# for name, price in name_price.items():
#     if price < 1000:
#         if name in name_color:
#             for color in name_color[name]:
#                 if color != 'red':
#                     print('name:{},color:{}'.format(name, color))
#     else:
#         print('name:{},color:{}'.format(name,'None'))


# 使用break与continue的版本
# for name, price in name_price.items():
#     if price >= 1000:
#         continue
#     if name not in name_color:
#         print('name:{},color:{}'.format(name,'None'))
#         continue
#     for color in name_color[name]:
#         if color == 'red':
#             continue
#         print('name:{},color:{}'.format(name, color))

# while循环：当condition满足时，一直重复循环内部的操作，直到condition不再满足，跳出循环
# while condition:
#     ...

# while和for循环是可以相互转换的
l = [1, 2, 3, 4, 5]
index = 0
while index < len(l):
    print(l[index])
    index += 1

# while和for循环的使用场景
# for：遍历一个已知的集合，找出满足条件的元素，并进行相应的操作
# while:在满足某个条件前，不停的进行某些操作，并且没有特定的集合去遍历

# for 和 while循环的效率问题
i = 0
while i < 100000:
    i += 1

for i in range(0, 100000):
    pass

# 上面同样循环了100000次，但是由于range()函数直接C语言写的，调用速度快，而while循环 "i += 1"这个操作是解释器间接调用底层C，且涉及到对象的创建与删除，所以for循环效率好


# 条件与循环的复用
# 将条件与循环做一行的操作： expression1 if condition else expression2 for items in iterable
# 加入没有else则为：expression for items in iterable if condition

# # 比如要将文件中逐行读取的一个完整语句，按逗号分割单词，去掉首位的空字符，并过滤掉长度小于等于3的单词，最后返回单词组成的列表
test = " Today, is, Sunday"
test_list = [s.strip() for s in test.split(',') if len(s.strip()) > 3]
print(test_list)

# # 这样的复用不仅仅局限于一个循环，比如给定两个列表x，y要求返回x，y中所有元素对组成的元组，相等的情况除外
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
print([(xx, yy) for xx in x for yy in y if xx != yy])

# # 将下面的两个列表对应
attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'],
['mike', '1999-01-01', 'male'],
['nancy', '2001-02-01', 'female']
]
#
# # 方式一
for index in range(0, len(values)):
    print(dict(zip(attributes, values[index])))

# 方式二
print([dict(zip(attributes, values[index])) for index in range(0, len(values))])

# 方式三
dic = {}
li = []
for v in values:
    for index in range(0, len(v)):
        tup = (attributes[index], v[index])
        li.append(tup)
print(li)

