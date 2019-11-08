import threading
import time

gol_nam = 100


def test1(num):
    global gol_nam
    for i in range(num):
        gol_nam += 1
        print("---test1=%d" % gol_nam)


def test2(num):
    global gol_nam
    for i in range(num):
        gol_nam += 1
        print("---test2=%d----" % gol_nam)


def main():
    t1 = threading.Thread(target=test1, args=(100000,))
    t2 = threading.Thread(target=test2, args=(100000,))
    t1.start()
    t2.start()
    time.sleep(5)
    print("---最终结果%d---" % gol_nam)


if __name__ == "__main__":
    main()
