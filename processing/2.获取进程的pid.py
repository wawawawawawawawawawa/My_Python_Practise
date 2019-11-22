import multiprocessing
import os
import time


def test1():
    while True:
        print("子进程的pid=%d---父进程的pid=%d" % (os.getpid(), os.getppid()))
        time.sleep(1)


def main():
    print("主进程的pid=%d---父进程的pid=%d" % (os.getpid(), os.getppid()))
    p1 = multiprocessing.Process(target=test1)
    p1.start()


if __name__ == "__main__":
    main()
