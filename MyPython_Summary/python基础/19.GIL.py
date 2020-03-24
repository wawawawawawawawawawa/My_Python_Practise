# GIL:Global Interpreter Lock:是CPython中的一个技术术语，他的意思是全局解释器锁，类似于操作系统的Mutex(互斥锁)\
# 每一个Python线程，在CPython解释器执行时，都会先锁住自己的线程，阻止别的线程执行
import sys
import threading

a = []
b = a
print(sys.getrefcount(a)) # 结果为3，分别被a,b和作为参数传递的getrefcount三个地方引用
# 这样一来，如果两个Python线程同时引用了a，就会造成引用计数的race condition，引用计数器可能最终只增加1，这样就会造成\
# 内存污染，因为第一个线程结束时，会把引用计数减1，这样能达到内存释放条件，第二个线程再访问a就找不到了


# 所以为了避免这样的情况CPython中有check_interval的机制，意思是Python解释器会去轮询检查线程GIL的锁住情况，每隔一段时间\
# Python解释器就会强制当前线程去释放GIL，这样别的线程才有机会


# GIL的设计主要是为了方便CPython解释器层面的编写者，而不是应用层面的程序猿，作为使用者我们还是需要lock等工具确保线程安全
n = 0
lock = threading.Lock()

def foo():
    global n
    with lock:
        n += 1


