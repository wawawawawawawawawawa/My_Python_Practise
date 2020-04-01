# 1.数据再运算
a = range(10)
b = [x ** 2 for x in a]
print(b)

# 2.一串随机数：生成10个0到1的随机浮点数，保留小数点后两位
from random import random

a = [round(random(), 2) for _ in range(10)]
print(help(random))

# 3. if嵌套for
a = range(11)
b = [x ** 2 for x in a if x % 2 == 0]
print(b)
# 列表生成式中嵌套for,一行代码生成99乘法表中所有的45个元素
a = [str(i) + '*' + str(j) + "=" + str(i * j) for i in range(10) for j in range(1, i + 1)]
print(a)

# 4.zip和列表
a = range(5)
b = ['a', 'b', 'c', 'd', 'e']
c = [str(x) + str(y) for x, y in zip(a, b)]
print(c)

# 5.打印键值对
a = {'a': 1, 'b': 2, 'c': 3}
b = [k + '=' + str(v) for k, v in a.items()]
print(b)
import calendar

print(help(calendar.monthrange))

# 6.文件列表
import os

a = [d for d in os.listdir(r'C:\Users\LiuWenJing\Desktop')]
print(a)
# 再结合if,只查找出文件夹
dirs = [d for d in os.listdir(r'C:\Users\LiuWenJing\Desktop') if os.path.isdir(d)]
print(dirs)
# 只查找出文件
files = [d for d in os.listdir(r'C:\Users\LiuWenJing\Desktop') if os.path.isfile(d)]
print(files)

# 7.转为小写
a = ['Hello', 'World', '2019Python']
b = [w.lower() for w in a]
print(b)
# 以上转换可能会有问题，因为列表中可能有任何类型元素，比如int类型就没有lower()方法，所以应该做类型检查
b = [w.lower() for w in a if isinstance(w, str)]
print(b)


# 8.筛选分组
def bifurcate(lst, filter):
    return [
        [x for i, x in enumerate(lst) if filter[i] == True],
        [x for i, x in enumerate(lst) if filter[i] == False]
    ]


print(bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True]))


# 9.函数分组
def bifurcate_by(lst, fn):
    return [
        [x for x in lst if fn(x)],
        [x for x in lst if not fn(x)]
    ]


bifurcate_by(['Python3', 'up', 'users', 'people'], lambda x: x[0] == 'u')