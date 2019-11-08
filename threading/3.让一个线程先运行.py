# coding:utf-8
import threading
import time


def test1():
    for i in range(5):
        print("test1开始执行")
        time.sleep(1)


def test2():
    for i in range(5):
        print("test2开始执行")
        time.sleep(1)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
#    time.sleep(1)
    print("test1-----")
    t2.start()
#    time.sleep(1)
    print("test2------")
    time.sleep(10)
    print(threading.enumerate())


if __name__ == "__main__":
    main()
