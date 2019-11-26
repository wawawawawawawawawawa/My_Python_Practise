def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        yield a
        a, b = b, a + b
        current_num += 1


obj = create_num(10)

ret = next(obj)
print(ret)
ret = next(obj)
print(ret)
ret = next(obj)
print(ret)
ret = next(obj)
print(ret)
obj2 = create_num(2)
ret = next(obj2)
print(ret)
ret = next(obj)
print(ret)