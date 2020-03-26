import time


def find_product_price(products, product_id):
    for id, price in products:
        if id == product_id:
            return price
    return None

products = [
    (143121312, 100),
    (432314553, 30),
    (32421912367, 150)
]

print('The price of product 432314553 is {}'.format(find_product_price(products, 432314553)))
# 字典(dict):在Python3.7+，字典被确认时有序的，在之前是无序的，其大小长度可变，元素可以任意的删改和改变
# 相比与列表和元组，字典的性能更优，特别对于添加，查找，删除操作，字典都能在常数时间复杂度内完成
# 集合(set):集合和字典基本相同，唯一的区别就是集合没有键和值的配对，是一系列无序的，唯一的元素组合


# 创建方式:
d1 = {'name': 'test', 'age': 15}
d2 = dict({'name': 'test', 'age': 15})
d3 = dict([('name', 'test'), ('age', 15)])
d4 = dict(name='test', age=15)

s1 = {1, 2, 3}
s2 = set([1, 2, 3])


# 字典的索引访问：
# 1.字典可以直接索引键，如果不存在就会抛出异常
# 2.也可以使用get(key, default)函数来进行索引，如果键不存在，调用get()函数可以返回一个默认值
d = {'name': 'test', 'age': 15}
d.get('name')
d.get('falsetest', 'null')  # 这里会返回null


# 集合的访问：
# 集合并不支持索引操作，因为集合本质上是一个哈希表，和列表不一样
# 想要判断一个元素在不在字典或者集合里，可以使用value in dict/set 来判断
s = {1, 2, 3}
1 in s
d = {'name': 'test', 'age': 15}
'name' in d

# 字典和集合的增，删，更新等操作：
d = {'name': 'test', 'age': 15}
d['gender'] = 'male'  # 增加元素对'gender': 'male'
d['name'] = 'hello'  # 更新元素对的值
d.pop('name')        # 删除键为'name'的元素对

s = {1, 2, 3}
s.add(4)
s.remove(4)
# 需要注意的是集合的pop()操作是删除集合的最后一个元素，可是集合本身是无序的，所以不知道会删除哪个元素


# 字典和集合的排序
# 对于字典，通常会根据键或值，进行升序或降序排序
d = {'a': 2, 'b': 1, 'c': 10}
d_sort_by_key = sorted(d.items(), key=lambda x: x[0])  # 根据字典键的升序排列
d_sort_by_value = sorted(d.items(), key=lambda x: x[1])  # 根据字典值的 升序排列
# d_sorted_by_key
# [('a', 2), ('b', 1), ('c', 10)]
# d_sorted_by_value
# [('b', 1), ('a', 2), ('c', 10)]
# 这里返回了一个列表，列表中的每一个元素，是由原字典的键和值组成的元组

# 集合：和列表和元组类似，直接调用sorted(set)即可，结束会返回一个排好序的列表


# 字典和列表的使用效率比较
# 比如某电商平台后台存储了没见商品的ID，名称与价格，需求是找出一共有多少种价格，首先使用列表，可以看到在最差的情况下需要O(n^2)的时间复杂度
# list version
def find_unique_price_using_list(products):
    unique_price_list = []
    for _, price in products:
        if price not in unique_price_list:
            unique_price_list.append(price)
    return len(unique_price_list)

products = [
    (143121312, 100),
    (432314553, 30),
    (32421912367, 150),
    (937153201, 30)
]

print('number of unique price is:{}'.format(find_unique_price_using_list(products)))
# 但是我们选择集合数据结构的话，由于集合是高度优化的哈希表，里面元素不能重复，并且其添加和查找操作只需要O(1)的复杂度


def find_unique_price_using_set(products):
    unique_price_set = set()
    for _, price in products:
        unique_price_set.add(price)
    return len(unique_price_set)
print(find_unique_price_using_set(products))

products = [
    (143121312, 100),
    (432314553, 30),
    (32421912367, 150),
    (937153201, 30)
]

print('number of unique price is:{}'.format(find_unique_price_using_set(products)))

# 集合和列表性能对比，例子中初始化了还有100000个元素的产品，分别计算统计产品价格数量的运行时间,可以看出二者的差别很大
uid = [x for x in range(0, 100000)]
price = [x for x in range(200000, 300000)]
products = list(zip(uid, price))  # 这里使用内置函数zip()创建uid和price为一个迭代器对象

# 计算列表版本的时间
start_using_list = time.perf_counter()
find_unique_price_using_list(products)
end_using_list = time.perf_counter()
print("time elapse using list: {}".format(end_using_list - start_using_list))
# 输出
# time elapse using list: 41.61519479751587

# 计算集合版本的时间
start_using_set = time.perf_counter()
find_unique_price_using_set(products)
end_using_set = time.perf_counter()
print("time elapse using set: {}".format(end_using_set - start_using_set))
# 输出
# time elapse using set: 0.008238077163696289

# 字典和集合的工作原理：
# 字典：内部结构为一张哈希表，这张表存储了哈希值，键和值这3个元素
# 集合：内部结构为一张哈希表，这张表没有键值匹配，只有单一元素
# 插入操作：每次向字典或集合插入一个元素时，Python 会首先计算键的哈希值（hash(key)），再和 mask = PyDicMinSize - 1 做与操作，
# 计算这个元素应该插入哈希表的位置 index = hash(key) & mask。如果哈希表中此位置是空的，那么这个元素就会被插入其中
# 查找操作：和前面的插入操作类似，Python 会根据哈希值，找到其应该处于的位置
# 删除操作：对于删除操作，Python 会暂时对这个位置的元素，赋于一个特殊的值，等到重新调整哈希表的大小时，再将其删除

# 字符串去重
test_str = 'csabhhbsbjkakasyysnksnnalllqwiopxsan'
length = len(test_str)
key = [x for x in test_str]
value = [x for x in range(length)]
product = list(zip(key, value))
dic = dict(product)
for i in dic:
    print(i, end="")

# 遍历字典以及获取所有键,值集合
d = {'a':1,'b':2,'c':3}
for key, value in d.items():
    print(key, value)

# 获取所有键的集合
print(set(d))
print(set(d.keys()))

# 获取所有值的集合
print(set(d.values()))

# 字典视图
# 字典自带的三个方法 d.items()、d.keys()、d.values()，分别返回字典元素集，键的集合以及值的集合
# 他们都是原字典的视图，修改原字典对象，视图对象的值也会改变

# 字典值的范围
# 可哈希的对象才能作为字典的键，不可变对象才是可哈希的，所以可变对象不能作为字典的键

# 集合的范围
# 可哈希的对象才能作为集合的元素，不可变对象才是可哈希的，所以可变对象不能作为字典的键

# set自带的方法与数学中的集合操作比较类似，提供查找集合间并，交，差集，子集判断
# 求并集
a = {1, 3, 5, 7}
b, c = {3, 4, 5, 6}, {6, 7, 8, 9}
a.union(b, c)
# 求差集
d = a.difference(b, c)
# 求交集
e = a.intersection(b, c)
# a 是 b的子集吗？
print(a.issubset(b))

# 字典与集合的使用
# 1.update:实现批量插入键值对到已有字典中
d = {'a': 1, 'b': 2}
d.update({'c': 3, 'e': 4})

# 2.setdefault:仅当字典中不存在某个键值对时才插入到字典中，如果存在，不必插入(也就不会修改键值对)
r = d.setdefault('c', 33) # 因为已经存在了c的键值对，所以这里值不会更新


# 3.字典并集：{**d1, **d2}实现合并d1和d2，返回一个字典
def merge(d1, d2):
    return {**d1, **d2}


print(merge({'a': 1, 'b': 2}, {'c': 3}))


# 4.字典差
def difference(d1, d2):
    return dict([(k, v) for k, v in d1.items() if k not in d2])


# 5.按键排序
def sort_by_key(d):
    return sorted(d.items(), key=lambda x: x[0])


# 6.按值排序
def sort_by_value(d):
    return sorted(d.items(), key=lambda x: x[1])


# 7.最大键
def max_key(d):
    if len(d) == 0:
        return []
    max_key1 = max(d.keys())
    return (max_key1, d[max_key1])


# 8.最大值,注意这里的最大值可能不止一个
def max_value(d):
    if len(d) == 0:
        return []
    max_val = max(d.values())
    return [(key, max_val) for key in d if d[key] == max_val]


# 9.集合最值，找到最大最小值，装到元组返回
def max_min(s):
    return (max(s), min(s))


# 10.更长集合:按照元素长度比较大小，找出更长的集合
def longer(s1, s2):
    return max(s1, s2, key=lambda x: len(x))


# 11.重叠最多：在两个列表中，找出重叠次数最多的元素，默认只返回一个
def max_overlap(lst1, lst2):
    overlap = set(lst1).intersection(lst2)
    ox = [(x, min(lst1.count(x), lst2.count(x)) for x in overlap)]
    return max(ox, key=lambda x: x[1])


# 12.topn:找出字典前n个最大值,对应的键
from heapq import nlargest


def top_dict(d, n):
    return nlargest(n, d, key=lambda k: d[k])


# 13.一键多值字典
d = {}
lst = [(1, 'apple'), (2, 'orange'), (1, 'compute')]
for k, v in lst:
    if k not in d:
        d[k] = []
    d[k].append(v)


# 这里有一处if判断，不是很优雅，可以使用collections中的defaultdict
from collections import defaultdict
d = defaultdict(list)
for k, v in lst:
    d[k].append(v)