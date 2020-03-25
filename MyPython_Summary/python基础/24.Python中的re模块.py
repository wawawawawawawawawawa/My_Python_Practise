import re
# 1.compile():编译一个正则表达式，返回一个对象的模式
# 格式：re.compile(pattern, flags = 0)
# pattern:编译时用的表达式字符串
# flags编译标志位：用于修改正则表达式的匹配方式，如：是否区分大小写，多行匹配等  re.I():使匹配对大小写不敏感\
# re.M()多行匹配，影响 ^ 和 $
tt = "Tina is a good girl,she is so cool,and.."
rr = re.compile(r'\w*oo\w*')
print(rr.findall(tt))  # 查找所有包含'oo'的单词


# 2.