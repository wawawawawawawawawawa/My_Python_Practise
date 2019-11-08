import time
import threading

gal_nam = [100, 22]


def test1(temp):
    temp.append(33)
    print("---test1=%s---" % str(temp))


def test2(temp):
    print("---test2=%s---" % str(temp))


def main():
    t1 = threading.Thread(target=test1, args=(gal_nam,))
    t2 = threading.Thread(target=test2, args=(gal_nam,))
    t1.start()
    time.sleep(1)
    t2.start()
if __name__ == "__main__":
    main()
