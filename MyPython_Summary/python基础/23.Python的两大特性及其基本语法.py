# Python 是一门动态的强类型语言

# 动态语言：首先要理解类型检查，编译器或者解释器通常在编译阶段或者运行阶段做类型检查，类型检查就是查看"变量"和他们的"类型"\
# 然后判断表达式是否合理，例如不能使用int和string相加，如果类型检查发生与程序运行阶段(run time)那么就是动态类型语言(dynamically tyoed languages)\
# 若类型检查发生于编译阶段(compile time)则是静态类型语言(statically typed languages)

# 强类型语言：不管是在编译阶段或者运行阶段你，一旦某种类型绑定到变量后，此变量便会持有此类型，并且不能与其他类型在计算表达式时混合使用

# Python的常用且不同于其他语言的关键字：
# True和False表示真假，而Java中为true和false
# None表示空值，Java是null
# 逻辑运算符 not or and 对应Java中的 ！ ||  &&
# Python中使用的是elif，Java中是else if

# Python的三个比较特殊的运算符：
# 1. // 用于两个数值相除且向下取整
print(5 // 2)  # 2
# 2. ** 用于幂运算
print(2 ** 3) # 8
# 3. := 海象运算符 ，Python3.8以后支持的新运算符
n = len([1, 2, 3])
if n > 0:
    print(f"{n}大于0")
# 使用海象运算符
# if (n := len([1, 2, 3])) > 0:
#     print("{}大于0".format(n))   # 这里是可以运行的，因为Pycharm还不支持显示就先注释掉，可以观察到使用海象运算法更简洁


