# # threading的方法current_thead()返回当前线程
# import threading
#
# t = threading.current_thread()
# print(t)
# # getName()获得这个线程的名字，ident获得线程id，isAlive()判断线程
# print(t.getName())
# print(t.ident)
# print(t.isAlive())
#
#
# # 创建线程，需要告诉这个线程，它能做什么，做什么通过参数target传入，参数类型为callable
# # args指定函数print_i的参数，类型为元组
# def print_i(i):
#     print(f"i的值为{i}")
#
#
# my_thread = threading.Thread(target=print_i, args=(1,))
# my_thread.start()
#
# # 根据操作系统的调度算法，多线程之间轮训获得CPU时间片
# # 多线程会争夺全局变量导致全局变量的修改出现问题
# import time
#
# a = 0
#
#
# def add1():
#     global a
#     tmp = a + 1
#     time.sleep(0.2)  # 延迟0.2秒模拟写入所需时间
#     a = tmp
#     print(f"{threading.current_thread().getName()} adds a to 1:{a}")
#
#
# threads = [threading.Thread(name=f"t{(i,)}", target=add1) for i in range(10)]
# [t.start() for t in threads]
# # 这里的执行结果是不能累加到9而是依然是1，因为一个线程休眠后cpu会调用下一个，直到所有的线程被分配到计算资源，计算完a+1,0.2秒的休眠时间还没用完，所以最后结果取到的a都是0
#
#
# # 加锁
# locka = threading.Lock()
# a = 0
#
#
# def add1():
#     global a
#     try:
#         locka.acquire()  # 获得锁
#         tmp = a + 1
#         time.sleep(0.2)
#         a = tmp
#
#     finally:
#         locka.release()  # 释放锁
#
# # 加锁也有他的问题，当有多个锁时，很容易发生死锁
#
#
# # 协程是在同一线程中函数间的切换，而不是线程间的切换
#
#
# # threading的方法current_thead()返回当前线程
# import threading
#
# t = threading.current_thread()
# print(t)
# # getName()获得这个线程的名字，ident获得线程id，isAlive()判断线程
# print(t.getName())
# print(t.ident)
# print(t.isAlive())
#
#
# # 创建线程，需要告诉这个线程，它能做什么，做什么通过参数target传入，参数类型为callable
# # args指定函数print_i的参数，类型为元组
# def print_i(i):
#     print(f"i的值为{i}")
#
#
# my_thread = threading.Thread(target=print_i, args=(1,))
# my_thread.start()
#
# # 根据操作系统的调度算法，多线程之间轮训获得CPU时间片
# # 多线程会争夺全局变量导致全局变量的修改出现问题
# import time
#
# a = 0
#
#
# def add1():
#     global a
#     tmp = a + 1
#     time.sleep(0.2)  # 延迟0.2秒模拟写入所需时间
#     a = tmp
#     print(f"{threading.current_thread().getName()} adds a to 1:{a}")
#
#
# threads = [threading.Thread(name=f"t{(i,)}", target=add1) for i in range(10)]
# [t.start() for t in threads]
# # 这里的执行结果是不能累加到9而是依然是1，因为一个线程休眠后cpu会调用下一个，直到所有的线程被分配到计算资源，计算完a+1,0.2秒的休眠时间还没用完，所以最后结果取到的a都是0
#
#
# # 加锁
# locka = threading.Lock()
# a = 0
#
#
# def add1():
#     global a
#     try:
#         locka.acquire()  # 获得锁
#         tmp = a + 1
#         time.sleep(0.2)
#         a = tmp
#
#     finally:
#         locka.release()  # 释放锁
#
# # 加锁也有他的问题，当有多个锁时，很容易发生死锁
#
#
# # 协程是在同一线程中函数间的切换，而不是线程间的切换
#
#
# # threading的方法current_thead()返回当前线程
# import threading
#
# t = threading.current_thread()
# print(t)
# # getName()获得这个线程的名字，ident获得线程id，isAlive()判断线程
# print(t.getName())
# print(t.ident)
# print(t.isAlive())
#
#
# # 创建线程，需要告诉这个线程，它能做什么，做什么通过参数target传入，参数类型为callable
# # args指定函数print_i的参数，类型为元组
# def print_i(i):
#     print(f"i的值为{i}")
#
#
# my_thread = threading.Thread(target=print_i, args=(1,))
# my_thread.start()
#
# # 根据操作系统的调度算法，多线程之间轮训获得CPU时间片
# # 多线程会争夺全局变量导致全局变量的修改出现问题
# import time
#
# a = 0
#
#
# def add1():
#     global a
#     tmp = a + 1
#     time.sleep(0.2)  # 延迟0.2秒模拟写入所需时间
#     a = tmp
#     print(f"{threading.current_thread().getName()} adds a to 1:{a}")
#
#
# threads = [threading.Thread(name=f"t{(i,)}", target=add1) for i in range(10)]
# [t.start() for t in threads]
# # 这里的执行结果是不能累加到9而是依然是1，因为一个线程休眠后cpu会调用下一个，直到所有的线程被分配到计算资源，计算完a+1,0.2秒的休眠时间还没用完，所以最后结果取到的a都是0
#
#
# # 加锁
# locka = threading.Lock()
# a = 0
#
#
# def add1():
#     global a
#     try:
#         locka.acquire()  # 获得锁
#         tmp = a + 1
#         time.sleep(0.2)
#         a = tmp
#
#     finally:
#          locka.release()  # 释放锁
#
# # 加锁也有他的问题，当有多个锁时，很容易发生死锁
#
#
# # 协程是在同一线程中函数间的切换，而不是线程间的切换
#
# # 列表和迭代器的区别：
# # 列表不论遍历多少次，表头位置始终是第一个元素
# # 迭代器遍历结束后，不再指向原来的表头位置，而是为最后元素的下一个位置
# # 要想迭代器重新指向表头，需要重新创建一个新的迭代器
# # 我们无法通过调用len获得迭代器的长度，只能迭代到最后一个末尾元素时才能知道他的长度
#
# # 求一组数据累积乘，比如：三个数 [1,2,3]，累积乘后返回 [1,2,6]
# # 一般的方法：
# def accumulate_div(a):
#     if a is None or len(a) == 0:
#         return []
#
#     rtn = [a[0]]
#     for i in a[1:]:
#         rtn.append(i * rtn[-1])
#     return rtn
#
#
# rtn = accumulate_div([1, 2, 3, 4, 5, 6])
# print(rtn)
#
#
# # 生成器
# def accumulate_yield(a):
#     if a is None or len(a) == 0:
#         return []
#
#     it = iter(a)
#     total = next(it)
#     yield total
#     for i in it:
#         total = total * i
#         yield total
#
#
# rtn = list(accumulate_div([1, 2, 3, 4, 5, 6]))
# print(rtn)
#
# # 拼接迭代器
# # chain函数实现元素拼接：chain(*iterables)
# from itertools import *
#
# chain_iterator = chain(['I', 'love'], ['python'], ['very', 'much'])
# for i in chain_iterator:
#     print(i)
# # 它和join串联字符串很像，join只是一次串联一个序列对象，而chain能串联多个可迭代对象生成一个更大的可迭代对象
#
#
# # 累积迭代器：返回可迭代对象的累积迭代器：accumulate(iterable[,func,*,initial=None])
# # 如果不提供func，默认进行累积和
# accu_iterator = accumulate([1, 2, 3, 4, 5, 6])
# for i in accu_iterator:
#     print(i)
#
# # func 接收两个参数，根据func的累积行为返回结果
# accu_iterator = accumulate([1, 2, 3, 4, 5, 6], lambda x, y: x * y)
# for i in accu_iterator:
#     print(i)
#
# # 漏斗迭代器：compress(data,selectors),类似于漏斗功能，经过selectors过滤后，返回一个更小的迭代器
# compress_iter = compress('abcdefg', [1, 1, 0, 1])
# for i in compress_iter:
#     print(i)
# # a b c
# # compress 返回元素个数，等于两个参数中较短序列的长度
#
#
# # drop迭代器：扫描可迭代对象iterable,从不满足条件处往后全部保留，返回一个更小的迭代器
# # dropwhile(predicate, iterable)
# drop_iterable = dropwhile(lambda x: x < 3, [1, 0, 2, 4, 1, 1, 3, 5, -5])
# for i in drop_iterable:
#     print(i)
#
#
# def dropwhile(predicate, iterable):
#     iterable = iter(iterable)
#     for i in iterable:
#         if not predicate:
#             yield i
#             break
#     for i in iterable:
#         yield i
#
#     # 先将iterable包装为迭代器
#
#
# # 如果不满足条件 predicate，yield i，然后跳出迭代，迭代完 iterable 剩余所有元素
# # 如果满足条件 predicate，就继续迭代，如果所有都满足，则返回空的迭代器。
#
#
# # take迭代器：扫描列表，只要满足条件就从可迭代对象中返回元素，直到不满足条件为止
# # takewhile(predicate,iterable)
# take_iterator = takewhile(lambda x: x < 5, [1, 4, 6, 4, 1])
# for i in take_iterator:
#     print(i)
#
#
# def takewhile(predicate, iterable):
#     for x in iterable:
#         if predicate:
#             yield x
#         else:
#             break
#
#
# # 克隆迭代器：tee实现对原迭代器的复制，以元组的形式返回，并且复制出的迭代器相互独立
# # tee(iterable,n=2),这里的n的值为复制的个数
# a = tee([1, 4, 6, 4, 1], 3)
# print(a)
#
# # repeat:实现复制元素n次
# print(repeat(6, 3))
# print(repeat([1, 2, 3], 2))
#
#
#
#
#
#
#
