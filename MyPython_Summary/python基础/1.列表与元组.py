# 列表和元组都是一个可以放置任意数据类型的有序集合
# 区别：
# 列表是动态的，长度大小不固定，可以随意的增加，删减或者改变元素(mutable)
# 元组是静态的，长度大小固定，无法随意的删减或者改变(immutable)
l = [1, 2, 3, 4]
l[3] = 40  # l[3]表示访问第四个元素，这里可以修改第四个元素为四十

tup = (1, 2, 3, 4)
tup[3] = 40  # 这里会报错，因为元组没法修改元素的值

# 需要注意的是，单元素元组末尾必须加一个逗号，不然会被认为是元素本身
tup_singer = (1, )

# 如果想对已有的元组做任何改变只能重新开辟一块内存，创建新的元组，而列表只需要简单得在末尾加入对应元素
tup = (1, 2, 3, 4)
new_tup = tup + (5,)
l = [1, 2, 3, 4] # 将元素5添加到列表末尾
l.append(5)

# python中的列表和元组都支持负数索引，-1表示最后一个元素，-2表示倒数第二个元素
# 除了基本的初始化和索引外，列表和元组都支持切片操作
# 列表与元组可以通过list()和tuple()函数相互转换
list((1, 2, 3))
tuple([1, 2, 3])

# 列表和元组中常用的内置函数
# 1.count(item):表示统计列表/元组中item出现的次数
# 2.index(item):表示返回列表/元组中item第一次出现的索引
# 3.list.reverse()和list.sort()分别表示原地倒转列表和排序(注意，元组没有内置这两个函数)
# 4.reversed()和sorted()同样表示对列表/元组进行倒转和排序，但是会返回一个倒转后或者排好序的新的列表/元组


# 列表和元组储存方式的差异：
# 列表和元组最重要的区别是列表是动态的，可变的，由于列表是动态的，所以他需要存储指针，来指向对应的元素，另外由于列表可变，所以需要额外存储
# 已经分配的长度的大小(8字节)，python每次分配空间时都会额外分配一些，这样的机制(over-allocating)保证了其操作的高效性：增加/删除的时间复杂度度
# 均为 O(1) ,但是对于元组就不同了，元组长度大小固定，元素不可变，所以存储空间固定


# 列表和元组的性能：
# 元组比列表更加轻量级，性能速度也略优于列表
# Python会在后台，对静态数据做一些资源缓存(resource caching).Python的垃圾回收对于一些静态变量例如元组会暂时缓存这部分内存，
# 下次我们创建同样大小的元组时就不用再向操作系统请求内存了，大大加快程序运行速度
# 但如果是二者的索引操作的话二者的差别非常小


# list和tuple的内部实现都是array的形式，list因为可变，所以是一个over-allocate的array，tuple因为不可变，所以长度大小固定


# 去最求平均,这里的round是四舍五入，round(number, digits) digits是保留小数位数
def socre_mean(lst):
    lst.sort()
    lst2 = lst[1:-1]
    return round(sum(lst2)/len(lst2), 1)

# 使用sample，从100个样本中随机抽样10个
# simple(序列a, n):从序列a中随机的抽取n个元素，并将这n个元素以list形式返回
from random import randint,sample
lst = [randint[0, 50] for _ in range(100)]
lst_sample = sample(lst, 10)

# 列表的方法：
# insert[number, item]:在number索引出插入
# pop：末尾弹出
# remove(item):移除item

# 切片
a = list(range(1, 20, 3))   # 利用range(start, stop, step)生成数列数据并转换为列表
# 使用 a[1:5:2] 生成索引 [1,5) 但步长为 2 的切片 [4,10]
# 使用 a[::3] 生成索引 [0,len(a)) 步长为 3 的切片 [1,10,19]
# 使用 a[::-3] 生成逆向索引 [len(a),0) 步长为 3 的切片 [19,10,1]  逆向：从列表的最后一个元素访问列表的第一个元素的方向


# list和tuple的经典使用
# 1.判断list内有无重复元素
def is_duplicated(lst1):
    return len(lst1) != len(set(lst))


# 2.列表反转
def reverse(lst2):
    return lst2[::-1]


# 3.找出列表中所有重复元素
def find_duplicated(lst3):
    ret = []
    for i in lst3:
        if lst3.count(i) > 1 and i not in ret:
            ret.append(i)
        return ret


# 4.斐波那契数列
# 普通实现版
def fibonacci(n):
    if n <= 1:
        return [1]
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[len(fib)-1] + fib[len(fib)-2])
    return fib


# 生成器版
def finonacci1(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# 5.出镜最多
# max函数时内置函数，不需要导入，max有一个key参数，指定如何进行值的比较
def mode(lst5):
    if lst5 is None or len(lst5) == 0:
        return None
    return max(lst5, key=lambda v: lst5.count(v))


lst = [1, 5, 4, 9, 7, 8]
r = mode(lst)
print(f'{lst}中出现最多的元素为{r}')


# 支持返回多个
def mode__multi(lst5):
    if lst5 is None or len(lst5) == 0:
        return None
    max_freq_elem = max(lst5, key=lambda v: lst5.count(v))
    max_freq = len(max_freq_elem)
    ret = []
    for i in lst5:
        if i not in ret and lst5.count(i) == max_freq:
            ret.append(i)
    return ret


# 6.更长列表，其中 * 是可变参数，意味着能传入多个位置参数,key定义函数怎么比较大小，lambda的参数V是lists中的一个元素
def max_len(*lst6):
    return max(*lst6, key=lambda v: len(v))


r = max_len([1, 2, 3], [4, 5, 6, 7], [8])
print(f'更长的列表是{r}')


# 7.求表头，返回列表的第一个元素，如果为空时返回None,注意if else的这种简单写法
def head(lst7):
    return lst7[0] if len(lst7) > 0 else None


# 8.求表尾
def tail(lst8):
    return lst8[-1] if len(lst8) > 0 else None


# 9.打印乘法表
def mul_table():
    for i in range(10):
        for j in range(i + 1):
            print(str(j) + "*" + str(i) + "=" + str(i*j), end="\t")
        print()  # 打印一个换行


mul_table()


# 10.重洗数据集
# random中的shuffle函数，能冲洗数据，他是对输入列表就地洗牌，节省存储空间，所谓冲洗就是将序列中的所有元组随机排序
from random import shuffle
lst10 = [randint(0, 50) for _ in range(100)]
shuffle(lst10)


# 11.生成满足均匀分布的坐标点
from pyecharts.charts import Scatter
import pyecharts.options as opts
from random import uniform


def draw_uniform_points():
    x, y = [i for i in range(100)], [
        round(uniform(0, 10), 2) for _ in range(100)]
    print(y)
    c = (
        Scatter()
        .add_xaxis(x)
        .add_yaxis('y', y)
    )
    c.render()


draw_uniform_points()

# 导入相关图表包
# 进行图表的基础设置，创建图表对象
# 利用add()方法进行数据输入与图表设置(可以使用print_echarts_options()来输出所有可配置项)
# 利用render()方法来进行图表保存
# 有很多种图，中文版手册在pyecharts

