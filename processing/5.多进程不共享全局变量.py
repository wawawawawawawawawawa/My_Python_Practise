import time
import multiprocessing

arg = [1, 2, 3]


def test1():
    arg.append(22)
    print(arg)


def test2():
    print(arg)


def main():
    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2)
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()
