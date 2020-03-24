# 内存泄漏：
# 1.这里的泄漏并不是说内存出现了信息安全的问题，被恶意程序利用了，而是指程序本身没有涉及好，导致程序未能释放已不再使用的内存
# 2.内存泄漏也不是指内存在物理上消失了，而是代码在分配某段内存后，因为设计错误，失去了对这段内存的控制，从而造成了内存的浪费
import os
import psutil
import gc


#显示当前python程序占用内存大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used:{}MB'.format(hint, memory))

def func():
    show_memory_info('initial')
    a = [i for i in range(10000000)]
    show_memory_info('after a created')

func()
show_memory_info('finished')

# 手动释放内存:需要先调用del a来删除一个对象，然后强制调用gc.collect()即可手动启用垃圾回收
# show_memory_info('initial')
#
# a = [i for i in range(10000000)]
#
# show_memory_info('after a created')
#
# del a
# gc.collect()
#
# show_memory_info('finish')
# print(a)


# 循环引用造成内存泄漏的问题
def func():
    show_memory_info('initial')
    a = [i for i in range(10000000)]
    b = [i for i in range(10000000)]
    show_memory_info('after a, b created')
    a.append(b)
    b.append(a)

func()
# gc.collect()
show_memory_info('finished')

# 这里a, b相互引用，并且作为局部变量，在函数func调用结束后，ab这两个指针从程序意义上来说已经不存在了，但是现在任有内存占用\
# 这是因为相互引用，导致他们的引用数都不为0
# 上述代码可以加入gc.collect()手动垃圾回收
# 这种相互调用的情况还是比较容易发现的，更加隐蔽的是出现引用环

# Python使用标记清除(mark-sweep)算法和分代收集(generationl),来启用针对循环引用的自动垃圾回收
# 标记清除：从一个节点出发进行遍历，并标记其经过的所有节点，遍历后没有被标记的点就是不可达节点即被回收\
# 遍历全图是巨大的性能浪费，所以Python的垃圾回收实现中，mark-sweep使用双向链表维护了一个数据结构，并且只考虑容器类的对象(只有容器类对象才可能出现循环引用)
# 分代收集算法：Python将所有的对象分为三代，刚刚创建为第0代，经过一次垃圾回收后仍然存在的，便会依次从上一代挪到下一代\
# 而每一代启动自动垃圾回收的阈值，则是可以单独指定的。当垃圾回收器中新增对象减去删除对象达到相应的阈值时，就会对这一代对象启动垃圾回收。





















