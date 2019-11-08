# coding-utf-8
import threading


def test1():
    print("test1运行----")


def main():
    print(threading.enumerate())
    t1 = threading.Thread(target=test1)
    print(threading.enumerate())
    t1.start()
    print(threading.enumerate())
#  调用start之后才会创建线程

if __name__ == "__main__":
    main()
