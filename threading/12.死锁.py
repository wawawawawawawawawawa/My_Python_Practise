import time
import threading


class MyThread1(threading.Thread):
    def run(self):
        # 对mutexA上锁
        mutexA.acquire()
        # 对mutexA上锁后等待一秒，让线程2中的mutexB上锁

        print(self.name + '---do1---up---')
        time.sleep(1)
        mutexB.acquire()
        mutexB.release()
        mutexA.release(0)


class MyThread2(threading.Thread):
    def run(self):
        # 对mutexA上锁
        mutexB.acquire()
        # 对mutexA上锁后等待一秒，让线程2中的mutexB上锁

        print(self.name + '---do1---up---')
        time.sleep(1)
        mutexA.acquire()
        mutexB.release()
        mutexA.release(0)


mutexA = threading.Lock()
mutexB = threading.Lock()

if __name__ == "__main__":
    t1 = MyThread1()
    t2 = MyThread2()
    t1.start()
    t2.start()
   