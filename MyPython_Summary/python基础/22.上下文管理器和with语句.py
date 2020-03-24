import threading
# 上下文管理器(context manager):能够帮助你自动分配并且释放资源，最典型的应用便是with语句
for x in range(1000):
    with open('text.txt', 'w') as f:
        f.write('hello')

# 每次打开文件并写入hello后，这个文件便会自动关闭，相应的资源也可以得到释放
# 另一个典型的例子是Python的threading.lock类，比如想要获取一个锁，执行相应的操作，完成后释放
some_lock = threading.Lock()
some_lock.acquire()
try:
    pass
finally:
    some_lock.release()

# 对应的with语句
some_lock = threading.Lock()
with some_lock:
    pass

