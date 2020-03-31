# 文件的读操作
import os
import re


def read_file(filename):
    if os.path.exists(filename) is False:
        raise FileNotFoundError('{}不存在'.format(filename))
    f = open(filename, encoding='utf-8')
    content = f.read()
    f.close()
    return content


print(read_file(r'C:\Users\LiuWenJing\Desktop\test1.py'))


# 使用with简化步骤
def read_file1(filename):
    if os.path.exists(filename) is False:
        raise FileNotFoundError('{}不存在'.format(filename))
    with open(filename, encoding='utf-8') as f:
        content = f.read()
    return content


# 数据多的话一次读取可能对内存有较大挑战，应该采用逐行读入
def read_file_line(filename):
    if os.path.exists(filename) is False:
        raise FileNotFoundError('{}不存在'.format(filename))
    with open(filename, mode='r+', encoding='utf-8') as f:
        for line in f:
            print(line, end='')


read_file_line(r'C:\Users\LiuWenJing\Desktop\test1.py')


# 文件写操作
# 文件写操作需要先判断写入的文件路径是否存在，若不存在，通过mkdir创建出路径；否则，直接写入文件
# 这里的os.path.join()是拼接路径  参考：https://www.jb51.net/article/171478.htm
def write_to_file(file_path, file_name):
    if os.path.exists(file_path) is False:
        os.mkdir(file_path)

    whole_path_filename = os.path.join(file_path, file_name)
    to_write_content = ''' 
                        Hey, Python
                        I just love Python so much,
                        and want to get the whole python stack by this 60-days column
                        and believe!
                        '''
    with open(whole_path_filename, mode="w", encoding='utf-8') as f:
        f.write(to_write_content)
    print('__write done___')
    with open(whole_path_filename, encoding='utf-8') as f:
        content = f.read()
        print(content)
        if to_write_content == content:
            print('content is equal by reading and writing')
        else:
            print('----Warning: NO Equal-----------------')


write_to_file(r'C:\Users\LiuWenJing\Desktop', 'test1.py')

# 获取文件名
# 有时拿到一个文件名时，名字带有路径，这时使用os.path.split方法可以实现路径和文件的分离
import os

file_ext = os.path.split('./data/py/test.py')  # 这里会返回一个元组对象包含两个值：('./data/py','test.py')
print(file_ext)
print(file_ext[1])
print(re.split('\.', file_ext[1])[1])  # 这里是提取文件的后缀名









