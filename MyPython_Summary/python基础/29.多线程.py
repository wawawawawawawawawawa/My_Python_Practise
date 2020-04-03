# threading的方法current_thead()返回当前线程
import threading

t = threading.current_thread()
print(t)
# getName()获得这个线程的名字，ident获得线程id，isAlive()判断线程
print(t.getName())
print(t.ident)
print(t.isAlive())


# 创建线程，需要告诉这个线程，它能做什么，做什么通过参数target传入，参数类型为callable
# args指定函数print_i的参数，类型为元组
def print_i(i):
    print(f"i的值为{i}")


my_thread = threading.Thread(target=print_i, args=(1,))
my_thread.start()

# 根据操作系统的调度算法，多线程之间轮训获得CPU时间片
# 多线程会争夺全局变量导致全局变量的修改出现问题
import time

a = 0


def add1():
    global a
    tmp = a + 1
    time.sleep(0.2)  # 延迟0.2秒模拟写入所需时间
    a = tmp
    print(f"{threading.current_thread().getName()} adds a to 1:{a}")


threads = [threading.Thread(name=f"t{(i,)}", target=add1) for i in range(10)]
[t.start() for t in threads]
# 这里的执行结果是不能累加到9而是依然是1，因为一个线程休眠后cpu会调用下一个，直到所有的线程被分配到计算资源，计算完a+1,0.2秒的休眠时间还没用完，所以最后结果取到的a都是0


# 加锁
locka = threading.Lock()
a = 0


def add1():
    global a
    try:
        locka.acquire()  # 获得锁
        tmp = a + 1
        time.sleep(0.2)
        a = tmp

    finally:
        locka.release()  # 释放锁

# 加锁也有他的问题，当有多个锁时，很容易发生死锁


# 协程是在同一线程中函数间的切换，而不是线程间的切换


# threading的方法current_thead()返回当前线程
import threading

t = threading.current_thread()
print(t)
# getName()获得这个线程的名字，ident获得线程id，isAlive()判断线程
print(t.getName())
print(t.ident)
print(t.isAlive())


# 创建线程，需要告诉这个线程，它能做什么，做什么通过参数target传入，参数类型为callable
# args指定函数print_i的参数，类型为元组
def print_i(i):
    print(f"i的值为{i}")


my_thread = threading.Thread(target=print_i, args=(1,))
my_thread.start()

# 根据操作系统的调度算法，多线程之间轮训获得CPU时间片
# 多线程会争夺全局变量导致全局变量的修改出现问题
import time

a = 0


def add1():
    global a
    tmp = a + 1
    time.sleep(0.2)  # 延迟0.2秒模拟写入所需时间
    a = tmp
    print(f"{threading.current_thread().getName()} adds a to 1:{a}")


threads = [threading.Thread(name=f"t{(i,)}", target=add1) for i in range(10)]
[t.start() for t in threads]
# 这里的执行结果是不能累加到9而是依然是1，因为一个线程休眠后cpu会调用下一个，直到所有的线程被分配到计算资源，计算完a+1,0.2秒的休眠时间还没用完，所以最后结果取到的a都是0


# 加锁
locka = threading.Lock()
a = 0


def add1():
    global a
    try:
        locka.acquire()  # 获得锁
        tmp = a + 1
        time.sleep(0.2)
        a = tmp

    finally:
        locka.release()  # 释放锁

# 加锁也有他的问题，当有多个锁时，很容易发生死锁


# 协程是在同一线程中函数间的切换，而不是线程间的切换


# threading的方法current_thead()返回当前线程
import threading

t = threading.current_thread()
print(t)
# getName()获得这个线程的名字，ident获得线程id，isAlive()判断线程
print(t.getName())
print(t.ident)
print(t.isAlive())


# 创建线程，需要告诉这个线程，它能做什么，做什么通过参数target传入，参数类型为callable
# args指定函数print_i的参数，类型为元组
def print_i(i):
    print(f"i的值为{i}")


my_thread = threading.Thread(target=print_i, args=(1,))
my_thread.start()

# 根据操作系统的调度算法，多线程之间轮训获得CPU时间片
# 多线程会争夺全局变量导致全局变量的修改出现问题
import time

a = 0


def add1():
    global a
    tmp = a + 1
    time.sleep(0.2)  # 延迟0.2秒模拟写入所需时间
    a = tmp
    print(f"{threading.current_thread().getName()} adds a to 1:{a}")


threads = [threading.Thread(name=f"t{(i,)}", target=add1) for i in range(10)]
[t.start() for t in threads]
# 这里的执行结果是不能累加到9而是依然是1，因为一个线程休眠后cpu会调用下一个，直到所有的线程被分配到计算资源，计算完a+1,0.2秒的休眠时间还没用完，所以最后结果取到的a都是0


# 加锁
locka = threading.Lock()
a = 0


def add1():
    global a
    try:
        locka.acquire()  # 获得锁
        tmp = a + 1
        time.sleep(0.2)
        a = tmp

    finally:
         locka.release()  # 释放锁

# 加锁也有他的问题，当有多个锁时，很容易发生死锁


# 协程是在同一线程中函数间的切换，而不是线程间的切换




