def create_num(all_number):
    a, b = 1, 0
    current_num = 0
    while current_num < all_number:
        yield a
        a, b = b, a + b
        current_num += 1
    return "ok..."


obj1 = create_num(10)
while True:
    try:
        ret = next(obj1)
        print(ret)
    except Exception as ret:
        print(ret.value)
        break
