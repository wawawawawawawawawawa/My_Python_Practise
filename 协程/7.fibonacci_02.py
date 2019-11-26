class Fibonacci(object):
    def __init__(self, all_number):
        self.all_number = all_number
        self.current_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < self.all_number:
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1
            return ret
        else:
            raise StopIteration


fibonacci = Fibonacci(10)

for fi in fibonacci:
    print(fi)
