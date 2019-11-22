import multiprocessing
import time


def test1(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


def main():
    p1 = multiprocessing.Process(target=test1, args=(11, 22, 33, 44, 55, 66), kwargs={"nam": 11})
    p1.start()


if __name__ == "__main__":
    main()
