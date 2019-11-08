import time
import threading

gal_nam = 100


def test1():
    global gal_nam
    gal_nam += 100
    print("---in test1 gal_nam=%d---" % gal_nam)


def test2():
    print("---in test2 gal_nam=%d---" % gal_nam)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t1.start()
    time.sleep(1)
    t2.start()


if __name__ == "__main__":
    main()
