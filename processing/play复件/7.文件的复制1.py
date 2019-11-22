import multiprocessing
import os


def copy_file(temp, old_filename, new_filename):
    old_f = open("../" + old_filename + "/" + temp, "rb")
    print(old_f)
    content = old_f.read()
    old_f.close()

    new_f = open(new_filename + "/" + temp, "wb")
    new_f.write(content)
    new_f.close()


def main():
    # 1.确认拷贝的文件夹
    old_filename = input("请输入要拷贝的文件夹")
    # 2.新建文件夹
    new_filename = old_filename + "复件"
    os.mkdir(new_filename)
    # 3.确认文件名
    file_name = os.listdir(old_filename)
    print(file_name)
    # 4.建立进程池
    po = multiprocessing.Pool(5)
    # 5.向进程池添加对象
    for temp in file_name:
        po.apply_async(copy_file, args=(temp, old_filename, new_filename))
    po.close()
    po.join()


if __name__ == "__main__":
    main()
