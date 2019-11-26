import time
from collections import Iterable


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return Classiterator()


class Classiterator(object):
    def __iter__(self):
        pass

    def __next__(self):
        return 11


def main():
    classmate = Classmate()
    classmate.add("老王")
    classmate.add("老李")
    print(isinstance(classmate, Iterable))
    for temp in classmate:
        print(temp)
        time.sleep(1)


if __name__ == "__main__":
    main()
