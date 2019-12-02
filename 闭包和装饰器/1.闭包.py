# 实现计算一条直线上的点


class Line(object):
    def __init__(self, k, b):
        self.k = k
        self.b = b

    def __call__(self, x):
        print(self.k * x + self.b)


line1 = Line(1, 2)
line1(5)
print("*" * 50)


def line1(k, b):
    def create_y(x):
        print(k * x + b)

    return create_y


line2 = line1(2, 3)
line2(5)
