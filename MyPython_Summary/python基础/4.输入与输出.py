# input()函数暂停程序运行同等待键盘输入，直到回车被按下，函数的参数即为提示语，输入的类型永远是字符串类型(str)
# print()函数则接受字符串，数字，字典，列表甚至一些自定义类的输出
a = input()
b = input()
print('a + b = {}'.format(a + b))
print('type of a is {},type of b is {}'.format(type(a), type(b)))  # 结果都是字符串类型
# Python对 int 类型没有最大限制，对float有精度限制

# 分析一下文本文件的读写，假设有一个文本文件in.txt
# 做一个NLP(自然语言处理)，基本四步，1.读取文件 2.去除所有的标点符号 3.合并相同的词，词频排序  4.输出到out.txt
import re


def parse(text):
    # 使用正则表达式去除非数字字母
    text = re.sub(r'[^\w]', ' ', text)
    # 转为小写
    text = text.lower()
    # 生成所有单词的列表
    word_list = text.split(' ')
    # 去除空白单词
    word_list = filter(None, word_list)
    # 生成单词和词频字典
    word_cnt = {}
    for word in word_list:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] += 1
    # 按照词频排序
    sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)
    return sorted_word_cnt
with open('./resource/in.txt', 'r') as fin:
    text = fin.read()
word_and_freq = parse(text)
with open('./resource/out.txt', 'w')as fout:
    for word, freq in word_and_freq:
        fout.write('{} {} \n'.format(word, freq))

# 这里先用open()函数拿到文件的指针，第一个参数表示位置，第二个参数可以输入 r：表示读取  w：表示写入  a：表示追加写入
# 拿到指针后通过read()函数来将文件所有内容读取到内存，并赋值给变量text，这样很方便我们使用parse函数分析，但是文件过大会导致内存崩溃
# 这里的with函数可以自动调用close()

# JSON序列化
# JSON(JavaScript Object Notation)是一种轻量级的数据交换格式，它的设计意图是把所有事情都用设计的字符串来表示
# Python中和JSON串的交互可以理解为两种黑箱：一是输入杂七杂八的信息，比如一个Python字典，输出一个字符串；二是输入这个字符串，输入原始字典
import json
params = {
    'symbol':'123456',
    'type': 'limit',
    'price': 123.4
}
params_str = json.dumps(params)
print('after serialization,type of params_str={},parmas_str={}'.format(type(params_str), params_str))
original_params = json.loads(params_str)
print('after deserialization,type of original_str={},original_params={}'.format(type(original_params), original_params))

# json.dumps()这个函数，接收Python的基本数据类型，然后将其序列化为string
# json.loads()这个函数，接受一个合法字符串，然后将其反序列化为Python的基本数据类型
