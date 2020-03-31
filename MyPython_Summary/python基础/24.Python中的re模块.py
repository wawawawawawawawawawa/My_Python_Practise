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

# 反转字符串
s = "python"
# 方法一
rs = ''.join(reversed(s))
print(rs)
# 方法二
rs = s[::-1]
print(rs)

# 字符串的替换，使用repalce方法
s = "i love python".replace('o', '0')
print(s)

# 子串判断
# 方式1：使用in
a = 'our'
b = 'flourish'
print(a in b)
# 方式2：使用find方法，返回字符串b中匹配子串a的最小索引,如果不是子串，会返回 -1
print(b.find(a))

# 正则表达式常用的通用字符：
# \s 匹配空白字符
# \w 匹配任意字母/数字/下划线
# \W 和小写 w 相反，匹配任意字母/数字/下划线以外的字符
# \d 匹配十进制数字
# \D 匹配除了十进制数以外的值
# [0-9] 匹配一个 0~9 之间的数字
# [a-z] 匹配小写英文字母
# [A-Z] 匹配大写英文字母

# 使用search方法，找出子串的第一个匹配位置
r = re.search(a, b)
print(r.span())  # 这里是以tuple()的形式返回范围,这里匹配不到的话会直接抛异常

# finditer匹配迭代器：使用正则模块，finditer方法，返回所有子串匹配位置的迭代器
# 通过返回对象re.Match，使用它的方法span找出匹配的位置
s = "1乘以1结果还是1"
pat = '1'
r = re.finditer(pat, s)
for i in r:
    print(i)

# findall：findall方法能查找出子串的所有匹配
s = '一共20行代码运行时间13.59s'
pat = r'\d+'
r = re.findall(pat, s)
print(r)  # ['20', '13', '59']

# 会发现没有找到期望的13.59，可以使用表达式 r'\d+\.?\d+'
s = '一共2行代码运行时间13.59s'
pat = r'\d+\.?\d+'
r1 = re.findall(pat, s)
print(r1)  # ["13.59"]

# 会发现没有匹配到2，因为表达式中的 \d+表示至少两位数，所以应该改成 \d*才可以

# 匹配正整数
s = [-16, 1.5, 11.43, 10, 5]
pat = r'^[1-9]\d*$'
print([i for i in s if re.match(pat, str(i))])

# re.I忽略大小写
s = 'That'
pat = r't'
r = re.finditer(pat, s, re.I)
for i in r:
    print(i.span())

# 分隔复杂的字符串
s = 'This,,,   module ; \t   provides|| regular ; '
pat = r'[,\s;|]+'
word = re.split(pat, s)
print(word)

# 贪心与非贪心捕获
content = '''<h>ddedadsad</h><div>graph</div>bb<div>math</div>'''
# 比如要捕获<div>中的内容,使用贪心捕获的话 (.*)表示捕获任意多的字符，尽可能多的匹配字符
pat = r'<div>.*</div>'
print(re.findall(pat, content))
# 如果使用非贪心捕获的话  (.*?)就可以严格捕获区间的内容
pat = r'<div>(.*?)</div>'
print(re.findall(pat, content))



