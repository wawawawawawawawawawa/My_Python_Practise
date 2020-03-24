# assert：是一个debug的好工具，主要用于测试一个条件是否满足，如果测试条件满足，则什么也不做，相当于执行了pass语句\
# 如果测试条件不满足，便会抛出异常AssertionError,并返回具体的错误信息(optional)
assert 1 == 2
# 相当于
# if __debug__:
#     if not expression: raise AssertionError
# 这里的__debug__是一个常数，如果Python程序执行时附带了-O这个选项，比如Pythontest.py -O,那么程序中所有的asset语句都会失效\
# 常数__debug__便为False，反之为True
assert 1 == 2, "asserting is wrong"
# 需要注意使用assert时不能使用括号

# assert 的使用：
# 1：商品促销活动，准备对一些商品打折，所以需要一个apply_discount()函数，要求输入为原来的价格和折扣，输出为折后的价格


def appla_discount(price, discount):
    updated_price = price * (1-discount)
    assert 0 <= updated_price <=price, 'price should greater or equal to 0 and less or equal to original price'
    return updated_price

# 2
def func(input):

    assert isinstance(input, list), 'input must be type of list'
    # 下面的操作都是基于前提：input必须是list

# 需要注意的是使用assert就表示你很确定这个条件一定会发生或者一定不会发生，比如上面确定是list，若可能是其他的话就得使用if/else了








