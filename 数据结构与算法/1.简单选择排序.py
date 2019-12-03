import time
import random


def set_func(func):
    def call_func(c):
        start_time = time.time()
        func(c)
        end_time = time.time()
        print("执行时间%f" % ((end_time - start_time) * 1000000))
        return func(c)

    return call_func


@set_func
def select_sort(origin_items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j

        items[i], items[min_index] = items[min_index], items[i]

    return items


@set_func
def select_sort1(origin_items):
    """简单选择排序"""
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if items[j] < items[min_index]:
                min_index = j

        items[i], items[min_index] = items[min_index], items[i]

    return items


list1 = list()
for i in range(1000):
    list1.append(random.randint(0, 1000))
select_sort(list1)
select_sort1(list1)

# 试验结果显示这里完全没有必要使用lambda表达式，会增加运行的时间
