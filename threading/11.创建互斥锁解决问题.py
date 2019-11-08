import time
import threading

glo_num = 0


def test1(temp):
    global glo_num
    for i in range(temp):
        mutex.acquire()
        glo_num += 1
        mutex.release()
    print("---test1结束的结果为：%d----" % glo_num)


def test2(temp):
    global glo_num
    for i in range(temp):
        mutex.acquire()
        glo_num += 1
        mutex.release()
    print("---test2结束的结果为：%d----" % glo_num)


mutex = threading.Lock()


def main():
    t1 = threading.Thread(target=test1, args=(100000,))
    t2 = threading.Thread(target=test2, args=(100000,))
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()
