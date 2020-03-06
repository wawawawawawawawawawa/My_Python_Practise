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
