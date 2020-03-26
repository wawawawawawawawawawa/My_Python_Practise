import re
# 1.compile():编译一个正则表达式，返回一个对象的模式
# 格式：re.compile(pattern, flags = 0)
# pattern:编译时用的表达式字符串
# flags编译标志位：用于修改正则表达式的匹配方式，如：是否区分大小写，多行匹配等  re.I:使匹配对大小写不敏感\
# re.M多行匹配，影响 ^ 和 $
tt = "Tina is a good girl,she is so cool,and.."
rr = re.compile(r'\w*oo\w*')
print(rr.findall(tt))  # 查找所有包含'oo'的单词


# 2.match():决定re是否在字符串刚开始的位置匹配  注：这个方法并不是完全匹配
# re.match(pattern, string, flags)
print(re.match('com', 'Comwww.runcomob', re.I).group())

# 3.search():函数会在字符串内查找模式匹配，只要找到第一个匹配的

# match和search一旦匹配成功，就是一个match object对象，有以下方法：
# group()：返回被匹配的字符串？
# start():返回匹配开始的位置
# end():返回匹配结束的位置
# span():返回一个元组包含匹配(开始,结束)的位置

# 4.findall():遍历匹配，可以获取字符串中所有匹配的字符串并返回一个列表
p = re.compile(r'\d+')
print(p.findall('o1n2m3k4'))  # 返回['1', '2', '3', '4']

# 5.split():按照能够匹配的子串讲string分割后返回列表
# re.split(pattern, string[, maxsplit])  maxsplit用于指定最大分割次数，不指定将全部分割
print(re.split(r'\d+', 'one1two2three3four4five5', 2))

# 6.sub():使用re替换string中每一个匹配的子串后返回替换后的字符串
# re.sub(pattern,repl,string,count),repl代表替换后的字符串，count代表替换个数
text = "JGood is a handsome boy, he is cool, clever, and so on..."
print(re.sub(r'\s+', '_', text))

# 注意：re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。





