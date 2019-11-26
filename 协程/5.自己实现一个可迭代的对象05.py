import time
from collections import Iterable


class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration


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
