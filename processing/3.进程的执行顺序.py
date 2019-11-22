import multiprocessing
import time
import os


def test1():
    while True:
        print("子进程1的pid=%d---父进程的pid=%d" % (os.getpid(), os.getppid()))
        time.sleep(1)


def test2():
    while True:
        print("子进程2的pid=%d---父进程的pid=%d" % (os.getpid(), os.getppid()))
        time.sleep(1)


def main():
    print("主进程的pid=%d---父进程的pid=%d" % (os.getpid(), os.getppid()))
    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2)
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()
