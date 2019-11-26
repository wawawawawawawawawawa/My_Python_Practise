import time


def tack1():
    while True:
        print("---1---")
        time.sleep(0.1)
        yield


def tack2():
    while True:
        print("---2---")
        time.sleep(0.1)
        yield


def main():
    t1 = tack1()
    t2 = tack2()

    while True:
        next(t1)
        next(t2)


if __name__ == "__main__":
    main()
