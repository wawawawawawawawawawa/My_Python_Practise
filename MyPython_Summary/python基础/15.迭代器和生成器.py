# 容器：Python中一切皆对象，对象的抽象就是类，而对象的集合就是容器
# 列表，元组，字典，集合都是容器，容器都是可迭代的(iterable)
# 迭代器(iterator)提供了一个next的方法，调用这个方法后，要么得到容下的下一个对象，要么得到一个StopIteration的错误，不需要
# 指定元素的索引，因为字典和集合这样的容器没有索引的说法

# 而可迭代对象通过iter()函数返回一个迭代器，再通过next()函数就可以实现遍历。for in 语句将这个过程隐化


def is_iterable(param):
    try:
        iter(param)
        return True
    except TypeError:
        return False
params = [
    1234,
    '1234',
    [1, 2, 3, 4],
    set([1, 2, 3, 4]),
    {1:1, 2:2, 3:3, 4:4},
    (1, 2, 3, 4)
]

for param in params:
    print('{} is iterable? {}'.format(param, is_iterable(param)))

# 生成器是懒人版本的迭代器
# 声明一个迭代器很简单，[i for i in range(100000000)]就可以生成一个包含一亿个元素的列表，每个元素生成呼都会保存到内存中，会占用巨量内存
# 而生成器只有调用next()函数时，才会生成下一个变量，生成器的写法是小括号：(i for i in range(100000000)),即初始化了一个生成器

# 给定一个列表和一个数字，求这个数字在列表中的位置


def index_normal(L, target):   # 普通版
    result = []
    for i, num in enumerate(L):
        if num == target:
            result.append(i)
    return result
print(index_normal([1, 6, 5, 2, 4, 2, 6], 6))


def index_generator(L, target):
    for i, num in enumerate(L):
        if num == target:
            yield i

print(list(index_generator([1, 6, 5, 2, 4, 2, 6], 6)))
# yield是魔法的关键，函数运行到这一行会暂停，跳到下一次next()函数，当next()还是调用的时候，暂停的程序继续向下执行，yield后面接的是它的返回值
# index_generator会返回一个Generator对象，需要使用list转换为列表后，才能使用print输出

# 给定一个序列，判断第一个是不是第二个的子序列


def is_subsequence(a, b):
    b = iter(b)
    return all(i in b for i in a)
print(is_subsequence([1, 3, 5], [1, 2, 3, 4, 5]))
print(is_subsequence([1, 4, 3], [1, 2, 3, 4, 5]))

# 这里的 b = iter(b) 将b变成一个迭代器，使得他可以调用next()方法
# 这里的(i in b)相当于：
"""
while True:
    val = next(b)
    if val == i:
        yield True
"""
# 非常巧妙的利用生成器的特性，next()函数运行时保存了当前的指针
b = (i for i in range(5))

print(2 in b)
print(4 in b)
print(3 in b)

# (i for i in a)产生一个生成器，这个生成器可以遍历对象a
# all() 判断一个迭代器元素是否全部为True


