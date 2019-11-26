def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        ret = yield a
        print(ret)
        a, b = b, a + b
        current_num += 1


obj1 = create_num(10)
ret = next(obj1)
print(ret)

ret = obj1.send("aaa")
print(ret)
